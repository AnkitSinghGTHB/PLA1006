# Blood Relations - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./03_Logical_Reasoning_CheatSheet.md)

This document contains step-by-step mental math strategies for the `Blood Relations.pdf` practice set.

> [!TIP]
> **The Backwards Trace Trick:** Whenever someone is pointing to a photograph and describing a relationship, **never read left to right**. Locate the word `"MY"` or `"MINE"` and resolve the family tree backwards step-by-step.

---

### Question 3
**Question:** On seeing a photograph of a boy, a man said, *"He is the son of the only son of my mother."* How is the man related to that boy?
*   **Mental Trick (Trace Backwards):**
    1.  Start at `"my mother"`.
    2.  Move backwards to `"only son of (my mother)"`. Since the speaker is a man, the *only* son of his mother is **HIMSELF**.
    3.  Move backwards to `"son of (MYSELF)"`.
    4.  So, the boy in the photograph is his son.
*   **Answer:** The man is the **Father** of the boy.

---

### Question 4
**Question:** Rama told Lakshmana, *"Yesterday, I met the only brother of the daughter of my grandmother."* Whom did Rama meet?
*   **Mental Trick:**
    1.  Start at `"my grandmother"`.
    2.  Move backward: `"daughter of (my grandmother)"`. Your grandmother's daughter is your **Mother** (or aunt, but usually assume mother unless stated otherwise).
    3.  Move backward: `"only brother of (my Mother)"`. Your mother's brother is your **Maternal Uncle**.
*   **Answer:** Rama met his **Maternal Uncle**.

---

### Question 5
**Question:** Pointing to a photo, Mr. Bean said: *"I have no brother or sister but that fellow’s father is my father’s son."* Whose photo is it?
*   **Mental Trick:**
    *   Condition: `"I have no brother or sister"`.
    *   Therefore, `"my father's son"` can only be exactly one person: **Mr. Bean himself**.
    *   Substitute this back into the sentence: *"that fellow's father is [Mr. Bean himself]"*.
*   **Answer:** It is a photo of **His Son**.

---

### Question 6
**Question:** In Mr. Mehta’s family, there are: 1 grand father, 1 grand mother, 2 fathers, 2 mothers, 1 father-in-law, 1 mother-in-law, 4 children, 3 grandchildren, 1 brother, 2 sisters, 2 sons, 2 daughters, 1 daughter-in-law. How many physical members are there?
*   **Mental Trick (Role Overlapping):** Do not add these numbers up! One person plays multiple roles. Build the minimum 3-generation tree.
    *   **Generation 1:** Grandfather & Grandmother (2 people). They act as 1 father, 1 mother, FIL, MIL.
    *   **Generation 2:** They have exactly 1 Son, who is married (1 Daughter-in-law). (2 people). The son acts as a father, a son, and a child. The wife acts as a mother and a DIL.
    *   **Generation 3:** They have 3 grandchildren (1 boy, 2 girls). (3 people). This gives us the 1 brother, 2 sisters, 2 sons (the father + the grandson), 2 daughters (the two granddaughters), and 4 total children across all generations (1 father + 3 kids).
    *   Count the actual bodies: `2 + 2 + 3 = 7`.
*   **Answer:** There are exactly **7 members**.

---

### Question 7
**Question:** `A + B` means A is mother of B. `A - B` means A is brother of B. `A % B` means A is father of B. `A x B` means A is sister of B. Which shows P is maternal uncle of Q?
*   **Options:** `[A) Q-N+MxP  B) P+SxN-Q  C) P-M+NxQ  D) Q-S%P]`
*   **Mental Trick (Symbol Scanning):** A maternal uncle is a male (Brother of the mother).
    *   So, P must be a brother. That means we need `P - (?)`. Look at the options instantly. Only Option C starts with `P - M`.
    *   Let's verify Option C: `P - M + N x Q`.
    *   P is the brother of M. M is the mother (+) of N. N is the sister of Q.
    *   Since M is the mother of Q's sister, M is the mother of Q. P is M's brother. So P is Q's uncle!
*   **Answer:** **C) P - M + N x Q**.

---

### Question 8
**Question:** Looking at a portrait of a man, Rajanikanth said, *"his mother is the wife of my father's son. Brothers and sisters I have none."* At whose portrait was Rajanikanth looking?
*   **Mental Trick:**
    *   Condition: `"Brothers and sisters I have none"`. So, `"my father's son"` is **Rajanikanth himself**.
    *   Trace backward: `"wife of (Rajanikanth)"`.
    *   Substitute: *"his mother is my wife"*.
    *   If the man's mother is Rajani's wife, the man is Rajani's son.
*   **Answer:** **A) His son**.

---

### Question 14
**Question:** Pointing to a girl in the photograph, Amar said, *"Her mother's brother is the only son of my mother's father."* How is the girl's mother related to Amar?
*   **Mental Trick (Split and Equalize):** Break the sentence at "is".
    *   Right side: `"only son of my mother's father"`. Mother's father = Grandfather. Only son of Grandfather = **Amar's Uncle** (Maternal).
    *   Left side: `"Her mother's brother"` = **The girl's Uncle** (Maternal).
    *   Equality: Amar's Uncle = The Girl's Uncle.
    *   This usually means Amar and the girl are siblings, or the girl's mother could actually just be Amar's mother! 
    *   If they share the same maternal uncle, the girl's mother is the uncle's sister. Amar's mother is also the uncle's sister. Assuming there is only one sister (standard in such problems unless Aunt is specified), the girl's mother IS Amar's Mother.
*   **Answer:** **A) Mother** or **C) Aunt** (Depends on options, usually implies Mother if "only son" is specified).
