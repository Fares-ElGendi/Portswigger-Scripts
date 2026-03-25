import os

current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(current_dir,"usernames.txt"),"r") as file:
    usernames = file.read().splitlines()

with open(os.path.join(current_dir,"passwords.txt"),"r") as file:
    passwords = file.read().splitlines() 

