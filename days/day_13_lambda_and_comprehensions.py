# # result = lambda a,b : a*b
# # print(result(4,5))

# # def re(x):
# #     return lambda n: x**n
# # print(re(2)(3))

# # Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# result = [i for i in numbers if i < 1 ]
# print(result)


# # Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# li=[]
# for i in list_of_lists:
#     for j in i:
#         li.append(j)
# print(li)


# result = [i for row in list_of_lists   for i in row ]


# # Using list comprehension create the following list of tuples:


# # result = [
# #     (i, i**0, i**1, i**2, i**3, i**4, i**5)
# #     for i in range(11)
# # ]


# # result = [ ]
# # for i in range(11):
# #     rwo = [i]
# #     for j in range(6):
# #         rwo.append(i**j)
# #         result.append(tuple(rwo))
# # print(result)


# # Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# # output:
# # [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# result = [[con[0][0].upper(), con[0][0][:3].upper(),con[0][1].upper()] for con in countries ]
# print(result)
# countries = [[('Finland', 'Helsinki')],
#              [('Sweden', 'Stockholm')],
#              [('Norway', 'Oslo')]]


# # new=[]
# # for i in countries :
# #     con = i[0][0].upper()
# #     adv = con[:3].upper()
# #     cap=i[0][1].upper()

# #     # cont= con.upper()
# #     # adv = con[:3].upper()
# #     # capp=cap.upeer()
# #     new.append(con,adv,cap)
# # print(new)
# # countries = [
# #     [('Finland', 'Helsinki')],
# #     [('Sweden', 'Stockholm')],
# #     [('Norway', 'Oslo')]
# # ]

# # result = []

# # for con in countries:
# #     country = con[0][0]
# #     capital = con[0][1]

# #     country_upper = country.upper()
# #     abbreviation = country[:3].upper()
# #     capital_upper = capital.upper()

# #     result.append((country_upper, abbreviation, capital_upper))

# # print(result)
# # new = []

# # for i in countries:
# #     con = i[0][0].upper()
# #     adv = con[:3]
# #     cap = i[0][1].upper()

# #     new.append([con, adv, cap])

# # print(new)


# # Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# # output:
# # [{'country': 'FINLAND', 'city': 'HELSINKI'},
# # {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# # {'country': 'NORWAY', 'city': 'OSLO'}]

# result = [
#     {'country':con[0][0].upper(),'city':con[0][1].upper()}for con in countries
# ]
# # print(result)

# list=[]

# for con in countries:
#     cont=con[0][0].upper()
#     city = con[0][1].upper()
#     di={'contry':cont,'city':city}
#     list.append(di)
#     # di['contry']=cont
#     # di['city']=city
# print(list)


# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# # output
# # ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# result=[
#     name [0][0]+' '+ name[0][1]for name in names
# ]
# print(result)

# lis=[]
# for i in names:
#     na = i[0][0]+" "+i[0][1]
#     lis.append(na)
# print(lis)


# m = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
# b = lambda y,x : y-(m*x)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# result=[i for i in a if i in b ]
# print(set(result))


# def chek():

#     number=int(input('write your number: '))
#     if number <= 1:
#         return 'not prim'

#     for num in range(2,number):
#         if number % num ==0:
#             return 'very baaaad'

#     return 'prifict'

# print(chek())


# def check():
#     number = int(input("Write your number: "))
#     print("You entered:", repr(number))
#     if number <= 1:
#         return 'Not prime'

#     for num in range(2, number):
#         if number % num == 0:
#             return 'Not prime'

#     return 'Prime'

# print(check())


# def chek(listt):

#     return [listt[0],listt[-1]]

# print(chek([1,12,5,2]))


def fibo():

    number_user= int (input('writ your number: '))

    result = [1,1]
    for i in range(number_user-2):
        summ = result[-1]+result[-2]
        result.append(summ)
    return result [:number_user]

# print(fibo())


def new_list(list):

    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new
print(new_list([1,1,4,6,6]))

def new_listt(listt):
    new = set(listt)
    neww = list(new)
    return neww
# print(new_listt([1,1,2,3,3,4]))


def opsite_name(string):
    word = string
    sp = word.split()
    sp.reverse()
    return " ".join(sp)

print(opsite_name('hi byby'))
