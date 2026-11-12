# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'


# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)


# names = [
#     'Finland', 'Sweden', 'Norway', 'Denmark',
#     'Iceland', 'Estonia', 'Russia'
# ]

# nordic_countries = *'Iceland'


#
# try:
#     age = int(input("Enter your age: "))
#     print(age)
# # except ValueError:
# #     print('fix your name')
# # else:
# #     print('right')

# finally:
#     ('finch')

# try:
#     print("Starting the program...")
#     result = 10 / 0

# # except ZeroDivisionError:
# #     print("You cannot divide by zero!")

# finally:
#     print("Program finished!")


# try:
#     print("Start")
#     1 / 0
# finally:
#     print("Finally ran")


# def multiply_all(*s):
#     j=1
#     for i in s:
#         j*=i
#     return j

# print(multiply_all(*[1,5,7,9]))


# def show_student(**info):
#     return info

# print(show_student(name='sulatn',AGE=30,MY_F='BOOKS'))


# def tryi(a,b,c):
#     return a+b+c
# scores = [10, 20, 30]
# print(tryi(*scores))


# dic={}
# languages = ["Python", "SQL", "Java"]

# for i ,j in enumerate(languages):
#      dic[i]=j
# print(dic)

# students = ["Ali", "Sara", "Omar"]
# scores = [85, 92, 78]

# for st,sc in zip(students,scores):
#      print(st,sc)

# re = []
# for i in range(len(scores)):
#      re.append((students[i],scores[i]))
# print(re)


# names = [
#     "Finland", "Sweden", "Norway", "Denmark",
#     "Iceland", "Estonia", "Russia"
# ]

# *nordic_countries , re , ru = names
# print(nordic_countries)
# print(re)
# print(ru)

# tasks = ["Study Python", "Practice SQL", "Review ML"]
# for i, j in enumerate(tasks,start=1):
#     print(f'number tasks: {i} tasks: {j}')


# products = ["USB-C cable", "Wireless mouse", "Keyboard"]
# stock = [24, 8, 15]

# for number,(prodct,stock) in enumerate(zip(products,stock)):
#     print(number,prodct,stock)

from datetime import datetime
# def get_datetime():

#     now = datetime.now()
#     day=now.day
#     m=now.month
#     h=now.hour
#     s=now.second
#     timp=now.timestamp()

#     return day,m,h,s,timp

# print(get_datetime())


now = datetime.now()
# string = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(string)


# date_string = "5 December, 2019"
# result = datetime.strptime(date_string, '%d %B, %Y')
# print(result)

# next_year = datetime(now.year +1,1,1)
# result= next_year - now
# print(result)

# result = datetime(1970,1,1)
# dif = now - result
# print(dif,dif.total_seconds())

# # futer = datetime(2027,1,1)
# # difrints = futer - now
# # print(difrints)

# now = datetime.now()
# total_scond = now.timestamp()
# reult = total_scond / (365*24*60*60)
# print(reult)

countries = [
    'Estonia', 'Finland', 'Sweden',
    'Denmark', 'Norway', 'Iceland'
]

# def find(x):
#     return x.upper()
# result = map(find,countries)
# print(list(result))

numbers = [1, 2, 3, 4, 5]
# def numbr(x):
#     return x**2
# result = map (numbr,numbers)
# print(list(result))

# result=map(lambda x:x**2,numbers)
# print(list(result))

# countries = [
#     'Estonia', 'Finland', 'Sweden',
#     'Denmark', 'Norway', 'Iceland'
# ]
# def find(x):
#     return 'land' in x
# result = filter(find,countries)
# print(list(result))

# def char_6 (x):
#     return len(x) == 6
# result=filter(char_6,countries)
# print(list(result))

# def new_list(x):
#     return x[0] == 'E'
# result = filter(new_list,countries)
# print(list(result))

# def tran_upper(x):
#     return  'land' in x

# ressult = filter(tran_upper,countries)
# def  upeer(x):
#      return x.upper()

# result= map(upeer,ressult)
# print(list(result))

# def filter_upper(countries):
#     filtered = filter(lambda x: 'land' in x ,countries)
#     upper = map(str.upper,filtered)
#     return list(upper)
# print(filter_upper(countries))


def string(countries):
    result = filter(lambda x:isinstance(x,str),countries)
    print (list(result))
string(countries)


# def string_2(info):
#     r = []

#     for i in info:
#         r.append(str(i))
#     return r


# from functools import reduce
# numbers = [1, 2, 3]
# def reedus(x,y):
#     return x + y
# result = reduce(reedus,numbers)
# print(result)

# result = reduce(lambda x,y: x+y,numbers )
# print(result)


def get_first_five(x):
    j=[]
    for i in range(len(x)-3,len(x)):
        j.append(x[i])
    return j
print(get_first_five(countries))


# def get_first_fivee(x):
#     return x[-3:]

# result = get_first_fivee(countries)
# print(result)

# countries = ["Yemen", "Egypt", "Oman"]
# result = []

# for i in countries:
#     result.insert(0, i)

# print(result)


# def sort_countries(x):
#     return sorted(x)
