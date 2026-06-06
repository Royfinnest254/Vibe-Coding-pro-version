# Feature Specification Prompt Template

Copy and paste this template when prompting Antigravity to build a new feature or modify an existing one. Fill in the brackets with details and remove unused constraints.

```markdown
FEATURE: [Short, one-line feature name]

WHAT IT DOES (Plain language, one paragraph):
[Describe what the user experiences, start to finish, and what the user value is]

DATA MODEL (What's stored and how it relates):
- [Entity Name], fields: [field_name: type, constraints, e.g., "email: text, required, unique"]
- [Entity Name] belongs to / has many [Entity Name]
- Relational database (PostgreSQL/Supabase)

WHO CAN DO WHAT (Roles & Permissions):
- Logged out user: can [...], cannot [...]
- [Role/User type]: can [...], cannot [...]
- Enforce ALL permission checks on the SERVER.

RULES THE SERVER MUST ENFORCE (Business logic, not UI styling):
- [e.g., "A booked slot is never offered to another user again"]
- [e.g., "Free plan limits block the 51st booking on the server-side API"]

INPUTS & ERRORS:
- Validate every input on the server: [Specify fields and validation rules]
- Handle edge cases: empty form submissions, duplicate submits, expired sessions. Do not fail silently.

INTEGRATIONS / SECRETS:
- Uses [Service/API name]. API key is a SERVER-SIDE secret managed in environment variables.

DONE WHEN (Acceptance Criteria — how this will be verified):
- [ ] [...]
- [ ] [Security-critical criterion]
- [ ] [Happy path test]
- [ ] [Unhappy path test]

CONSTRAINTS:
- Create an implementation plan as an Artifact first; wait for my approval before writing code.
- Touch only the files absolutely required for this feature.
- Do not refactor unrelated code.
- Follow the rules defined in AGENTS.md.
```
