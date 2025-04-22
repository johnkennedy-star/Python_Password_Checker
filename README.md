# Python_Password_Checker
## 🛡️ Password Strength Checker

A simple Python program that evaluates the strength of a password based on length, character variety, and special symbols. It provides feedback such as "Weak," "Moderate," or "Strong" to help users improve their password security.

---

### 📌 Features

- Checks password length
- Validates use of uppercase and lowercase letters
- Confirms presence of digits
- Detects special characters (e.g., `@`, `#`, `$`, `!`, etc.)
- Repeats until user chooses to exit

---

### ⚙️ How It Works

The program evaluates passwords based on the following criteria:

| Criteria                     | Description                                  |
|-----------------------------|----------------------------------------------|
| Length                      | Minimum 8 characters                         |
| Uppercase & Lowercase       | At least one of each                         |
| Digit                       | At least one digit                           |
| Special Characters          | At least one symbol like @, !, %, etc.       |

Each condition met contributes to a total strength score out of 4.

---

### 🚀 How to Run

1. Clone the repository or copy the script.
2. Run the Python file in terminal or IDE:

```bash
python password_checker.py
```

3. Enter passwords and receive feedback.
4. Type `exit` to stop the program.

---

### 💻 Sample Output

```
Enter your password (or type 'exit' to quit): Pass123
Password Strength: Moderate

Enter your password (or type 'exit' to quit): Strong@Pass1
Password Strength: Strong
```

---

### 📚 Requirements

- Python 3.x
- No external libraries needed (uses built-in `re` module)

---

### ✅ Outcomes

- Understanding of regular expressions
- Use of conditionals and loops in Python
- Hands-on experience with user input handling
- Reinforces cybersecurity best practices

---
