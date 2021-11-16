import requests

r = requests.get('http://localhost:3000/hello')

print(r)
print(r.text)
