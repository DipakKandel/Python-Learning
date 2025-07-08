# 🧪 Day 6 – Exception Handling & Validation in Python

This day's exercises focus on **making programs safer and more user-friendly** using exception handling, assertions, and input validation. These are essential skills for writing real-world Python applications that don’t crash on bad user input.

## ✅ What I Practiced

### 1. **`try`, `except`, `finally`**

Handled errors gracefully without crashing the program.

```python
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Division completed.")
```

🧑‍💼 Employee Salary Report
This mini-project collects and validates employee names and salaries, then prints a clean report with statistics:

✔ Features:
Input validation using try/except

Assertion for positive salary

Real-time error messages

Prints:

Each employee’s salary

Average salary

Highest & lowest salaries

💡 What I Learned
Exception handling (try, except, finally)

How to raise custom exceptions with raise and assert

Validating user input before processing

Using Python dictionaries to store and display structured data

Clean formatted output with f"{value:.2f}"
