import requests

print(requests.__version__)

google_request = requests.get("http://www.google.com")
print(google_request)

git_request = (requests.get("https://raw.githubusercontent.com/timvm1108/CMPUT404_Lab1/main/vanmaren_Lab1.py"))
print(git_request.text)