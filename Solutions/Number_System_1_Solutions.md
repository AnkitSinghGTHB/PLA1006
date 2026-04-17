# Number System 1 - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./05_Number_System_Geometry_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Number system 1.pdf` practice set.

> [!TIP]
> **The Prime Factorization Trick:** Almost every number system problem (Factors, HCF, LCM, trailing zeroes) is solved by breaking the numbers into their prime powers first.

---

### Question 1
**Question:** What is the least number which when divided by 7, 8 and 11 always gives 6 as remainder?
*   **Options:** `[A) 624  B) 622  C) 616  D) 654]`
*   **Mental Trick (LCM + Remainder):**
    *   Find the LCM of 7, 8, 11. Since they are all co-prime, just multiply them.
    *   `7 * 8 = 56`.
    *   `56 * 11 = 616`. (Trick: Write 5 and 6, and insert their sum in the middle: 616).
    *   Since it leaves a remainder of 6, just add 6 to the LCM.
    *   `616 + 6 = 622`.
*   **Answer:** **B) 622**.

---

### Question 2
**Question:** GCD of two numbers is 3. Their LCM is 36. One number is 9. Find the other.
*   **Options:** `[A) 18  B) 12  C) 14  D) 16]`
*   **Mental Trick (The Product Rule):**
    *   `Product of Numbers = LCM * GCD`.
    *   `9 * B = 3 * 36`.
    *   `9 * B = 108`.
    *   `B = 108 / 9 = 12`.
*   **Answer:** **B) 12**.

---

### Question 3
**Question:** Find the Greatest Number that divides 70 and 125 leaving remainders 5 and 8 respectively.
*   **Options:** `[A) 12  B) 11  C) 13  D) 15]`
*   **Mental Trick (Subtract first, then HCF):**
    *   Subtract the remainders from the numbers.
    *   `70 - 5 = 65`.
    *   `125 - 8 = 117`.
    *   Now find the Highest Common Factor (HCF) of 65 and 117.
    *   Think about the factors of 65: `1, 5, 13, 65`.
    *   Does 13 divide 117? Yes, `13 * 9 = 117`.
    *   So, the greatest number is 13.
*   **Answer:** **C) 13**.

---

### Question (i-powers)
**Question:** `(i^799 + i^800 + i^801 + i^802) / (i^343 + i^344 + i^345 + i^346)` = ?
*   **Options:** `[A) 1  B) 2  C) 0  D) Can't be determined]`
*   **Mental Trick (Cycle of i):**
    *   The sum of any **four consecutive powers** of imaginary number `i` is ALWAYS zero.
    *   The numerator is four consecutive powers. Numerator = 0.
    *   Therefore, the whole expression is 0.
*   **Answer:** **C) 0**.

---

### Question 3 (Factors)
**Question:** How many factors of 1080 are perfect squares?
*   **Options:** `[A) 4  B) 6  C) 8  D) 5]`
*   **Mental Trick:**
    *   Prime factorize 1080: `108 * 10` = `27 * 4 * 2 * 5` = `2^3 * 3^3 * 5^1`.
    *   For a factor to be a perfect square, its prime powers must be **even**.
    *   Allowed powers of 2 (from max 3): `2^0, 2^2`. (That's **2** options).
    *   Allowed powers of 3 (from max 3): `3^0, 3^2`. (That's **2** options).
    *   Allowed powers of 5 (from max 1): `5^0`. (That's **1** option).
    *   Multiply options: `2 * 2 * 1 = 4`.
*   **Answer:** **A) 4**.

---

### Question 4
**Question:** How many factors of `2^4 * 5^3 * 7^4` are odd numbers?
*   **Options:** `[A) 100  B) 99  C) 20  D) 24]`
*   **Mental Trick (Ignore the Evens):**
    *   To get an odd factor, you must **completely ignore** the Prime Factor 2. (Treat its power as 0).
    *   Just look at `5^3 * 7^4`.
    *   Number of factors = Add 1 to each power and multiply.
    *   `(3 + 1) * (4 + 1) = 4 * 5 = 20`.
*   **Answer:** **C) 20**.

---

### Question 5
**Question:** What is the highest power of 12 in 100!?
*   **Options:** `[A) 12  B) 48  C) 24  D) 97]`
*   **Mental Trick (Trailing Zero Variation):**
    *   12 is made of `2^2 * 3^1`. We need the bottleneck (limiting resource). Let's find both in 100!
    *   Powers of 3: `100/3 + 100/9 + 100/27 + 100/81 = 33 + 11 + 3 + 1 = 48`. (Integer division).
    *   Powers of 2: `100/2 + 100/4 + 100/8 + ... = 50 + 25 + 12 + 6 + 3 + 1 = 97`.
    *   To make a 12, we need ONE power of 3 and TWO powers of 2.
    *   We have 48 threes. We have 97 twos, meaning we can form `97 / 2 = 48` pairs of twos.
    *   Since we have 48 of both components, we can form exactly 48 twelves.
*   **Answer:** **B) 48**.

---

### Question 11
**Question:** What will be remainder when 17^200 is divided by 18?
*   **Options:** `[A) 17  B) 16  C) 1  D) 2]`
*   **Mental Trick (Negative Remainders):**
    *   When dividing 17 by 18, the remainder can be written as `-1`.
    *   So, substitute 17 with `-1`.
    *   `(-1)^200`. Since 200 is an **even** power, the negative cancels out.
    *   Result = `1`.
*   **Answer:** **C) 1**.

---

### Question 12
**Question:** The H.C.F. of 9/10, 12/25, 18/35 and 21/40 is:
*   **Options:** `[A) 3  B) 4/5  C) 3/1400  D) 3/400]`
*   **Mental Trick (Fraction Formula):**
    *   `HCF of Fractions = HCF of Numerators / LCM of Denominators`.
    *   Numerators: `9, 12, 18, 21`. Their highest common factor is strongly **3**.
    *   Denominators: `10, 25, 35, 40`.
    *   Their LCM must contain `25` (5^2), `8` (2^3), and `7`. Let's multiply them: `25 * 8 = 200`. `200 * 7 = 1400`.
    *   Fraction = `3 / 1400`.
*   **Answer:** **C) 3/1400**.
