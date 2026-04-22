# Data Interpretation & Sufficiency

---

## 1. Data Interpretation (DI)

### 🚫 The Ultimate Rule: NEVER Calculate Exact Values!
Look at the options first. If they are widely spaced, heavily round your numbers. 

*   **Example Question:** A table shows company revenue growing from $49,732 in 2021 to $101,564 in 2022. The options for percentage growth are: `[A) 48%, B) 74%, C) 104%, D) 140%]`
    *   **Mental Solution:** 
        *   Don't subtract 101,564 - 49,732! 
        *   Mentally round $49,732 to roughly $50k. Round $101,564 to roughly $100k.
        *   $50k growing to $100k is exactyl doubling. Doubling = a **100% increase**.
        *   Which option is closest to 100%? **Option C (104%)**. You solved it in 5 seconds.

### 📊 Pie Chart Conversion Trick
**1% of a Pie Chart = 3.6 Degrees**
*   **Example Question:** A pie chart showing monthly expenses allocates a sector of 72° to "Rent". What percentage of the budget is spent on Rent?
    *   **Mental Solution:** Just divide by 3.6. 
    *   `72 / 3.6` (multiply both by 10 to clear decimal) -> `720 / 36` = **20%**.

### 📈 Single vs. Multiple Charts (DI)
*   **Single Chart:** Usually straightforward. The key is to establish the "total" or "base value" immediately before attempting to calculate individual slices, bars, or line points.
*   **Multiple Charts:** Commonly a Pie Chart (showing percentages of a total) paired with a Data Table (showing ratios within those percentages, e.g., Male:Female ratio).
    *   *Strategy:* **Never calculate absolute values until the final step.** If the question asks for a ratio or percentage, you can almost always solve it using just the percentage and ratio units from the charts, completely ignoring the massive absolute total (e.g., "Total Population = 4,567,890").

---

## 2. Data Sufficiency (DS)

### ⚠️ The Golden Rule: DO NOT SOLVE FOR VALUES!
The only question you are asking yourself is: **"Is there enough information to force exactly ONE unique answer?"**

*   **Example Question:** Question: What is the specific value of x?
    *   *Statement 1:* `x^2 = 25`
    *   *Statement 2:* `x is a negative integer`
    *   **Mental Solution:** 
        1. **Evaluate Statement 1 alone:** `x^2 = 25` means x could be 5 OR -5. It doesn't give a *single unique* answer. Therefore, S1 alone is **Insufficient**.
        2. **Evaluate Statement 2 alone:** `x` is negative. This doesn't give us any numerical value at all. S2 alone is **Insufficient**.
        3. **Evaluate Both Together:** If `x` can be 5 or -5, AND `x` is negative, then `x` MUST be exactly `-5`. Because it yields a single, unique answer, they are sufficient *together*.
        *   **Answer:** Both statements 1 and 2 together are necessary and sufficient.

### 🧠 Variable Counting Trick
If a question asks for the exact ages of 3 people (3 variables), you generally need 3 distinct, independent mathematical equations.
*   **Example Question:** What are the exact prices of an apple, banana, and cherry?
    *   *Statement 1:* 2 apples + 3 bananas = $5
    *   *Statement 2:* 1 apple + 1 cherry = $3
    *   **Mental Solution:** Look at the structure instantly. We have 3 variables (A, B, C) but only 2 equations inside the statements. You mathematically cannot lock down 3 unique variables with only 2 equations. 
    *   **Answer:** Instantly mark: Both statements together are STILL insufficient. (Saves 3 minutes of algebra).

---

## 🔥 High-Frequency Exam Patterns & Hotspots

### 📉 The "Base" Trap in DI
When comparing two percentages, ensure you know what the base is. 10% of a 2021 budget is not the same as 10% of a 2022 budget. Do not blindly add percentages from different pie charts without converting them to absolute values first.

### ❓ The DS "Yes/No" Trap
In Data Sufficiency, if a question asks "Is X > Y?", a definitive "**NO**" means the statement IS sufficient. Sufficiency is about having enough data to answer the question definitively, even if the answer is negative.

### 🧮 Simultaneous Equations Trap in DS
Two variables generally require two equations. BUT, if the equations are proportional (e.g., `x + y = 10` and `2x + 2y = 20`), they are functionally only ONE equation. Beware of redundant statements posing as new information.
