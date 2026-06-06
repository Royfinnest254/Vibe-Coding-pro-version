# Chapter 0: Introduction & Foundations

## PART 0 — HOW TO USE THIS

The gap this closes is **judgment and direction**: telling the AI exactly what a senior engineer would, spotting when it does something dangerous, and fixing things calmly when they break. You don't learn to write code. You learn what to *specify* and what to *check*.

### The build rhythm (tape this to your monitor)

```
   ┌─────────────────────────────────────────────────────────────┐
   │  1. SPEC      → write what you want + "done when" criteria    │
   │  2. PLAN      → make the AI plan it; you approve before code  │
   │  3. COMMIT    → checkpoint before any big change              │
   │  4. SLICE     → build ONE small piece                         │
   │  5. CHECK     → does it match the spec? unhappy paths? server?│
   │  6. COMMIT    → works → save it. broken → roll back, re-slice │
   │  ↺ repeat from 4 for the next slice                           │
   └─────────────────────────────────────────────────────────────┘
```

### The first 30 minutes of ANY new project (the startup ritual)

Do these before building a single feature. It's the difference between an app that holds together and one that fights you by week two.

1. **New folder, new Antigravity workspace.** One project = one folder = one workspace. Never mix projects in one thread.
2. **Set up Git immediately and push to GitHub.** Your undo button, in place *before* you can lose anything.
3. **Drop in your `AGENTS.md` rules file.** This is your always-on technical layer — security non-negotiables, process rules, stack. Set once, obeyed every task.
4. **Lock your stack** in the rules file so the AI can't drift between tools.
5. **Write the one-paragraph "what this is."** What the app does, who uses it, and what *"works"* means (not "runs" — what does good look like to a real user?).
6. **Write the spec for your first feature** with "done when" criteria *before* prompting anything.

Thirty minutes here saves you days later. Every time.

---

## PART 1 — FOUNDATIONS

### 1. The mindset: you're the director and verifier

The AI is the fastest junior developer alive: brilliant, tireless, literal, and with zero stake in the outcome. It does what you say, not what you meant, and it doesn't care if the result is safe. **If nobody is the engineer, the project has no engineer — and now that's you.** Your value isn't typing. It's *direction* and *verification*.

**Your operating rule, forever:** *"It runs" is not "it works." My job is to make it work.* "Runs" = the screen lit up and nothing crashed. "Works" = it does the right thing, for the right people, safely, and still will next month.

### 2. The map of the house (architecture you reason and prompt with)

You don't hand-build architecture. You use it as a *map* — to prompt precisely and to spot when the AI puts something in the wrong place. Every web app is the same handful of pieces:

- **Frontend (the storefront).** Everything in the user's browser — pages, buttons, forms. **The one fact that matters most: the user can see and change anything here.** So nothing you need to keep honest can live only in the frontend.
- **Backend (the back office).** The server you control, where real decisions happen — "is this slot free?", "is this person allowed?", "save this." The user can't see or touch it. **This is where trust lives.**
- **Database (the filing cabinet).** Where information is stored so it survives. Usually *relational* (PostgreSQL — neat connected tables, best when things relate).
- **API (the order window).** How the storefront talks to the back office. The frontend never touches the database directly — it passes a request through the API and gets an answer.
- **Auth (the lock and the keycard).** *Authentication* = who are you (login). *Authorization* = what you're allowed to do (owner opens billing; staff doesn't).
- **Deployment / hosting (the building with an address).** Where it all lives so strangers can visit.

**Before building any feature, answer four questions out loud:**
1. What does the user *see*? (frontend)
2. What decision must be *trusted*, so it lives on the server? (backend)
3. What must be *remembered* after they close the tab? (database)
4. Who is *allowed* to do this? (authorization)

### 3. Choosing your stack (sensible defaults)

Pick once, write it into `AGENTS.md`, and don't let the agent switch tools mid-project.

*   **Frontend**: React + Next.js
*   **Styling**: Tailwind CSS
*   **Language**: TypeScript (catches mistakes before they ship)
*   **Database + Auth + Storage**: Supabase (hosted PostgreSQL with built-in APIs and auth)
*   **Backend logic**: Next.js API routes or Node + Express
*   **Payments**: Stripe
*   **Email**: Resend
*   **Hosting**: Vercel (frontend) + Supabase (database)
