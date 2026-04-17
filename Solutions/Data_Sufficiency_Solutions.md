# Data Sufficiency - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./04_Data_Sufficiency_Interpretation_CheatSheet.md)

This document contains step-by-step logic frameworks for the `Data Sufficiency.pdf` practice set.

> [!TIP]
> **The Golden Rule of Data Sufficiency:** You NEVER need to actually solve the problem. You only need to determine if a unique solution *exists*. A definitive "NO" is just as sufficient as a definitive "YES".

**Options Code:**
*   **A:** Statement 1 alone is sufficient.
*   **B:** Statement 2 alone is sufficient.
*   **C:** Both statements together are necessary.
*   **D:** Either statement 1 or 2 alone is sufficient.
*   **E:** Neither is sufficient.

---

### Question 1
**Question:** What is the value of x?
*   **S1:** `3 < x < 5`. (x could be 3.5, 4, 4.1... since "integer" isn't specified). **Not Sufficient.**
*   **S2:** `x^2 = 16`. (x could be 4 or -4). **Not Sufficient.**
*   **Combination:** `3 < x < 5` AND `x = ±4`. The only overlapping value is exactly `x = 4`.
*   **Answer:** **C - Both statements taken together are sufficient**.

### Question 4
**Question:** Is the length of a side of equilateral triangle E less than the length of a side of square F? (Is $a < s$?)
*   **S1:** Perimeters are equal. $3a = 4s \implies a = 1.33s$. Therefore, $a$ is GREATER than $s$. We can definitively answer the question with a "NO". **Sufficient!**
*   **S2:** Ratio of Height(E) to Diagonal(F) = $2\sqrt{3} : 3\sqrt{2}$. 
    *   Height(E) = $\frac{\sqrt{3}a}{2}$ and Diagonal(F) = $\sqrt{2}s$. 
    *   Equating the ratios completely cancels the square roots and yields the exact same equation: $a = 1.33s$. Again, a definitive "NO". **Sufficient!**
*   **Answer:** **D - Either 1 or 2 is sufficient**.

### Question 7
**Question:** When did Santosh reach the college?
*   **S1:** Distance = 10km. **Not Sufficient.**
*   **S2:** Speed = 40 km/hr. **Not Sufficient.**
*   **Combination:** We know Time Taken = $10 / 40 = 15$ mins. BUT we have absolutely no idea what time he started driving! Thus we cannot find arrival time.
*   **Answer:** **E - Both together are not sufficient**.

### Question 11
**Question:** In a race of A, B, C, D, who finishes last?
*   **S1:** A beats B by 100m, C by 60m, D by 40m. This means at the exact moment A crosses the finish line, B is the furthest away (100m behind). Thus B is unambiguously last. **Sufficient.**
*   **S2:** B beats C and D by 20m and 10m. This means B is ahead of C and D, so B is NOT last, but we have no idea who is last. **Not Sufficient.**
*   **Answer:** **A - Statement 1 alone is sufficient**.

### Question 12
**Question:** A straight corridor has doors A, B, C, D in that order. Distance between B and C?
*   **Line Map:** `A ---- B ---- C ---- D`
*   **S1:** BD = 10. (BC + CD = 10). **Not Sufficient.**
*   **S2:** AC = 12. (AB + BC = 12). **Not Sufficient.**
*   **Combination:** We have two equations `BC + CD = 10` and `AB + BC = 12`, but 3 variables (`AB, BC, CD`). We cannot isolate `BC`. Example: `BC` could be 2 or it could be 5, both work.
*   **Answer:** **E - Both together are not sufficient**.

### Question 13
**Question:** How many articles are written by staff with >5 yrs exp?
*   **Core Fact:** The question prompt gives us percentages relative to the Total. $0.60 \times 0.75 \times \text{Total} = \text{Target Answer}$. To solve this, we ONLY need the numeric value of the `Total`.
*   **S1:** 20 articles written by staff. Since prompt says "50% of total are by staff", we know $50\% = 20 \implies \text{Total} = 40$. We can now solve it. **Sufficient.**
*   **S2:** Gives a random percentage about another sub-group. No absolute numbers. **Not Sufficient.**
*   **Answer:** **A - Statement 1 alone is sufficient**.

### Question 15
**Question:** Is x = -11?
*   **S1:** $x^2 = 144 \implies x$ is either $12$ or $-12$. Is it $-11$? Definitely NO. A decisive "NO" is sufficient! **Sufficient.**
*   **S2:** x is a natural number (1, 2, 3...). Is it $-11$? Definitely NO. **Sufficient.**
*   **Answer:** **D - Either 1 or 2 is sufficient**.
