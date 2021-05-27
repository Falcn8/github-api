import requests

r = requests.get("https://api.github.com/gists/public").json()

for i in r:
    print("Author: "+i["owner"]["login"])
    if i["description"] == "":
        i["description"] = "None"
    print("Description: "+i["description"])
    for x in i["files"]:
        print("Filename: "+x)
        print("Language: "+str(i["files"][x]["language"]))
        print("Size: "+str(i["files"][x]["size"]))
    print("-"*15)
