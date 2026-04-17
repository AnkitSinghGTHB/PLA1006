# Time and Work / Pipes and Cisterns - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./02_Time_Speed_Work_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Time and Work Pipes and Cisterns.pdf` practice set.

> [!TIP]
> **The LCM Method:** Almost every pipe question can be solved implicitly in your head by giving the "Tank" an arbitrary volume equal to the Least Common Multiple (LCM) of the given times. Never use fractions!

---

### Question 1
**Question:** P fills in 10m, Q fills in 15m, R empties in 12m. How much time if all three open?
*   **Options:** `[A) 12  B) 10  C) 7  D) 15]`
*   **Mental Trick (LCM Capacity):**
    *   Find LCM of (10, 15, 12). It's **60**. Let the tank capacity = 60 liters.
    *   **Efficiency:** P = `+6 L/m`. Q = `+4 L/m`. R = `-5 L/m` (emptying).
    *   **Combined Efficiency:** `6 + 4 - 5 = +5 L/m`.
    *   **Time to fill:** `60 / 5 = 12` minutes.
*   **Answer:** **A) 12**.

---

### Question 2
**Question:** Cistern takes 20m to fill normally. Due to a leak, it takes 10 extra minutes (total 30m). How much time for the leak alone to empty it?
*   **Options:** `[A) 20  B) 30  C) 60  D) 35]`
*   **Mental Trick (LCM):**
    *   LCM of (20, 30) = **60**.
    *   Normal Pipe Efficiency = `60 / 20 = +3 L/m`.
    *   New Efficiency (Pipe - Leak) = `60 / 30 = +2 L/m`.
    *   Logic: The normal pipe brings in 3. But only 2 stays in the tank. Where did the missing 1 go? The leak ate it!
    *   Leak Efficiency = `-1 L/m`.
    *   **Time for leak:** `60 / 1 = 60` minutes.
*   **Answer:** **C) 60**.

---

### Question 3
**Question:** Tap X fills in 32m, Y fills in 40m. Both open. Later X is closed. Y alone fills the rest. Total time taken was 25 minutes. How long was X open?
*   **Options:** `[A) 15  B) 16  C) 14  D) 12]`
*   **Mental Trick (Isolation):**
    *   LCM of (32, 40) is **160** units.
    *   Tap X = `+5`. Tap Y = `+4`.
    *   We know Tap Y was NEVER closed. It ran for the full 25 minutes.
    *   Total work done by Tap Y = `25 * 4 = 100` units.
    *   Remaining work = `160 - 100 = 60` units. This MUST have been done by X before it was closed.
    *   Time X was open = `60 / 5 = 12` minutes.
*   **Answer:** **D) 12**.

---

### Question 5
**Question:** P fills in 60m, Q fills in 40m. How many minutes to fill from empty if Q is used for half the time, and P+Q fill it for the other half?
*   **Options:** `[A) 15m  B) 20m  C) 27.5m  D) 30m]`
*   **Mental Trick:**
    *   LCM of (60, 40) is **120** units.
    *   P = `+2`. Q = `+3`.
    *   P+Q together = `+5`.
    *   The total time is split perfectly in half. So you basically have an "average" efficiency.
    *   Average Efficiency = `(Q alone + P&Q together) / 2` = `(3 + 5) / 2` = `4` units per minute overall.
    *   Time = `120 / 4 = 30` minutes.
*   **Answer:** **D) 30 min**.

---

### Question 10
**Question:** A drain pipe drains in 12 hours. A fill pipe fills in 6 hours. A total of 'n' pipes (mix of fill and drain) fill the tank in 2 hours. How many of the following values could 'n' take? [24, 16, 33, 13, 9, 8]
*   **Options:** `[A) 3  B) 4  C) 2  D) 1]`
*   **Mental Trick (Algebraic Pattern Spotting):**
    *   LCM(12, 6) = 12 units.
    *   Fill = `+2`. Drain = `-1`.
    *   Net required efficiency to fill 12 units in 2 hours = `+6 L/h`.
    *   Let $x$ be fill pipes, $y$ be drain pipes. Total pipes $n = x + y$.
    *   Equation: `2x - 1y = 6`. Which means `y = 2x - 6`.
    *   Substitute $y$ back into $n$: $n = x + (2x - 6) = 3x - 6$.
    *   Notice that $3x - 6$ is a **multiple of 3**. Therefore, the total number of pipes $n$ MUST be a multiple of 3.
    *   Look at the given values: 24 (Yes), 16 (No), 33 (Yes), 13 (No), 9 (Yes), 8 (No).
    *   There are exactly 3 possible values.
*   **Answer:** **A) 3**.
