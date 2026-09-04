# 🔐 Secure Login System

A simple and beginner-friendly **Secure Login System** developed using **Python**, **SHA-256 Password Hashing**, **JSON**, and **File Handling**.

This project provides a basic user authentication system where users can register an account and securely store their password in hashed form. Registered users can then log in using their username and password.

---

## 🚀 Features

* 📝 User Registration
* 🔐 SHA-256 Password Hashing
* 🔑 Secure Password Input using `getpass`
* 👤 Username Validation
* 🔄 Password Confirmation
* 💪 Basic Password Strength Validation
* 💾 User Data Storage in JSON
* 🔓 User Login System
* 🚫 Maximum 3 Login Attempts
* ❌ Invalid Login Handling
* 🖥️ Simple Command-Line Interface

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| 🐍 Python    | Main programming language |
| 🔐 `hashlib` | SHA-256 password hashing  |
| 📄 `json`    | User data storage         |
| 📁 `os`      | File existence checking   |
| 🔒 `getpass` | Hidden password input     |
| 💻 Terminal  | User interface            |

---

## 📂 Project Structure

```text
SecureLoginSystem/
│
├── login_system.py
├── users.json
└── README.md
```

### Files Description

* **`login_system.py`** – Main Python application
* **`users.json`** – Stores usernames and hashed passwords
* **`README.md`** – Project documentation

> `users.json` is automatically created when the first user successfully registers.

---

## ⚙️ Requirements

You need:

* Python 3.x

Check your Python version:

```bash
python --version
```

For Windows:

```bash
py --version
```

### External Libraries

No external packages are required.

The project uses Python's built-in modules:

```python
import hashlib
import json
import os
from getpass import getpass
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SecureLoginSystem.git
```

### 2. Open the Project Folder

```bash
cd SecureLoginSystem
```

### 3. Run the Program

```bash
python login_system.py
```

For Windows:

```bash
py login_system.py
```

---

## 🖥️ Application Menu

When the application starts, you will see:

```text
===== LOGIN SYSTEM =====

1. Register
2. Login
3. Exit

Enter choice:
```

---

## 📝 User Registration

Select option `1` to create a new account.

Example:

```text
Enter choice: 1
Enter username: dharmendra
Enter password:
Confirm password:

✅ Registration successful!
```

The password is not stored as plain text. It is converted into a SHA-256 hash before being saved.

---

## 🔐 Password Hashing

The project uses Python's `hashlib` module to hash passwords.

```python
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

For example:

```text
Original Password:
mypassword123

Stored Password:
SHA-256 Hash
```

Therefore, the actual password is not directly stored in `users.json`.

---

## 💪 Password Strength

The current application requires the password to contain at least **6 characters**.

```python
def is_strong_password(password):
    return len(password) >= 6
```

If the password is too short:

```text
❌ Password must be at least 6 characters!
```

---

## 🔑 User Login

Select option `2` to log in.

Example:

```text
Enter choice: 2
Enter username: dharmendra
Enter password:

✅ Login successful!
```

The entered password is hashed again and compared with the stored hash.

---

## 🚫 Login Attempt Protection

The system allows a maximum of **3 incorrect password attempts**.

Example:

```text
❌ Wrong password! Attempts left: 2
❌ Wrong password! Attempts left: 1
❌ Wrong password! Attempts left: 0

🚫 Too many failed attempts!
```

---

## 💾 Data Storage

User information is stored in:

```text
users.json
```

Example:

```json
{
    "dharmendra": "hashed_password_here",
    "student01": "hashed_password_here"
}
```

Only the hashed password is stored rather than the original password.

---

## 🧠 Concepts Used

This project demonstrates important Python concepts including:

* Functions
* User input
* Conditional statements
* Loops
* Dictionaries
* JSON
* File handling
* SHA-256 hashing
* Password masking
* Exception/error handling
* OS file checking
* Authentication logic

---

## 🔄 Program Flow

```text
              ┌─────────────────┐
              │   Start Program │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Main Menu     │
              └───────┬─────────┘
                      /|\
                     / | \
                    /  |  \
                   ▼   ▼   ▼
            Register Login Exit
               │      │
               ▼      ▼
          Hash Password
               │      │
               ▼      ▼
          Save JSON  Verify Hash
                      │
                      ▼
                Login Success
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

1. How password hashing works
2. How to store data using JSON
3. How to create a registration system
4. How to implement login authentication
5. How to hide password input
6. How to validate user input
7. How to limit login attempts
8. How to work with Python's built-in modules

---

## ⚠️ Security Note

This project is designed primarily for **learning and educational purposes**.

Although SHA-256 hashing is better than storing plaintext passwords, a production authentication system should use a password-specific, salted password-hashing algorithm such as **Argon2id, bcrypt, or scrypt**, together with additional protections such as rate limiting and secure secret management.

Do **not** use this simple JSON-based implementation as-is for a real production authentication service.

---

## 🔮 Future Improvements

The project can be upgraded with:

* 🔐 Salted password hashing
* 🛡️ Argon2/bcrypt password hashing
* 📧 Email verification
* 🔑 Password reset functionality
* 👤 User profile management
* 🔒 Account lockout
* ⏱️ Login rate limiting
* 👨‍💼 Admin login
* 👥 Role-based authentication
* 🗄️ SQLite/MySQL database
* 🌐 Flask/Django web authentication
* 🔑 JWT authentication
* 📱 OTP-based verification
* 📊 Login activity tracking
* 🖥️ Tkinter GUI

---

## 📸 Screenshots

You can add screenshots of your application here.

Recommended screenshots:

```text
screenshots/
│
├── main-menu.png
├── registration.png
├── login-success.png
├── wrong-password.png
└── users-json.png
```

Example:

```markdown
![Login System](screenshots/main-menu.png)
```

---

## 📌 Project Information

```text
Project Name     : Secure Login System
Language         : Python
Interface        : Command Line
Data Storage     : JSON
Password Hashing : SHA-256
Difficulty       : Beginner
Project Type     : Authentication System
```

---

## 👨‍💻 Author

**Dharmendra Singh**

### Skills Demonstrated

`Python` • `JSON` • `Hashing` • `File Handling` • `Authentication` • `Security Basics` • `Problem Solving`

---

## ⭐ Support

If you found this project useful for learning Python and authentication concepts, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for **educational and learning purposes**.
