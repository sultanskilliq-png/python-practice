# import random
# import string

# # def password_random(passs=6):

# #     password = string.ascii_lowercase+string.digits

# #     resuult=[]
# #     for i in range(passs):
# #         resuult.append(random.choice(password))
# #     return ''.join(resuult)
# # print(password_random())


# # def password_random(passs=6,count=3):

# #     password = string.ascii_lowercase+string.digits

# #     # resuult=[]
# #     for i in range(passs):
# #         result=[]
# #         for j in count:
# #             z = random.choice(password)
# #             result.append()


# #     return result
# # print(password_random())


# import string
# import random
# def chooes(langh,count):

#     password= string.ascii_letters+string.digits
#     passwords=[]
#     for i in range(count):
#         result=[]
#         for j in range (langh):
#             result.append(random.choice(password))
#         passwords.append(''.join(result))
#     return passwords
# print(chooes(6,3))


# def random_ch(lan,coun):

#     password = string.ascii_letters + string.digits

#     passwords=[
#         ''.join(random.choice(password) for _ in range(lan))
#         for _ in range(coun)
#     ]

#     return passwords

# print(random_ch(5,3))


# import requests
# from bs4 import BeautifulSoup

# headers = {'User-Agent': 'Mozilla/5.0'}

# url = 'https://www.nytimes.com/'

# respon = requests.get(url, headers=headers)

# soup = BeautifulSoup(respon.content, 'html.parser')

# print(respon.status_code)
# print(soup.title)

import string
import random
# def cows_and_bulls():

#     print('  Welcome to the Cows and Bulls Game! ')

#     secrat_number = ''.join(random.choices(string.digits,k=4))

#     gess = 0

#     while True:

#         user = input('Enter a 4-digit number:')

#         if len(user) != 4 or not user.isdigit():
#             print('into numbers and not more than 4')
#             continue

#         gess+=1

#         cow=0
#         Bull = 0

#         for i in range(4):
#             if user[i]==secrat_number[i]:
#                 cow+=1
#             elif user[i] in secrat_number:
#                 Bull+=1

#         print(f'{cow} cow  , {Bull} Bull')

#         if user == secrat_number:
#             print('prifict man')
#             print(gess)
#             break

# if __name__=='__main__':
#     cows_and_bulls()


# def Cow_Bull ():

#     password = ''.join(random.choices(string.digits,k=4))

#     guss = 0

#     while True:

#         user = input('Enter your nnumber')

#         if len(user) !=4 or not user.isdigit:
#             print('plase into 4 numbers:')

#             continue

#         guss+=1

#         cow=0
#         Bull=0

#         for i in range(4):
#             if password[i]==user[i]:
#                 cow+=1
#             elif user[i] in password:
#                 Bull+=1
#         print(f'{cow}cow  {Bull}Bull')


#         if user == password:
#             print('congarliching')
#             print('your winer: ',guss)
#             break
# if __name__=='__main__':
#     Cow_Bull()


# headers = {'User-Agent': 'Mozilla/5.0'}

# url='https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

# respon = requests.get(url,headers=headers)

# soup = BeautifulSoup(respon.content,'html.parser')


# print(respon.status_code)


# def element_search(num):

#     numbers = [1, 3, 5, 7, 9]

#     if num in numbers:
#         return True
#     return False

# # print(element_search(5))


# def element_search(num):

#     numbers = [1, 3, 5, 7, 9]

#     for i in num:
#         for i in numbers:

#             return True
#     return False

# print(element_search([2,5]))


# def element(numbers, target):

#     result=[]
#     for targe in target:
#         if targe in numbers:
#             result.append(True)
#         else:
#             result.append(False)
#     return result


# print(element([1,4,5,6],[1,2,3,4,6,8,7]))
