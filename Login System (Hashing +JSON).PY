import hashlib
import json
import os
from getpass import getpass

# ---------- Hash Function ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Load Users ----------
def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)

# ---------- Save Users ----------
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# ---------- Password Strength ----------
def is_strong_password(password):
    return len(password) >= 6

# ---------- Register ----------
def register():
    users = load_users()

    username = input("Enter username: ")

    if username in users:
        print("❌ Username already exists!")
        return

    password = getpass("Enter password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match!")
        return

    if not is_strong_password(password):
        print("❌ Password must be at least 6 characters!")
        return

    users[username] = hash_password(password)
    save_users(users)
    print("✅ Registration successful!")

# ---------- Login ----------
def login():
    users = load_users()
    username = input("Enter username: ")

    if username not in users:
        print("❌ Username not found!")
        return

    attempts = 3
    while attempts > 0:
        password = getpass("Enter password: ")
        if users[username] == hash_password(password):
            print("✅ Login successful!")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong password! Attempts left: {attempts}")

    print("🚫 Too many failed attempts!")

# ---------- Main Menu ----------
def main():
    while True:
        print("\n===== LOGIN SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

# ---------- Run ----------
if __name__ == "__main__":
    main()