import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.put(BASE + "video/1", {"name": "Hit the road Jack", "views": 947296964, "likes": 359080})
#print(response.json())
#input()
response = requests.get(BASE + "video/1")
print(response.json())