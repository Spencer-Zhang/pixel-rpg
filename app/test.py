import requests
import json

headers = {
    'content-type': 'application/json'
}

data = {
    'username': 'Kevin',
    'email': 'kmit@test.com',
    'password': 'testpassword'
}

res = requests.post('http://localhost:5000/users', headers=headers, data=json.dumps(data))
print res.content

res = requests.post('http://localhost:5000/users', headers=headers, data=json.dumps(data))
print res.content

res = requests.get('http://localhost:5000/users', headers=headers)
print json.dumps(res.json(), indent=4)

res = requests.get('http://localhost:5000/users/Kevin', headers=headers)
print json.dumps(res.json(), indent=4)

res = requests.delete('http://localhost:5000/users/Kevin', headers=headers)
