# import requests

# r = requests.put('http://127.0.0.1:5000/api/v1.0/students/1'
#                  ,json={'ame':'jana','country':'syri','city':'Dmachig'})

# print(r.status_code)
# print(r.text)


# import requests

# # send new data for student number 1
# r = requests.put('http://127.0.0.1:5000/api/v1.0/students/1',
#                  json={'name': 'ali', 'country': 'yemen', 'city': 'aden'})
# print(r.status_code)  # should be 200
# print(r.json())       # should show the new name "ali"


import requests
url='http://127.0.0.1:5000/api/3'
r = requests.put(url,json={'name':'sultan','country':'yemen','city':'secret'})

print(r.status_code)
print(r.text)
