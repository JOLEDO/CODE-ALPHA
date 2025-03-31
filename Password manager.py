# Password Manager with Encryption
import os
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
PASSWORD_FILE = "passwords.txt"


def write_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


# Ensure key exists
write_key()
key = load_key()
fer = Fernet(key)


def view():
    if not os.path.exists(PASSWORD_FILE):
        print("No saved passwords yet.")
        return

    with open(PASSWORD_FILE, "r") as f:
        for line in f:
            data = line.strip()
            user, _, passw = data.partition("-----")
            if passw:
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_pass}")
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")
            else:
                print(f"Skipping invalid entry: {data}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{name}-----{encrypted_pwd}\n")

    print("Password saved!")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit: ").lower()

    if mode == "q":
        print("👋 Goodbye!")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Try again!")
