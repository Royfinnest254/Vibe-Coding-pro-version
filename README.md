# The Vibe Coder's Handbook (Pro Version)

Welcome to the Pro Version repository of the Vibe Coder's Handbook. This repository contains the complete structured guide, rulesets, and ready-to-copy prompt templates for pair programming with Antigravity to build high-quality full-stack applications safely.

## Repository Layout

*   [AGENTS.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/AGENTS.md) — The universal constitution file with coding, design, security, and verification rules. Copy this to the root of any new project.
*   `handbook/` — Individual guide chapters:
    *   [00_introduction.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/handbook/00_introduction.md) — Mindsets, map of the house, and default technology stack choices.
    *   [01_build_system.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/handbook/01_build_system.md) — The 8 disciplines of building with AI (Spec, Prompting, Git, Slices, Security, Verification, Shipping).
    *   [02_driving_antigravity.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/handbook/02_driving_antigravity.md) — Token optimization, plan/diff reviews, debugging playbook, and red flags checklist.
    *   [03_technical_dictionary.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/handbook/03_technical_dictionary.md) — The complete glossary of web development terms for prompting.
*   `templates/` — Copy-paste prompt templates and checklists:
    *   [technical_spec_prompt.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/templates/technical_spec_prompt.md) — The 6-part feature brief skeleton.
    *   [security_review_prompt.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/templates/security_review_prompt.md) — Quick security review checks.
    *   [debugging_prompt.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/templates/debugging_prompt.md) — Root-cause debugging guide.
    *   [launch_checklist.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/templates/launch_checklist.md) — The pre-ship quality gate.

---

## The Build Rhythm

Always follow this loop when developing features:

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

## The Startup Ritual (First 30 Minutes of any Project)

1. **New Folder, New Workspace**: Keep one project per workspace/thread. Never mix contexts.
2. **Setup Version Control**: Initialize Git, create `.gitignore` (excluding `.env`, etc.), and make the initial commit.
3. **Set Universal Rules**: Drop [AGENTS.md](file:///c:/Users/roych/OneDrive/Pictures/Vibe%20coding/AGENTS.md) in the root.
4. **Lock Your Stack**: Formally declare your technologies (React, Supabase, Tailwind, etc.) inside `AGENTS.md`.
5. **Write What This Is**: Author a one-paragraph definition of what "works" means for this app.
6. **Spec the First Slice**: Write the spec for your first micro-feature *before* you prompt any code.
