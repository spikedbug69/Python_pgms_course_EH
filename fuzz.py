import requests
import sys

res =requests.get(url=f"#link")
print(res)
data =res.json()
print(data)