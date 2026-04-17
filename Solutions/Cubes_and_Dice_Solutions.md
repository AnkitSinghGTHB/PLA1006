# Cubes & Dice - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./03_Logical_Reasoning_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Cubes.pdf` practice set.

> [!TIP]
> **The `n-2` Rule for Cubes:** When an $N \times N \times N$ cube is painted on all sides:
> *   **3 faces painted:** 8 (Always the corners)
> *   **2 faces painted:** $12 \times (n-2)$ (The edges)
> *   **1 face painted:** $6 \times (n-2)^2$ (The center of the faces)
> *   **0 faces painted:** $(n-2)^3$ (The hidden core)

---

### Questions 1-3
**Setup:** 8cm cube cut to 2cm cubes. $N = 8/2 = 4$.
*   **Q1: No face painted?**
    *   Core = $(N-2)^3 = (4-2)^3 = 2^3 = 8$. **[Ans: 8]**
*   **Q2: 1 face painted?**
    *   Face centers = $6 \times (N-2)^2 = 6 \times 2^2 = 24$. **[Ans: 24]**
*   **Q3: 2 faces painted?**
    *   Edges = $12 \times (N-2) = 12 \times 2 = 24$. **[Ans: 24]**

---

### Questions 4-8
**Setup:** Cut into 64 cubes -> $N = \sqrt[3]{64} = 4$. Red on 2 adjacent, Black on opposites, Green on remaining.
*   **Q4: Only one side coloured?**
    *   This is independent of the alternating colours. Formula $6 \times (N-2)^2 = 24$. **[Ans: 24]**
*   **Q5: At least one side Red?**
    *   Red is on 2 adjacent faces.
    *   Each face has $N^2 = 16$ cubes. Total = 32.
    *   However, the 4 edge cubes where the two red faces meet are counted twice!
    *   Total = $32 - 4 = 28$. **[Ans: 28]**
*   **Q6: Red on one side, Black on opposite?**
    *   **Impossible.** A single small cube cannot have paint on opposite sides because the small cube itself does not span the entire width of the large cube. **[Ans: 0]**
*   **Q7: Three sides painted?**
    *   Always the 8 corners. **[Ans: 8]**

---

### Question 13
**Question:** Hollow 5cm cube made of 1cm cubes. 4 outer faces painted. How many unpainted faces of small cubes?
*   **Mental Trick (Total vs Painted):**
    *   A hollow 5x5x5 cube has no center. Number of cubes = $5^3 - 3^3 = 125 - 27 = 98$ cubes.
    *   Each small cube has 6 faces. Total small faces = $98 \times 6 = 588$ faces.
    *   Each outer face of the big 5cm cube contains $5 \times 5 = 25$ small faces.
    *   If 4 outer faces are painted, $4 \times 25 = 100$ small faces are covered in paint.
    *   Unpainted faces = $588 - 100 = 488$. 
*   **Answer:** **b) 488**.

---

### Question 17
**Question:** Least number of cuts to get 84 identical pieces?
*   **Mental Trick (Closest Factors):**
    *   Number of pieces = $(L+1) \times (B+1) \times (H+1)$.
    *   We need 3 factors of 84 that are as close to each other as possible.
    *   Factors: $3 \times 4 \times 7 = 84$.
    *   Cuts required = $(3-1) + (4-1) + (7-1) = 2 + 3 + 6 = 11$ cuts.
*   **Answer:** **a) 11**.

---

### Question 18
**Question:** 12cm cube cut into 1cm cubes. Opposite Reds, Opposite Blues, 1 Black, **1 UNPAINTED**. Number of 0-face painted cubes?
*   **Mental Trick (Inner Volume Adjustment):**
    *   Normally, the core is $(N-2)^3$. We subtract 2 because paint is on BOTH opposite faces.
    *   Pair 1 (Red): 2 faces painted -> $(12 - 2) = 10$.
    *   Pair 2 (Blue): 2 faces painted -> $(12 - 2) = 10$.
    *   Pair 3 (Black / Unpainted): Because one face has NO PAINT, we don't subtract an outer layer for that face!
    *   Inner core for Pair 3 = $(12 - 1) = 11$.
    *   Total 0-face painted = $10 \times 10 \times 11 = 1100$.
*   **Answer:** **a) 1100**.

---

### Question 20
**Question:** 125 cubes (5x5x5). Four corner columns removed. Rest exposed faces painted red (EXCEPT bottom face). How many have NO coloured face?
*   **Mental Trick (Core Analysis):**
    *   The "0-face painted" cubes are always the internal core.
    *   Normally for 5x5x5, core = $3 \times 3 \times 3 = 27$.
    *   However, the bottom face is NOT painted. This means the bottom-most layer of the $3 \times 3$ inner core column is suddenly safe from paint!
    *   The protected core height becomes $(N-1) = 4$ instead of $(N-2)$.
    *   Core dimensions = $3 \times 3 \times 4 = 36$ cubes.
    *   *Did removing the corner columns expose the core?* No. The corner columns are at the edges (grid $1,1$). The core is strictly inside (grid $2,3,4$). Removing corners does not touch the core.
*   **Answer:** **d) 36**.
