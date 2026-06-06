# Chapter 1: The Build System (The 8 Disciplines)

### 4. Spec before code — *kills "logic drift"*

**The failure:** As the project grows, it is less like a contractor who remembers your project and more like briefing a brand-new one every morning. The chat-based AI holds limited memory, leading to quiet rebuilds and conflicting methods.

**The fix — the spec is the truth, not the chat.** Write down what you want in a durable document and have the AI build *from it* every time.
- **The Constitution / `AGENTS.md`** (written once): standing rules every build obeys.
- **The Feature Spec** (per feature): what it does, who can use it, and the **acceptance criteria** — the exact "it's done when…" checklist.

---

### 5. Prompting as spec-writing — *kills the vague-prompt disaster*

**The failure:** Prompting for a "vibe" leads to a vibe-sized blast radius where unrelated code is rewritten or broken.

**The fix — a good prompt is a tiny spec with guardrails.** Anatomy of a good prompt:
1. **Context** — *"Read the spec and AGENTS.md first."*
2. **The change** — one clear thing, one paragraph.
3. **Blast radius** — *"Tell me which files this touches and what could break."*
4. **Constraint** — *"Don't touch anything outside that. Don't 'improve' unrelated code."*
5. **Plan-gate** — *"Show the plan and wait for my 'go' before writing code."*
6. **Done-check** — *"When done, tell me how to confirm it against the acceptance criteria."*

---

### 6. Git, your safety net — *kills the catastrophe of lost work*

**The failure:** Large, sudden changes fast, leading to catastrophic losses when a tool refactors incorrectly.

**The fix — Git is safety equipment, not a developer hobby.** 
- **A commit is a checkpoint** — a saved snapshot you can always return to. Commit *constantly* (every working change).
- **A branch is an experiment** — a parallel copy to try something risky; if it breaks, throw it away.
- **A push is a backup** — sent to GitHub.

---

### 7. Build in small slices — *kills the "70% wall"*

**The failure:** Piling on large features in big sweeping prompts leads to untangling cascading errors.

**The fix — one slice, one checkpoint, one check.** A slice is *the smallest thing that's whole on its own and that you can verify before moving on.* Trade the *feeling* of speed (one giant prompt) for *actual* speed (no untangling later).

---

### 8. Security you can't skip — *kills bypasses, leaks, and data theft*

**The failure:** Skip the guards because "it runs" without them, leading to paywall bypasses, rate limit failures, or data leaks.

**The fix — enforce the 5 security non-negotiables:**
1. **Permission checks on the server, not the browser.** Decide authorization behind the API.
2. **Secrets live only on the server**, in env vars, never committed to Git.
3. **Never trust what users type.** Clean and validate inputs on the server.
4. **Rate limit** public endpoints to prevent bot abuse.
5. **Check who can see whose data** on every database read.

---

### 9. Verification — *kills the step every broken app skipped*

**The failure:** Code passes a manual click-through, but fails in production where edge cases or direct API calls bypass the UI.

**The fix — three layers of verification:**
- **Check against the spec.** Walk the acceptance criteria one by one.
- **Walk the unhappy paths.** Empty form, giant input, double-click, expired session.
- **Go around the front door.** Test the server API directly. Does the paywall still hold? Can a user read another's data?

---

### 10. Ship & maintain — *kills "never launched" and "rotted"*

**The failure:** Deployment feels like a wall, or code becomes an unmaintainable tangle because decisions lived only in chats.

**The fix — standard shipping discipline:**
- Frontend on Vercel, backend/database on a managed host (Supabase).
- Set secrets as env variables on the host.
- Configure CORS so the live frontend can call the live backend.
- The spec and `AGENTS.md` are the memory. Change the spec first, then rebuild.
