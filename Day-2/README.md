
# 🎓 CLI Result Grading System (Day 2)

A command-line based **student result grading system** built with Python as part of the **30 Days Python Pro Challenge**.

---

## 🚀 Features

* Takes marks for **5 subjects**:

  * Math
  * English
  * Physics
  * Chemistry
  * CSE
* Calculates:

  * Total marks
  * Average marks
* Automatically assigns grades based on average:

  * A+, A-, B, C, D
* Handles invalid input length
* Uses a clean, function-based structure

---

## 🛠 Concepts Used

* Functions
* Lists & list operations
* Built-in functions (`sum`, `len`)
* Conditional statements (`if / elif / else`)
* Input handling
* Modular program structure with `main()`

---

## 📂 Files

* `result_grading.py` → Main program file

---

## ▶ How to Run

```bash
python result_grading.py
```

---

## 📌 Example

```
#######----Check Your Result Grading---#######

Enter You Marks by using spaces in this order !

Math English Physics Chemistry CSE
80 75 90 85 88

Your Average Grade: A-
```

---

## 📈 Grading Logic

| Average Marks | Grade          |
| ------------- | -------------- |
| < 0           | Needs Help     |
| 0 – 55        | D              |
| 56 – 71       | C              |
| 72 – 79       | B              |
| 80 – 89       | A-             |
| 90 – 100      | A+             |
| > 100         | Over Genius 😄 |

---

## 🎯 Learning Outcome

This project helped practice:

* Breaking a problem into small functions
* Passing data between functions
* Real-world conditional logic
* Writing clean CLI programs

