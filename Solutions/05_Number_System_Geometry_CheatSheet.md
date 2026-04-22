# Number System & Geometry (Mensuration)

---

## 1. Number System

### 🔢 Essential Divisibility Rules (Saves heavy division)
*   **Divisibility by 3 & 9:** The SUM of all digits must be divisible by 3 (or 9).
    *   *Ex:* Is 1458 divisible by 9? Sum = `1+4+5+8 = 18`. Yes!
*   **Divisibility by 11:** Difference between alternating sums is 0 or a multiple of 11.
    *   *Ex:* Is 2728 divisible by 11? `(2+2 = 4) - (7+8 = 15)` -> `|4 - 15| = 11`. Yes!

### 🔄 Unit Digit Cyclicity
When asked for massive exponents, find the cycle length.
*   Powers of 2, 3, 7, 8 repeat their last digit every 4th power.
*   **Example Question:** What is the unit digit of `3^145`?
    *   **Mental Solution:** Take the exponent `145` and divide by 4. 
    *   `145 / 4` leaves a remainder of **1**.
    *   Therefore, the unit digit of `3^145` acts exactly like `3^1`. 
    *   Answer: **3**.

---

## 2. Mensuration (2D/3D Geometry)

### 🧮 The Target "Pi (11)" Ratio Trick
In almost any geometry problem involving circles, cylinders, cones, or spheres, the formula includes **Pi (π)**.
Since π is usually given as `22/7` (which is `2 * 11 / 7`), the final correct numerical volume/area is very frequently a **multiple of 11**.

*   **Example Question:** Find the total volume of a cylinder with radius 5cm and height 14cm. 
    *   *Options:* `A) 1100`, `B) 1120`, `C) 1150`, `D) 1200`
    *   **Mental Solution:** Don't do `(22/7)*25*14` if you are in a rush. Check which option is divisible by 11 using the alternating sum trick.
        *   A: 1100 -> `(1+0) - (1+0) = 0`. Divisible!
        *   B: 1120 -> `(1+2) - (1+0) = 2`. No.
        *   C: 1150 -> `(1+5) - (1+0) = 5`. No.
        *   D: 1200 -> `(1+0) - (2+0) = -1`. No.
    *   **Answer:** You can confidently mark **1100** without solving the math.

### 📐 Ratios of Areas and Volumes
If the ratio of the side lengths (or radii) of two similar figures is `a : b`:
*   Area Ratio = `a^2 : b^2`
*   Volume Ratio = `a^3 : b^3`
*   **Example Question:** Two spheres have radii in the ratio 2:3. What is the ratio of their surface areas, and their volumes?
    *   **Mental Solution:** Don't write out the `4πr^2` formulas!
        *   Surface Area Ratio = square them -> `2^2 : 3^2` = **4 : 9**.
        *   Volume Ratio = cube them -> `2^3 : 3^3` = **8 : 27**.

---

## 🔥 High-Frequency Exam Patterns & Hotspots

### 💯 Trailing Zeros (Number System)
To find the number of trailing zeros in a factorial (e.g., `100!`), continuously divide the number by 5 and sum the quotients. 
*   `100 / 5 = 20`. 
*   `20 / 5 = 4`. 
*   Total trailing zeros = `20 + 4 = 24`.

### 🧊 Melting and Recasting (Mensuration)
When a 3D object is melted down to create another shape, **Volume is always constant** (Surface Area changes). 
*   Always equate `Volume_1 = n * Volume_2` to find the number `n` of new objects.

### 🛣️ Paths in/around Rectangles
*   **Path *outside* a rectangle of L,B:** Area = `2w(L + B + 2w)`
*   **Path *inside* a rectangle of L,B:** Area = `2w(L + B - 2w)`
*   *(Where `w` is the width of the path).*
