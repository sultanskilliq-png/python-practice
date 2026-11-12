# import random

# rand= random.randint(1,10)
# contener=0
# while True:

#     user= int(input('writ your guuss: '))
#     contener+= 1


#     if user > rand:
#         print('toooo higt')

#     elif user < rand:
#         print('tooo low')

#     else:
#         print('your prifct maaan')
#         print(f'count: {contener}')


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# result= [s for s in a if s in b ]
# print(result)


# def price_after_discount(price, discount=10):
#     new_price = price * (1 - discount / 100)
#     return new_price

# print(f'hello_1: {price_after_discount(200)}')
# print(f'hello_2: {price_after_discount(200,20)}')
# print(f'hello_2: {price_after_discount(200,20)}')
# print(f'hello_4: {price_after_discount(200)+5}')
# # print(f'hello_2{price_after_discount('price', 'discount')}')


# from string import ascii_letters as scii, digits as di
# from random import random as r,choice as ch

# result= scii + di
# ch(result)
# rssult = ''

# for i in range(6):
#     rssult+=ch(ch(result))

# print(rssult)


# import string
# import random


# def random_user_id(lengeh=6):
#     result = string.ascii_letters + string.digits

#     empty = ''

#     for i in range(lengeh):
#         empty += random.choice(result)

#     return empty


# uid = random_user_id()
# print(uid)
# print(random_user_id(10))
# # print(len(uid) == 6)
# def user_id_gen_by_user():


#     lengeh = int (input('what i your number: '))
#     count = int(input ('whhat is your number: '))

#     result = []

#     for i in range(count):
#         one = random_user_id(lengeh)
#         result.append(one)

#     return result

# ids = user_id_gen_by_user()
# print(ids)
# print(len(ids))
# print(len(ids[0]))

import random
# def rgb_color_gen ():


#     a = random.randint(0,255)
#     b = random.randint(0,255)
#     c = random.randint(0,255)
#     return f' {a},{b},{c}'

# print(rgb_color_gen ())


# import random
# import string
# def list_of_hexa_colors(n):

#     result = string.ascii_letters + string.digits

#     empty = ''

#     for i in range(n):
#         empty+=random.choice(result)
#     return empty
# print(list_of_hexa_colors())

# # def user():

#     langh = int(input('what is your langh'))
#     count= int(input ('how mutch you want repeted'))

#     new_list = []

#     for i in range(count):
#         new = list_of_hexa_colors(langh)
#         hash = '#'
#         N = hash + new
#         new_list.append(N)
#     return new_list

# print(user())

# import random
# def hax_():
#     box = 'abc'
#     return random.choice(box)

# def hax_coloer():
#     hash = '#'
#     for i in range(6):
#         hash+=hax_()
#     return hash
# def user_color(n):

#     new=[]

#     for i in range(n):
#         new.append(hax_coloer())
#     return new
# print(user_color(3))


def great(name='mohmed'):
    return 'hi' + ' ' + name
print(great('sultan'))
print(great())


# def repeat_word(string,num):
#     n=[]
#     for i in range(num):
#         n.append(string)

#     return n


# def list_of_rgb_colors(n):
#      a = random.randint(0,255)
#      b = random.randint(0,255)
#      c = random.randint(0,255)
#      colors = []
#      for i in range(n):
#         d = a,b,c
#         # the 3 lines (a, b, c) go here, inside the loop
#         colors.append(d)
#      return  colors
# print(list_of_rgb_colors(5))


# def list_of_rgb_colors(n):
#     colors = []
#     for i in range(n):
#         a = random.randint(0, 255)      # new random number every round
#         b = random.randint(0, 255)
#         c = random.randint(0, 255)

#         d = f'rgb({a}, {b}, {c})'       # f-string: makes ONE text, not a tuple
#         colors.append(d)
#     return colors

# def list_of_hexa_colors(n):

#     re = []

#     for i in range (n):
#         hash = '#'
#         re.append(list_of_rgb_colors)
#     return re


# def list_of_hexa_colors(n,m=6):
#    colors=[]
#    for i in range(n):
#        color = '#'
#        for j in range (m):
#            color+=random.choice('0123456789abcdef')
#        colors.append(color)
#    return colors
# print(list_of_hexa_colors(3,10))


# def random_():


#     empty=[]

#     for i in range(7):
#         ra=random.randint(1,9)
#         empty.append(ra)
#     return empty
# print(random_())


def shuffle_list(n):

    past_list = n
    random.shuffle(past_list)
    return past_list

print(shuffle_list([1,2,3,4]))
