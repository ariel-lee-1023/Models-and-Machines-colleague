# Introduction to Embedded Systems: A Cyber-Physical Systems Approach — Edward Ashford Lee and Sanjit Arunkumar Seshia
**Format**: md | **Sections**: 17 | **Depth**: study | **Type**: technical
**Edition**: Second edition, version 2.2, MIT Press, 2017. Chapter and section locators refer to this edition.

## Mental Model (read first)

[M1,M2,M3,M4,M5] A cyber-physical system joins logical computation to physical dynamics. Modeling, design, and analysis are distinct but interacting activities. Correct values are insufficient when they arrive too late, sensors misrepresent the plant, or composition changes possible behaviors. This reference retains the book's modeling and assurance concepts; it does not replace its implementation exercises or supply a deployment certification.

## Frameworks & Structure

### Chapters 1–2: Models, dynamics, and feedback

- [M1,M3] **Modeling, Design, Analysis** (§1.3): a model describes selected aspects for reasoning; design constructs a realization; analysis examines properties. State which claims concern mathematical behavior and which concern measured execution. A physical system is realized in matter; a logical system, such as an algorithm, is a conceptual description.
- [M1,M3,M4] **Actor Models; Feedback Control** (ch. 2): actors relate input and output signals; feedback joins them into a loop. Modeling the plant, controller, sensors, and environment together makes stability and response meaningful. Preserve units, sampling assumptions, and timing; a controller that works for one plant model need not work for another.

### Chapters 3–4: State and hybrid dynamics

- [M2] **Determinacy and Receptiveness** (§3.3.4): a deterministic state machine has at most one enabled transition for each state and input. A receptive machine has at least one. Together they give exactly one. Determinacy concerns identical outputs for identical inputs, so distinct internal transitions need not imply observable indeterminacy. Name which notion is being asserted.
- [M1,M2] **Nondeterminism; Behaviors and Traces** (§§3.5–3.6): multiple allowed behaviors can express unknown details or permitted implementation choices. Nondeterminism is not automatically a probability distribution. A trace records behavior at a chosen observation boundary; internal differences can disappear when only external traces are compared.
- [M1,M4,M5] **Modal Models; Hybrid Systems** (ch. 4): continuous evolution operates within modes; guards and resets govern discrete transitions. Check guard overlap, boundary behavior, and what happens when multiple transitions become eligible. Hybrid modeling exposes the discrete/continuous boundary central to M5 without making every hybrid system ill-defined.
- [M1,M5] **Zeno Systems** (§4.2): infinitely many modeled discrete events can occur in finite modeled time, as in idealized bouncing. This is a property of the idealization; a physical ball eventually rests. An implementation needs a justified treatment of the event accumulation, not an assumption that a simulator can execute an infinite loop in finite time.

### Chapters 5–6: Composition has semantics

- [M2,M4] **Synchronous and Asynchronous Composition; Shared Variables** (ch. 5): components can react together or interleave. Shared updates and scheduling can add alternatives absent from each isolated machine. Specify the transition and observation rules; visually similar block diagrams can denote different systems.
- [M2,M4] **Fixed-Point Semantics; Synchronous-Reactive Models** (§§6.1–6.2): feedback can require a simultaneous solution for signal values. A unique, constructible reaction cannot be assumed from local determinism. Distinguish a well-formed feedback network from an equation loop whose reaction is absent, ambiguous, or not constructively available.
- [M1,M2,M4] **Dataflow; Synchronous Dataflow; Process Networks** (§6.3): token production, consumption, ordering, and blocking rules define execution. Fixed rates can support static scheduling; more dynamic networks need additional analysis. A deterministic stream relation does not by itself guarantee bounded memory or freedom from deadlock.
- [M1,M4,M5] **Time-Triggered; Discrete Event; Continuous-Time Models** (§6.4): these assign different meanings to time and reaction. Simultaneous timestamps require semantics; numerical integration introduces approximations. Choose a model of computation for the property being protected, then justify its implementation.

### Chapters 7–12: Physical and execution assumptions

- [M1,M3] **Sensors and Actuators** (ch. 7): resolution, sampling, range, and dynamics condition the relationship between a physical quantity and a represented value. Examine error and latency on both observation and actuation. A formally correct decision on an invalid measurement does not establish successful control.
- [M1,M3,M4] **Processors, Memory Architectures, Input and Output** (chs. 8–10): parallelism, caches, memory ordering, interrupts, and peripheral interaction shape execution. A sequential program abstraction may omit the properties needed for timing or concurrency assurance. Make the relevant hardware and I/O assumptions explicit rather than treating them as incidental deployment details.
- [M2,M3,M4] **Multitasking; Scheduling; Mutual Exclusion** (chs. 11–12): threads and processes interact through shared state or messages. Rate Monotonic Scheduling and Earliest Deadline First are analyzed under specific task assumptions; blocking and resource protocols can change the result. Do not apply utilization conclusions without checking periods, deadlines, preemption, execution bounds, and processor assumptions.

### Chapters 13–17: Assurance and its boundary

- [M1,M3] **Invariants; Linear Temporal Logic** (ch. 13): invariants constrain reachable states; temporal formulas express behavior over traces. Safety excludes bad behavior, whereas liveness requires progress. An eventuality may depend on fairness or environmental cooperation; do not substitute a finite test trace for the quantified property.
- [M1,M3] **Equivalence and Refinement** (ch. 14): type compatibility, trace-language containment, simulation, and bisimulation establish different relationships. Choose a relation that preserves the intended property. Refinement reduces allowed implementation behavior only relative to a specified semantics and observation interface.
- [M1,M3] **Reachability Analysis; Abstraction in Model Checking** (ch. 15): explore reachable behavior under an environment model. Overapproximation can support universal safety claims but may generate spurious counterexamples. Validate a counterexample against the concrete model before classifying it as a physical defect; narrow abstractions can miss behavior entirely.
- [M1,M3,M4] **Execution-Time Analysis** (ch. 16): control-flow paths, feasible paths, block costs, and memory behavior constrain execution time. Measurement of typical runs is not automatically a worst-case bound. A quantitative requirement must be traced through the assumptions of the analysis to the actual platform.
- [M1,M3,M4] **Security, Privacy, Information Flow** (ch. 17): adversarial environments differ from ordinary disturbance models. Cryptography, protocol behavior, software faults, sensors, actuators, and side channels occupy different layers. A protected channel does not establish security of everything connected to it. This is conceptual coverage of the edition, not current security advice.

## Worked Example

[M1,M4,M5] **Reconstructed from the bouncing-ball example in ch. 4.** Use position and velocity as continuous state, gravity during flight, a ground-contact guard, and a velocity reset that loses energy at each bounce. The time between collisions shrinks; the idealization admits infinitely many impacts in finite time. Inspect whether the model defines continuation after that limit. A practical simulation may introduce a resting mode or a contact model, but that is a changed model whose thresholds must be justified. Successful numerical termination alone does not establish fidelity to a real ball.

## Decision Rules & Judgment

- [M2,M4] For any determinism claim, specify the machine, input history, state, scheduling, and observation boundary.
- [M1,M3] For a proof, record specification, environment assumptions, abstraction, verification method, and physical correspondence evidence.
- [M3,M4] For a deadline, include sensing, computation, blocking, communication, and actuation under the chosen end-to-end boundary.
- [M1,M5] For a simulation anomaly, test whether it comes from the physical approximation, numerical method, or event semantics before changing the controller.

## Key Takeaways

1. [M3] Functional and temporal correctness need explicit contracts.
2. [M4] The composition operator is part of the system model.
3. [M1,M5] A verified abstraction still needs a justified relation to its realization.
