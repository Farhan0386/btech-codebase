# 📝 **README**

````markdown
# 🍽️ Daily Calorie Tracker (Python CLI)

### 👨‍💻 Author: Farhan Hussain  
**Roll Number:** 2501730002  
**Date:** 09-11-2025
**Faculty:** Mr. Sameer Farooq

---

## 📖 Overview
The **Daily Calorie Tracker** is a Python command-line tool that helps users record meals, calculate total and average calories, compare them with a daily limit, and optionally save the report to a file.

---

## ⚙️ Features
- Add multiple meals with calorie values  
- Calculates **total** and **average** calorie intake  
- Compares total calories with user’s daily limit  
- Shows results in a **colored, formatted table** using f-strings  
- Option to **save session report** as `calorie_log.txt`

---

## 🧠 Concepts Used
- `input()`, `while` & `for` loops  
- Lists and `sum()` function  
- f-strings and string alignment  
- `if...else` for comparison  
- File handling (`open()`, `write()`)  
- ANSI color codes for colored output

---

## 🖥️ Example Output
```text
S NO MEAL NAME           CALORIES
--------------------------------------------------
1    BREAKFAST           350.0
2    LUNCH               450.0
3    DINNER              650.0
--------------------------------------------------
Total Calories Consumed : 1450.0
Average Calories per Meal : 483.33
YOU ARE WITHIN YOUR DAILY CALORIE LIMIT.
````

---

## 📂 Output File Example

```text
===== DAILY CALORIE TRACKER REPORT =====
NAME: FARHAN HUSSAIN
ROLL NUMBER: 2501730002
DATE: 2025-11-09

Total Calories Consumed: 1450.0
Average Calories per Meal: 483.33
Daily Calorie Limit: 2000.0
STATUS: You are within your daily calorie limit.
```

---

## 🧩 Requirements

* Python 3.x
* Works in any terminal
  (Optional: install `colorama` for better color support on Windows)

---

## 🏫 Credits

Developed by **Farhan Hussain**
B.Tech CSE (AI & ML), **K.R. Mangalam University**
FACULTY: **MR. SAMEER FAROOQ**
