import requests


# r = requests.delete('http://127.0.0.1:5000/api/v1.0/students/3')
# print(r.status_code)
# print(r.json())


import requests

import requests

base = 'http://127.0.0.1:5000/api/v1.0/students/'   # the fixed part, written once

def chooes(id):
    # f before the quote = put the value of id inside {}
    url = f'{base}{id}'
    return url

# print(chooes(1))   # http://127.0.0.1:5000/api/v1.0/students/1
# print(chooes(3))   # http://127.0.0.1:5000/api/v1.0/students/3

# r=requests.delete(chooes((2,4)))

for i in [2,4]:
    r=requests.delete(chooes(i))
print(r.status_code,r.json())
