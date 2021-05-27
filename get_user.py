import requests

username = input("GitHub Username: ")

r = requests.get(f"https://api.github.com/users/{username}")

print(r.text)
