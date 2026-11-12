# import requests

# r = requests.post('http://127.0.0.1:5000/api/v1.0/students',
#                   json={'name':'ALi','country':'Egipt','city':'Trablis'})

# url = 'http://127.0.0.1:5000/api/v1.0/students'

# students = [
#     {'name': 'mohmed','country':'Yemen','city':'hathrmout'},
#     {'name': 'doland Tramp','country':'united stite','city':'loss Anglos'},
#     {'name': 'it\'s secreat','country':'MY_countrry','city':'MY city'}
# ]


# for s in students:
#     r= requests.post(url,json=s)
#     print(r.status_code)
#     print(r.json())


# import requests

# r=requests.post('http://127.0.0.1:5000//aip/v.1/stedent'
#                 ,json=({"name":"mohmad","country":"TRKIH","city":"ATambol"}))

# url= 'http://127.0.0.1:5000//aip/v.1/stedent'

# stedents = [
#     {"name":"jaci chan","country":"japan","city":"krabsh"},
#     {"name":"labnony","country":"labnan","city":"labnan"},
#     {"name":"chana","country":"chana","city":"trables"}
# ]

# for s in stedents:
#     r=requests.post(url,json=s)
#     print(r.status_code)
#     print(r.json())


import requests

url='http://127.0.0.1:5000/api'
# r= requests.post(url,json={'name':'samar','country':'US','city':'US'})

student = [
    {'name':'hhhhhhh','country':'ajfhgdfda','city':'jbhjfdhjk'},
    {'name':'jjjjjjjj','country':'jjjjjj','city':'jjjjj'},
    {'name':'iiiiiiii','country':'iiiiiiii','city':'iiiiiiiii'}
]


for s in student:
    r=requests.post(url,json=s)
    print(r.status_code)
    print(r.text)
