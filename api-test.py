import requests

response = requests.get("https://api.github.com")
if response.status_code >= 200 and response.status_code < 300:
    data = response.json()
    print("GitHub API response:", data)
else:
    print("Request failed with status code:", response.status_code)
