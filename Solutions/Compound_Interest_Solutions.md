# Compound Interest - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./01_Arithmetic_Percentages_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Compound Interest.pdf` practice set.

> [!TIP]
> **The Fractional Multiplier Trick:** Treat Compound Rate percentages as fractions (`5% = 1/20`) and add 1 to get the multiplier (`21/20`). Then literally square or cube it depending on the years. Skip the complicated $P(1+r/100)^n$ formula.

---

### Question 1
**Question:** Compound interest on Rs. 8000 at 5% per annum for 3 years?
*   **Options:** `[A) 1262  B) 1261  C) 1260  D) 1361]`
*   **Mental Trick:**
    *   `5% = 1/20`. The growth multiplier is `21/20`.
    *   3 years = Cube the multiplier. `(21/20)^3 = 9261 / 8000`.
    *   This fraction perfectly maps to our principal of 8000! 
    *   Final Amount = 9261. 
    *   Interest = `9261 - 8000 = 1261`.
*   **Answer:** **B) Rs. 1261**.

---

### Question 2
**Question:** Invested at CI payable annually. Interest in 1st year = Rs. 400. Interest in 2nd year = Rs. 420. Find the sum.
*   **Options:** `[A) 8000  B) 7500  C) 8500  D) 6500]`
*   **Mental Trick (Interest on Interest):**
    *   The extra Rs. 20 generated in the 2nd year is literally just the interest ON the first year's Rs. 400 interest.
    *   Rate = `20 / 400 = 1/20 = 5%`.
    *   We know 5% of the main Principal generated the first year's 400 Rs interest.
    *   `5% of P = 400`.
    *   `100% of P = 400 * 20 = 8000`.
*   **Answer:** **A) Rs. 8000**.

---

### Question 3
**Question:** Sum of $2000 returned as $2205 after 2 years compounded annually. Rate?
*   **Options:** `[A) 2%  B) 3%  C) 4%  D) 5%]`
*   **Mental Trick (Square Root Mapping):**
    *   Take the ratio of Amount to Principal: `2205 / 2000`.
    *   Simplify by dividing by 5: `441 / 400`.
    *   Since it's 2 years, what is the square root of that? `21 / 20`.
    *   `21/20` means generating an extra 1 part on a base of 20. 
    *   `1/20 = 5%`.
*   **Answer:** **D) 5%**.

---

### Question 4
**Question:** CI on Rs. 500 for 1 year at 40% p.a. compounded quarterly.
*   **Options:** `[A) 146.01  B) 133.1  C) 732.50  D) 232.05]`
*   **Mental Trick (Successive % Rule for 4 Cycles):**
    *   Quarterly rate = `40% / 4 = 10%`.
    *   Time = 4 quarters (cycles).
    *   Apply successive formula `A + B + AB/100` for 10% four times.
    *   Combine first two 10%s: `10 + 10 + 1 = 21%`.
    *   Now combine two 21%s: `21 + 21 + (441/100) = 42 + 4.41 = 46.41%`.
    *   Calculate exactly 46.41% of 500. `0.4641 * 500 = 46.41 * 5 = 232.05`.
*   **Answer:** **D) Rs. 232.05**.

---

### Question 7
**Question:** Car purchased 3 years ago for 0.4 million (400,000). Depreciates 20% p.a. Present value?
*   **Options:** `[A) 691200  B) 241800  C) 204800  D) 24800]`
*   **Mental Trick:**
    *   Depreciation of 20% (`1/5`) means retaining `4/5` of the value each year.
    *   Multiplier for 3 years = `(4/5)^3 = 64 / 125`.
    *   Calculation: `400,000 * (64 / 125)`.
    *   *Quick Division:* `1000 / 125 = 8`. So `400,000 / 125 = 400 * 8 = 3200`.
    *   `3200 * 64 = 204,800`.
*   **Answer:** **C) 204800**.

---

### Question 11
**Question:** Effective annual rate corresponding to 8% p.a. payable half-yearly.
*   **Options:** `[A) 8.16%  B) 6.16%  C) 7.16%  D) 5.16%]`
*   **Mental Trick:**
    *   Half-yearly rate = `8% / 2 = 4%`.
    *   This 4% is applied twice in one year.
    *   Effective rate = `4 + 4 + (4*4)/100 = 8 + 0.16 = 8.16%`.
*   **Answer:** **A) 8.16%**.

---

### Question 12
**Question:** Amounts after 2nd and 3rd year are Rs. 19860 and Rs. 21846. Rate?
*   **Options:** `[A) 10%  B) 20%  C) 30%  D) 40%]`
*   **Mental Trick:**
    *   In Compound Interest, the Amount at the end of Year 2 acts as the *Principal* for Year 3.
    *   Interest generated in Year 3 = `21846 - 19860 = 1986`.
    *   Rate = `(Interest / Principal) * 100` = `(1986 / 19860) * 100 = 10%`.
*   **Answer:** **A) 10%**.

---

### Question 18
**Question:** Bank offers 10% CI half-yearly. Customer deposits Rs. 1000 on Jan 1 and Rs. 1000 on July 1. Total interest by end of year?
*   **Options:** `[A) 2152.50  B) 152.50  C) 1152.50  D) 315]`
*   **Mental Trick:**
    *   "10% half-yearly" means 5% every 6 months.
    *   **January Deposit:** Stays in bank for two 6-month cycles. Effective return = `5 + 5 + 0.25 = 10.25%`. Interest on 1000 = **102.50**.
    *   **July Deposit:** Stays in bank for only one 6-month cycle. Return = `5%`. Interest on 1000 = **50.00**.
    *   Total interest = `102.50 + 50.00 = 152.50`.
*   **Answer:** **B) Rs. 152.50**.
