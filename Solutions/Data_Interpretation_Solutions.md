# Data Interpretation - Mental Math & Trap Avoidance Guide

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./04_Data_Sufficiency_Interpretation_CheatSheet.md)

Due to the visual nature of Data Interpretation (Pie Charts, Bar Graphs, Tables), standard text extraction hides the raw numbers. However, the questions extracted from the `Data Interpretation.pdf` sets reveal classic **Exam-Hall Traps** that you must know how to navigate!

Here is how you solve the exact question types present in your PDFs using mental math and trap-avoidance.

> [!CAUTION]
> **The Golden Rule of DI:** Never calculate absolute values unless explicitly asked. Always solve in percentages or ratios first, and only apply the absolute total at the very last step!

---

### Type 1: The "Profit Percentage" Trap (Question 16)
**The Scenario:** You are given a graph showing the **Annual Profit Percent** of a company from 1995 to 2000. 
**Question:** In which year is the Expenditure maximum?
*   a) 2000
*   b) 1997
*   c) 1995
*   d) Cannot be determined

**The Exam-Hall Strategy:**
*   Profit Percentage = $\frac{\text{Income} - \text{Expenditure}}{\text{Expenditure}} \times 100$.
*   The graph ONLY gives you percentages (the ratio). It gives you absolutely ZERO information about the base values.
*   A company could have a 100% profit on Rs. 10 (Exp = 10), or a 2% profit on Rs. 1,000,000 (Exp = 1M).
*   **Without at least one absolute value (total income, total profit in Rs, etc.), you can NEVER calculate absolute expenditure or income.**
*   **Answer:** **D) Cannot be determined**. (Do not waste time trying to read the graph!).

---

### Type 2: The Pie Chart "Difference" Shortcut (Question 1)
**The Scenario:** A pie chart shows company expenditure on sports. Total amount = Rs. 1,80,00,000.
**Question:** How much does the amount spent on Cricket exceed Hockey?

**The Mental Math Approach:**
*   **Amateur Method:** 
    1. Calculate Cricket Amount = (Cricket % / 100) * 1,80,00,000.
    2. Calculate Hockey Amount = (Hockey % / 100) * 1,80,00,000.
    3. Subtract Hockey from Cricket. *(Takes 2-3 minutes, high error rate)*
*   **Exam-Hall Method:**
    1. Look at the Pie Chart and subtract the percentages directly in your head!
    2. If Cricket is 35% and Hockey is 15%, the difference is **20%**.
    3. Now just calculate 20% of 1,80,00,000. 
    4. 10% is 18,00,000. So 20% is **Rs. 36,00,000**. *(Takes 10 seconds)*.

---

### Type 3: The "Rate of Change" Bar Graph (Question 8)
**The Scenario:** Bar graph showing sales from 1997 to 2002. 
**Question:** Between which two consecutive years is the rate of change minimum?

**The Mental Math Approach:**
*   "Rate of change" = $\frac{\text{Final} - \text{Initial}}{\text{Initial}}$.
*   Do NOT calculate this fraction for every single pair of years!
*   **Visual Shortcut:** 
    1. Look for the two bars that are almost the same height. 
    2. A perfectly flat step between two bars means the change is 0 (Minimum!). 
    3. Just visually identify the smallest vertical step between any two consecutive bars. Verify the math ONLY for the two smallest visual steps.

---

### Type 4: Complex Tournaments / Missing Data (Questions 9-12)
**The Scenario:** A partial table showing runs scored by 5 players in 4 matches. Two values missing per column. Rule: "Missing values cannot be more than 10% of total runs".
**The Strategy:**
*   This is a classic logical-DI puzzle. 
*   **Constraint Satisfaction:** The key is the "10% rule". If the total runs for a match is 200, the missing values CANNOT be strictly greater than 20. 
*   Subtract all *known* scores from the Total. You will get a remaining balance.
*   You must split that balance between the two missing players such that NEITHER value exceeds the 10% cap. Often, there is only one mathematically possible pair of integers that satisfies this, locking the data in place!

---

### Type 5: Cricket Partnerships Logic (Questions 16-20)
**The Scenario:** Table 1 = Score at fall of each wicket. Table 2 = Runs by each batsman. 
**Question:** "Who lost his wicket between Hayden and Hussey's dismissal?"
**The Strategy:**
*   Cricket DI requires understanding the rules of cricket:
    1. A partnership is the difference between the score at "Wicket N" and "Wicket N-1".
    2. Batsmen come out in order. Wicket 1 means 1 batsman is out, 1 remains, Batsman 3 comes in.
*   **Mapping:** Trace the "Fall of Wicket" score against the individual runs. If Wicket 1 fell at 25 runs, and Opener A scored 20 and Opener B scored 50, Opener A MUST be the one who got out (he couldn't score 20 if the team score was 100!).
*   Use chronological scoring caps to eliminate batsmen.
