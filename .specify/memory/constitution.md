# Evolution of Todo - Phase I: In-Memory Python Console Application Constitution

## Core Principles

### Spec-Driven Development
All features must originate from markdown specifications; no manual coding permitted. Every implementation must be traceable to a specification document in /specs_history folder.

### AI-First Architecture
Claude Code generates 100% of implementation code from refined specifications. Human intervention is limited to specification creation, refinement, and validation of output.

### Iterative Refinement
Specifications must be refined until Claude Code produces correct, working output. No manual fixes to generated code are allowed - only spec improvements.

### Clean Code Standards
Generated code must follow Python best practices, proper structure, and maintainability principles. Code must pass basic Python linting standards.

### Console-First Interface
All application functionality must be accessible via console commands. Focus on clear user feedback and robust input validation in console environment.

### In-Memory Data Management
Data storage is limited to in-memory only for Phase I. No persistence mechanisms outside of application memory. Proper data validation and error handling required.

## Technology Compliance
- Python version: 3.13+
- Package manager: UV exclusively
- Development tools: Claude Code + Spec-Kit Plus
- Environment: WSL 2 for Windows users (Ubuntu 22.04)
- No database, API, or cloud deployment in Phase I

## Development Workflow
1. Write specification in markdown format in /specs_history
2. Submit to Claude Code via Spec-Kit Plus workflow
3. Review generated code against acceptance criteria
4. Refine spec if output is incorrect (no manual code fixes allowed)
5. Iterate until Claude Code generates correct implementation
6. All features must have dedicated spec files before implementation

## Quality Gates
- All 5 core features must be fully implemented (Add Task, View Tasks, Update Task, Delete Task, Mark Complete/Incomplete)
- Code must prevent application crashes through proper error handling
- User input validation must be robust
- All features must be demonstrable via console commands
- Data must persist during single session (in-memory)

## Governance

This constitution defines the mandatory practices for the Evolution of Todo - Phase I project. All development activities must comply with these principles. Amendments require explicit documentation of changes, approval from project stakeholders, and a migration plan for existing artifacts. All pull requests and code reviews must verify constitution compliance. Development complexity must be justified against these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
