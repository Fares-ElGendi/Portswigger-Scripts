import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "passwords.txt")

with open(file_path, "r") as file:
    passwords = file.read().splitlines()

print(passwords)