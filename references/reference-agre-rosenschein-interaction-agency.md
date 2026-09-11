# Computational Theories of Interaction and Agency — edited by Philip E. Agre and Stanley J. Rosenschein
**Format**: md | **Sections**: 22 | **Depth**: study | **Type**: technical
**Edition**: MIT Press, 1996; contributions reprinted from Artificial Intelligence 72–73 (1995).
**Coverage**: Seventeen substantive contributions below; five concluding book reviews excluded. Locators are the volume's printed start pages, not the journals' restarted pagination. Cleaner text from the matching PDF supplements fragmented Markdown. This is a conceptual methods reference, not a reproduction of algorithm proofs.

## Mental Model (read first)

[M1,M3,M4] These contributors make the agent–environment relationship an object of analysis and design. They disagree about architecture and representation: logical methods, dynamic programming, dynamical systems, and situated control coexist. The shared lesson is to identify the environmental properties that make a mechanism successful instead of attributing all success to intelligence inside the agent. M-tags are an editorial bridge to Lee, not claims of a single theory shared by the volume.

## Frameworks & Structure

### 1. Agre — Computational research on interaction and agency (p. 1)

- [M1,M3,M4] **Principled Characterizations of Interaction; Toast**: explain living agents or design artificial ones by analyzing how they are involved in environments. A simple mechanism can exploit structure that an isolated-agent account overlooks. Toast's breakfast-making case directs attention to task and material regularities; its simplicity is conditional on that setting.

### 2. Arbib and Liaw — Sensorimotor transformations (p. 53)

- [M1,M3,M4] **Action-Oriented Perception; Schemas; Cooperative Computation**: perceptual and motor schemas coordinate approach, avoidance, detours, and planning. Schema-level organization and neural implementation are different explanatory levels. A biological analogy supplies design hypotheses, not evidence that a robot implements the same biological mechanism. Preserve the relation between function and structure when transferring an idea.

### 3. Barto, Bradtke, and Singh — Real-time dynamic programming (p. 81)

- [M1,M2,M3] **Real-Time Dynamic Programming (RTDP); Asynchronous DP**: improve decisions through value backups concentrated on states encountered during interaction. The method bridges planning and reinforcement learning, including uncertain transitions. Its optimality results depend on the stated problem class and update assumptions; “real-time” in the title is not a hard deadline guarantee on a deployed processor.
- [M1,M3] **Markovian Decision Problems; Discounted Cost**: in the discounted formulation, a policy is assessed by expected accumulated cost with discount factor strictly between zero and one. The recurrence exploits the modeled state structure. Before using its conclusion, establish that the state carries the relevant history and that the objective reflects the task; optimization cannot repair a misframed cost function.

### 4. Basye, Dean, and Kaelbling — Learning dynamics (p. 139)

- [M1,M2,M3] **System Identification; Perceptual Errors**: infer deterministic finite-state dynamics from action/observation sequences while distinguishing errors in observing outputs from errors in knowing which actions occurred. Exploration affects the evidence obtained. A learned deterministic model and noisy observations are compatible; apparent randomness does not alone identify which source of uncertainty is present.

### 5. Beer — A dynamical systems perspective (p. 173)

- [M1,M3,M4] **Coupled Dynamical Systems; Adaptive Fit**: model agent and environment as interacting dynamical systems, and assess whether their joint trajectories satisfy a constraint. The walking example locates behavior in their coupling. An agent's isolated dynamics do not by themselves establish performance after a change in body, terrain, or coupling.

### 6. Donald — On information invariants in robotics (p. 217)

- [M1,M3,M4] **Information Invariants; Sensor Reductions**: compare task requirements across internal state, collaborating agents and communication, environmental modifications, sensing, and computation. A reduction relates sensor systems under specified transformations of these resources. Intelligence can be redistributed across the arrangement; replacing one resource is not necessarily a free saving.

### 7. Hammond, Converse, and Grass — Stabilization of environments (p. 305)

- [M1,M3,M4] **Stabilization; FIXPOINT**: agents can modify environments so that useful conditions recur, rather than only adapting themselves to a given world. Examine the acts that establish and preserve those conditions and the cues that trigger them. A supposedly robust mechanism may actually rely on a stabilized workspace; performance should include the work of producing that workspace.

### 8. Hayes-Roth — Adaptive intelligent systems (p. 329)

- [M1,M3,M4] **AIS Niches; Dynamic Control Plans; Meta-control**: tasks, resources, context, and performance criteria vary within a niche. Adapt perception, reasoning tasks, methods, and global control accordingly. Explicit control plans guide choices among situation-triggered behaviors. This is an important counterweight to any claim that situated approaches uniformly reject plans.

### 9. Horswill — Analysis of adaptation and environment (p. 367)

- [M1,M3] **Conditional Optimizations**: an environmental constraint licenses a transformation into a more efficient mechanism with equivalent behavior under that constraint. Post-hoc analysis can reveal what a working robot relies on and why it fails elsewhere. Record each constraint with its optimization; without the condition, the preserved-behavior argument does not travel.

### 10. Kirsh — The intelligent use of space (p. 397)

- [M1,M3,M4] **Three Uses of Space**: arrangements can simplify choice, simplify perception, or simplify internal computation. Cooking, assembly, packing, and Tetris illustrate spatial action as part of thinking. A movement that seems redundant relative to physical progress may reduce cognitive difficulty. Evaluate the combined cost of action and reasoning before optimizing the movement away.

### 11. Lespérance and Levesque — Indexical knowledge and robot action (p. 435)

- [M1,M3,M4] **Indexical vs. Objective Knowledge**: knowing an object's position relative to oneself can suffice to act without knowing its absolute coordinates. Their modal-logical account specifies knowledge prerequisites and effects in this setting. Logic is therefore compatible with situated knowledge; do not treat every logical formalism as committed to a complete detached world model.

### 12. Lyons and Hendriks — Exploiting patterns of interaction (p. 483)

- [M1,M3,M4] **RS Process Algebra; Reaction Construction**: analyze a procedural environment model to derive useful context-sensitive action descriptions, including servo-like ways of exploiting dynamics. These feed an Interval Temporal Logic planning framework. The resulting actions depend on the modeled dynamics and cannot be transferred by retaining their names alone.

### 13. Rosenschein and Kaelbling — Representation and control (p. 515)

- [M1,M2,M3,M4] **Situated-Automata Theory**: describe what computational states indicate about an environment using a rigorous semantic relation, without requiring symbolic interpretation at runtime. The guarantee depends on how the machine is situated and how its states track conditions. Design-time logical justification and runtime symbolic reasoning are separate issues.

### 14. Schoppers — A space-faring rescue controller (p. 541)

- [M1,M3,M4] **Universal Plan; Goal-Directed Active Perception**: the EVAR controller acts on estimates, observes progress, and exploits orbital and subsystem dynamics. Often it is appropriate to wait while dynamics do useful work. The paper analyzes conditions for robustness despite imperfect estimates; its prototype argument is not a flight-certification claim.

### 15. Shoham and Tennenholtz — Social laws, off-line design (p. 597)

- [M1,M3,M4] **Social Laws for Artificial Agent Societies**: constrain individual behavior in advance to make coexistence and goal achievement possible. Assess what restrictions preserve useful possibilities for participants and what the model assumes about their compliance. An admissible coordination law in a formal society is not thereby a legitimate policy for humans.

### 16. Webber and colleagues — Instructions, intentions, and expectations (p. 619)

- [M1,M3,M4] **AnimNL; Interpretation During Action**: instructions contribute intentions and expectations that complement environmental information. Their interpretation can develop as action unfolds, so language understanding cannot always be isolated as a completed front-end translation. State how perception updates the meaning of an instruction and how resulting expectations guide activity.

### 17. Whitehead and Lin — Non-Markov decision processes (p. 637)

- [M1,M2,M3] **Hidden State Tasks; Markov Assumption**: the agent's current representation must contain information relevant to predicting action effects for the usual Markov formulation. Limited sensors and controllable sensing can violate that condition even when the underlying environment admits a state model. Distinguish environmental state from current observation.
- [M1,M3,M4] **Consistent Representation (CR) Method**: first choose perceptual actions to obtain an adequate representation, then choose overt action. It unifies approaches including Lion, G-algorithm, and CS-QL. It assumes suitable sensing can identify the relevant current condition; it is unsuitable where information must be remembered across time.
- [M1,M3] **Stored-State Algorithms**: combine current input with maintained internal state when immediate sensing cannot disambiguate the situation. A better current observation and a history-sensitive representation solve different problems. Choose based on what is hidden and whether present sensing can recover it; the reference does not reproduce individual algorithm convergence proofs.

## Worked Example

[M1,M3,M4] **Reconstructed from Kirsh's spatial analysis (p. 397 onward).** A person rearranges task materials so that the next choice is easier to see, or manipulates a Tetris piece to expose its relation to available space. An action-only model can count the move as unnecessary because it does not directly advance the final arrangement. A model including perception and computation can explain its contribution. Before deleting the move from a workflow, test whether the replacement preserves those cognitive benefits. The categories distinguish simplified choice, perception, and computation; this example compresses their use rather than reproducing an experiment or effect size.

## Decision Rules & Judgment

- [M1,M3] If a mechanism looks unexpectedly simple, inspect the environmental constraints supporting it.
- [M1,M2] If learning fails, distinguish stochastic transitions, noisy observations, unknown actions, and inadequate state representation.
- [M3,M4] If an agent changes its environment, include the setup and maintenance work when assessing performance.
- [M1,M3] If a formal guarantee is transferred, carry its objective, state definition, environment constraints, and execution assumptions with it.
- [M1,M4] If comparing “reactive” and “deliberative” systems, compare actual runtime and design-time mechanisms rather than treating the labels as exclusive camps.

## Key Takeaways

1. [M1,M4] The explanatory unit often includes the environment.
2. [M3] Specialization is defensible when its conditions are explicit.
3. [M1,M3] Situated action admits several competing formal approaches.
