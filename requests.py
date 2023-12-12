import requests
r=requests.get("https://www.codecademy.com/resources/docs/python/requests-module")
print(r)
print(r.content())
