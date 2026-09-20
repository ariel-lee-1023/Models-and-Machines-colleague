#!/usr/bin/env python3
"""Audit this library's source routing, per-unit M-tags, and published discovery."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
TAG = re.compile(r"^\[(?:M[1-5])(?:,M[1-5])*\]\s+")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REQUIRED = ["Mental Model (read first)", "Frameworks & Structure", "Worked Example",
            "Decision Rules & Judgment", "Key Takeaways"]


def audit() -> dict:
    errors = []
    core = (ROOT / "SKILL.md").read_text()
    manifest = json.loads((ROOT / "fidelity-ledger/source-manifest.json").read_text())
    refs = sorted((ROOT / "references").glob("reference-*.md"))
    declared = {x["reference"] for x in manifest["sources"]}
    actual = {str(p.relative_to(ROOT)) for p in refs}
    expected = manifest["source_count"]
    match = re.search(r"\*\*Books\*\*:\s*(\d+)", core)
    if len(refs) != expected or len(manifest["sources"]) != expected or declared != actual or not match or int(match[1]) != expected:
        errors.append("Source manifest, core count, and references must match")
    if "name: models-and-machines-colleague\n" not in core:
        errors.append("Unexpected skill slug")
    alias = ROOT / ".agents/skills/models-and-machines-colleague"
    if not alias.is_symlink() or str(alias.readlink()) != "../.." or alias.resolve() != ROOT:
        errors.append("Discovery alias does not resolve to the canonical root")
    for anchor in range(1, 6):
        if f"- **M{anchor}**" not in core:
            errors.append(f"Missing core anchor M{anchor}")
    files = {}
    for p in refs:
        rel = str(p.relative_to(ROOT))
        t = p.read_text()
        if f"]({rel})" not in core:
            errors.append(f"Unrouted reference: {rel}")
        for heading in REQUIRED:
            if f"## {heading}" not in t:
                errors.append(f"{rel}: missing {heading}")
        active = False
        count = 0
        totals = {f"M{k}": 0 for k in range(1, 6)}
        for n, line in enumerate(t.splitlines(), 1):
            if line.startswith("## Mental Model"):
                active = True
            if not active or not line.strip() or line.startswith("#"):
                continue
            unit = re.sub(r"^(?:- |\d+\. )", "", line)
            match = TAG.match(unit)
            if not match:
                errors.append(f"{rel}:{n}: untagged substantive unit")
                continue
            count += 1
            for tag in set(re.findall(r"M[1-5]", match.group())):
                totals[tag] += 1
        files[rel] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                      "tagged_units": count, "tag_counts": totals}
    # Explicit file lists avoid traversing the discovery symlink back into the root.
    for p in [*ROOT.glob("*.md"), *refs, *(ROOT / "fidelity-ledger").glob("*.md")]:
        for target in LINK.findall(p.read_text()):
            if re.match(r"^[a-z]+:", target, re.I) or target.startswith("#"):
                continue
            dest = p.parent / unquote(target.split("#", 1)[0])
            if not dest.exists():
                errors.append(f"{p.relative_to(ROOT)}: broken link {target}")
    core_hash = hashlib.sha256((ROOT / "SKILL.md").read_bytes()).hexdigest()
    return {"passed": not errors, "errors": errors, "source_count": len(manifest["sources"]),
            "reference_count": len(refs), "core_sha256": core_hash,
            "total_tagged_reference_units": sum(x["tagged_units"] for x in files.values()),
            "references": files,
            "limits": "Mechanical audit; tag relevance and authorial fidelity require editorial review."}


if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["passed"] else 1)
