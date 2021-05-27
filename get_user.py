import requests

username = input("GitHub Username: ")

r = requests.get(f"https://api.github.com/users/{username}")

if r.status_code == 200:
    r = r.json()
    print("User ID: " + str(r["id"]))
    print("Node ID: " + str(r["node_id"]))
    print("Avatar URL: " + str(r["avatar_url"]))
    print("Type: " + str(r["type"]))
    print("Site Admin: " + str(r["site_admin"]))
    print("Name: " + str(r["name"]))
    print("Company: " + str(r["company"]))
    print("Website: " + str(r["blog"]))
    print("Location: " + str(r["location"]))
    print("Email: " + str(r["email"]))
    print("Hireable: " + str(r["hireable"]))
    print("Bio: " + str(r["bio"]))
    print("Twitter: " + str(r["twitter_username"]))
    print("Repo Count: " + str(r["public_repos"]))
    print("Gist Count: " + str(r["public_gists"]))
    print("Followers: " + str(r["followers"]))
    print("Following: " + str(r["following"]))
    print("Created At: " + str(r["created_at"]))
    print("Updated At: " + str(r["updated_at"]))
else:
    print("Invalid Username")
