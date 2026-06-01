# Chapter 2: Driving Antigravity & Debugging Playbook

## PART 3 — DRIVING ANTIGRAVITY

### 11. How to drive Antigravity right

Antigravity is agent-first "Mission Control," not a chatbot. Avoid long single threads that drift and burn tokens:

1. **Always start in Planning mode. Read the plan before it codes.** Review the implementation plan Artifact first. Catch wrong approaches early.
2. **Set up `AGENTS.md` / Rules once.** This is your always-on technical layer. Set it in the workspace and rules system.
3. **Keep autonomy at "agent-assisted," and commit constantly.** 
4. **One task = one agent = one folder.** Keep tasks scoped. Parallelize if needed.
5. **Use browser automation.** Ask agents to test in a browser, capture recordings, and report results.

### 12. Cost & token management

- Short, scoped tasks beat one giant thread.
- Put stable rules in `AGENTS.md`, not in every prompt.
- Don't paste huge files if the agent can read them from the project.
- Use Planning mode to avoid expensive rebuilds.

### 13. Reviewing the plan & the diff without being technical

Scan the plan or code diff for these 5 indicators:
1. **Scope size**: Too many files touched is a red flag.
2. **Deletions**: Are working functions being rewritten or deleted?
3. **Trust location**: Are checks described as frontend/browser checks? Move them to the server.
4. **Uninvited extras**: Is the agent trying to refactor things you didn't ask for?
5. **Unhappy paths**: Are error cases, empty states, and validations missing?

---

## PART 4 — WHEN THINGS GO WRONG

### 14. The debugging playbook

When something breaks, do not re-prompt blindly with "it's still broken, fix it."

1. **Stay calm; you have Git.** Roll back to the last working commit if needed.
2. **Capture the actual error.** Grab terminal output, browser console logs, or host production logs.
3. **Reproduce it.** Pin down the exact steps that trigger the error.
4. **Ask for the cause *before* the fix.** Ask the AI: *"Explain what's causing this and where, then propose a fix and what it touches."*
5. **Isolate if it's murky.** Add targeted logging to trace the data.
6. **Fix on a branch, verify, then merge.**
7. **Add a test so it can't come back.**

### 15. Red flags in AI output (the judgment checklist)

#### Security Red Flags:
- Check happens in the frontend/browser.
- API keys, passwords, or secrets hardcoded in the codebase.
- No server-side input validation.
- Database read doesn't check record ownership.
- Public endpoints have no rate limiting.

#### Reliability Red Flags:
- Missing error handling.
- Missing loading/empty states in UI.
- Hallucinated libraries or API functions.
- Unrequested modifications to working code.

#### Maintainability Red Flags:
- Sprawling scope (e.g. 15 files changed for a button).
- Duplicated logic (multiple ways of doing the same thing).
- Magic numbers/hardcoded values.
- Lack of comments on non-obvious code.
