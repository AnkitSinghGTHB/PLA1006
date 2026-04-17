# Direction Sense Test - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./03_Logical_Reasoning_CheatSheet.md)

This document contains step-by-step Cartesian Coordinate (Mental Map) strategies for the `Directions.pdf` practice set.

> [!TIP]
> **The `(x, y)` Cartesian Trick:** Never draw messy lines that overlap! Just track the coordinates. 
> *   North = `+y`
> *   South = `-y`
> *   East = `+x`
> *   West = `-x`
> *   Distance = $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

---

### Question 3
**Question:** Man walks 40m North, turns left walks 40m, turns left walks 15m, turns right walks 20m. Distance from start & direction?
*   **Options:** `[A) 55m NW  B) 36m NE  C) 65m SE  D) 65m NW]`
*   **Mental Map `(x,y)`:**
    *   Start: `(0, 0)`
    *   40m North: `(0, 40)`
    *   Left (West) 40m: `(-40, 40)`
    *   Left (South) 15m: `(-40, 40 - 15)` = `(-40, 25)`
    *   Right (West) 20m: `(-40 - 20, 25)` = **`(-60, 25)`**
    *   **Direction:** From origin `(0,0)`, an x of -60 and y of +25 is immediately **North West**.
    *   **Distance:** $\sqrt{60^2 + 25^2} = \sqrt{3600 + 625} = \sqrt{4225} = 65m$.
*   **Answer:** **D) 65m, Northwest**.

---

### Questions 4-5
**Setup:** N is 5m East of L, 4m North of B. D is 13m East of L. E is 5m SE of B and 4m East of F. If E goes 7m North, he is EXACTLY between N and D.
*   **Mental Map `(x,y)`:**
    *   Let $L = (0,0)$.
    *   $N = (5, 0)$.
    *   Since N is 4m North of B, $B = (5, -4)$.
    *   $D = (13, 0)$.
    *   "Middle of N and D" = `((5+13)/2, 0)` = `(9, 0)`.
    *   If E goes 7m North to reach `(9,0)`, then E must currently be at **`(9, -7)`**.
    *   $F$ is 4m West of E, so $F = (5, -7)$.
*   **Q4: Direction of F with respect to N?**
    *   N is `(5, 0)`. F is `(5, -7)`. F is exactly **South** of N.
    *   **Answer: D) South**.
*   **Q5: Direction of L with respect to E?**
    *   E is `(9, -7)`. L is `(0, 0)`.
    *   To get from E to Origin, you must go Left (-x, West) and Up (+y, North) -> **North West**.
    *   **Answer: B) North west**.

---

### Question 7
**Question:** Planes A,B,C,D fly East. A,D turn right, B,C turn left. Then B,C turn left and A,D turn left. Current directions (A,B,D,C)?
*   **Options:** `[A) N, S, E, W  B) E, W, W, E  C) E, W, E, W  D) S, N, N, S]`
*   **Mental Headings:**
    *   Initial for all = `EAST`.
    *   **Planes A & D:** East -> Right Turn = `SOUTH`. Left Turn = **`EAST`**.
    *   **Planes B & C:** East -> Left Turn = `NORTH`. Left Turn = **`WEST`**.
    *   Order requested: **A, B, D, C**.
    *   Result: East, West, East, West.
*   **Answer:** **C) East, West, East, West**.

---

### Question 8
**Question:** Arya East 12km, anti-clock 270°, travels 12km. Bindya South 12km, clock 90°, runs 18km, then opposite 30km. True statement?
*   **Options:** `[A) Bindya travelled 30km more  B) Both SE of original  C) Both at diff point]`
*   **Mental Map `(x,y)`:**
    *   Start = `(0, 0)`.
    *   **Arya:** `(12, 0)`. Currently facing East. 270° Anti-Clockwise = North -> West -> South. Walks 12km South to **`(12, -12)`**.
    *   **Bindya:** Walks South 12km to `(0, -12)`. 90° Clockwise = West. Runs 18km to `(-18, -12)`. Then opposite direction (East) for 30km. `(-18 + 30, -12)` = **`(12, -12)`**.
    *   They are at the EXACT same point!
    *   Point `(12, -12)` is South-East of the origin.
*   **Answer:** **B) Both are to the south east of original position**.

---

### Questions 11-12
**Setup:** Man walks 8m East (P), turns right walks 5m (Q), turns left walks 9m (R), turns right walks 11m (S), turns right walks 20m (T).
*   **Mental Map `(x,y)`:**
    *   Start = `(0,0)`
    *   P = `(8, 0)`
    *   Q (South 5m) = `(8, -5)`
    *   R (East 9m) = `(17, -5)`
    *   S (South 11m) = `(17, -16)`
    *   T (West 20m) = `(17 - 20, -16)` = `(-3, -16)`
*   **Q11: Walks 3m East from T to reach U. Distance U to Start?**
    *   U = `(-3 + 3, -16)` = `(0, -16)`.
    *   Distance from `(0,0)` to `(0,-16)` is **16m**.
    *   **Answer: A) 16m**.
*   **Q12: Distance Start to Q?**
    *   Start is `(0,0)`, Q is `(8,-5)`.
    *   Distance = $\sqrt{8^2 + 5^2} = \sqrt{64 + 25} = \sqrt{89}$.
    *   **Answer: C) Sqrt(89) m**.

---

### Questions 13-15
**Setup:**
*   **Bus F map:** From $D(0,0)$ → North 4 to `(0,4)` → East 6 to $T(6,4)$ → North 3 to `(6,7)` → West 4 to stop at $U(2,7)$.
*   **Bus G map:** From $H(10,0)$ → North 9 to $S(10,9)$ → West 4 to `(6,9)` → South 2 to stop at $A(6,7)$.
*   **Q13: Which city do they both cross?**
    *   Look at coordinates! F passed through `(6,7)` before turning left to U. G literally parked at $A(6,7)$. Thus they both passed City A. **[Ans: C) A]**
*   **Q14: If P is 2km West of H, distance D to P?**
    *   H is `(10,0)`. P is `(8,0)`. D is `(0,0)`. Distance = 8km. **[Ans: A) 8 km]**
*   **Q15: Total distance covered by F?**
    *    $4 + 6 + 3 + 4 = 17$ km. **[Ans: B) 17]**

---

### Questions 16-18
**Setup:** Starts A(0,0) -> 3km N (0,3) -> 3km E (3,3) -> 2km S (3,1) -> 4km E (7,1) -> 6km S to reach B(7,-5).
*   **Q16: Direction from start?**
    *   From `(0,0)` to `(7,-5)` is +X and -Y = **South East**. **[Ans: B) South east]**
*   **Q17: Total walked distance?**
    *   $3 + 3 + 2 + 4 + 6 = 18$ km. **[Ans: A) 18]**
*   **Q18: Distance from start?**
    *   $\sqrt{7^2 + (-5)^2} = \sqrt{49 + 25} = \sqrt{74} \approx 8.60$ km. **[Ans: C) 8.60 km]**
