# Security Review Prompt Template

Use this prompt template to perform a quick security audit on a completed feature or plan before merging.

```markdown
Review the proposed implementation against the 5 security non-negotiables:

1. **Permission Checks**: Are authorization and permission checks performed on the server (behind the API), rather than just hiding UI components in the browser?
2. **Secrets & Keys**: Are there any API keys, passwords, credentials, or private URLs written directly in the code (especially frontend client files) instead of environment variables?
3. **Input Validation**: Is every field in every user input validated and cleaned on the server before database write or processing?
4. **Rate Limiting**: Are public or unauthenticated endpoints rate-limited to prevent abuse or bot spam?
5. **Data Isolation**: Does every database query verify record ownership, ensuring one user cannot fetch or modify another user's records simply by changing an ID parameter?

For each rule:
- Answer YES or NO.
- State exactly where in the codebase this rule is enforced (file and line numbers).
- Highlight any concerns or remediation steps if a rule is not fully satisfied.
```
