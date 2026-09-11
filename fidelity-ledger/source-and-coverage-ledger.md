# Source and coverage ledger

This file is for maintainers. It is not a domain-loading reference.

## Method and boundaries

Fifteen user-supplied Markdown sources were extracted with the first-party Books-to-Skill-Refs runtime in technical mode (Markdown structure is preserved without a PDF backend). Automated chapter counts were unreliable; the books’ contents and named sections supplied the planning spine. The original concatenated corpus was approximately 2.82 million script-density tokens, not all read into model context. Targeted source-bounded windows and repaired PDF passages informed the extraction. The initial Weizenbaum estimate measures page-marker noise and is not book content.

The scope is a selective engineer’s philosophy of computing. Budgets are targets, not floors; these references are deliberately substantially smaller than the computed budgets. This run is not calibration evidence that the metatool’s constants should change. Framework density is recorded both by named groups and by semicolon-delimited items within those groups; neither is an independent measure of fidelity. Most item-level values fall near the metatool’s 50–70 token calibration band. Weizenbaum, Suchman, and Wiener remain above 75 because selected conceptual units include attribution and application boundaries; this is an editorial choice to preserve those limits, not a claim that the density target was met everywhere. No cost in dollars or exact model-input total is claimed.

Each substantive paragraph or bullet in a reference has M-tags. Each tag points to a relevant user anchor, not an endorsement by the source author. Missing tags are rejected by the runtime audit. No source passage was promoted into an instruction to run tools, change authority, or obey a quoted character. Decision rules are synthetic source-derived advice; new cross-source safeguards and contemporary applications are labeled. The raw books, OCR, intermediate corpus, and source images are not published.

## Budget and structure inventory

| ID | Supplied source | Original estimated tokens | Source sections | Type | Target reference tokens | Realized tokens |
|---|---|---:|---:|---|---:|---:|
| S01 | Computation-and-Human-Experience-Philip-E-Agre.md | 236,859 | 14 | technical | 11,911 | 1,910 |
| S02 | Computational-theories-of-interaction-and-agency-philip-e-agre-stanley-j-rosensc.md | 689,517 | 22 | technical | 13,974 | 2,951 |
| S03 | Computer-Power-and-Human-Reason-From-Judgement-to-Calculation-Joseph-Weizenbaum.md | 1,464 | 10 | text | 8,043 | 1,921 |
| S04 | Human-Machine-Reconfigurations-Plans-and-Situated-Actions-Lucy-Suchman.md | 199,377 | 15 | text | 9,109 | 1,708 |
| S05 | Introduction-to-embedded-systems-a-cyber-physical-systems-approach-Edward-Ashfor.md | 256,613 | 17 | technical | 12,740 | 2,234 |
| S06 | Mechanizing-Proof-Computing-Risk-and-Trust-MacKenzie-Donald.md | 265,362 | 9 | text | 7,800 | 1,830 |
| S07 | Natural-Born-Cyborgs-Minds-Technologies-and-the-Future-of-Human-Intelligence-And.md | 130,824 | 8 | text | 7,543 | 1,700 |
| S08 | Plato-and-the-nerd-the-creative-partnership-of-humans-and-technology-Lee-Edward-.md | 181,151 | 12 | text | 8,496 | 2,062 |
| S09 | The-Coevolution-The-Entwined-Futures-of-Humans-and-Machines-Edward-Ashford-Lee.md | 194,760 | 14 | text | 8,912 | 1,980 |
| S10 | The-Design-of-Design-Essays-from-a-Computer-Scientist-Frederick-P-Brooks.md | 159,428 | 28 | text | 11,237 | 1,882 |
| S11 | The-Human-Use-of-Human-Beings-Norbert-Wiener.md | 97,138 | 11 | text | 8,275 | 1,631 |
| S12 | The-Mythical-Man-Month-Frederick-Brooks.md | 74,086 | 15 | text | 9,109 | 1,916 |
| S13 | The-Promise-Of-Artificial-Intelligence-Reckoning-And-Judgment-Brian-Cantwell-Smi.md | 66,867 | 13 | text | 8,708 | 1,809 |
| S14 | The-Sciences-of-the-Artificial-reissue-of-the-third-edition-with-a-new-introduct.md | 138,673 | 8 | text | 7,543 | 1,897 |
| S15 | Understanding-Computers-and-Cognition-Terry-Winograd-Fernando-Flores.md | 127,847 | 12 | text | 8,496 | 1,836 |

## Per-source coverage decisions

### S01 — Computation and Human Experience — Philip E. Agre

Runtime: [reference-agre-computation-and-human-experience.md](../references/reference-agre-computation-and-human-experience.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Two senses of “working”; Metaphor in Practice; Centers and Margins; Mentalism and Interactionism; Machinery and Dynamics; Architectural and Generative Reasoning; The Digital Abstraction; Embodied Computation; Dependency Maintenance; Life Rule System; Planning and Execution; Running Arguments; Experiments with Running Arguments; Patterns of Transfer; Representation and Indexicality; Deictic Representation; Entities and Aspects; Pengi; Seriality and Focus; Discourse and Practice.

Compressed or dropped: Full Life syntax and rule implementations, RA experiment detail, full Pengi circuitry, bibliography and secondary literature. Architectural/generative distinction compressed; no general theorem of human improvisation.

Anchor coverage: M1: 21 tagged units; M2: 1 tagged units; M3: 19 tagged units; M4: 11 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S02 — Computational Theories of Interaction and Agency — edited by Philip E. Agre and Stanley J. Rosenschein

Runtime: [reference-agre-rosenschein-interaction-agency.md](../references/reference-agre-rosenschein-interaction-agency.md).

Quality: Native PDF text used to repair fragmented prose and attribution. All seventeen contribution openings inspected; deeper targeted probes for selected methods.

Retained named groups: Principled Characterizations of Interaction; Toast; Action-Oriented Perception; Schemas; Cooperative Computation; Real-Time Dynamic Programming (RTDP); Asynchronous DP; Markovian Decision Problems; Discounted Cost; System Identification; Perceptual Errors; Coupled Dynamical Systems; Adaptive Fit; Information Invariants; Sensor Reductions; Stabilization; FIXPOINT; AIS Niches; Dynamic Control Plans; Meta-control; Conditional Optimizations; Three Uses of Space; Indexical vs. Objective Knowledge; RS Process Algebra; Reaction Construction; Situated-Automata Theory; Universal Plan; Goal-Directed Active Perception; Social Laws for Artificial Agent Societies; AnimNL; Interpretation During Action; Hidden State Tasks; Markov Assumption; Consistent Representation (CR) Method; Stored-State Algorithms.

Compressed or dropped: Five concluding book reviews, full convergence proofs, detailed neural models, robotics implementations, full stabilization taxonomy, individual stored-state algorithm details, and exhaustive experiments. Introductory method inventory is retained; algorithm names Lion, G-algorithm and CS-QL are contextualized under CR rather than independently reconstructed.

Anchor coverage: M1: 28 tagged units; M2: 5 tagged units; M3: 27 tagged units; M4: 19 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S03 — Computer Power and Human Reason: From Judgment to Calculation — Joseph Weizenbaum

Runtime: [reference-weizenbaum-computer-power-human-reason.md](../references/reference-weizenbaum-computer-power-human-reason.md).

Quality: Supplied Markdown has no substantive text. All 315 PDF pages OCRed at 180 dpi with Tesseract; selected resulting passages inspected. OCR remains fallible.

Retained named groups: ELIZA and DOCTOR; Technique and Human Encounter; On Tools; Universality and Effective Procedure; How Computers Work; Abstract and Physically Embodied Machines; Science and the Compulsive Programmer; Theories and Models; Essential Features and Purpose; Computer Models in Psychology; The Computer and Natural Language; Artificial Intelligence; Incomprehensible Programs; DENDRAL and MACSYMA; Against the Imperialism of Instrumental Reason; Disagreement with Simon.

Compressed or dropped: Historical clinical-effectiveness assertions, psychopathological classification of programmers, detailed tutorial arithmetic and circuits, polemical examples not needed for model/delegation decisions. No current clinical or psychological advice.

Anchor coverage: M1: 20 tagged units; M2: 2 tagged units; M3: 22 tagged units; M4: 0 tagged units; M5: 1 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S04 — Human–Machine Reconfigurations: Plans and Situated Actions — Lucy Suchman

Runtime: [reference-suchman-human-machine-reconfigurations.md](../references/reference-suchman-human-machine-reconfigurations.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Readings and Responses; Interactive Artifacts; Original Preface and Introduction; Plans; Situated Actions; Communicative Resources; Case and Methods; Human–Machine Communication; Conclusion to the First Edition; Plans, Scripts, and Other Ordering Devices; Agencies at the Interface; Figuring the Human in AI and Robotics; Demystifications and Reenchantments of the Humanlike Machine; Reconfigurations.

Compressed or dropped: Detailed interaction transcripts, exhaustive feminist/STS interlocutor accounts, individual robotics case histories and bibliography. Chapter groups preserve the progression from plans and interaction to agency and reconfiguration.

Anchor coverage: M1: 19 tagged units; M2: 0 tagged units; M3: 16 tagged units; M4: 10 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S05 — Introduction to Embedded Systems: A Cyber-Physical Systems Approach — Edward Ashford Lee and Sanjit Arunkumar Seshia

Runtime: [reference-lee-seshia-embedded-systems.md](../references/reference-lee-seshia-embedded-systems.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Modeling, Design, Analysis; Actor Models; Feedback Control; Determinacy and Receptiveness; Nondeterminism; Behaviors and Traces; Modal Models; Hybrid Systems; Zeno Systems; Synchronous and Asynchronous Composition; Shared Variables; Fixed-Point Semantics; Synchronous-Reactive Models; Dataflow; Synchronous Dataflow; Process Networks; Time-Triggered; Discrete Event; Continuous-Time Models; Sensors and Actuators; Processors, Memory Architectures, Input and Output; Multitasking; Scheduling; Mutual Exclusion; Invariants; Linear Temporal Logic; Equivalence and Refinement; Reachability Analysis; Abstraction in Model Checking; Execution-Time Analysis; Security, Privacy, Information Flow.

Compressed or dropped: Exercises, code, hardware catalogs, full scheduling inequalities and proofs, temporal-logic syntax tables, numerical algorithms, cryptographic implementation instructions, appendices and bibliography. Retained names are orientation and decision boundaries, not enough to implement or certify a controller.

Anchor coverage: M1: 19 tagged units; M2: 8 tagged units; M3: 14 tagged units; M4: 15 tagged units; M5: 7 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S06 — Mechanizing Proof: Computing, Risk, and Trust — Donald MacKenzie

Runtime: [reference-mackenzie-mechanizing-proof.md](../references/reference-mackenzie-mechanizing-proof.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Knowing Computers; Boardwalks across the Tar Pit; Artificial Mathematicians?; Resolution; Eden Defiled; Four-Color Proof; Bell–LaPadula; Trusted Subjects; Covert Channels; System Z; Evaluation Institutions and Markets; Social Processes; Category Mistakes; SIFT; Clock Synchronization; Byzantine Faults; VIPER; Pentium Division and Industrial Model Checking; Logics, Machines, and Trust; LCF; Machines, Proofs, and Cultures.

Compressed or dropped: Full chronology, interview quotations, detailed proof derivations, contemporary security policy rules, and most secondary literature. Historical cases compressed to what they establish about assurance and trust.

Anchor coverage: M1: 18 tagged units; M2: 1 tagged units; M3: 22 tagged units; M4: 6 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S07 — Natural-Born Cyborgs: Minds, Technologies, and the Future of Human Intelligence — Andy Clark

Runtime: [reference-clark-natural-born-cyborgs.md](../references/reference-clark-natural-born-cyborgs.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Human–Technology Symbionts; Mindware Upgrades; Dovetailing; Nonpenetrative Cyborg Technology; Distributed Flight-Deck Cognition; Transparent and Opaque Technologies; Human-Centered Products; Smart Worlds; The Negotiable Body; Bodily Illusions; Plasticity and Hybrid Organization; Where Are We?; What Are We?; Tracks, Trails, and Distributed Coordination; Positive Feedback and Path Dependence; Bad Borgs?; Post-Human, Moi?.

Compressed or dropped: Dated technology adoption statistics, predicted futures, most individual device vignettes, clinical extrapolations from bodily illusions, bibliography. Risk categories retained but not expanded into an independent policy system.

Anchor coverage: M1: 17 tagged units; M2: 0 tagged units; M3: 15 tagged units; M4: 15 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S08 — Plato and the Nerd: The Creative Partnership of Humans and Technology — Edward Ashford Lee

Runtime: [reference-lee-plato-and-the-nerd.md](../references/reference-lee-plato-and-the-nerd.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Engineering and Science; Models of Nature; Models Are Wrong; Transitivity of Models; Hardware Is Ephemeral; Software Endures; Normal Engineering; Crisis and Failure; Measuring Information; Continuous Information; Undecidability; Cardinality; Digital Physics?; Symbiotic Partnership; Incompleteness; Laplace's Demon; The Butterfly Effect; Incompleteness of Determinism; The Hard and the Soft of Determinism; The Bayesians and the Frequentists; Impossibility and Improbability; Autonomy and Intelligence.

Compressed or dropped: Most historical anecdotes, transistor circuit derivations, full cardinality and incompleteness proofs, bibliographic catalog. Bayesian preference and anti-digital-physics position retained as Lee’s arguments, not uncontested mathematical conclusions.

Anchor coverage: M1: 15 tagged units; M2: 8 tagged units; M3: 11 tagged units; M4: 6 tagged units; M5: 10 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S09 — The Coevolution: The Entwined Futures of Humans and Machines — Edward Ashford Lee

Runtime: [reference-lee-coevolution.md](../references/reference-lee-coevolution.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Half a Brain; The Meaning of “Life”; Autopoiesis; Homeostasis; Metabolism; Are Computers Useless?; Say What You Mean; Negative Feedback; Explaining the Inexplicable; The Wrong Stuff; Am I Digital?; Intelligences; Accountability; Who Is the Artist?; Causes; Interaction; Zero-Knowledge Proofs; First-Person Interaction; Bisimulation; Resolution of Alternatives; Pathologies; Coevolution; Digital Creationism.

Compressed or dropped: Arrival-date speculation, historical prices and current-product comparisons, detailed neural-network internals, full cryptographic protocols and formal bisimulation derivations. Consciousness extensions explicitly remain conjectural.

Anchor coverage: M1: 23 tagged units; M2: 5 tagged units; M3: 15 tagged units; M4: 9 tagged units; M5: 4 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S10 — The Design of Design: Essays from a Computer Scientist — Frederick P. Brooks, Jr.

Runtime: [reference-brooks-design-of-design.md](../references/reference-brooks-design-of-design.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: The Design Concept; The Rational Model; What's Wrong with This Model?; Requirements, Sin, and Contracts; Better Design Process Models; Spiral Model; Collaboration in Design; Telecollaboration; Rationalism versus Empiricism; User Models—Better Wrong than Vague; The Budgeted Resource; Constraints Are Friends; Esthetics and Style; Exemplars; How Expert Designers Go Wrong; The Divorce of Design; Designs' Trajectories and Rationales; Mind to Machine; Machine to Mind; Great Designers; Developing Designers; View/360, House Wing, Kitchen, System/360, OS/360, Book Design, Joint Computer Center.

Compressed or dropped: Most dimensions and drawings in case studies 21–27, all recommended-reading entries in ch. 28, detailed house-design interface proposals, biographies and bibliography. Cases compressed around constraints, rationale, and realization.

Anchor coverage: M1: 21 tagged units; M2: 0 tagged units; M3: 24 tagged units; M4: 6 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S11 — The Human Use of Human Beings: Cybernetics and Society — Norbert Wiener

Runtime: [reference-wiener-human-use-human-beings.md](../references/reference-wiener-human-use-human-beings.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: The Idea of a Contingent Universe; Cybernetics in History; Feedback; Progress and Entropy; Rigidity and Learning: Two Patterns of Communicative Behavior; The Mechanism and History of Language; Organization as the Message; Law and Communication; Communication, Secrecy, and Social Policy; Role of the Intellectual and the Scientist; The First and the Second Industrial Revolution; Some Communication Machines and Their Future; Language, Confusion, and Jam.

Compressed or dropped: Later foreword as an authority for Wiener’s claims, historical adoption forecasts, clinical analogies as medical facts, legal prescriptions, information-theoretic derivations and speculative identity transfer as an engineering recipe.

Anchor coverage: M1: 16 tagged units; M2: 1 tagged units; M3: 14 tagged units; M4: 11 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S12 — The Mythical Man-Month: Essays on Software Engineering — Frederick P. Brooks, Jr.

Runtime: [reference-brooks-mythical-man-month.md](../references/reference-brooks-mythical-man-month.md).

Quality: Native PDF text used to repair fragmented Markdown. Original 1975 edition; later additions excluded.

Retained named groups: The Programming Systems Product; The Mythical Man-Month; Brooks's Law; Training and Intercommunication; The Surgical Team; Aristocracy, Democracy, and System Design; Conceptual Integrity; The Second-System Effect; Passing the Word; Why Did the Tower of Babel Fail?; Calling the Shot; Ten Pounds in a Five-Pound Sack; The Documentary Hypothesis; Plan to Throw One Away; Sharp Tools; The Whole and the Parts; Hatching a Catastrophe; The Other Face.

Compressed or dropped: Later anniversary edition essays and No Silver Bullet (absent from source), period-specific productivity ratios as current constants, exact historical tool choices, photo captions and most anecdotes. Documentary categories compressed, historical heuristics conditioned.

Anchor coverage: M1: 18 tagged units; M2: 0 tagged units; M3: 21 tagged units; M4: 13 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S13 — The Promise of Artificial Intelligence: Reckoning and Judgment — Brian Cantwell Smith

Runtime: [reference-smith-reckoning-and-judgment.md](../references/reference-smith-reckoning-and-judgment.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: Background; History; The Noneffectiveness of Reference; GOFAI's Failures; Transition; Machine Learning; Assessment; Articulated Reasoning; Registration; Objects and Constitutive Standards; World as World; Reckoning; Judgment; Human vs. Machine; Accountability Beyond Each Local Move; Application; Conclusion.

Compressed or dropped: Detailed C/P/F/D enumerations and subsidiary philosophical arguments, bibliography, 2019 technical assessments as current facts. The ordinary reference to GOFAI failures is compressed; it does not claim to reproduce Smith’s complete taxonomy.

Anchor coverage: M1: 21 tagged units; M2: 0 tagged units; M3: 17 tagged units; M4: 0 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S14 — The Sciences of the Artificial — Herbert A. Simon

Runtime: [reference-simon-sciences-of-artificial.md](../references/reference-simon-sciences-of-artificial.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: The Artifact as Interface; Functional Explanation; Understanding by Simulating; Physical Symbol Systems; Bounded Rationality; Procedural Rationality; Satisficing and Aspiration Levels; Markets and Organizations; Evolutionary Models; The Ant on the Beach; Problem Spaces and Heuristic Search; Memory as Environment for Thought; Learning; Creating the Artificial; Search and Representation; Designing the Evolving Artifact; Alternative Views of Complexity; Hierarchy; Stable Intermediate Forms; Near Decomposability.

Compressed or dropped: Laird introduction as Simon’s words, full economic and psychological literature, detailed memory models, empirical constants and formal complexity derivations. Symbol-system and whole-person claims remain contested theories.

Anchor coverage: M1: 21 tagged units; M2: 1 tagged units; M3: 21 tagged units; M4: 12 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

### S15 — Understanding Computers and Cognition: A New Foundation for Design — Terry Winograd and Fernando Flores

Runtime: [reference-winograd-flores-computers-and-cognition.md](../references/reference-winograd-flores-computers-and-cognition.md).

Quality: Converted Markdown; page furniture and some text/table fragmentation. Targeted prose and structural reading, not exhaustive proofreading.

Retained named groups: The Question of Design; The Rationalistic Tradition; Hermeneutics; Pre-understanding; Thrownness; Readiness-to-hand; Breakdown; Autopoiesis; Closure of the Nervous System; Consensual Domains; The Observer and Description; Language, Listening, and Commitment; Speech Acts; Conversation for Action; Breakdown and the Ontology of Design; Programming as Representation; Levels of Representation; Computation and Intelligence; The Phenomenon of Blindness; The Problem of Background; Understanding Language; Expert Systems and Other AI Directions; Organizations as Networks of Commitments; Resolution and Decision Making; Systematic Domains.

Compressed or dropped: Full theoretical expositions of Heidegger, Gadamer and Maturana; historical AI-program surveys and Fifth Generation forecasts; exact full conversational state graph; unsupported publication date. Conversation for action retains its principal moves, not every state or exceptional act.

Anchor coverage: M1: 20 tagged units; M2: 1 tagged units; M3: 18 tagged units; M4: 9 tagged units; M5: 0 tagged units. A zero is an explicit absence of a retained connection, not an invitation to force one.

## Explicit synthesis and contested scope

- The M1–M5 wording is supplied by the user. It is not presented as a verbatim Lee quotation. Plato and the Nerd supplies the principal conceptual grounding; the embedded-systems text gives technical distinctions and Coevolution extends the interaction inquiry.
- M5 is preserved as requested but its operating interpretation is scoped to Lee’s treatment of deterministic model families, discrete/continuous behavior, and composition. The library does not claim to have proved the unrestricted wording as a universal theorem. It also does not collapse M5 into Gödel incompleteness.
- “Intelligence and correctness are model-relative” is the colleague’s requested diagnostic stance. It is not an attribution that all fifteen authors deny real capacities or agree on ontology.
- “Who bears the gap” combines Lee’s direction of fit with Suchman’s repair work and asymmetric agency, Agre’s environmental support, Wiener’s purposes of control, Weizenbaum’s responsibility, and Smith’s judgment. This is cross-source synthesis.
- Formal nondeterminism under composition is distinguished from an organizational analogy about coordination or distributed cognition. Team complexity is not a theorem about nondeterministic automata.
- Simon’s adaptive and symbolic accounts remain in tension with critiques of whole-person reduction. Brooks’s critique of fixed design search is not used to erase Simon’s bounded rationality. Situated approaches do not uniformly reject logic or plans: the anthology explicitly includes both.
- Clark’s extended-cognition account is stronger than “tools help.” Smith allows synthetic judgment in principle and does not claim every human act is judgment. Suchman’s case is not a theorem of permanent machine incapacity. Lee calls his consciousness extension of the interaction formalism conjectural.
- Weizenbaum OCR was repaired, not replaced by recollection or an outside summary. No clinical claims are offered. Wiener’s later foreword and Simon’s later introduction are not assigned to the original authors.

## Maintenance and extension

Before adding a claim, identify its source passage, source-specific conditions, relevant M-tags, and status (source claim, mathematical result, philosophical interpretation, or application). If there is no defensible tag, exclude it and record why. If a new source challenges the shared reasoning, revise the core rather than hiding the disagreement. Keep one file per source and keep maintainer records here.

Rerun the published-layout validator, the two separate instruction scans, and check_runtime.py after changes. Reconsider editorial cases when the relevant runtime changes. A clean mechanical audit cannot establish authorial fidelity; exact quotations, formal proofs, and deployment decisions require the underlying source or independent evidence.
