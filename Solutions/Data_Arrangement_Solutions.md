# Data & Sitting Arrangements - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./03_Logical_Reasoning_CheatSheet.md)

This document contains step-by-step mental mapping for the `Data Arrangement.pdf` practice set.

> [!TIP]
> **The Lock-In Strategy:** Create a visual array slot representation `_ _ _ _`. Find the one clue that anchors a person to a definitive absolute position (e.g. "Q is at an end" or "Exactly 2 finish ahead of B"). Build everything relative to that anchor!

---

### Questions 1-5: The Race
*   **1) Exactly 2 ahead of Benny (B):** Position of B is `3`. → `_ _ B _ _ _`
*   **4) Benny ahead of Esha (E) with one intervening:** B is at 3, gap at 4, E is at `5`. → `_ _ B _ E _`
*   **2) Two separate Esha & Dolly (D):** E is at 5, so D must be at `2` (positions 3 and 4 separate them). → `_ D B _ E _`
*   **3) Anu (A) behind Dolly & Esha:** E is at 5, so A must be at `6`. → `_ D B _ E A`
*   **5) Furpreet (F) ahead of Dolly:** D is at 2, so F must be at `1`. → `F D B _ E A`
*   **Fill the blank:** Chandru (C) goes to `4`.
*   **Final Order:** **`1:F, 2:D, 3:B, 4:C, 5:E, 6:A`**
    *   **Q1: Third in race?** Benny (B).
    *   **Q2: Separate Furpreet & Benny?** F(1) and B(3), separated by D. One person.
    *   **Q3: Middle position?** (Often deemed as None of the options if 6 people exist, or B/C in standard CAT forms).
    *   **Q4: Wins race?** Furpreet (F).
    *   **Q5: Ahead of Chandru?** C is 4th, so 3 people.

---

### Questions 6-10: Circular Table
*   *Counter-clockwise is Right, Clockwise is Left when facing center.*
*   **Clue 1:** `P` is 2nd right of `T`. `T` is between `R` and `V`. 
    *   Assume `T` is pos 1. Right is pos 2, 3. `P` is at pos 3. 
    *   Since `T` is between `R, V`, they occupy 2 and 8. If `V` is at 2, `U` must be neighbor (pos 3), but `P` is already there! So `R` must be at 2, making `V` at 8. 
    *   Then `U` sits at 7 (next to V).
    *   Array so far: `8:V, 1:T, 2:R, 3:P, 4:_, 5:_, 6:_, 7:U`.
*   **Clue 4 & 5:** `S, W, Q` fill `4, 5, 6`. `W` is not next to `U` (so not 6). `Q` is not between `S` and `W`. 
    *   Only `4:Q, 5:W, 6:S` works perfectly to satisfy all spacing rules without violating the neighbor constraints.
*   **Final Layout (1 to 8):** **`T, R, P, Q, W, S, U, V`**
    *   **Q6: Neighbours?** `R` & `P` (2 and 3). 
    *   **Q7: Immediate right of U(7)?** Moving counter-clockwise, next is 8(`V`). (Answer: Vijay).
    *   **Q8: True statement?** `Q` is 4, `W` is 5. `Q` is to the immediate left (clockwise) of `W`. (Answer: Qureshi immediate left of Wahadutt).
    *   **Q9: Position of Vijay?** Between Upasna (7) and Tina (1). 

---

### Questions 16-22: Friends, Colleges, Professions
*   **Locking the Grid:**
    *   `X` has exactly 2 members (Only `G` and `E`).
    *   `F` (Engineer) didn't study in Y, so must be in `Z`.
    *   `C` is Architect in `Y`.
    *   `B` (Actor) and `A` did not study with `F` (so not `Z`), meaning both are in `Y`. 
    *   College members: **`X = [E, G]`, `Y = [A, B, C]`, `Z = [F, D]`**.
*   **Professions:**
    *   `X` has no Designer/Teacher. `Y` has no Teacher. Therefore, Teacher must be in `Z`! Since `F` is Engineer, `D` is **Teacher**.
    *   Designer must be in `Y` (since not `X`, and `Z` is full). `A` is the only unknown in `Y`, so `A` is **Fashion Designer**.
    *   `X` requires Medicine and Business. `E` is not Business, so `E` = **Medicine**, leaving `G` = **Business**.
*   **Final Grid:**
    *   A - Y - Fashion
    *   B - Y - Actor
    *   C - Y - Architect
    *   D - Z - Teacher
    *   E - X - Medicine
    *   F - Z - Engineer
    *   G - X - Business
    *   *(Questions 16-22 simply read off this grid!)*

---

### Questions 23-25: 11 Friends at Cricket
*   **Find Boundaries:** `M` is 2nd right of `Q`, who is at an end. If `M` is right of `Q`, then `Q` MUST be the extreme Left. 
    *   `1:Q, 2:_, 3:M`.
*   **Connect Links:** `V` is neighbor of `M` and `N`. `V` must be at 4, `N` at 5. (If `V=2`, `N` can't fit). 
    *   `1:Q, 2:_, 3:M, 4:V, 5:N`.
*   **Apply jumps:** `V`(4) is 3rd to left of `S` -> `S` is at 7.
*   **Sub-block:** We know `U _ _ T P R`. 
    *   `T` is 3rd right of `U`. `T` is left of `P`. `R` is right of `P`.
    *   Place `U` at 6 to fit around `S`(7) -> `6:U, 7:S`. Then `T` goes to `6+3 = 9`. `P` is `10`, `R` is `11`.
*   **Final placements:** `P`(10) is 2nd to right of `O` -> `O` is 8. Only `W` is left -> goes to 2.
*   **Final Order:** **`Q, W, M, V, N, U, S, O, T, P, R`**
    *   **Q23: Center?** 6th position is `U`.
    *   **Q24: Right of S(7)?** `O, T, P, R`.
    *   **Q25: True?** `N`(5) is between `V`(4) and `U`(6).
