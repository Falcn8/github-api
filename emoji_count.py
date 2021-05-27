import requests

r = requests.get("https://api.github.com/emojis").json()

cnt = 0

for i in r:
    cnt += 1

print("There are "+str(cnt)+" emojis.")
