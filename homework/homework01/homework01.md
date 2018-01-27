# Homework 1
#### Allison Morgan

> 1. Define the term essential difficulties as it is used by Brooks. Provide background and context with your answer and at least one example of an essential difficulty.

Brooks divides the difficulties of software technology development into two categories: those that are "essential", and those that are "accidental". Essential difficulties are inherent to software engineering. For example, software is inherently complex. The process of scaling up a personal project to one which will support a wider variety of inputs and outputs, and will work continuously, requires introducing new unique structures within code, and new states in which new types of data might be analyzed or generated.

> 2. Define the term accidental difficulties as it is used by Brooks. Provide background and context with your answer and at least one example of an accidental difficulty.

Unlike essential difficulties, accidental difficulties are not inherent, and arise in the process of software development (e.g. the development of a new feature, may have resulted in new a bug). Brooks argues that most developments to software engineering address these accidental difficulties.

Three developments to software which have reduced accidental difficulties are: (1) high-level languages, (2) time-sharing, and (3) unified programming environments. For example, high-level languages reduce the overall complexity by allowing users to avoid the low-level interactions within your computer (e.g. those dealing with bits and channels).

> 3. List and briefly describe the four essential difficulties of developing software systems that Brooks identifies. Provide additional examples of each type of the four essential difficulties.

The four properties of essential difficulties are: complexity, conformity, changeability, and invisibility.

- **Complexity:** Arises from the fact that no two parts are alike within software engingeering. And because of this, the process of scaling up software is necessarily more complex, since this requires the introduction of more parts, and typically the various states which software can live in has increased nonlinearly. 
- **Conformity:** Arises from arbitrary complexity - restrictions developed by humans or organizations and with no hopes of reduction via some underlying principle. For example, version updates to third-party APIs require maintenance on a project's development to continue to conform to the requirements and output of those APIs. A change such as this one, can be hard to predict, and so, one must wait for it to occur.
- **Changeability:** Arises from the constant pressure to change. For example, as software starts being used, developers begin to extend their software to better meet users' needs - extending to new use cases, or supporting different operating systems.
- **Invisibility:** Arises from the fact that software is not easily visualized. Diagramming the flow of data or the dependency graph generates several superimposed directed networks, which cannot be embedded in a low-dimensional space.

> 4. Define what Brooks means by a silver bullet and reconstruct his argument as to why he believes there is no silver bullet for software engineering.

Here, a silver bullet refers to a single development in software engineering technology that results in 10 fold increase in efficiency, reliability, or simplicity. Brooks believes that most developments in software engineering are to reduce accidental difficulties. (Though he proposes developments which may reduce essential difficulties.) And therefore, to reduce system complexity by an order of magnitude, 
- (a) it would need to be the case that these accidental difficulties consitute a large fraction of software development, and further, 
- (b) that a single technique would reduce the majority of these accidental difficulties. 

Brooks believes neither (a) or (b) to be the case: that essential difficulties generate a not-insignificant contribution, and because each new development is prone to new bugs, it's likely that no single tool will work across the board.

> 5. In lecture, software engineering's relationship to computer science was described by analogy by discussing the differences between a chemist (chemistry) and a chemical engineer (chemical engineering). Define software engineering and its relationship to computer science; make use of the chemist vs. chemical engineer analogy when answering this question.

Just as a chemist is concerned with the theoretical findings of atoms and elements, a computer scientist could be interested in the development of new algorithms or data structures. Motivated by the chemist's work, a chemical engineer considers combinations of atoms or elements under practical constraints (e.g. the need for a material which can withstand a particular temperature), just as a software engineer may build upon a computer scientist's algorithm and apply it to a particular problem (e.g. implementing PageRank at scale).

> 6. In lecture, we discussed the importance of the following concepts to software engineers: abstractions, conversations, specification, translation, and iteration. Define each of these concepts as they are related to software engineering and discuss their importance.

- **Abstractions:** Turn the software problem into something that is well-defined, understandable, and at the appropriate level of complexity for your application.
- **Conversations:** Can help a developer better understand the software problem at hand, or the code being developed upon, or help understand if our software is working. 
- **Specification:** Defines the software requirements and design. Important for others looking to use a software package.
- **Translation:** Converts one set of structures or abstractions to another. Important for reaching the level of abstraction convient for developers.
- **Iteration:** Develops software, step by step or version by version, until we decide to stop. Leads to packages which are in keeping with the needs of its users.
