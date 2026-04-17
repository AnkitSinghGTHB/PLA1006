# Number System 2 - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./05_Number_System_Geometry_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Number system 2.pdf` practice set.

> [!TIP]
> **The Prime Factor Translation:** In advanced Number System questions, English phrases often secretly translate to Prime Factor rules.
> *   "Exactly 2 signatures/factors" = **Prime Number**
> *   "Exactly 3 factors" = **Square of a Prime Number** `(p^2)`

---

### Question 1
**Question:** X alarms toll at regular intervals. All of them toll together 12 times a day. If intervals are whole minutes, maximum possible value of X?
*   **Options:** `[A) 14  B) 16  C) 18  D) 20]`
*   **Mental Trick (LCM Factorization):**
    *   1 day = 1440 minutes.
    *   Tolling together implies finding a common synchronization point (an LCM).
    *   If they toll 12 times a day, their collective LCM must be `1440 / 12 = 120 minutes`.
    *   The maximum number of unique alarms `X` that can synchronize at exactly 120 minutes is simply the total number of distinct factors of 120!
    *   Prime factorize 120: `120 = 12 * 10 = (2^2 * 3) * (2 * 5) = 2^3 * 3^1 * 5^1`.
    *   Number of factors = `(3+1) * (1+1) * (1+1) = 4 * 2 * 2 = 16`.
*   **Answer:** **B) 16**.

---

### Question 3
**Question:** Let N be the largest number with exactly 3 factors that will perfectly divide 24!. How many factors does (N + 4) have?
*   **Options:** `[A) 12  B) 4  C) 6  D) 10]`
*   **Mental Trick:**
    *   Translation: "Exactly 3 factors" means N MUST be the square of a prime number ($p^2$).
    *   We need the largest prime whose square divides 24!.
    *   Primes in 24! are 2, 3, 5, 7, 11, 13, etc.
    *   Let's check 13: `13^2 = 169`. Does 169 divide 24!? No, 24! only contains one 13.
    *   Let's check 11: `11^2 = 121`. Does 121 divide 24!? Yes, 24! contains 11 and 22, so it contains two 11s!
    *   So, `N = 11^2 = 121`.
    *   The question asks for factors of `(N + 4)`. `121 + 4 = 125`.
    *   `125 = 5^3`. Number of factors = `3 + 1 = 4`.
*   **Answer:** **B) 4**.

---

### Question 4
**Question:** A positive number is divided by 100 to get a remainder thrice the quotient. If the number is divisible by 11, how many such numbers are less than 100000?
*   **Options:** `[A) 8  B) 5  C) 3  D) None of these]`
*   **Mental Trick (Algebraic Remainder Theorem):**
    *   `Number = (Divisor * Quotient) + Remainder`.
    *   `N = 100 * Q + R`.
    *   We are told `R = 3Q`. Substitute it: `N = 100Q + 3Q = 103Q`.
    *   Rule of division: Remainder must be LESS than divisor! So, `3Q < 100`, which means `Q ≤ 33`.
    *   We are also told `N` must be divisible by 11. 
    *   Since 103 is not divisible by 11, the `Q` term MUST be the multiple of 11!
    *   How many multiples of 11 exist up to 33? 
    *   Exactly three: `11, 22, 33`.
*   **Answer:** **C) 3**.

---

### Question 8
**Question:** Employee N signs all pages divisible by N. How many pages among the first 100 pages have exactly two signatures?
*   **Options:** `[A) 30  B) 25  C) 27  D) 24]`
*   **Mental Trick (Translation):**
    *   Employee 1 signs everything. A page gets a signature for every divisor it has.
    *   "Exactly two signatures" literally means the page number has "Exactly two factors".
    *   Numbers with exactly two factors (1 and themselves) are **Prime Numbers**!
    *   How many prime numbers exist between 1 and 100? This is a static math trivia number you must memorize for exams: **25**.
*   **Answer:** **B) 25**.

---

### Question 10
**Question:** Find the 260th term of the series a, b, b, c, c, c, d, d, d, d...
*   **Options:** `[A) u  B) w  C) t  D) v]`
*   **Mental Trick (Triangular Numbers):**
    *   The position of the last letter of any group follows the sum of N integers: `N(N+1)/2`.
    *   We need `N(N+1)/2 ≈ 260`, or `N(N+1) ≈ 520`.
    *   Mentally estimate squares: `20^2 = 400`, `22^2 = 484`.
    *   Let's try 22: `22 * 23 = 506`.
    *   So, `506 / 2 = 253`.
    *   This means the 253rd term is the final letter of the 22nd group ("v").
    *   The 254th term starts the 23rd group, which consists entirely of the 23rd letter of the alphabet.
    *   23rd letter is **w**. (Term 260 safely falls inside this block).
*   **Answer:** **B) w**.

---

### Question 11
**Question:** HCF of two natural numbers is 33 and sum is 528. Number of pairs satisfying?
*   **Options:** `[A) 4  B) 5  C) 3  D) 6]`
*   **Mental Trick:**
    *   If HCF is 33, numbers are `33x` and `33y` where `x` and `y` are purely co-prime.
    *   `33x + 33y = 528`  →  `x + y = 528 / 33`.
    *   Mentally divide: `528 / 33 = 16`.
    *   Now find pairs of CO-PRIME numbers that add to 16:
        *   (1, 15) ✅
        *   (2, 14) ❌ (divisible by 2)
        *   (3, 13) ✅
        *   (4, 12) ❌
        *   (5, 11) ✅
        *   (6, 10) ❌
        *   (7, 9) ✅
        *   (8, 8) ❌
    *   Total valid pairs = 4.
*   **Answer:** **A) 4**.
