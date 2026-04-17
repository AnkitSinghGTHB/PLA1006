# Calendars - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./03_Logical_Reasoning_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Calendars.pdf` practice set.

> [!TIP]
> **The Odd Day Rule:** Every calendar problem reduces to finding the remainder when the total number of days is divided by 7. 
> *   Normal year = 1 odd day.
> *   Leap year = 2 odd days.

---

### Question 3
**Question:** Which year will have the same calendar as that of the year 2007?
*   **Options:** `[a) 2014  b) 2016  c) 2018  d) 2019]`
*   **Mental Trick (The +11 / +6 / +28 Rule):** Memorize the calendar repetition cycles based on their position relative to the previous Leap Year:
    *   **Leap Year:** Repeats after **+28 years**.
    *   **Leap Year + 1:** Repeats after **+6 years**.
    *   **Leap Year + 2:** Repeats after **+11 years**.
    *   **Leap Year + 3:** Repeats after **+11 years**.
*   **Execution:** 2007 is exactly 3 years after the leap year 2004. So it falls into the `+3` category.
*   `2007 + 11 = 2018`.
*   **Answer:** **c) 2018**.

---

### Question 5
**Question:** Find the maximum number of Saturdays in the month of February.
*   **Options:** `[a) 3  b) 4  c) 5  d) 6]`
*   **Mental Trick:** Think of the extremes.
    *   Minimum case: A normal February has 28 days = exactly 4 weeks. Every day of the week occurs exactly 4 times.
    *   Maximum case: A leap year February has 29 days = 4 weeks + 1 extra day. 
    *   If that 1st day of the month happens to be a Saturday, that extra 29th day will also be a Saturday! This yields `4 + 1 = 5` Saturdays.
*   **Answer:** **c) 5**.

---

### Question 7
**Question:** What cannot be the last day of a century among the given options?
*   **Options:** `[a) Monday  b) Tuesday  c) Wednesday  d) Friday]`
*   **Mental Trick:** You have to memorize the 4 possible ending days of centuries based on their odd days (100y=5, 200y=3, 300y=1, 400y=0).
    *   5 odd days = **Friday**
    *   3 odd days = **Wednesday**
    *   1 odd day = **Monday**
    *   0 odd days = **Sunday**
    *   The days a century NEVER ends on are **Tuesday, Thursday, and Saturday** (TTS). 
*   **Answer:** **b) Tuesday**.

---

### Question 8
**Question:** In a particular year, January had exactly 4 Thursdays and 4 Sundays. On which day of the week did January 1 occur?
*   **Options:** `[a) Monday  b) Tuesday  c) Wednesday  d) Thursday]`
*   **Mental Trick (The 3-Day Block):**
    *   January has 31 days. `31 / 7 = 4 weeks + 3 days`.
    *   This means exactly 3 days will appear **5 times**, and the other 4 days will appear **4 times**.
    *   The 3 days that appear five times are ALWAYS consecutive (e.g. 1st, 2nd, 3rd of the month).
    *   We know Thursday and Sunday appear 4 times. That means our block of three consecutive 5x days *cannot* contain Thursday or Sunday.
    *   The only 3-day block that doesn't touch Sunday or Thursday is **Monday-Tuesday-Wednesday**.
    *   Therefore, Jan 1st was Monday, 2nd was Tuesday, 3rd was Wednesday.
*   **Answer:** **a) Monday**.

---

### Question 9
**Question:** By multiplying my birth date by 31 and month by 12, I got a total of 494. What could be my birth date and my birth month?
*   **Options:** `[a) 22nd July  b) 10th June  c) 12th April  d) 14th May]`
*   **Mental Trick (Even/Odd Logic & Unit Digits):**
    *   Equation: `(Date * 31) + (Month * 12) = 494`.
    *   Notice that 494 is **Even**. Since `(Month * 12)` is ALWAYS even, `(Date * 31)` MUST also be even for the sum to be even.
    *   This means the Date **must be an even number**. All options happen to be even Dates. 
    *   Let's check option d instantly using Unit Digits: `14 * 31` ends in **4**. `5 (May) * 12` ends in **0**. `4 + 0 = 4`. Matches the `4` in `494`!
    *   Verification: `(14 * 31) = 434`. `(5 * 12) = 60`. `434 + 60 = 494`. Perfect.
*   **Answer:** **d) 14th May**.

---

### Question 10
**Question:** Pinky was born on 29th February 2016 (a Monday). If she lives till her birthday in 2099, how many birthdays would she celebrate on a Monday other than what is given?
*   **Options:** `[a) 1  b) 2  c) 3  d) 5]`
*   **Mental Trick (The 28-Year Rule):** 
    *   For a Leap Year birthday (like 29th Feb) to fall on the exact same day of the week again, it requires a full **28-year cycle**.
    *   First repeat: `2016 + 28 = 2044` (Valid leap year).
    *   Second repeat: `2044 + 28 = 2072` (Valid leap year).
    *   Third repeat: `2072 + 28 = 2100` (Wait! 2100 is a century year not divisible by 400, so it is **NOT** a leap year. There is no Feb 29 in 2100!). Plus, it's after the 2099 cutoff anyway.
    *   She will only experience it 2 times.
*   **Answer:** **b) 2**.
