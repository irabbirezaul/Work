import requests

response = requests.get("https://ipinfo.io")
print(response.json())
