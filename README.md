# digital-literacy
this is an 
project which checks the password strength

# 🔐 Password Strength Analyzer (Digital Literacy Security Tool)

## 📌 Project Overview

The **Password Strength Analyzer** is a simple Python-based tool that evaluates the strength of a password based on common cybersecurity rules.
It helps users understand whether their password is **Weak, Medium, or Strong** and provides helpful suggestions to improve password security.

This project demonstrates **basic cybersecurity concepts**, **string handling**, and **Python programming skills**.

---

## 🎯 Features

* ✅ Checks password length (minimum 12 characters recommended)
* 🔠 Detects uppercase letters (A–Z)
* 🔡 Detects lowercase letters (a–z)
* 🔢 Detects numbers (0–9)
* 🔣 Detects special characters (!@#$%^&*)
* 📊 Gives password strength rating:

  * 🔴 Weak
  * 🟡 Medium
  * 🟢 Strong
* 💡 Provides expert advice to improve password security

---

## 🧠 How It Works

The program evaluates the password using **five security criteria**:

1. Password length ≥ 12 characters
2. Contains uppercase letters
3. Contains lowercase letters
4. Contains numbers
5. Contains special characters

Each satisfied rule increases the **score**.

### Strength Levels:

| Score | Strength  | Meaning              |
| ----- | --------- | -------------------- |
| 0–2   | 🔴 WEAK   | Password is insecure |
| 3–4   | 🟡 MEDIUM | Needs improvement    |
| 5     | 🟢 STRONG | Secure password      |

---

## 🛠️ Technologies Used

* Python 3.x 🐍
* Built-in Python Libraries:

  * `string`

No external libraries are required.

---

## 📂 Project Structure

```
Password-Strength-Analyzer/
│
├── password_analyzer.py   # Main Python program
├── README.md              # Project documentation
```

---

## ▶️ How to Run the Program

### Step 1: Install Python

Make sure Python is installed on your system.

Check installation:

```bash
python --version
```

---

### Step 2: Save the Code

Save your code in a file named:

```
password_analyzer.py
```

---

### Step 3: Run the Program

Open terminal or command prompt and run:

```bash
python password_analyzer.py
```

---

### Step 4: Enter Password

Example:

```
--- Digital Literacy: Security Analyzer ---
Enter a password to test its strength: MySecure@12345

Strength Rating: 🟢 STRONG
Expert Advice: Great job! This password is hard for 'Brute Force' attacks to crack.
```

---

## 📊 Example Test Cases

| Password       | Result    |
| -------------- | --------- |
| 12345          | 🔴 Weak   |
| Password123    | 🟡 Medium |
| MySecure@12345 | 🟢 Strong |

---

## 🔐 Cybersecurity Concepts Used

This project demonstrates:

* Password Security
* Brute Force Attack Resistance
* Digital Literacy Awareness
* Secure Password Creation
* Authentication Basics

---

## 🚀 Future Improvements

Possible upgrades:

* Add password entropy calculation
* Detect common weak passwords
* Add dictionary attack detection
* Create GUI version using Tkinter
* Build web version using Flask
* Add password generator feature

---

## 🎓 Learning Outcomes

By completing this project, you will learn:

* Python functions
* Conditional statements
* String operations
* Boolean logic
* Cybersecurity basics
* User input handling

---

## 👨‍💻 Author

**Student Developer Project**

Designed as part of **Digital Literacy & Cybersecurity Learning**.

---

## 📜 License

This project is free to use for **educational purposes**.

---

## ⭐ Acknowledgment

Inspired by cybersecurity best practices and password safety guidelines used in modern systems.

