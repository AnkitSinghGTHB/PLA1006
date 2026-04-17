# Problems on Trains - Mental Math Solutions

[⬅️ Back to Main Navigation](./README.md) | [📖 Read Cheatsheet](./02_Time_Speed_Work_CheatSheet.md)

This document contains step-by-step mental math strategies for the `PROBLEMS ON TRAINS.pdf` practice set.

> [!TIP]
> **The Constant Speed "Extra Distance" Trick:** If a train crosses a pole in `T1` seconds, and a platform of length `L` in `T2` seconds, its speed is literally just `L / (T2 - T1)`.

---

### Question 1
**Question:** Train passes pole in 10s. Passes 120m long platform in 18s. Length of train?
*   **Options:** `[A) 130 m  B) 150 m  C) 180 m  D) 240 m]`
*   **Mental Trick (Marginal Distance):**
    *   Crossing a pole = crossing its own length (takes 10s).
    *   Crossing the platform = crossing its own length + 120m (takes 18s).
    *   The extra 120m distance added exactly **8 extra seconds** `(18 - 10)`.
    *   Speed of train = `120m / 8s = 15 m/s`.
    *   Length of train = distance traveled in the baseline 10s = `15 * 10 = 150m`.
*   **Answer:** **B) 150 m**.

---

### Question 2
**Question:** Two trains of 120m each. Opposite direction cross in 4s. Same direction cross in 12s. Speed of faster train?
*   **Options:** `[A) 72 km/h  B) 80 km/h  C) 120 km/h  D) 144 km/h]`
*   **Mental Trick:**
    *   Total crossing distance is always `120 + 120 = 240m`.
    *   `V1 + V2 = 240m / 4s = 60 m/s`.
    *   `V1 - V2 = 240m / 12s = 20 m/s`.
    *   To find `V1` (faster train), simply add them and divide by 2: `(60 + 20) / 2 = 40 m/s`.
    *   Convert `40 m/s` to km/h by multiplying by `18/5` (or just 3.6).
    *   `40 * 3.6 = 144 km/h`.
*   **Answer:** **D) 144 km/h**.

---

### Question 3
**Question:** Two identical trains cross in opposite directions in 2 minutes. One train increases from 12 bogies to 16. How much extra time to cross?
*   **Options:** `[A) 40 s  B) 50 s  C) 60 s  D) 20 s]`
*   **Mental Trick:**
    *   Initially, both trains have 12 bogies. Total length being crossed = **24 bogies**.
    *   Time for 24 bogies = `2 minutes = 120 seconds`.
    *   This means it takes exactly `120 / 24 = 5 seconds` to cross **one bogie**.
    *   The new train has 16 bogies. It added exactly **4 extra bogies**.
    *   Extra time = `4 bogies * 5 seconds = 20 seconds`.
*   **Answer:** **D) 20 s**.

---

### Question 4
**Question:** A and B are 110km apart. Train 1 starts at 7am at 20kmph. Train 2 starts at 8am at 25kmph. Meeting time?
*   **Options:** `[A) 9 am  B) 10 am  C) 11 am  D) None of these]`
*   **Mental Trick (Sync the clocks):**
    *   Train 1 travels alone from 7am to 8am. Distance covered = `20km`.
    *   At exactly 8am, the remaining gap is `110 - 20 = 90km`.
    *   Now both are moving towards each other. Relative speed = `20 + 25 = 45 kmph`.
    *   Time to close the 90km gap = `90 / 45 = 2 hours`.
    *   Two hours after the synchronized 8am start is **10 am**.
*   **Answer:** **B) 10 am**.

---

### Question 6
**Question:** Cat in tunnel located at 3/8 from entrance A. If it runs to A, train catches it right at entrance. If it runs to B, train catches it right at exit B. Ratio of Train speed to Cat speed?
*   **Options:** `[A) 3:1  B) 4:1  C) 5:1  D) None of these]`
*   **Mental Trick (The Cat's Ghost Game):**
    *   Cat is at `3/8` position.
    *   Scenario 1: Cat runs `3/8` back to A. In this exact time, the train just reaches entrance A.
    *   Scenario 2: If the Cat instead ran forward towards B for that same exact amount of time, the cat would cover `3/8` track. The cat would now be at `3/8 + 3/8 = 6/8` of the track! The train, simultaneously, would just be reaching entrance A.
    *   Now the train is at `0/8` (entrance) and the cat is at `6/8`.
    *   To reach B (the exit), the train must traverse the full `8/8` of the tunnel.
    *   In the exact same time, the Cat traverses the remaining `8/8 - 6/8 = 2/8` of the tunnel.
    *   Speed Ratio = Distance Ratio = `(8/8) : (2/8) = 8 : 2` = **4 : 1**.
*   **Answer:** **B) 4:1**.

---

### Question 9
**Question:** Train travels 20 m/s. Arjun jumps in last bogie, runs inside towards front at 10 m/s. Building explodes when he is 300m away from it. Time elapsed?
*   **Options:** `[A) 30 s  B) 10 s  C) 15 s  D) 20 s]`
*   **Mental Trick:**
    *   Relative to the ground (and the building), Arjun's total forward velocity is the Train's velocity PLUS his own running velocity!
    *   Arun's absolute speed = `20 m/s (train) + 10 m/s (Arjun) = 30 m/s`.
    *   Time to travel 300m = `300 / 30 = 10 seconds`.
*   **Answer:** **B) 10 s**.

---

### Question 11
**Question:** Train travels 500km to destination at 60 kmph, returns at 40 kmph. Average speed?
*   **Options:** `[A) 48 kmph  B) 64 kmph  C) 72 kmph  D) 45 kmph]`
*   **Mental Trick (Harmonic Mean):**
    *   Whenever distances are equal (outbound and return), ignore the distance explicitly! Just use `2ab/(a+b)`.
    *   `2 * 60 * 40 / 100`.
    *   `4800 / 100 = 48`.
*   **Answer:** **A) 48 kmph**.

---

### Question 13
**Question:** Crosses lamp post in 9s, takes 13.5s to cross platform 99m long. Length of train?
*   **Options:** `[A) 99m  B) 198m  C) 135m  D) 12m]`
*   **Mental Trick (Marginal Distance):**
    *   Extra distance = `99m`.
    *   Extra time = `13.5s - 9.0s = 4.5s`.
    *   Train Speed = `99 / 4.5 = 22 m/s`.
    *   Train Length = distance covered in purely crossing itself (the 9s pole crossing).
    *   `22 * 9 = 198m`. (Quick math: `22 * 10 - 22`).
*   **Answer:** **B) 198 m**.
