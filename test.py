import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Hit the road Jack", "views": 947296964, "likes": 359000},
    {"name": "Billie Jean", "views": 54356001, "likes": 582000},
    {"name": "Beat It", "views": 16763888, "likes": 193000}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())