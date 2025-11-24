# Scope of ASEN 3502: Computational Methods

## Topics

A topic is a broad subject area or category of study within a course. It provides the context or "bucket" for learning.

For example, in ASEN 3402: Aerospace Heat Transfer, conduction, radiation, and convention are topics.

### CLO1: Numerical Methods

- Numerical solution of linear algebraic equations
- Numerical solution of nonlinear algebraic equations
- Numerical solution of ODEs (IVPs and BVPs)
- Numerical optimization
- Regression and data-fitting
- Visualizing and interpreting computed results

### CLO2: Problem Formulation

- Construction of mathematical model from physics
- Identifying key assumptions and neglected effects
- Qualitative understanding of well-posedness (existence, uniqueness, stability)
- Classification of mathematical models (algebraic, ODE, optimization)
- Domain of validity and physical interpretation

### CLO3: Evaluation

- Grid/time-step refinement and empirical order estimation
- Stability analysis, stiffness, and time-step limits (e.g., CFL number)
- Performance profiling and scalability
- Verification (against benchmark or analytical solutions)
- Validation (against experimental data)
- Presenting and defending computational decisions with evidence

### CLO4: Implementation

- Scientific programming in MATLAB
- Modular code structure and testing frameworks
- Performance profiling and vectorization
- Version control (Git/GitHub) for collaborative labs and projects
- Technical communication

### CLO5: Self-Learning

- Exploration of external aerospace-related libraries
- Adapting third-party algorithms or data sources
- Designing small experiments to test or verify new methods
- Summarizing and presenting self-directed work to peers

### CLO Matrix

| Topic                                        | 1 | 2 | 3 | 4 | 5 |
|----------------------------------------------|---|---|---|---|---|
| Linear algebraic equations                   | X |   |   |   |   |
| Nonlinear algebraic equations                | X |   |   |   |   |
| ODEs (IVPs and BVPs)                         | X |   |   |   |   |
| Numerical optimization                       | X |   |   |   |   |
| Regression and data-fitting                  | X |   |   |   |   |
| Visualizing and interpreting results         | X |   |   |   |   |
| Mathematical model construction              |   | X |   |   |   |
| Assumptions and neglected effects            |   | X |   |   |   |
| Well-posedness                               |   | X |   |   |   |
| Model classification                         |   | X |   |   |   |
| Domain of validity and interpretation        |   | X |   |   |   |
| Grid/time-step refinement                    |   |   | X |   |   |
| Stability analysis and time-step limits      |   |   | X |   |   |
| Performance profiling and scalability        |   |   | X | X |   |
| Verification                                 |   |   | X |   |   |
| Validation                                   |   |   | X |   |   |
| Presenting computational decisions           |   |   | X |   |   |
| Scientific programming in MATLAB             |   |   |   | X |   |
| Modular code structure and testing           |   |   |   | X |   |
| Version control (Git/GitHub)                 |   |   |   | X |   |
| Technical communication                      |   |   |   | X |   |
| Exploration of external libraries            |   |   |   |   | X |
| Adapting third-party algorithms              |   |   |   |   | X |
| Designing experiments for new methods        |   |   |   |   | X |
| Presenting self-directed work                |   |   |   |   | X |



## Concepts

A concept is a fundamental idea, principle, or relationship that helps explain how things work within a topic. It builds understanding of the theory behind engineering phenomena.

Concepts are being developed in [this google spreadsheet](https://docs.google.com/spreadsheets/d/1NU_O-n32ccqgSSqnjh-YYHleyFIDzCBkznIUxrpPsAk/edit?usp=sharing) (you will need your CU account to access it).

> [!NOTE]
> I assigned each concept to a "seed" topic, but, since most concepts have an Error Analysis and Control component, I did not use that as a seed topic.

> [!NOTE]
> In the CLO table, I am least confident about the Evaluation CLO. I basically linked concepts to this CLO if I could think of a theoretical basis for evaluating them. This is not very rigorous or reliable.

## Skills

> [!NOTE]
> Skills are a work in progress! I have not had a chance to develop the skills yet.

A skill is a practical ability to apply concepts to solve problems, analyze systems, or design solutions.  It focuses on application - what a student can do with their knowledge attained in a class.

- Reasoning about an algorithm apart from implementation (i.e. with pseudocode) [Essential]
    - Correctness
    - Complexity
    - Accuracy
- Translating a concrete engineering problem into a computational problem (perhaps not essential because they do this in other classes) [Highly desirable]
- Defining an algorithms that operationalizes a methods studied in the course [Highly desirable]
- Implementing an algorithm as an efficient computer program [Essential]
- Using code written by others and writing code for others to use [Somewhat desirable]
- Finding and implementing an algorithm to solve an engineering problem without previous exposure to the algorithm [Highly desirable]
- Using a computer to solve a simple example of the following problems:
    - Systems of linear algebraic equations [Essential]
    - Systems of nonlinear algebraic equations [Somewhat desirable]
    - Ordinary differential equations [Essential]
    - Partial differential equations [Highly desirable]
    - Optimization problems [Highly desirable]
    - Regression problems [Essential]
