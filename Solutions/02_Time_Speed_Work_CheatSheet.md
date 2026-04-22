# Time, Speed, Distance & Work

---

## 1. Time & Work / Pipes & Cisterns

### 🔧 The LCM Method (The Holy Grail)
**Avoid fraction equations like `1/A + 1/B` at all costs.** Set Total Work to the LCM of the given days.
*   **Example Question:** A can complete a task in 10 days, B can do it in 15 days. How long will they take working together?
    *   **Mental Solution:** 
        *   **Total Work:** LCM of (10, 15) = 30 units.
        *   **Efficiency A:** 30 / 10 = 3 units/day.
        *   **Efficiency B:** 30 / 15 = 2 units/day. 
        *   **Combined:** 3 + 2 = 5 units/day.
        *   **Time Taken:** 30 units / 5 units/day = **6 days**.

### 👥 Work Equivalence (MDH Rule)
**(M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2** (Men * Days * Hours / Work)
*   **Example Question:** If 15 men can build a 10m wall in 5 days, how many men are needed to build a 20m wall in 3 days?
    *   **Mental Solution:** `(15 * 5) / 10 = (M2 * 3) / 20`
    *   Simplify mentally: left side is `75 / 10 = 7.5`. 
    *   `7.5 = M2 * 3 / 20` -> `7.5 * 20 = 150`. 
    *   `M2 = 150 / 3` = **50 men**. 

---

## 2. Time, Speed, and Distance (TSD)

### ⚖️ The Proportionality Rule (Saves Algebraic equations)
*   **If Distance is constant:** Speed and Time are inversely proportional. 
*   **Example Question:** A goes at 40 kmph and B goes at 50 kmph. If A takes 1 hour longer than B to reach the destination, find the distance.
    *   **Mental Solution:**
        *   Speed Ratio (A:B) = `40 : 50 = 4 : 5`
        *   Time Ratio (A:B) = `5 : 4`. (Difference is 1 unit of time).
        *   The question says the difference is exactly 1 hour. So A takes 5 hours, B takes 4 hours.
        *   Distance = Speed * Time = 40 kmph * 5 hrs = **200 km**.

### 🚗 Average Speed Trick
If a person travels equal *halves of a distance* at different speeds: **Avg Speed = `(2 * S1 * S2) / (S1 + S2)`**
*   **Example Question:** Man goes from home to office at 60 kmph, returns at 40 kmph. Find average speed.
    *   **Mental Solution:** `(2 * 60 * 40) / (60 + 40)` = `4800 / 100` = **48 kmph**. (Notice it is NOT 50).

---

## 3. Trains, Boats & Relative Speed

### 🚂 Train Crossing Rules
When a train crosses an object with length: Distance = Train + Object. Speed = `Distance / Time`.
*(Remember: Convert kmph to m/s by multiplying by `5/18`)*
*   **Example Question:** A 150m long train running at 72 km/hr crosses a 250m long platform. How long does it take?
    *   **Mental Solution:** 
        *   Total Distance = 150 (train) + 250 (platform) = 400 meters.
        *   Speed in m/s = `72 * (5/18)` = 4 * 5 = **20 m/s**.
        *   Time = Distance / Speed = 400 / 20 = **20 seconds**.

### 🚤 Boats & Streams
`U` = Upstream (Subtract), `D` = Downstream (Add)
*   Boat Speed = `(D + U) / 2` 
*   Stream Speed = `(D - U) / 2`
*   **Example Question:** A boat travels 24km downstream in 2 hours, and takes 4 hours for the same upstream. Find the speed of the stream.
    *   **Mental Solution:**
        *   Downward Speed (D) = `24 / 2` = 12 kmph
        *   Upward Speed (U) = `24 / 4` = 6 kmph
        *   Stream speed = `(12 - 6) / 2` = `6 / 2 = ` **3 kmph**.

---

## 🔥 High-Frequency Exam Patterns & Hotspots

### 🚶 Escalator & Boat Drift Traps
Escalators moving with/against you use the exact same logic as Boats and Streams.
*   **Moving WITH Escalator (Downstream):** Your Speed + Escalator Speed.
*   **Moving AGAINST Escalator (Upstream):** Your Speed - Escalator Speed.

### ⏰ Late / Early Arrival (TSD)
Very frequent: "If I walk at 4kmph I am 10 mins late, at 5kmph I am 5 mins early."
*   **Direct Formula:** `Distance = (S1 * S2) / |S1 - S2| * (Time Difference in hours)`.
*   *Mental check:* Convert minutes to hours before multiplying!

### 🔄 Alternate Days Work (Time & Work)
When A and B work on alternate days (A on Day 1, B on Day 2, etc.):
1. Find their combined 2-day cycle efficiency.
2. Divide total work by this cycle efficiency to find the number of *full cycles*.
3. Calculate remaining work, and assign it to the next person in the sequence.
