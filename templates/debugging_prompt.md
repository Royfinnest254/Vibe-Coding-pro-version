# Debugging Prompt Template

Use this prompt template when encountering an error, crash, or unexpected behavior. This guides the AI to analyze the root cause before attempting code edits.

```markdown
Here is an issue that needs debugging:

EXACT ERROR MESSAGE / LOG:
[Paste the raw error message, stack trace, browser console log, or server log here]

REPRODUCTION STEPS:
[List the exact steps, inputs, or navigation actions that trigger this error]

INSTRUCTIONS:
1. Do not modify or edit any files yet.
2. Explain the root cause of this error in plain English.
3. Show exactly where the error occurs (files and line numbers).
4. Propose a specific fix and list all files that will be touched by it.
5. Wait for my approval before making any code modifications.
```
