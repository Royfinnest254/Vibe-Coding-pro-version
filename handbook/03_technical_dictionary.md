# Chapter 3: The Technical Dictionary

A comprehensive glossary of modern web engineering terms, defined simply and showing exactly how to use them when prompting or reviewing.

---

## SECTION 1 — THE BIG PICTURE (How an App is Shaped)

*   **Full-stack** — An app that has both a frontend (what users see) and a backend (the server + database).
*   **Frontend (client / client-side)** — Everything running in the user's browser (pages, buttons, forms). *Nothing here can be trusted entirely since users can manipulate browser states.*
*   **Backend (server / server-side)** — The part you control that the user cannot see or touch. *This is where trusted business rules, logins, and validations live.*
    *   *Prompt Pattern:* `"Validate the user's eligibility and check plan limits on the server, not in the client."`
*   **Database** — The storage system where data persists after the user closes their browser tab.
*   **API (Application Programming Interface)** — The messenger between frontend and backend.
*   **Request / Response Cycle** — The heartbeat of the web: Browser sends a *request* (e.g., "book slot") → server processes it → server sends a *response* back (e.g., "success").
*   **The Stack** — The specific set of technologies your app is built from (e.g., React, Express, Supabase).
*   **Environment (dev / staging / production)** — *Dev* is local building; *staging* is a private test copy online; *production (prod)* is the live site accessed by real users.
*   **Localhost** — Your app running on your own computer, typically at an address like `localhost:3000`.
*   **Monolith vs. Microservices** — *Monolith* is the entire app in one single codebase (simplest and best for most apps). *Microservices* are chopped up into independent services.

---

## SECTION 2 — FRONTEND (What Users See & Touch)

*   **HTML** — HyperText Markup Language. The structural skeleton of a web page (headings, paragraphs, inputs).
*   **CSS** — Cascading Style Sheets. The styling layers (colors, layouts, spacing, sizes).
*   **JavaScript (JS)** — The programming language that runs in the browser to make pages interactive.
*   **TypeScript (TS)** — A structured version of JavaScript that catches spelling mistakes and type mismatches before they build. Highly recommended for AI development.
*   **React** — The most popular frontend library. UI is constructed out of reusable modular blocks called *components*.
*   **Next.js** — A framework built on React that handles page routing, server components, and optimizations automatically.
*   **Component** — One reusable UI piece (e.g., a button, a booking form).
*   **Props** — External parameters passed into a component to configure it.
*   **State (frontend)** — The live memory of a component (e.g., text typed in a form, whether a dropdown is open).
*   **Responsive Design** — Making sure layouts adapt fluidly to screen sizes from phones to widescreen monitors.
*   **DOM (Document Object Model)** — The browser's active internal tree structure of your webpage.
*   **Render** — The process of the browser drawing or updating the UI on the screen.

---

## SECTION 3 — BACKEND (The Trustworthy Side)

*   **Server** — The remote, always-on computer that processes API requests, runs backend logic, and connects to the database.
*   **Runtime** — The engine that executes your backend code (e.g., Node.js, Go).
*   **Express** — A minimalist framework for Node.js used to build API endpoints quickly.
*   **Business Logic** — The absolute rules of your business (e.g., "cannot book a slot in the past", "maximum of 3 draft accounts"). *Always enforce this on the server.*
*   **Endpoint / Route** — A specific address on the server that performs an action (e.g., `POST /api/bookings`).
*   **Middleware** — Helper functions that run *between* the arrival of a request and the final handler (e.g., checking if a user is logged in before letting them see the dashboard).
*   **Serverless** — Backend code that runs inside temporary, on-demand containers instead of a dedicated server.

---

## SECTION 4 — DATABASE & DATA (What gets remembered)

*   **Schema / Data Model** — The blueprint of how data is structured, defining what tables exist and how they relate.
*   **Table (SQL) / Collection (NoSQL)** — A structured group of similar records (e.g., a `users` table).
*   **Row / Record** — A single item in a table (e.g., User ID #1052).
*   **Column / Field** — An attribute of a record (e.g., `email_address`).
*   **Relational Database (SQL)** — Highly structured tables that link together via IDs (e.g., PostgreSQL, MySQL). Recommended default.
*   **NoSQL / Document Database** — Flexible folders of JSON documents (e.g., MongoDB).
*   **Primary Key** — The unique ID that identifies a specific record in a database table.
*   **Foreign Key** — A field in one table that references the primary key of another table, creating a relationship.
*   **ORM (Object-Relational Mapping)** — A translation tool (like Prisma or Drizzle) that lets you talk to the database using standard code instead of raw SQL queries.
*   **Migration** — A version-controlled script that safely updates the structure of your database without deleting existing data.
*   **Seed Data** — Fake mock data inserted into the database during development to test UI elements.
*   **Constraint (Unique / Not-Null)** — Rules enforced by the database (e.g., "no two accounts can have the same email address").
*   **CRUD** — Create, Read, Update, Delete. The 4 fundamental actions of any database application.
*   **Soft Delete** — Marking a record as `deleted = true` instead of permanently erasing it, preserving history.
*   **Transaction** — A database operation where all actions must succeed together, or none do (e.g., making a payment and booking a ticket must occur as a single transaction).

---

## SECTION 5 — APIs & HOW THINGS TALK

*   **REST** — Representational State Transfer. The standard API pattern mapped to URLs and HTTP verbs.
*   **HTTP Methods (Verbs)** — The type of action: `GET` (fetch data), `POST` (create new), `PUT`/`PATCH` (update existing), `DELETE` (remove).
*   **JSON** — JavaScript Object Notation. The universal, human-readable text format used for sending data over the internet.
*   **Status Code** — The server's short verdict: `200` (OK), `201` (Created), `400` (Bad Request), `401` (Unauthorized), `403` (Forbidden), `404` (Not Found), `409` (Conflict), `500` (Server Error).
*   **Headers** — Metadata sent alongside requests/responses (e.g., authentication keys, content type format).
*   **Query Parameters** — Filters appended to URLs (e.g., `/bookings?status=confirmed`).
*   **Webhook** — An automatic request sent from an external service (like Stripe) to *your* backend when an event happens (e.g., "payment succeeded").
*   **Rate Limiting** — Capping requests to block scrapers, attackers, or runaway loops.
*   **CORS (Cross-Origin Resource Sharing)** — The browser security check defining which domains are allowed to talk to your backend.
*   **Idempotency** — Ensuring that repeating an API call multiple times does not result in duplicate actions (e.g., double-clicking a submit button).

---

## SECTION 6 — AUTH (Who you are & what you can do)

*   **Authentication (AuthN)** — Proving *who you are* (e.g., logging in with email and password).
*   **Authorization (AuthZ)** — Checking *what you are allowed to do* (e.g., checking if user is an Admin before deleting data).
*   **Session** — The temporary memory stored on the server that keeps a user logged in.
*   **Token / JWT (JSON Web Token)** — A cryptographically signed digital security badge passed in headers on every API request.
*   **Cookie** — A small text storage in the browser managed directly by HTTP headers. Safe from typical script theft if set as `HttpOnly`.
*   **Hashing** — Scrambling passwords one-way so they can never be decoded. Plaintext passwords must *never* be saved.
*   **OAuth / SSO (Single Sign-On)** — Allowing users to sign in using existing credentials from Google, GitHub, or Apple.
*   **RBAC (Role-Based Access Control)** — Structuring permissions based on defined roles (e.g., Owner, Manager, Employee).

---

## SECTION 7 — DEPLOYMENT & INFRASTRUCTURE

*   **DNS (Domain Name System)** — The phonebook of the web. It translates human-friendly domains (e.g., `myapp.com`) to computer-readable IP addresses.
*   **A Record / CNAME** — *A Record* points a domain to a physical server IP. *CNAME* redirects a subdomain to another domain.
*   **DNS Propagation** — The global distribution delay (up to 48 hours) as internet servers update their DNS records.
*   **SSL / TLS (HTTPS)** — Secure encryption of all web traffic between client and server. 
*   **Environment Variables (`.env`)** — Key-value pairs stored securely on the hosting server to manage keys and passwords outside of version-controlled code.

---

## SECTION 8 — TESTING & QUALITY

*   **Unit Test** — Code that tests a single function in complete isolation.
*   **Integration Test** — Code that tests how several parts of an application interact together.
*   **End-to-End (E2E) Test** — Automated scripts that load a headless browser and click through actual user flows (e.g., opening the app, logging in, making a payment).
*   **Linter** — An automated code reviewer (like ESLint) that flags formatting problems, syntax errors, and suspicious code patterns before building.
