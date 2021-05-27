import jsonpickle, requests

GITHUB_TOKEN = input("GitHub Token: ")
GITHUB_USERNAME = input("GitHub Username: ")
GITHUB_REPO_NAME = input("GitHub Repo Name: ")

TITLE = input("Issue Title: ")
BODY = input("Issue Body: ")

url = 'https://api.github.com/repos/%s/%s/issues' % (GITHUB_USERNAME, GITHUB_REPO_NAME)
session = requests.Session()
session.auth = (GITHUB_USERNAME, GITHUB_TOKEN)
session.headers = {"accept": "application/vnd.github.v3+json", 'User-Agent': 'request'}
issue = {'title': TITLE, 'body': BODY}
r = session.post(url, jsonpickle.encode(issue))
print(r.text)
