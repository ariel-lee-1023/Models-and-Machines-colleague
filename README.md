# Models and Machines Colleague

I work with you on the gap between a model and the machine or activity it describes. When a system is called correct, deterministic, intelligent, or autonomous, I ask what those words mean within the description and what evidence connects that description to the system in use. A proof can establish a valuable bounded guarantee. Whether the specification captures the intended work is a further question, with different evidence behind it.

If two components behave deterministically on their own, I examine the scheduling, shared state, simultaneous events, and feedback before extending that property to their combination. If an automated workflow follows its rules yet repeatedly needs a person to repair the result, I examine what the model leaves out and who supplies it. Missing context, an inadequate interface, and an implementation fault call for different engineering changes.

I use Edward A. Lee's M1–M5 anchor to keep descriptions, directions of fit, composition, and modeling limits explicit. I also ask who notices divergence and has the authority and resources to respond. Human supervision cannot carry a guarantee if the supervisor lacks the information or power it requires. I turn the analysis into a tighter claim, a design revision, or a discriminating test, preserving both useful formal assurances and the limits of their application.

This Agent Skill supports engineering design and critique through source references on computing, situated action, proof, trust, and judgment. Technology arrival-date forecasting is outside its scope.

## Edward A. Lee anchor

The user's five organizing commitments are retained in full in [SKILL.md](SKILL.md):

| Tag | Organizing question |
|---|---|
| M1 | What description is being used, and how does it differ from the thing itself? |
| M2 | Which model has the asserted determinism property? |
| M3 | Are we fitting the model to the system, or constructing the system to match the model? |
| M4 | Does the claimed property survive the specified composition? |
| M5 | What limits appear when the model family accommodates discrete and continuous alternatives? |

Every substantive extracted unit has one or more relevant M1–M5 tags. Untagged candidates are excluded. Tags mean relevance to the anchor, not that every author endorses Lee or that each passage supports all five theses. M5's broad user formulation is kept visible alongside the more specific scope of Lee's deterministic composition argument; it is not presented as a theorem about every possible collection of models.

## Use

Open this repository as an agent project. [AGENTS.md](AGENTS.md) directs domain conversations to the root skill, and the discovery alias points to that same canonical content.

```sh
git clone https://github.com/ariel-lee-1023/Models-and-Machines-colleague.git
cd Models-and-Machines-colleague
```

For a host using a personal `.agents/skills` directory, clone the complete repository into its skill directory instead:

```sh
git clone https://github.com/ariel-lee-1023/Models-and-Machines-colleague.git \
  ~/.agents/skills/models-and-machines-colleague
```

Use one installation approach appropriate to your host. If its skill location differs, place the complete root skill and `references/` tree there. Do not install `SKILL.md` without its references. A checkout that cannot preserve symlinks can load the root skill directly.

Example requests:

- “The services are individually deterministic. Review the claim that the distributed system is deterministic.”
- “Our simulator reproduces the benchmark. What does that establish about the physical mechanism?”
- “This program is formally verified. Trace the remaining assumptions between the proof and the deployed machine.”
- “Users keep working around our AI workflow. Analyze the model of work and who handles its omissions.”
- “Compare Simon and Suchman on a plan-driven design process without smoothing over their disagreements.”
- “An AI review step is called human judgment. What would the reviewer need to understand and be able to change?”

Only the shared core is loaded initially. Its task-based routing selects the relevant source references; each book is one independently loadable file. M-tags organize extraction and audit and need not appear in ordinary answers.

## Sources

| Book | Author(s) | Principal contribution |
|---|---|---|
| [Plato and the Nerd: The Creative Partnership of Humans and Technology](references/reference-lee-plato-and-the-nerd.md) | Edward Ashford Lee | Models, direction of fit, determinism, composition, formal limits |
| [Introduction to Embedded Systems: A Cyber-Physical Systems Approach](references/reference-lee-seshia-embedded-systems.md) | Edward Ashford Lee and Sanjit Arunkumar Seshia | State, time, hybrid dynamics, concurrency, refinement, assurance |
| [The Coevolution: The Entwined Futures of Humans and Machines](references/reference-lee-coevolution.md) | Edward Ashford Lee | Feedback, interaction, accountability, technological change |
| [Computation and Human Experience](references/reference-agre-computation-and-human-experience.md) | Philip E. Agre | Critical technical practice, deictic representation, improvisation |
| [Computational Theories of Interaction and Agency](references/reference-agre-rosenschein-interaction-agency.md) | Philip E. Agre and Stanley J. Rosenschein, editors; individual contributors named in the reference | Seventeen approaches to agent–environment interaction |
| [Computer Power and Human Reason: From Judgment to Calculation](references/reference-weizenbaum-computer-power-human-reason.md) | Joseph Weizenbaum | Model selection, ethical choice, limits of instrumental reason |
| [Human–Machine Reconfigurations: Plans and Situated Actions](references/reference-suchman-human-machine-reconfigurations.md) | Lucy Suchman | Plans as resources, repair, asymmetric agency |
| [Mechanizing Proof: Computing, Risk, and Trust](references/reference-mackenzie-mechanizing-proof.md) | Donald MacKenzie | Proof scope, physical implementation, trust and institutions |
| [Natural-Born Cyborgs: Minds, Technologies, and the Future of Human Intelligence](references/reference-clark-natural-born-cyborgs.md) | Andy Clark | Extended cognition, fluent tools, dependence |
| [The Design of Design: Essays from a Computer Scientist](references/reference-brooks-design-of-design.md) | Frederick P. Brooks, Jr. | Evolving goals, user models, constraints, design rationale |
| [The Human Use of Human Beings: Cybernetics and Society](references/reference-wiener-human-use-human-beings.md) | Norbert Wiener | Feedback, communication, automation, purposes of control |
| [The Mythical Man-Month: Essays on Software Engineering](references/reference-brooks-mythical-man-month.md) | Frederick P. Brooks, Jr. | Coordination, integration, conceptual integrity; 1975 edition |
| [The Promise of Artificial Intelligence: Reckoning and Judgment](references/reference-smith-reckoning-and-judgment.md) | Brian Cantwell Smith | Registration, world, accountability for the frame |
| [The Sciences of the Artificial](references/reference-simon-sciences-of-artificial.md) | Herbert A. Simon | Artifact interfaces, bounded rationality, hierarchy |
| [Understanding Computers and Cognition: A New Foundation for Design](references/reference-winograd-flores-computers-and-cognition.md) | Terry Winograd and Fernando Flores | Background, breakdown, language and commitments |

## Repository layout

```text
SKILL.md                     Shared reasoning core and loading triggers
references/                  Fifteen canonical source references
AGENTS.md                    Project discovery and maintenance instructions
README.md
LICENSE
.gitignore
.agents/skills/
  models-and-machines-colleague -> ../..
fidelity-ledger/              Provenance, coverage, evaluation, validation
```

The root skill and references are the only runtime copy. The relative symlink supports project discovery. Maintainer records are kept in `fidelity-ledger/` and are not automatically loaded for domain answers.

## Fidelity and limitations

Built with Books-to-Skill-Refs from fifteen supplied Markdown files using structural probes and targeted reading. The references preserve concepts and decision boundaries through synthetic prose, chapter locators, and compact reconstructed examples. They are selective working references, not complete substitutes for the books, implementation manuals, or reproductions of formal proofs.

The Weizenbaum Markdown contained only page markers; its matching local PDF was OCRed. Cleaner PDF text also repaired fragmented passages in the interaction anthology and the 1975 Brooks source. OCR and conversion can still contain errors. The original Brooks edition does not include later anniversary essays. Later introductions and forewords are distinguished from the original authors' arguments. See the [source and coverage ledger](fidelity-ledger/source-and-coverage-ledger.md) and [source manifest](fidelity-ledger/source-manifest.json).

The core preserves disagreements rather than claiming consensus. It distinguishes formal results, philosophical interpretations, and new design applications. Historical examples do not establish present tool capabilities, safety, law, adoption, or forecasts. Important new technical or empirical claims need current authoritative evidence.

## Validation

The build is checked against the metatool's published-repository layout and token budgets. Root `SKILL.md` and `references/` are scanned separately for anomalous instructions. A local audit checks tags, routes, relative links, source counts, and the discovery alias:

```sh
python3 fidelity-ledger/check_runtime.py
```

See [validation results](fidelity-ledger/validation.json), [runtime audit](fidelity-ledger/runtime-audit.json), and [editorial evaluation](fidelity-ledger/evaluation.md). Editorial cases are construction-time reviews, not independent model benchmarks. A clean instruction scan is advisory, not a security guarantee.

## License

Original skill instructions, synthetic reference text, and maintainer materials are provided under the [MIT License](LICENSE). The underlying books, quoted titles, and their authors' intellectual contributions retain their own rights and terms. This repository includes no raw books, recovered full text, or source-page images and does not relicense them.

Scope: This license applies to the original skill, synthetic references, and
maintainer materials in this repository. It does not grant rights to the
underlying source books, which remain subject to their respective terms.
