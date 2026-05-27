<picture>
  <source media="(prefers-color-scheme: dark)" srcset="connex_logo_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="connex_logo_light.png">
  <img alt="CONNEX" src="connex_logo_light.png" width="220">
</picture>

---

# Go Programming: Learn by Reading CONNEX
### A Beginner's Course Built From the Real Banking System

---

## 🧠 How This Course Was Built — The Science of Learning Faster

Before you read a single line of code, you need to know **why** this course is structured the way it is. Every section follows techniques proven by cognitive science research to make learning stick faster and longer.

| Technique | What It Means | Where You Will See It |
|-----------|--------------|----------------------|
| **Active Recall** | Force your brain to retrieve information instead of just re-reading it | Every Quiz asks you to write from memory before seeing the answer |
| **Spaced Repetition** | Revisit old concepts at regular intervals so they don't fade | The "Review Checkpoint" sections that appear after every 2 chapters |
| **Interleaving** | Mix different concepts in practice instead of drilling one thing | Later quizzes combine concepts from multiple chapters |
| **Feynman Technique** | If you can explain it simply, you truly understand it | Every chapter ends with a "Teach It Back" prompt |
| **Elaborative Interrogation** | Ask "Why?" and "How?" — not just "What?" | Every real code section ends with "Why did they write it this way?" |
| **Concrete Examples First** | Analogies before definitions | Every concept starts with a real-world analogy before the code |
| **Chunking** | Break complex ideas into small, digestible pieces | One concept per section, never more |
| **Immediate Practice** | Apply within minutes of learning | Every section has a hands-on exercise immediately after it |

> ⚠️ **Safety Rule:** Create a folder called `sandbox/` on your Desktop. ALL your practice goes in there. Never edit files inside `cmd/` or `internal/`. You cannot break the bank from your sandbox.

---

## Before You Start: 5-Minute Setup

Open PowerShell and run these commands:

```powershell
mkdir $HOME\Desktop\sandbox
cd $HOME\Desktop\sandbox
go version
```

If `go version` shows a version number, you are ready. If not, download Go from **https://go.dev/dl/** and install it first.

---

---

# Chapter 1: Packages and Imports

---

## 📖 The Analogy First

Imagine you are a chef opening a restaurant kitchen for the day. Before you cook anything you do two things:

1. You declare **which kitchen this is** — "This is the main kitchen, not just a prep room."
2. You gather your **tools from the supply room** — knives, pots, measuring cups.

In Go:
- `package main` = "This is the main kitchen — a runnable program."
- `import (...)` = "These are the toolboxes I need from the supply room."

---

## 🔍 Real Code: `cmd/witness/main.go` — Lines 11 to 27

This is the very first thing written in the Witness Node — the program that cryptographically signs every bank transaction:

```go
package main

import (
    "crypto/ed25519"   // 🔑 Ed25519 cryptographic signature toolbox
    "crypto/rand"      // 🎲 Secure random number generator
    "crypto/sha256"    // 🔒 SHA-256 hashing toolbox
    "encoding/base64"  // 📝 Convert binary bytes → readable Base64 text
    "encoding/hex"     // 🖊️  Convert binary bytes → hex strings like "3f8a1c"
    "encoding/json"    // 📋 Read and write JSON data
    "flag"             // 🚩 Read arguments from the command line
    "fmt"              // 🖨️  Format and print text to the screen
    "log/slog"         // 📓 Structured log messages with key=value pairs
    "net/http"         // 🌐 Build web servers and make HTTP requests
    "os"               // 💾 Read/write files and talk to the operating system
    "path/filepath"    // 📁 Work with file paths safely
    "time"             // ⏰ Dates, clocks, timers, durations
)
```

**Line by line breakdown:**

| Line | What it means |
|------|--------------|
| `package main` | "This file belongs to the `main` package — Go knows it is a complete, runnable program" |
| `import (` | "I am about to list the toolboxes I need" |
| `"crypto/ed25519"` | The `/` is a path separator, not division. This is the `ed25519` package inside Go's `crypto` folder |
| `"fmt"` | Short for "format" — this is the most common toolbox for printing text |
| `)` | End of the import list |

**Why did they import SO many toolboxes?**
Because a Witness Node does many complex jobs: it reads files from disk (`os`), serves a web API (`net/http`), handles cryptography (`crypto/*`), logs messages (`log/slog`), and reads startup settings (`flag`). Each toolbox handles one specific job.

---

## 🧠 Feynman Check — Teach It Back

Close this document. Open a notepad. Write in your own words, as if explaining to a 10-year-old:

> *"What does `package main` mean, and why do we have to import toolboxes?"*

If you can write two sentences that make sense, you understand it. If you struggle, re-read the analogy above.

---

## ❓ Elaborative Interrogation — Ask "Why?"

- **Why** does Go force you to list every import you need instead of just giving you everything automatically?
- **Why** would it be a problem if you imported a toolbox and never used it?

*(Answer: Go refuses to compile if you import something unused. This forces clean, intentional code — especially important in a banking system where every dependency is a potential security risk.)*

---

## ✏️ Quiz 1

**Create:** `sandbox/quiz1.go`

Write a program that:
1. Declares `package main`
2. Imports only `fmt` and `time`
3. Inside `main()`, prints: `"CONNEX Witness — Online"`
4. On the next line, prints the current time

**Run it:** `go run quiz1.go`

---

## ✅ Answer — Quiz 1

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("CONNEX Witness — Online")
    fmt.Println("Current time:", time.Now())
}
```

**Expected output:**
```
CONNEX Witness — Online
Current time: 2026-05-27 18:31:00.123456789 +0300 EAT
```

**Common mistake:** Writing `import "fmt"` and `import "time"` on two separate lines — this works but is not idiomatic Go. Always use the parenthesis block when importing more than one package.

---

---

# Chapter 2: Variables — Storing Data

---

## 📖 The Analogy First

A **variable** is a labeled box in your computer's RAM (temporary memory). You put a value in the box, give the box a name, and then refer to it by name whenever you need the value.

Think of it like Post-it notes on your desk:
- You write `amount = 5000` on a yellow Post-it
- Later, you look at the yellow Post-it whenever you need to know the amount
- You can erase it and write a new value anytime

When your program ends, all the Post-its (variables) are thrown away.

---

## 🔍 Real Code: `cmd/witness/main.go` — Lines 34–35

```go
privPath := keyPath          // Create box named "privPath", fill it with keyPath's value
pubPath  := keyPath + ".pub" // Create box named "pubPath", same value but ".pub" glued on
```

**The `:=` operator does two things at once:** creates the box AND puts a value in it.

If `keyPath` was `"keys/witness.key"`, then after these lines:
- `privPath` holds: `"keys/witness.key"`
- `pubPath` holds: `"keys/witness.key.pub"`

The `+` on strings glues them together — this is called **concatenation**.

---

## 🔍 Real Code: `cmd/gateway/main.go` — Line 198

```go
bundleID := fmt.Sprintf("CX-%s-%x", time.Now().UTC().Format("20060102150405.000000"), randBytes)
```

This one line creates the unique ID for every bank transaction. Let's unwrap it piece by piece:

```
"CX-%s-%x"
  │    │  └── %x = insert these bytes as a hex string
  │    └────── %s = insert a string here  
  └─────────── "CX-" = a fixed prefix for all CONNEX bundle IDs

time.Now().UTC()                    → current time in UTC
  .Format("20060102150405.000000") → formatted as: 20260522150405.000000

randBytes                           → 4 random bytes, shown as hex like "3f8a1c2b"
```

A finished bundle ID looks like: **`CX-20260522150405.000000-3f8a1c2b`**

Every single transaction in history will have a different ID because the time and random bytes together make it unique.

---

## 📊 Data Types in CONNEX — The Complete Reference Table

| Type | Holds | Real CONNEX Example |
|------|-------|---------------------|
| `string` | Text | `"QUORUM_MET"`, `"keys/witness.key"` |
| `int` | Whole number | `8091` (port number) |
| `float64` | Decimal number | `1000.00` (KES amount) |
| `bool` | True or false | `true` when quorum is achieved |
| `[]byte` | Raw binary bytes | The SHA-256 hash bytes before hex encoding |
| `error` | An error or `nil` | `nil` = no error; anything else = problem |
| `time.Duration` | A length of time | `150 * time.Millisecond` (the witness timeout) |

---

## 🧠 Feynman Check — Teach It Back

Without looking above, explain to yourself:

> *"What does `:=` do? What is the difference between `string`, `int`, and `float64`? When would you use each one in a banking system?"*

---

## ❓ Elaborative Interrogation — Ask "Why?"

- **Why** does CONNEX store the transaction amount as `float64` and not `int`?
- **Why** does CONNEX format the time as `"20060102150405"` — why those specific numbers?

*(Answer to #2: Go uses a specific reference date — January 2, 2006, 15:04:05 — as its time template. The digits 1-2-3-4-5-6 spell out the order of time components: month=1, day=2, hour=3, minute=4, second=5, year=6.)*

---

## ✏️ Quiz 2

**Create:** `sandbox/quiz2.go`

Write a program that creates these five variables and prints them in a formatted sentence:

| Variable | Type | Value |
|----------|------|-------|
| `bankName` | `string` | `"Central Bank of Kenya"` |
| `transactionCount` | `int` | `1247` |
| `totalAmountKES` | `float64` | `98750.50` |
| `systemOnline` | `bool` | `true` |
| `witnessPort` | `int` | `8091` |

**Required output:**
```
Bank: Central Bank of Kenya | Transactions: 1247 | Total: KES 98750.50 | Port: 8091 | Online: true
```

**Hint:** Use `fmt.Printf` with `%s`, `%d`, `%.2f`, `%v` as the format verbs.

---

## ✅ Answer — Quiz 2

```go
package main

import "fmt"

func main() {
    bankName         := "Central Bank of Kenya"
    transactionCount := 1247
    totalAmountKES   := 98750.50
    systemOnline     := true
    witnessPort      := 8091

    fmt.Printf("Bank: %s | Transactions: %d | Total: KES %.2f | Port: %d | Online: %v\n",
        bankName, transactionCount, totalAmountKES, witnessPort, systemOnline)
}
```

**Format verb cheat sheet:**

| Verb | Use for | Example output |
|------|---------|---------------|
| `%s` | strings | `Central Bank of Kenya` |
| `%d` | integers | `1247` |
| `%.2f` | floats (2 decimal places) | `98750.50` |
| `%v` | anything (default format) | `true` |
| `\n` | new line | moves cursor to next line |

---

---

## 🔄 Review Checkpoint 1 — Spaced Repetition

Before moving to Chapter 3, answer these from memory (no peeking):

1. What does `package main` tell Go?
2. What does `:=` do that `=` cannot?
3. What data type would you use to store a bank transaction amount?
4. Name three toolboxes imported in the CONNEX Witness Node and what each does.

*(Check your answers against Chapters 1 and 2 above.)*

---

---

# Chapter 3: Structs — Grouping Related Data

---

## 📖 The Analogy First

A single bank transaction is never just one value. It has a unique ID, an amount, a sender, a receiver, a time, and cryptographic signatures. Storing all of these in separate variables would be chaos.

A **struct** is like a custom form with labeled fields. You design the form once, then fill it out once per transaction. Every transaction gets its own filled form.

```
┌─────────────────────────────────────┐
│  CONNEX TRANSACTION PROOF BUNDLE   │
├─────────────────────────────────────┤
│  Bundle ID:     CX-20260522-3f8a   │
│  Timestamp:     2026-05-22T15:04Z  │
│  Original Hash: d503ffab67cf2bdb…  │
│  Enriched Hash: 94c2367ab6be1b8b…  │
│  Quorum Status: QUORUM_MET         │
│  Signatures:    [Alpha, Beta]       │
└─────────────────────────────────────┘
```

That form, in Go, is called a `Bundle` struct.

---

## 🔍 Real Code: `cmd/gateway/main.go` — Lines 41–51

```go
type Bundle struct {
    BundleID      string          `json:"bundle_id"`
    Timestamp     string          `json:"timestamp"`
    OriginalHash  string          `json:"original_hash"`
    EnrichedHash  string          `json:"enriched_hash"`
    PrevChainHash string          `json:"prev_chain_hash"`
    ChainHash     string          `json:"chain_hash"`
    Signatures    []SignatureEntry `json:"signatures"`
    QuorumStatus  string          `json:"quorum_status"`
    EnrichmentLog json.RawMessage `json:"enrichment_log"`
}
```

**Anatomy of one field:**

```
    BundleID      string          `json:"bundle_id"`
    ────────      ──────          ─────────────────
    Field name    Data type       Struct tag: tells json.Marshal to
    (Go uses it)  (string = text) use "bundle_id" in the JSON output
                                  instead of "BundleID"
```

**To create a Bundle:**
```go
myBundle := Bundle{
    BundleID:     "CX-20260522-3f8a",
    Timestamp:    "2026-05-22T15:04:05Z",
    QuorumStatus: "QUORUM_MET",
}
```

**To read a specific field, use a dot `.`:**
```go
fmt.Println(myBundle.BundleID)      // → CX-20260522-3f8a
fmt.Println(myBundle.QuorumStatus)  // → QUORUM_MET
```

---

## 🔍 Real Code: `cmd/witness/main.go` — Lines 74–80

```go
type witness struct {
    priv        ed25519.PrivateKey  // Secret signing key — NEVER sent outside
    pub         ed25519.PublicKey   // Public key — shared with the gateway
    fp          string              // First 16 hex chars of SHA-256(pub)
    witnessName string              // "alpha", "beta", or "gamma"
    token       string              // Bearer token for authentication
}
```

Notice the field names are **lowercase** (`priv`, `pub`). In Go, a lowercase field name is **private** — code outside this package cannot access it. This is intentional security: the private key can never leak out of the `witness` package.

---

## ❓ Elaborative Interrogation — Ask "Why?"

- **Why** does `Signatures` use the type `[]SignatureEntry` and not just `string`?
- **Why** does the `Bundle` struct use struct tags to rename fields for JSON?
- **Why** are the `witness` struct fields lowercase while `Bundle` struct fields are uppercase?

*(Answer to #3: Uppercase = exported = accessible from outside the package. Lowercase = unexported = private to the package. The `Bundle` is shared across the whole system, so its fields must be public. The `witness`'s private key must stay private.)*

---

## ✏️ Quiz 3

**Create:** `sandbox/quiz3.go`

1. Define a struct called `BankTransaction` with these fields:

| Go Field Name | Type | JSON Tag |
|---------------|------|----------|
| `ID` | `string` | `"id"` |
| `SenderBank` | `string` | `"sender_bank"` |
| `ReceiverBank` | `string` | `"receiver_bank"` |
| `AmountKES` | `float64` | `"amount_kes"` |
| `IsApproved` | `bool` | `"is_approved"` |

2. In `main()`, create one transaction with realistic values.
3. Convert it to JSON with `json.Marshal` and print the result.

---

## ✅ Answer — Quiz 3

```go
package main

import (
    "encoding/json"
    "fmt"
)

type BankTransaction struct {
    ID           string  `json:"id"`
    SenderBank   string  `json:"sender_bank"`
    ReceiverBank string  `json:"receiver_bank"`
    AmountKES    float64 `json:"amount_kes"`
    IsApproved   bool    `json:"is_approved"`
}

func main() {
    tx := BankTransaction{
        ID:           "TX-2026-001",
        SenderBank:   "KCB Bank",
        ReceiverBank: "Equity Bank",
        AmountKES:    15750.00,
        IsApproved:   true,
    }

    jsonBytes, err := json.Marshal(tx)
    if err != nil {
        fmt.Println("Error converting to JSON:", err)
        return
    }

    fmt.Println(string(jsonBytes))
}
```

**Expected output:**
```json
{"id":"TX-2026-001","sender_bank":"KCB Bank","receiver_bank":"Equity Bank","amount_kes":15750,"is_approved":true}
```

Notice `sender_bank` in the output — not `SenderBank`. The struct tag did its job.

---

---

# Chapter 4: Functions — Writing Reusable Recipes

---

## 📖 The Analogy First

Imagine the CONNEX gateway processes 10,000 transactions per day. Every single one needs to have its data "fingerprinted" (hashed with SHA-256). You could write the hashing code 10,000 times — or you could write it ONCE, give it a name, and call it whenever you need it.

That is a **function**: a named, reusable recipe. You write it once. The computer runs it as many times as you call it.

```
RECIPE: sha256Hex
─────────────────
  INGREDIENTS: any binary data ([]byte)
  STEPS:
    1. Compute SHA-256 hash of the data
    2. Convert the 32 raw bytes to a readable hex string
  RESULT: a hex string like "d503ffab67cf2bdb..."
```

---

## 🔍 Real Code: `cmd/gateway/main.go` — Lines 125–128

```go
func sha256Hex(data []byte) string {
    h := sha256.Sum256(data)
    return hex.EncodeToString(h[:])
}
```

**Every single piece:**

```
func sha256Hex  (data []byte)  string  {
│    │            │              │
│    │            │              └── This function gives back a string
│    │            └─────────────── The ingredient: raw bytes named "data"
│    └──────────────────────────── The recipe's name
└───────────────────────────────── The keyword that starts any recipe definition
```

Inside:
```go
h := sha256.Sum256(data)    // Compute the hash. h is of type [32]byte
return hex.EncodeToString(h[:]) // h[:] converts [32]byte to []byte, then encode to hex
```

This function is called on EVERY transaction in the Gateway. The `originalHash` and `enrichedHash` inside every Bundle are both produced by this exact function.

---

## 🔍 Real Code: Multiple Return Values — `cmd/witness/main.go` Lines 33, 63

Go functions can return multiple values at once. Most functions that can fail return a result AND an error:

```go
// This function returns THREE values:
func loadOrGenerate(keyPath string) (ed25519.PublicKey, ed25519.PrivateKey, error) {
    // ... does work ...
    return pub, priv, nil    // Success: public key, private key, no error (nil)
}

// The caller receives all three:
pub, priv, err := loadOrGenerate(*keyPath)
//   │     │     └── The third: error (nil if all went well)
//   │     └──────── The second: private key
//   └────────────── The first: public key
```

If a function returns two things and you only care about the first, use `_` to discard the rest:

```go
pub, _, err := loadOrGenerate(*keyPath)  // Discard the private key
```

---

## 🧠 Feynman Check — Teach It Back

Explain out loud, as if to a friend:

> *"What is a function? Why do Go functions often return two values? What does `return` do?"*

---

## ✏️ Quiz 4

**Create:** `sandbox/quiz4.go`

Write two functions:

**Function 1:** `hashText(input string) string`
- Takes any string
- Converts it to bytes with `[]byte(input)`
- Computes `sha256.Sum256` on those bytes
- Returns the hex string of the hash

**Function 2:** `makeTransactionID(bankCode string, seq int) string`
- Takes a bank code like `"KCB"` and a sequence number like `42`
- Returns a formatted ID: `"TX-KCB-042-20260527"` (zero-pad the number to 3 digits with `%03d`, use today's date)

Call both functions in `main()` and print the results.

---

## ✅ Answer — Quiz 4

```go
package main

import (
    "crypto/sha256"
    "encoding/hex"
    "fmt"
    "time"
)

// hashText hashes any string with SHA-256 and returns the hex representation.
func hashText(input string) string {
    h := sha256.Sum256([]byte(input))  // []byte() converts string to raw bytes
    return hex.EncodeToString(h[:])    // h[:] converts [32]byte array to a slice
}

// makeTransactionID creates a unique transaction ID from bank code + sequence + date.
func makeTransactionID(bankCode string, seq int) string {
    today := time.Now().Format("20060102") // Format: YYYYMMDD
    return fmt.Sprintf("TX-%s-%03d-%s", bankCode, seq, today)
    // %03d = integer with minimum 3 digits, zero-padded: 42 becomes "042"
}

func main() {
    hash := hashText("Hello CONNEX")
    fmt.Println("SHA-256:", hash)

    txID := makeTransactionID("KCB", 42)
    fmt.Println("Transaction ID:", txID)
}
```

**Expected output:**
```
SHA-256: 3b5d5c3712955042212316173ccf37be9baaea1bc23b9f1ec95b938db4c4d96c
Transaction ID: TX-KCB-042-20260527
```

---

---

## 🔄 Review Checkpoint 2 — Spaced Repetition

Answer from memory — no peeking:

1. What is the difference between `:=` and `=`?
2. What does a struct tag like `` `json:"bundle_id"` `` do?
3. A function has signature `func process(data []byte) (string, error)`. What does it take and what does it return?
4. What does `return` do inside a function?
5. Write the one-line function `sha256Hex` from memory.

---

---

# Chapter 5: Methods — Functions That Belong to a Struct

---

## 📖 The Analogy First

A `Bundle` struct holds transaction data. But it can also have **actions** it knows how to perform on itself — like a bank account knowing how to calculate its own balance.

In Go, you attach functions to structs. These are called **methods**. The difference:

```
Regular function:   sha256Hex(data)         — you pass data in
Method on struct:   bundle.ChainSummary()   — the struct is the context
```

To attach a function to a struct, you add a **receiver** before the function name:
```go
func (b *Bundle) ChainSummary() string {
//   │  │                                
//   │  └─ The struct type this method belongs to  
//   └──── The name we use to refer to THIS bundle inside the function
    return b.BundleID + " → " + b.ChainHash
}
```

---

## 🔍 Real Code: `cmd/witness/main.go` — Lines 82–93

```go
func (w *witness) handlePubkey(rw http.ResponseWriter, r *http.Request) {
    // Check if the request is a GET request
    if r.Method != http.MethodGet {
        http.Error(rw, "GET required", http.StatusMethodNotAllowed)
        return
    }
    // Set the response format to JSON
    rw.Header().Set("Content-Type", "application/json")
    // Build a JSON response and send it
    json.NewEncoder(rw).Encode(map[string]string{
        "witness":     w.witnessName,   // ← access witness fields with w.
        "public_key":  base64.StdEncoding.EncodeToString(w.pub),
        "fingerprint": w.fp,
    })
}
```

When the Gateway calls `GET http://localhost:8091/v1/pubkey`, this method runs. The `w` variable is the specific witness instance (Alpha, Beta, or Gamma) that is handling the request.

---

## 🔍 Real Code: `internal/iso8583/parser.go` — Lines 91–101

```go
func (m *Message) AmountKES() float64 {
    s, ok := m.Fields[4]          // Look for field 4 in the message's field map
    if !ok || s == "" {           // If field 4 is missing or blank...
        return 0                   // ...the amount is zero
    }
    n, err := strconv.ParseInt(strings.TrimLeft(s, "0 "), 10, 64)
    if err != nil {
        return 0
    }
    return float64(n) / 100.0    // ISO 8583 stores 1000.00 KES as "000000100000"
}
```

ISO 8583 stores money as an integer in cents. `"000000100000"` means `1000.00 KES`. This method does the conversion automatically. Every part of CONNEX that needs the transaction amount calls `msg.AmountKES()` — never reading `Fields[4]` directly.

---

## ✏️ Quiz 5

**Create:** `sandbox/quiz5.go`

1. Use your `BankTransaction` struct from Quiz 3
2. Add a method `Summary() string` that returns:
   `"TX-ID: [ID] | [SenderBank] → [ReceiverBank] | KES [AmountKES]"`
3. Add a method `IsLargeTransaction() bool` that returns `true` if `AmountKES > 100000`
4. In `main()`, create a transaction with amount `250000`, call both methods, and print the results with an appropriate message for large transactions

---

## ✅ Answer — Quiz 5

```go
package main

import "fmt"

type BankTransaction struct {
    ID           string
    SenderBank   string
    ReceiverBank string
    AmountKES    float64
    IsApproved   bool
}

// Summary returns a human-readable one-line description of the transaction.
func (t *BankTransaction) Summary() string {
    return fmt.Sprintf("TX-ID: %s | %s → %s | KES %.2f",
        t.ID, t.SenderBank, t.ReceiverBank, t.AmountKES)
}

// IsLargeTransaction flags transactions above the 100,000 KES threshold.
func (t *BankTransaction) IsLargeTransaction() bool {
    return t.AmountKES > 100000
}

func main() {
    tx := &BankTransaction{  // The & creates a pointer — the method can modify the original
        ID:           "TX-2026-099",
        SenderBank:   "KCB Bank",
        ReceiverBank: "Equity Bank",
        AmountKES:    250000.00,
        IsApproved:   true,
    }

    fmt.Println(tx.Summary())

    if tx.IsLargeTransaction() {
        fmt.Println("⚠️  ALERT: Large transaction — flagged for compliance review")
    } else {
        fmt.Println("✅  Standard transaction cleared")
    }
}
```

**Expected output:**
```
TX-ID: TX-2026-099 | KCB Bank → Equity Bank | KES 250000.00
⚠️  ALERT: Large transaction — flagged for compliance review
```

---

---

# Chapter 6: Error Handling — Never Let Problems Go Silent

---

## 📖 The Analogy First

Imagine a bank teller who processes a transaction, realizes the system rejected it, but just smiles and hands you a receipt saying "Approved!" That would be a catastrophe.

In Go, **silence is not allowed**. Every function that can fail returns an `error` as its last value. You MUST check it. If you don't, Go will actually warn you.

```
The Go Rule: If a function can fail, it MUST tell you.
The Your Rule: If a function tells you it can fail, you MUST check if it did.
```

The pattern appears in nearly every function call in CONNEX:

```go
result, err := doSomething()
if err != nil {              // "If there was an error..."
    // handle it — log it, return it, or stop
}
// If we reach here, everything worked perfectly
```

`nil` in Go means "nothing" or "empty". An `error` that equals `nil` means "no error occurred."

---

## 🔍 Real Code: `cmd/witness/main.go` — Lines 47–63

```go
// Generate fresh keypair
pub, priv, err := ed25519.GenerateKey(rand.Reader)
if err != nil {
    return nil, nil, fmt.Errorf("generate keypair: %w", err)
}

// Save private key to disk — 0600 means ONLY the owner can read it (maximum privacy)
if err := os.WriteFile(privPath, priv, 0600); err != nil {
    return nil, nil, fmt.Errorf("write private key: %w", err)
}

// Save public key to disk — 0644 means anyone can read it (it's meant to be shared)
if err := os.WriteFile(pubPath, pub, 0644); err != nil {
    return nil, nil, fmt.Errorf("write public key: %w", err)
}
```

**Key concepts:**

| Code | What it means |
|------|--------------|
| `if err != nil` | "Did something go wrong?" |
| `return nil, nil, err` | "Yes — stop everything and pass the error up to the caller" |
| `fmt.Errorf("context: %w", err)` | Wrap the error with extra context so the error message shows a trail |
| `0600` | File permission: only the owner can read/write. Private key must stay secret |
| `0644` | File permission: owner can write, everyone can read. Public keys are designed to be shared |

---

## 🔍 Real Code: `cmd/gateway/main.go` — Lines 268–272

```go
if err != nil {
    slog.Error("db write failed", "bundle", bundleID, "err", err)
    http.Error(w, "database write error", http.StatusInternalServerError)
    return
}
```

If writing to the SQLite ledger fails, CONNEX:
1. Logs the error with structured key-value pairs (`"bundle"`, `"err"`)
2. Returns HTTP 500 to the client
3. Returns immediately — it does NOT send back a "success" response

This is why a bank can trust CONNEX: it will never pretend a transaction succeeded if it wasn't stored.

---

## ✏️ Quiz 6

**Create:** `sandbox/quiz6.go`

Write a function `readTransactionFile(filename string) (string, error)` that:
1. Calls `os.ReadFile(filename)` to read a file
2. If it fails → returns `""` and a wrapped error: `fmt.Errorf("readTransactionFile: %w", err)`
3. If it succeeds → returns the file content as `string` and `nil`

In `main()`:
1. Call it with `"transactions.json"` (which does not exist)
2. Check the error and print `"Failed to load: [error message]"` if it fails
3. If no error, print the file content

---

## ✅ Answer — Quiz 6

```go
package main

import (
    "fmt"
    "os"
)

func readTransactionFile(filename string) (string, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        // Wrap with context: now the caller knows this came from readTransactionFile
        return "", fmt.Errorf("readTransactionFile: %w", err)
    }
    return string(data), nil  // nil = no error
}

func main() {
    content, err := readTransactionFile("transactions.json")
    if err != nil {
        fmt.Println("Failed to load:", err)
        return
    }
    fmt.Println("File contents:", content)
}
```

**Expected output:**
```
Failed to load: readTransactionFile: open transactions.json: The system cannot find the file specified.
```

Notice the chain: your message → original OS error. This chaining (`%w`) is what makes debugging in production fast. You always know exactly where in the code the failure happened.

---

---

## 🔄 Review Checkpoint 3 — Spaced Repetition

Answer from memory:

1. What does `nil` mean when it is the value of an `error`?
2. What does `fmt.Errorf("context: %w", err)` do that `fmt.Errorf("context: %v", err)` does not?
3. What is the difference between a regular function and a method?
4. In `func (m *Message) AmountKES() float64`, what does the `*` mean?
5. Why would a banking system NEVER silently ignore an error?

---

---

# Chapter 7: Goroutines — Running Code Simultaneously

---

## 📖 The Analogy First

Imagine you need signatures from three different bank officers — Alpha, Beta, and Gamma. 

**Bad approach:** Walk to Alpha's desk, wait for them to sign, walk to Beta's desk, wait, walk to Gamma's desk, wait. Total time: 3× the signing time.

**Good approach:** Send all three a signing request at the exact same moment. They all work in parallel. Total time: as long as the slowest one.

That is what a **goroutine** does. The keyword `go` before a function call launches it instantly in the background, so your main program keeps moving without waiting.

```go
processPayment("TX-A")   // Takes 50ms — main program WAITS here
processPayment("TX-B")   // Takes 50ms — main program WAITS here
// Total: 100ms

go processPayment("TX-A") // Launches in background — main program DOESN'T wait
go processPayment("TX-B") // Launches in background — main program DOESN'T wait
// Total: ~50ms (both run at the same time)
```

---

## 🔍 Real Code: `cmd/gateway/main.go` — Lines 87–121

This is the most important function in the entire CONNEX system. Read it slowly:

```go
func collectSignatures(witnesses []string, tokens []string, hashBytes []byte, timeout time.Duration) []SignatureEntry {

    // Step 1: Define a mini-struct to hold one goroutine's result
    type result struct {
        sig *SignatureEntry
        err error
    }

    // Step 2: Create a CHANNEL — a safe pipe goroutines use to send results back
    ch := make(chan result, len(witnesses))

    // Step 3: Launch ONE goroutine per witness — ALL start at the same time
    for i, w := range witnesses {
        w := w  // Capture the variable — important! (explained below)
        var token string
        if i < len(tokens) {
            token = tokens[i]
        }
        go func() {                                  // ← "go" = launch in background
            sig, err := requestSignature(w, token, hashBytes, timeout)
            ch <- result{sig, err}                   // ← push result into the pipe
        }()
    }

    // Step 4: Collect results as they arrive, with a timeout
    var sigs []SignatureEntry
    deadline := time.After(timeout)  // A timer that fires after [timeout] duration

    for range witnesses {
        select {
        case r := <-ch:                   // ← a result arrived through the pipe
            if r.err != nil {
                slog.Warn("witness error", "err", r.err)
            } else {
                sigs = append(sigs, *r.sig)
            }
        case <-deadline:                  // ← the timer ran out
            slog.Warn("witness timeout reached", "collected", len(sigs))
            return sigs                   // Return whatever we collected so far
        }
    }
    return sigs
}
```

**New concepts in this function:**

| Concept | Plain English |
|---------|--------------|
| `ch := make(chan result, 3)` | A channel is a pipe. Goroutines push data in; the main code pulls data out |
| `ch <- value` | **Send** a value into the channel (goroutine → channel) |
| `value := <-ch` | **Receive** a value from the channel (channel → main code) |
| `select { case ...: case ...: }` | "Wait for whichever of these events happens first" |
| `time.After(150ms)` | Creates a channel that sends one value after 150ms — the perfect timeout |

**Why `w := w` before the goroutine?**
In a loop, the variable `w` changes with every iteration. Without capturing it, all goroutines might share the same (last) value of `w`. By writing `w := w`, you create a new copy of `w` that belongs exclusively to this goroutine.

---

## ✏️ Quiz 7

**Create:** `sandbox/quiz7.go`

Simulate 3 witness nodes:

1. Create `results := make(chan string, 3)`
2. Launch 3 goroutines:
   - Goroutine 1: sleep 1 second → send `"Alpha signed ✓"`
   - Goroutine 2: sleep 2 seconds → send `"Beta signed ✓"`
   - Goroutine 3: sleep 5 seconds → send `"Gamma signed ✓"` *(will time out)*
3. In `main()`, use a `for` loop running 3 times. Inside, use `select` with:
   - A case to receive from `results` and print the message
   - A `case <-time.After(3 * time.Second)` that prints `"⏰ Timeout"`, then checks if you have ≥ 2 signatures (quorum) and returns

---

## ✅ Answer — Quiz 7

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    results := make(chan string, 3)

    // Launch all 3 goroutines simultaneously
    go func() {
        time.Sleep(1 * time.Second)
        results <- "Alpha signed ✓"
    }()

    go func() {
        time.Sleep(2 * time.Second)
        results <- "Beta signed ✓"
    }()

    go func() {
        time.Sleep(5 * time.Second) // Will not make it in time
        results <- "Gamma signed ✓"
    }()

    // Collect signatures with a 3-second deadline
    collected := 0
    for i := 0; i < 3; i++ {
        select {
        case msg := <-results:
            fmt.Println("Received:", msg)
            collected++
        case <-time.After(3 * time.Second):
            fmt.Println("⏰ Timeout — witness did not respond in time")
            if collected >= 2 {
                fmt.Printf("✅ QUORUM_MET — %d/3 signatures collected\n", collected)
            } else {
                fmt.Printf("❌ QUORUM_FAILED — only %d/3 signatures\n", collected)
            }
            return
        }
    }
}
```

**Expected output:**
```
Received: Alpha signed ✓
Received: Beta signed ✓
⏰ Timeout — witness did not respond in time
✅ QUORUM_MET — 2/3 signatures collected
```

This output perfectly mirrors what the real CONNEX Gateway produces when Witness Gamma is offline!

---

---

## 🔄 Review Checkpoint 4 — Interleaved Practice

This checkpoint mixes all 7 chapters together. Answer from memory:

1. **(Ch. 1)** What happens if you import a package but never use it?
2. **(Ch. 2)** What is the difference between `string` and `[]byte`? When would you use each?
3. **(Ch. 3)** What does the struct tag `` `json:"bundle_id"` `` do?
4. **(Ch. 4)** Write the complete `sha256Hex` function from memory.
5. **(Ch. 5)** What is the `*` in `func (w *witness) handlePubkey(...)` and why is it important?
6. **(Ch. 6)** What does `fmt.Errorf("context: %w", err)` do that plain string concatenation cannot?
7. **(Ch. 7)** What is a goroutine? What is a channel? How do they work together?

---

---

# Chapter 8: Reading the Real Code — You Are Ready

You have learned every concept used in the CONNEX source code. Let's prove it.

Open `cmd/witness/main.go` and find `main()` at line 164. Here it is, fully annotated:

```go
func main() {
    // Ch.1: This is the entry point — package main + func main()

    // Ch.2: Variables created from command-line flags
    port    := flag.Int("port", 8091, "Port to listen on")
    keyPath := flag.String("keypath", "keys/witness.key", "Keypair path")
    name    := flag.String("name", "witness", "Witness name")
    token   := flag.String("token", "", "Auth token")
    flag.Parse()  // Actually read the arguments from the command line

    // Ch.4 + Ch.6: Call a function, receive 3 values, check error
    pub, priv, err := loadOrGenerate(*keyPath)
    if err != nil {
        slog.Error("keypair setup failed", "err", err)
        os.Exit(1)  // Stop the whole program with exit code 1 (failure)
    }

    // Ch.4: Call fingerprint(), Ch.3: build a witness struct
    fp := fingerprint(pub)
    w := &witness{priv: priv, pub: pub, fp: fp, witnessName: *name, token: *token}
    // The & makes a POINTER to the struct — the methods can modify the original

    // Ch.5: Register HTTP routes — methods on the witness struct
    mux := http.NewServeMux()
    mux.HandleFunc("/v1/pubkey", w.handlePubkey)  // GET → returns public key
    mux.HandleFunc("/v1/sign",   w.handleSign)    // POST → signs a hash
    mux.HandleFunc("/health",    w.handleHealth)  // GET → health check

    // Ch.6: Start the server — handle any startup error
    addr := fmt.Sprintf(":%d", *port)
    if err := http.ListenAndServe(addr, mux); err != nil {
        slog.Error("server error", "err", err)
        os.Exit(1)
    }
}
```

Every single line — you now understand it completely.

---

## 🏆 Final Challenge

Open `cmd/gateway/main.go`. Find `handleCoordinate()` at line 148. It has **12 numbered steps** in the comments. For each step, write in a notebook:

1. What Go concepts from this course does this step use?
2. Why do you think the developer wrote it this way?

When you can do that exercise, you are ready to contribute to CONNEX.

---

## 📅 Recommended Study Schedule

Based on spaced repetition research, here is the optimal review schedule:

| Day | Activity |
|-----|----------|
| Day 1 | Read Chapters 1–2, complete Quizzes 1–2 |
| Day 2 | Complete Review Checkpoint 1, read Chapter 3, Quiz 3 |
| Day 3 | Complete Chapters 4–5, Quizzes 4–5, Review Checkpoint 2 |
| Day 5 | Re-do Quizzes 1–3 from memory (spaced repetition) |
| Day 6 | Complete Chapters 6–7, Quizzes 6–7 |
| Day 7 | Review Checkpoints 3–4, attempt Final Challenge |
| Day 10 | Re-do all quizzes from memory |
| Day 14 | Read `cmd/gateway/main.go` top to bottom — annotate every line |
