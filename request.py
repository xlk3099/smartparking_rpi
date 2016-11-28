import requests

data = {
  '1': {
    'id': 1,
    'available': True,
    'plateNo': 'aaa'
  },
  '2': {
    'id': 2,
    'available': False,
    'plateNo': 'casdfasdfcc'
  },
  '3': {
    'id': 3,
    'available': True,
    'plateNo': 'ABC1asdfasdf23'
  }
}


r = requests.put('http://127.0.0.1:8080/parking', json = data)
print(r.json())