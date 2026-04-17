# Mensuration & Geometry - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./05_Number_System_Geometry_CheatSheet.md)

This document contains mental math strategies and trap avoidance techniques for the `Mensuration.pdf` practice set.

> [!TIP]
> **The Proportionality Cheat Code:** Whenever dimensions scale, remember:
> *   Perimeters scale by a factor of $x$.
> *   Areas scale by a factor of $x^2$.
> *   Volumes scale by a factor of $x^3$.
> Never calculate raw volumes if you only need the scale factor!

---

### Question 3: The Brick Wall
**Question:** Bricks $13 \times 12 \times 19$ cm. Wall $390 \times 400 \times 410$ cm. 24% of the wall is sand and cement. How many bricks are needed?
*   **Options:** `[A) 20,000  B) 14,800  C) 18,200  D) 16,400]`
*   **Mental Trick (Ratio Cancellation before Multiplication):**
    *   Do NOT calculate absolute volumes first! Large numbers cause errors.
    *   If 24% is sand/cement, exactly $76\%$ of the wall's volume is made of bricks.
    *   $$Number = \frac{0.76 \times 390 \times 400 \times 410}{13 \times 12 \times 19}$$
    *   Notice the direct multiples!
        *   $390 / 13 = 30$
        *   $0.76 / 19 = 0.04$
    *   Equation becomes: $0.04 \times 30 \times 400 \times \frac{410}{12}$
    *   Simplify $0.04 \times 400 = 16$.
    *   $16 \times 30 / 12 = 480 / 12 = 40$.
    *   Finally: $40 \times 410 = 16,400$.
*   **Answer:** **D) 16,400**.

---

### Question 6: The Folded Cylinder
**Question:** A rectangular 11 cm × 4 cm paper is folded *without overlapping* to make a cylinder of height 4 cm. Volume?
*   **Options:** `[A) 27.5 cm3  B) 38.5 cm3  C) 25.3 cm3  D) 11.5 cm3]`
*   **Mental Trick (Unrolling the shape):**
    *   If the height is 4cm, then the `11 cm` length of the paper became the circular circumference of the base!
    *   $2\pi r = 11 \implies 2 \times (\frac{22}{7}) \times r = 11 \implies \frac{44}{7} r = 11 \implies r = \frac{7}{4}$.
    *   Volume = $\pi \times r^2 \times h$.
    *   Vol = $\frac{22}{7} \times (\frac{7}{4})^2 \times 4 = \frac{22}{7} \times \frac{49}{16} \times 4$.
    *   Cancel $7$ with $49$ (leaves 7). Cancel $4$ with $16$ (leaves 4).
    *   Vol = $\frac{22 \times 7}{4} = \frac{154}{4} = 38.5$.
*   **Answer:** **B) 38.5 cm3**.

---

### Question 10: Percentage Scaling
**Question:** If each edge of a cube is increased by 10%, what is the percentage increase in volume?
*   **Options:** `[A) 33.1%  B) 11.1%  C) 22.1%  D) 25.5%]`
*   **Mental Trick (Volume Multiplier):**
    *   Increase of 10% means the side is multiplied by $1.1$.
    *   Since Volume = $Side^3$, the new volume is multiplied by $1.1^3$.
    *   $1.1 \times 1.1 = 1.21$
    *   $1.21 \times 1.1 = 1.331$.
    *   A multiplier of $1.331$ is exactly a **33.1%** increase.
*   **Answer:** **A) 33.1%**.

---

### Question 12: Melting & Recasting
**Question:** Solid sphere of radius 26cm melted into a cone with *diameter* 26cm. Height of cone?
*   **Options:** `[A) 200  B) 392  C) 416  D) 304]`
*   **Mental Trick (Keep Pi and Variables till end):**
    *   Sphere: $R = 26$. Cone: $r = 13$ (since diameter is 26).
    *   Volume Sphere = $\frac{4}{3} \pi (26)^3$.
    *   Volume Cone = $\frac{1}{3} \pi (13)^2 \times h$.
    *   Equate and cancel $\frac{1}{3} \pi$ from both sides immediately.
    *   $4 \times 26^3 = 13^2 \times h$.
    *   Replace $26$ with $(2 \times 13)$:
    *   $4 \times (2^3 \times 13^3) = 13^2 \times h$.
    *   Notice $13^2$ cancels from both sides, leaving just one $13$ on the left.
    *   $4 \times 8 \times 13 = h \implies 32 \times 13 = h$.
    *   $32 \times 10 = 320$. $32 \times 3 = 96$. $320 + 96 = 416$.
*   **Answer:** **C) 416 cm**.

---

### Question 21: Longest Pole
**Question:** Longest pole in a room 12 m long, 8 m broad and 9 m high?
*   **Options:** `[A) 16  B) 17  C) 18  D) 9]`
*   **Mental Trick (3D Pythagorean Theorem):**
    *   The longest pole in any rectangular box is the internal diagonal.
    *   $D = \sqrt{L^2 + B^2 + H^2}$.
    *   $D = \sqrt{144 + 64 + 81} = \sqrt{289}$.
    *   You should memorize squares up to 25. $\sqrt{289} = 17$.
*   **Answer:** **B) 17m**.

---

### Question 23: Polygon Diagonals
**Question:** A polygon has 27 diagonals. Number of sides?
*   **Options:** `[A) 9  B) 10  C) 11  D) 12]`
*   **Mental Trick (Diagonal Formula):**
    *   Diagonals = $\frac{n(n-3)}{2}$.
    *   $27 = \frac{n(n-3)}{2} \implies 54 = n(n-3)$.
    *   Look for two factors of 54 that have a difference of 3.
    *   Factors: $6 \times 9 = 54$.
    *   Therefore, $n = 9$. (You don't need to solve quadratic equations!)
*   **Answer:** **A) 9**.

---

### Question 28: Flowing Water Rate
**Question:** Water flows into a tank $200m \times 150m$ from a pipe $1.5m \times 1.25m$ at 20 kmph. Time to rise 2m? (in minutes).
*   **Options:** `[A) 234  B) 1.2 hrs  C) 9 hrs  D) 96 min]`
*   **Mental Trick (Volume Rate logic):**
    *   Required Volume = $200 \times 150 \times 2 = 60,000 \text{ m}^3$.
    *   Flow Rate = Area of Pipe $\times$ Speed.
    *   Speed = 20 km/hr = $20,000 \text{ m/hr}$.
    *   Area of pipe = $1.5 \times 1.25 = \frac{3}{2} \times \frac{5}{4} = \frac{15}{8} \text{ m}^2$.
    *   Flow Rate = $\frac{15}{8} \times 20,000 = 15 \times 2500 = 37,500 \text{ m}^3\text{/hr}$.
    *   Time = $\frac{60,000}{37,500} = \frac{600}{375} = \frac{24}{15} = 1.6 \text{ hours}$.
    *   Convert to minutes: $1.6 \times 60 = 96 \text{ mins}$.
*   **Answer:** **D) 96 min**.
