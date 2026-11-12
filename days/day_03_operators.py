# My_age=24
# my_leaght=float(177.7)
# complex= 5j+4


# base = float(input())
# height = float(input())
# result = base * height * 0.5


# a= float(input())
# b=float(input())
# c=float(input())
# erea=a+b+c


# radius=input(float())
# pi=3.14
# caricle=radius*pi


# a=input(float())
# b=input(float())
# c=input(float())
# ruselt=a+b+c


# a=input(float())
# b=input(float())
# c=a*b
# d=2*(a+b)


# radius=input(float())
# pi=3.14
# erea= radius * pi
# circumference=2*radius*pi


# x1=2
# y1=2
# x2=6
# y2=10
# slope = (y2 - y1) / (x2 - x1)
# distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

# print('slope:',slope,'distance:',distance )


# hours=int(input())
# rate_per_hour =  int(input())
# pay=hours*rate_per_hour
# print(pay)


# years=int(input())
# seconds = years * 365 * 24 * 60 * 60


# for i in range(1, 6):
#     print(i, 1, i, i**2, i**3)


students = [
    {"name": "Ali", "scores": [80, 90, 70]},
    {"name": "Sara", "scores": [60, 50, 65]},
    {"name": "Omar", "scores": [95, 85, 90]},
    {"name": "Lina", "scores": [70, 72, 68]}
]

# result={}

# l=[]


result = {}

for student in students:
    average = sum(student["scores"]) / len(student["scores"])

    if average >= 70:
        # result.append((student["name"], average))
        result[student["name"]]=average
# print(result)


products = [
    {"name": "apple", "price": 3},
    {"name": "banana", "price": 2},
    {"name": "orange", "price": 4},
    {"name": "mango", "price": 6}
]


highest_price = 0
highest_product = ''
for produc in products:
    if produc['price'] > highest_price :
        highest_price = produc["price"]
        highest_product = produc["name"]


# print(highest_product)


students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 62},
    {"name": "Omar", "score": 91},
    {"name": "Lina", "score": 74},
    {"name": "Ahmed", "score": 58}
]


S={}
for student in students:
    if student['score'] >=70:
        S[student["name"]]=student['score']
# print(S)


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

p={}
for word in words:
    if word not in p:
       p[word]=0
    p[word]+=1
# print(p)


orders = [
    {"product": "apple", "quantity": 2},
    {"product": "banana", "quantity": 3},
    {"product": "apple", "quantity": 4},
    {"product": "orange", "quantity": 1},
    {"product": "banana", "quantity": 2}
]
total={}
for order in orders:
    if order["product"] not in total:

        total[order["product"]] =0
    total[order["product"]] += order['quantity']


print(total)
