# Boats, Streams & Escalators - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./02_Time_Speed_Work_CheatSheet.md)

This document contains step-by-step mental math strategies for the `PROBLEMS ON BOATS AND STREAMS ,ESCALATOR.pdf` practice set.

> [!TIP]
> **The `Relative Speed` Framework:** 
> *   For boats: Downstream = `Current + Boat`. Upstream = `Boat - Current`. 
> *   For escalators, it is the EXACT same! Walking with escalator = Downstream. Walking against = Upstream.

---

### Question 1
**Question:** Boat takes 7 hours from A to C (midpoint B). Takes 8 hours from A to B and return to A. C to A takes?
*   **Options:** `[A) 7 hours  B) 8 hours  C) 9 hours  D) None of these]`
*   **Mental Trick (Midpoint Logic):**
    *   Since B is the midpoint, A→B is exactly half of A→C.
    *   Time A→C is 7 hours. So Time A→B (Downstream) = `3.5 hours`.
    *   We are given `(A→B) + (B→A) = 8 hours`.
    *   `3.5 + (B→A) = 8`. So `B→A` (Upstream) = `4.5 hours`.
    *   The question asks for C→A (which is the full Upstream journey).
    *   Since half the journey (B→A) takes 4.5 hours, the full journey takes `4.5 * 2 = 9 hours`.
*   **Answer:** **C) 9 hours**.

---

### Question 2
**Question:** Escalator: 5 steps/sec takes 10s downwards (with). Walking back same speed takes 40s (against). Number of steps?
*   **Options:** `[A) 40  B) 60  C) 80  D) 120]`
*   **Mental Trick:**
    *   Let Escalator speed = `E`. Distance is identical both ways.
    *   `Distance = Speed * Time`.
    *   `(5 + E) * 10 = (5 - E) * 40`.
    *   `(5 + E) = 4 * (5 - E)`.
    *   `5 + E = 20 - 4E`  →  `5E = 15`  →  `E = 3` steps/sec.
    *   Distance = `(5 + 3) * 10 = 80 steps`.
*   **Answer:** **C) 80**.

---

### Question 5
**Question:** Man rows 15 km/h in still water. Takes twice as long to row up as to row down. Speed of current?
*   **Options:** `[A) 6 km/h  B) 6.5 km/h  C) 4.5 km/h  D) 5 km/h]`
*   **Mental Trick (Time/Speed Inverse Ratio):**
    *   Time ratio (Up : Down) = `2 : 1`.
    *   So Speed ratio (Down : Up) = `2 : 1`. Let speeds be `2parts` and `1part`.
    *   Still water speed `(M)` is average: `(2 + 1) / 2 = 1.5 parts`.
    *   Current speed `(C)` is difference/2: `(2 - 1) / 2 = 0.5 parts`.
    *   We can clearly see `C` is exactly `1/3` of `M`.  (0.5 is 1/3 of 1.5)
    *   We are given `M = 15`. So `C = 15 / 3 = 5 km/h`.
*   **Answer:** **D) 5 km/h**.

---

### Question 9
**Question:** Shyama and Vyom escalator. Shyama takes 3 steps for every 2 of Vyom. Shyama reaches top in 25 steps, Vyom in 20. Total steps?
*   **Mental Trick (Relative Time):**
    *   Speed ratio `S:V = 3:2`. Let their speeds be 3 and 2.
    *   Time taken by Shyama to reach 25 steps = `25 / 3` units.
    *   Time taken by Vyom to reach 20 steps = `20 / 2 = 10` units.
    *   Total Steps = (Person's steps) + (Escalator's steps).
    *   Equate both scenarios: `25 + E*(25/3) = 20 + E*(10)`.
    *   `5 = 10E - 25E/3 = 5E/3`.
    *   `E = 3`.
    *   Substitute back: `20 + 3*(10) = 50 steps`.
*   **Answer:** **50 steps** (If option matching standard CAT sets, this is the derived answer).

---

### Question 11
**Question:** Downstream travels 2km more than "still water" per hour. Upstream travels...?
*   **Options:** `[A) 6km less than downstream  B) 2km less than still water  C) 4km less than downstream  D) More than one...]`
*   **Mental Trick (Definition of Current):**
    *   Downstream distance per hour = `Boat + Current`.
    *   Still water per hour = `Boat`.
    *   Difference is simply the `Current`! So Current = `2 km/h`.
    *   Upstream speed = `Boat - Current`.
    *   Since Downstream = `Boat + Current`, the difference between Downstream and Upstream is always `2 * Current`.
    *   `2 * 2 = 4 km`. So Upstream is 4km less than Downstream!
    *   Wait, is it also 2km less than still water? Yes! Upstream is `Boat - 2`.
    *   Both B and C are correct, so D is the technical answer.
*   **Answer:** **D) More than one of the above**.

---

### Question 14
**Question:** Hat falls off. Boat continues upstream for 12 minutes, turns back and catches hat at starting point. Speed of river if hat flew off 31m from start?
*   **Mental Trick (The Floating Hat Concept):**
    *   Relative to the river, the hat is stationary!
    *   Therefore, the boat moves away from the hat at exactly its STILL WATER speed.
    *   Because of this, it takes the EXACT SAME AMOUNT OF TIME to return to the hat as it spent moving away from it.
    *   Moved away for 12 mins -> Returns in 12 mins.
    *   Total time the hat was floating = `12 + 12 = 24 minutes`.
    *   The hat floated 31 meters in 24 minutes. This defines the speed of the river.

---

### Question 15
**Question:** Ravi takes 40s to walk up moving upwards. Takes 60s to walk up moving downwards. Escalator stopped?
*   **Options:** `[A) 50 s  B) 100 s  C) 48 s  D) 60 s]`
*   **Mental Trick (Harmonic Mean of Time):**
    *   `Rate_With = 1/40`.
    *   `Rate_Against = 1/60`.
    *   Ravi's pure walking rate = Average of the two rates!
    *   `Average = (1/40 + 1/60) / 2 = (3/120 + 2/120) / 2 = 5/240 = 1/48`.
    *   If Ravi's rate is `1/48`, it takes him 48 seconds.
*   **Answer:** **C) 48 s**.
