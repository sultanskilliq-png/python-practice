# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# result = [i for i in numbers if i<=0]
# print(result)

# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result=[i for j in list_of_lists for i in j]
# print(result)


# [
#     (0, 1, 0, 0, 0, 0, 0),
#     (1, 1, 1, 1, 1, 1, 1),
#     (2, 1, 2, 4, 8, 16, 32),
#     (3, 1, 3, 9, 27, 81, 243),
#     # Continue the same pattern up to 10
# ]
# result = [
#     (i, *[i ** j for j in range(6)])
#     for i in range(11)
# ]

# print(result)

# countries = [[('Finland', 'Helsinki')],
#              [('Sweden', 'Stockholm')],
#              [('Norway', 'Oslo')]]

# result = [[i[0][0].upper(),i[0][0][:3].upper(),i[0][1].upper()]for i in countries]
# print(result)


# countries = [
#     [('Finland', 'Helsinki')],
#     [('Sweden', 'Stockholm')],
#     [('Norway', 'Oslo')]
# ]

# # result=[{'country':i[0][0].upper() , 'city':i[0][1].upper()}for i in countries]
# # print(result)

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
#          [('Donald', 'Trump')], [('Bill', 'Gates')]]
# result = [i[0][0] + ' ' + i[0][1] for i in names]
# print(result)


# slope = lambda y_1, y_2, x_1, x_2: (y_2 - y_1) / (x_2 - x_1)

# print(slope(2, 6, 1, 3))  # 2.0


# numbers = [1, 2, 2, 3, 4, 4, 5]
# def filter(numbers):

#     result=[]

#     for num in set(numbers):
#         result.append(num)
#     return result
# print(filter(numbers))


#     result=[]

#     for num in numbers:
#         if num not in result:
#             result.append(num)
#     return result
# print(filter(numbers))


# numbers = [1, 2, 2, 3, 4, 4, 5]
# def filter(numbers):
#     return list(set(numbers))
# print(filter(numbers))


# words = 'my name is sultan'
# def result(words):


#     save=words.split()
#     result = []

#     for re in save[::-1]:
#         result.append(re)


#     return " ".join(result)
# print(result(words))


# word = 'helllo my frind what is your name'

# save =word.split()
# save = save[::-1]
# print(" ".join(save))


# import random
# import string
# def random_password(numbers):

#     password = string.ascii_letters + string.digits

#     result=[]
#     for _ in range(numbers):
#         result.append(random.choice(password))
#     return "".join(result)
# print(random_password(5))


# import random
# import string
# def random_user_id():
#     random_password = random.randint + string.ascii_letters
#     result = []
#     for _ in range(6):
#         result.append(random.choice(random_password))
#     return result

# print(random_user_id())


# import random
# import string
# def random_user_id():
#     random_password =  string.ascii_letters + string.digits
#     result = []
#     for _ in range(6):
#         result.append(random.choice(random_password))
#     return "".join(result)

# print(random_user_id())


# def random_user_id():
#     random_password = string.ascii_letters + string.digits
#     string_pass = ''
#     for _ in range(6):
#         string_pass += random.choice(random_password)   # grow the text
#     return string_pass                                  # return the TEXT, after the loop

# print(random_user_id())    # one ID, like 'aB3xK9'


# def random_user_id():
#     user_langh= int(input('what the langhr you want: '))
#     user_count= int(input('what the count you want: '))
#     random_password = string.ascii_letters + string.digits
#     result = []
#     for i in range(user_count):
#         string_pass=''
#         for j in range(random_password):
#             string_pass+=random.choice(random_password)
#         result.append(string_pass)
#     return result

# print(random_user_id())    # one ID, like 'aB3xK9'

# import random
# import string

# def user_id_gen_by_user():
#     length = int(input('How many characters? '))   # per ID
#     count = int(input('How many IDs? '))
#     bag = string.ascii_letters + string.digits

#     ids = []                                       # the basket for all the IDs
#     for _ in range(count):                         # outer loop: one round per ID
#         user_id = ''                               # a fresh empty ID every round
#         for _ in range(length):                    # inner loop: one round per character
#             user_id += random.choice(bag)
#         ids.append(user_id)                        # save the finished ID
#     return '\n'.join(ids)                          # one ID per line

# print(user_id_gen_by_user())                       # type: 5 and 5


# import random
# def rgb_color_gen():
#         rgb_1 = random.randint(0,255)
#         rgb_2 = random.randint(0,255)
#         rgb_3 = random.randint(0,255)
#         # return rgb_1,rgb_2,rgb_3
#         return f'rgb ({rgb_1},{rgb_2},{rgb_3})'
# print(rgb_color_gen())


      # blank 2: the name of the rgb function

# def shuffle_list(numbers):
#         random.shuffle(numbers)
#         return numbers
# print(shuffle_list([1,2,3,4,5]))

# def shuffle_list(numbers):
#         new_copy = numbers.copy()
#         random.shuffle(new_copy)
#         return new_copy
# print(shuffle_list([1,2,3,4,5]))


# import random
# def seven_numbers():
#      result = list(range(0,10))
#      random.shuffle(result)
#      return result[:7]
# print(seven_numbers())


# def seven_numbers():
#     return random.sample(range(10),7)
# print(seven_numbers())


# import random

# def list_of_hexa_colors(n):
#     colors = []
#     for i in range(n):
#         color = '#'
#         for j in range(6):
#             color += random.choice('0123456789abcdef')   # one random hex character
#         colors.append(color)
#     return colors

# def list_of_rgb_colors(n):
#     colors = []
#     for i in range(n):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         colors.append(f'rgb({r}, {g}, {b})')
#     return colors

# def generate_colors(kind, n):
#     if kind == 'hexa':
#         return list_of_hexa_colors(n)     # call the hex machine, give it the number n
#     else:
#         return list_of_rgb_colors(n)      # call the rgb machine

# print(generate_colors('hexa', 3))   # ['#a3e12f', '#03ed55', '#eb3d2b']
# print(generate_colors('rgb', 2))    # ['rgb(5, 55, 175)', 'rgb(50, 105, 100)']


# def total(*args):                     # any number of positional arguments -> tuple
#     return sum(args)
# print(total(1, 2, 3, 4))


# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


# def add_all_nums(*arge):
#     for num in arge:
#         if not isinstance(num,(int,float)):
#           return 'All inputs must be numbers'
#     return sum(arge)
# print(add_all_nums(1,2,3,4))

# def show_args(**dect):
#     for key,value in dect.items():
#         print(key,value)


# show_args(name='Alice', age=30 , salary = 3000)    # Received: name: Alice, age: 30


# def number(numbers):
#     result = []
#     for num in numbers:
#         if num < 2:
#             continue

#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             result.append(num)

#     return result

# print(number([1, 2, 3, 4, 5, 6, 7, 13]))


# import random
# numbers = 100
# def numbers_1():
#     result = [i for i in range(1,500) if i%2==0 and i <101]
#     return result
# print(numbers_1())


# def even_odd_numbers():

#     result = [i+=1,j for i in range(101) if i%2==0 else j+=1  ]


# fruits = ['banana', 'orange', 'mango', 'lemon']
# result = [i for i in fruits if fruits[i][-1]==fruits[i][1]]
# print(result)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits=fruits[::-1]
# print(fruits)

# result = [fruits[i] for i in range(len(fruits)-1,-1,-1)]
# print(result)
# result = [i for i in fruits if fruits==fruits[::-1]]
# print(result)


# def numbers():

#     even = 0
#     odd = 0
#     for i in range(100):

#         if i %2==0:
#              even+=1
#         else:
#          odd+=1
#     return even,odd
# print(numbers())


# def numbers():

#     user_numbers_1 = int(input('what\'s your first number: '))
#     user_numbers_2 = int(input('what\'s your scound number: '))

#     if user_numbers_1 == user_numbers_2:
#         p = 'it\'s equl'

#     elif user_numbers_1 > user_numbers_2:
#         p = ' the numbrer 1 the great'

#     else:
#         p= ' the number 2 thr bigest'

#     return p
# print(numbers())


# def students(gread):

#     if gread >= 90:
#         return 'A'
#     if gread >= 80:
#         return 'B'
#     if gread >= 70:
#         return 'C'
#     if gread >= 60:
#         return 'D'
#     if gread < 60:
#         return 'go to home bey bey'
# print(students(59))


# def skill(skills):

#     if ['python,JS,API'] in skills:
#         return 'backend'


# # def skill(skills):
# #     if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
# #         return 'He is a front end developer'
# #     elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
# #         return 'He is a backend developer'
# #     elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
# #         return 'He is a fullstack developer'
# #     else:
# #         return 'unknown title'


# # person_skills = ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# # print(skill(person_skills))'
# class Statistics:
#     def __init__(self, data):
#         self.data = data

#     def count(self):
#         return len(self.data)

#     def sum(self):
#         return sum(self.data)

#     def min(self):
#         return min(self.data)

#     def max(self):
#         return max(self.data)

#     def range(self):
#         return max(self.data) - min(self.data)

#     def mean(self):
#         return sum(self.data) / len(self.data)

#     def median(self):
#         sorted_data = sorted(self.data)
#         n = len(sorted_data)
#         middle = n // 2

#         if n % 2 == 0:
#             return (sorted_data[middle - 1] + sorted_data[middle]) / 2
#         return sorted_data[middle]

#     def mode(self):
#         frequency = {}
#         for value in self.data:
#             frequency[value] = frequency.get(value, 0) + 1

#         most_common = max(frequency, key=frequency.get)
#         return most_common, frequency[most_common]

#     def var(self):
#         mean = self.mean()
#         return sum((x - mean) ** 2 for x in self.data) / len(self.data)

#     def std(self):
#         return self.var() ** 0.5

#     def freq_dist(self):
#         frequency = {}
#         for value in self.data:
#             frequency[value] = frequency.get(value, 0) + 1

#         total = len(self.data)
#         result = [(count / total * 100, value)
#                   for value, count in frequency.items()]
#         return sorted(result, reverse=True)

#     def describe(self):
#         return (
#             f"Count: {self.count()}\n"
#             f"Sum:  {self.sum()}\n"
#             f"Min:  {self.min()}\n"
#             f"Max:  {self.max()}\n"
#             f"Range:  {self.range()}\n"
#             f"Mean:  {self.mean():.0f}\n"
#             f"Median:  {self.median():.0f}\n"
#             f"Mode:  {self.mode()}\n"
#             f"Variance:  {self.var():.1f}\n"
#             f"Standard Deviation:  {self.std():.1f}\n"
#             f"Frequency Distribution: {self.freq_dist()}"
#         )


# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
#         33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# data = Statistics(ages)
# print(data.describe())


# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range()) # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# class PersonAccount:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.incomes = []
#         self.expenses = []

#     def add_income(self, amount, description):
#         self.incomes.append({
#             'amount': amount,
#             'description': description
#         })

#     def add_expenses(self, amount, description):
#         self.expenses.append({
#             'amount': amount,
#             'description': description
#         })

#     def total_income(self):
#         total = 0
#         for income in self.incomes:
#             total += income['amount']
#         return total

#     def total_expenses(self):
#         total = 0
#         for expense in self.expenses:
#             total += expense['amount']
#         return total

#     def balance(self):
#         return self.total_income() - self.total_expenses()

#     def account_info(self):
#         return (
#             f'Hello {self.first_name} {self.last_name}! '
#             f'Your balance is {self.balance()}.'
#         )


# p_1 = PersonAccount('sultan', 'AL_niserry')
# p_1.add_income(5000, 'gift')
# p_1.add_income(10000, 'salary')
# p_1.add_expenses(4000, 'rent')

# print(p_1.total_income())
# print(p_1.total_expenses())
# print(p_1.balance())
# print(p_1.account_info())


# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.amazon.it/gp/aw/d/B07TJW59YZ?pd_rd_plhdr=t&hsa_cr_id=0&qid=1792751057&sr=1-1-941ebe59-d25b-49d0-b214-12cc5b66c90f&i=aps&aref=K8elmb2WkP&_encoding=UTF8&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=tkBvW&content-id=amzn1.sym.5722dc73-61c6-4c20-bac8-7fd04943a4b8%3Aamzn1.sym.5722dc73-61c6-4c20-bac8-7fd04943a4b8&pf_rd_p=5722dc73-61c6-4c20-bac8-7fd04943a4b8&pf_rd_r=VTZ17DJCA7284G6E6935&pd_rd_wg=OtFeF&pd_rd_r=204e823a-de1a-4d06-8521-494bf2f8efb8'
# headers = {'user_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0'}
# respoes=requests.get(url,headers=headers,params={'k':'whatch&ref'})
# soup = BeautifulSoup(respoes.content,'html.parser')
# # print(respoes.status_code)
# # print(soup.prettify)

# total = soup.find('span',class_="a-offscreen")
# print(total.get_text())

# name = soup.find('span',id="productTitle")
# print(name.string.strip())

# new_dict={}
# dist = soup.find('div',id="features_and_specs")
# rwos = soup.find_all('tr')
# for rwo in rwos:
#     key = rwo.th.string.strip()
#     value = rwo.td.string.strip()
#     new_dict[key]=value


# url='https://www.bu.edu/president/boston-university-facts-stats/'
# headers={'user_Agent':'Mozilla/5.0'}
# respone = requests.get(url,headers=headers)
# soup = BeautifulSoup(respone.content,'html.parser')


# tital = soup.find('article', class_='content-area')
# p={}
# for i in tital.find_all('article', class_='bu-stat-single'):
#     key = i.find('h3', class_='bu-stat-title').get_text(strip=True)
#     value = i.find('div', class_='bu-stat-element').get_text(strip=True)
#     p[key] = value
# print(p)


# lists = tital.find_all('div', class_='bu-stat-list')

# tital_1 = lists[0]  # First list
# # print(len(lists))
# tital_2 = lists[1]  # Second list

# tital_11 = {}

# for i in tital_1.find_all('article', class_='bu-stat-single'):
#     key = i.find('h3', class_='bu-stat-title').get_text(strip=True)
#     value = i.find('div', class_='bu-stat-element').get_text(strip=True)
#     tital_11[key] = value

# tital_22 = {}

# for i in tital_2.find_all('article', class_='bu-stat-single'):
#     key = i.find('h3', class_='bu-stat-title').get_text(strip=True)
#     value = i.find('div', class_='bu-stat-element').get_text(strip=True)
#     tital_22[key] = value

# tital = soup.find('article', class_='content-area')

# tital_3={}
# for group in lists:
#       for i in group.find_all('article', class_='bu-stat-single'):
#         key = i.find('h3', class_='bu-stat-title').get_text(strip=True)
#         value = i.find('div', class_='bu-stat-element').get_text(strip=True)
#         tital_3[key] = value

# print(f'first result: {tital_11}, scond result{tital_22}, all_of them{tital_3}')

# tital = soup.find('article', class_='content-area')

# # coomainty = tital.find('ul',class_="custom-stat-list")
# # comm=coomainty[0]
# # li = coomainty.find_all('li')

# coomainty = tital.find_all('ul', class_='custom-stat-list')
# comm = coomainty[1]
# li = comm.find_all('li')

# result={}
# for i in li:
#     key = i.find('span',class_="stat-label").get_text(strip=True)
#     value=i.find('span',class_="stat-figure").get_text(strip=True)
#     result[key]=value
# print(result)

# taable = soup.find('table',class_="table")

# rows = taable.find_all('tr')

# for row in rows:
#     th = row.find_all('th')
#     th_th = [t.get_text(strip=True)for t in th]

#     if not th:
#        continue

#     result={}
#     td = row.find_all('td')
#     for key,value in enumerate(td):
#         result[th_th[key]]=value.get_text(strip=True)
# print(result)


# url='https://www.scrapethissite.com/pages/forms/'
# headers={'user_Agent':'Mozilla/5.0'}
# respone = requests.get(url,headers=headers)
# soup = BeautifulSoup(respone.content,'html.parser')


# taable = soup.find('table', class_="table")

# rows = taable.find_all('tr')
# result = {}
# td_d=[]

# for row in rows:
#     th = row.find_all('th')


#     if th:
#       th_th = [t.get_text(strip=True) for t in th]

#       continue

#     td = row.find_all('td')

#     for key, value in zip(th_th,td):
#         result[key] = value.get_text(strip=True)

# print(result)


# taable = soup.find('table', class_="table")
# rows = taable.find_all('tr')

# th_th = []
# result = {}


#     if th:
#         for t in th:
#             th_th.append(t.get_text(strip=True))
#         continue

#     td = row.find_all('td')

#     for key, value in enumerate(td):
#         result[th_th[key]] = value.get_text(strip=True)

# print(result)


# taable = soup.find('table', class_="table")

# rows = taable.find_all('tr')
# result = []

# th_new = [t.get_text(strip=True)for t in rows[0].find_all('th')]
# for row in rows[1:]:

#     td = row.find_all('td')
#     team={}

#     for key, value in zip(th_new,td):
#         team[key] = value.get_text(strip=True)
#     result.append(team)
# print(result[0])
# # print(team)

# import json

# with open('my_file.json','w',encoding='utf-8') as f:
#     json.dump(result,f,indent=4)


import requests
from bs4 import BeautifulSoup

# url='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
# headers={'user_Agent':'Mozilla/5.0'}
# response = requests.get(url,headers=headers,timeout=15)
# soup = BeautifulSoup(response.content,'html.parser')


# table = soup.find_all('table', class_="wikitable")
# print(len(table))

# print(response.status_code)
# print(response.url)
# print(soup.title.get_text(strip=True) if soup.title else "No title")
# print(len(soup.find_all('table')))


# url='https://books.toscrape.com/'
# headers={'user_Agent':'Mozilla/5.0'}
# response = requests.get(url,headers=headers,timeout=15)
# soup = BeautifulSoup(response.content,'html.parser')

# # print(response.status_code)

# books = soup.find('section')

# bookss = books.find('ol',class_="row")
# li = bookss.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# pricee=[]
# ratingg=[]
# p=0
# low = 1000
# for i in li:
#     name= i.find('h3').find('a')['title']
#     price = i.find('p',class_="price_color").get_text(strip=True)
#     fix = price.replace('£','')
#     dix=float(fix)
#     pricee.append(dix)
#     if dix < low:
#        low = dix

#     rating= i.find('p',class_="star-rating")['class'][1]
#     ratingg.append(rating)
#     if rating =='Five':
#      p+=1

# # print(pricee)
# print(ratingg)

# print(f'Number of five-star books:{p}')
# print(f'Cheapest book price:{low:.f}')
# print(f'Cheapest book price:{low}')


# class Statistics:
#     def __init__(self,data):

#         self.data=data

#     def count(self):
#       return len(self.data)
#     def sum(self):
#       return sum(self.data)
# age = [5,5,6,8,6,7,9]
# data = Statistics(age)
# # print(data.count())


# class PersonAccount:
#     def __init__(self, firstname, lastname):
#         # Runs when we create a new PersonAccount object.
#         self.firstname = firstname
#         self.lastname = lastname

#         # Store incomes and expenses as lists of records.
#         self.incomes = []
#         self.expenses = []

#     def add_income(self, income, description):
#         # Add an income amount and its description to the list.
#         self.incomes.append({
#             'income': income,
#             'description': description
#         })

#     def add_expense(self, expense, description):
#         # Add an expense amount and its description to the list.
#         self.expenses.append({
#             'expense': expense,
#             'description': description
#         })

#     def total_income(self):
#         # Start the total at zero.
#         total = 0

#         # Visit each income record in the list.
#         for item in self.incomes:
#             # Get the amount and add it to the total.
#             total += item['income']

#         # Return the final total.
#         return total

#     def total_expense(self):
#         total = 0

#         for item in self.expenses:
#             total += item['expense']

#         return total

#     def account_balance(self):
#         # Call the other methods to calculate the balance.
#         return self.total_income() - self.total_expense()

#     def account_info(self):
#         # Call the methods above to build the account summary.
#         return (
#             f"Name: {self.firstname} {self.lastname}\n"
#             f"Total income: {self.total_income()}\n"
#             f"Total expenses: {self.total_expense()}\n"
#             f"Balance: {self.account_balance()}"
#         )


# # Create an account object.
# account = PersonAccount("Sultan", "Ali")


# # Add some financial records.
# account.add_income(1000, "Salary")
# account.add_income(200, "Freelance work")
# account.add_expense(150, "Food")
# account.add_expense(100, "Transport")

# account_0 = PersonAccount('Ahmed','Amear')
# account_0.add_income(10000, "Salary")
# account_0.add_income(3000, "Freelance work")
# account_0.add_expense(2500, "Food")
# account_0.add_expense(1000, "Transport")

# # Display the results.
# print(account.account_info())
# print(account_0.account_info())


# import pandas as pd

# csv =pd.read_csv('hacker_news.csv')
# print(len(csv.columns))
# print(len(csv))
# print(csv.shape)

# print(csv[csv['title'].str.contains('Python',case=False)])
# print(csv[csv['title'].str.contains('Python',case=False)])
# print(len(csv[csv['title'].str.contains('Python',case=False)]))

# print(len(csv[csv['title'].str.contains('[p]ython',case=False)]))

# print(csv.info)
# print(csv.describe())
# print(csv.value_counts())
