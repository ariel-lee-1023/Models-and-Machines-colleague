# Mechanizing Proof: Computing, Risk, and Trust — Donald MacKenzie
**Format**: md | **Sections**: 9 | **Depth**: study | **Type**: text
**Edition**: MIT Press, 2001. Locators use chapter numbers and named cases.

## Mental Model (read first)

[M1,M3,M4] MacKenzie studies how people come to know and trust computer systems, including formal verification and mechanized mathematical proof. Deduction can be powerful without eliminating reliance on people, tools, institutions, and physical machines. Follow what a proof actually establishes and how its authority travels into practice; the sociology of acceptance neither invalidates a theorem nor certifies a realization.

## Frameworks & Structure

### Chapters 1–2: Knowing and engineering programs

- [M1,M3] **Knowing Computers** (ch. 1): testing, mathematical reasoning, testimony, and practical experience provide different grounds for belief. The sheer number of possible executions limits exhaustive testing; formal reasoning requires an explicit target and assumptions. Compare their contributions to a particular claim instead of demanding that one method answer every question.
- [M1,M3] **Boardwalks across the Tar Pit** (ch. 2): the software crisis prompted managerial, methodological, and mathematical responses. Program proof establishes a relation between a formal program description and a specification. Whether the specification expresses what users need is an additional question.

### Chapters 3–4: Proof by and with machines

- [M1,M3] **Artificial Mathematicians?; Resolution** (ch. 3): automated theorem proving combines logical representations, inference rules, and search. Logical capability does not make search tractable or determine mathematical interest. Distinguish a proof's validity, the process of finding it, and its usefulness to a community.
- [M1,M3] **Eden Defiled; Four-Color Proof** (ch. 4): the Appel–Haken case altered the relationship between mathematical argument, computation, and surveyability. Community acceptance involved judgments about programs and machines as well as the mathematical reduction. Do not report “computer-assisted” as either a defect or a guarantee without examining the dependency.

### Chapter 5: Security models and excluded channels

- [M1,M3,M4] **Bell–LaPadula; Trusted Subjects; Covert Channels** (ch. 5): a formal security policy requires a defined information-flow world. Practical systems can need privileged exceptions and can communicate through channels not represented in that world. Verify which flows the proof covers and which mechanisms remain outside it.
- [M1,M3] **System Z** (ch. 5): McLean's challenge showed how a system could satisfy a formal account yet violate the security intuition it was supposed to express. Debate and model revision exposed disagreements about assumptions and policy. This is a specification-adequacy issue, not automatic evidence that the deduction was erroneous.
- [M3] **Evaluation Institutions and Markets** (ch. 5): evaluation requirements, development cost, secrecy, and the size of a market shape which verified systems get built. A strong mathematical technique does not guarantee adoption, and adoption does not itself validate a stronger technical claim.

### Chapter 6: Competing critiques

- [M1,M3] **Social Processes** (ch. 6): DeMillo, Lipton, and Perlis emphasize how understandable arguments are checked, reused, corrected, and accepted. A large formal derivation can be difficult to integrate into such practices. MacKenzie reports the dispute; the reader must not conflate this objection with a demonstration of logical invalidity.
- [M1,M3] **Category Mistakes** (ch. 6): Fetzer distinguishes formal mathematical objects from causally operating physical programs. That differs from the social-process critique. The useful design consequence is to label proof about a description separately from evidence that an actual device realizes it; it is not to abandon proof.

### Chapters 7–8: Machines and trusted mechanisms

- [M1,M2,M3,M4] **SIFT; Clock Synchronization; Byzantine Faults** (ch. 7): fault-tolerant control depends on assumptions about components, clocks, and communication. Mathematical treatment of severe fault behavior can clarify what a system tolerates. A physical implementation must still meet the relevant timing and failure assumptions.
- [M1,M3] **VIPER** (ch. 7): disputes about a verified microprocessor involved which design levels were connected by proof and which relied on other evidence. Identify every correspondence step from specification through circuit description to fabricated hardware. “Verified chip” is too broad unless those boundaries are supplied.
- [M1,M3] **Pentium Division and Industrial Model Checking** (ch. 7): a concrete arithmetic fault can change commercial and engineering attitudes toward assurance. The historical case shows how mathematical concerns become consequential through actual use and trust; it does not supply current defect rates or a universal hierarchy of verification tools.
- [M1,M3] **Logics, Machines, and Trust; LCF** (ch. 8): proof assistants embody particular logics and implementation strategies. The LCF tradition controls construction of theorem objects through a small trusted mechanism. Reducing the trusted base is useful without making compilers, runtime, hardware, or the chosen logic disappear.

### Chapter 9: Proof cultures and dependability

- [M1,M3] **Machines, Proofs, and Cultures** (ch. 9): dependability develops through technical practices and institutions that make claims inspectable and errors corrigible. Explain what changes the grounds for trust, not merely whether a system carries an assurance label. Formal rigor and social organization are interacting parts of this explanation.

## Worked Example

[M1,M3,M4] **Reconstructed from the security-model discussion in ch. 5.** A system is judged against a specified information-flow policy. Its proof succeeds, yet an omitted communication path or a permitted policy transition defeats the intended protection. First inspect whether the contested behavior is represented and whether it is allowed by the formal rules. If it is allowed, repair the policy or its assumptions; if it lies outside the model, widen the assurance boundary. Only if the proved relation fails on its own terms is a faulty proof or implementation the immediate diagnosis. The generalized sequence here distills the Bell–LaPadula, covert-channel, and System Z discussions rather than presenting them as one identical incident.

## Decision Rules & Judgment

- [M1,M3] When told “proved correct,” ask: which description, specification, logic, assumptions, and correspondence steps?
- [M1,M3] When a verified system disappoints, distinguish wrong specification, missing environment behavior, failed realization, and flawed deduction.
- [M3,M4] When trust is delegated to a checker, identify its trusted base and the people responsible for maintaining that base.
- [M3] When verification adoption fails, inspect institutional and economic conditions alongside mathematical strength.

## Key Takeaways

1. [M1,M3] A proof's scope must survive the move into an assurance claim.
2. [M4] Omitted channels and component assumptions matter to the whole.
3. [M3] Mechanization reorganizes trust; it does not eliminate it.
