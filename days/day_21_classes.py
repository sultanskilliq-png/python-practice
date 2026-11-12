class person :
#     def __init__(self,first_name,age,last_name):
#         self.first_name=first_name
#         self.age=age
#         self.last_name=last_name

# p =person('sultan',25,'fuking you')
# print(f'hello {p.first_name} i hope you doing will your age{p.age} so we hope a long age for you, yaaah also yor last name is{p.last_name}')


#     def person_info(self):
#         return({self.first_name},{self.age},{self.last_name})
# p =person('sultan',25,'fuking you')
# print(p.person_info())
# p_2 = person('mohmed',30,'Ahmer')
# print(p_2.person_info())


# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#           self.skills = []

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
#       def add_skill(self, skill):
#           self.skills.append(skill)

# p1 = Person()
# print(p1.person_info())
# p1.add_skill('HTML')
# p1.add_skill('CSS')
# p1.add_skill('JavaScript')
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)


# class Student(person):

# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')


# class Dog:                          # class = the blueprint. The name starts with a capital letter
#     def __init__(self, name, age):  # __init__ runs automatically when you create a dog
#         self.name = name            # self = "this dog". We save the name inside it
#         self.age = age

#     def bark(self):                 # a method = a function that belongs to the dog
#         return f'{self.name} says woof'

# d1 = Dog('Rex', 3)                  # create an object. Python sends 'Rex' and 3 to __init__
# d2 = Dog('Luna', 5)                 # a second object, from the same blueprint

# print(d1.name)                      # Rex
# print(d2.bark())                    # Luna says woof


# import statistics                          # the ready-made module (small s), at the top of the file


# class Statistics:                          # your own class (big S)
#     def __init__(self, data):
#         self.data = data                   # save the list inside the object

#     def count(self):
#         return len(self.data)

#     def sum(self):
#         return sum(self.data)

#     def min(self):
#         return min(self.data)

#     def max(self):
#         return max(self.data)

#     def range(self):
#         return self.max() - self.min()     # my own methods, called with self.

#     def mean(self):
#         return round(statistics.mean(self.data))          # statistics. = the module

#     def median(self):
#         return statistics.median(self.data)

#     def mode(self):
#         m = statistics.mode(self.data)
#         return (m, self.data.count(m))                    # (the value, how many times)

#     def var(self):
#         return round(statistics.pvariance(self.data), 1)

#     def std(self):
#         return round(statistics.pstdev(self.data), 1)

#     def sqr(self):
#         dict ={}

#         for count in self.data:
#             if count not in dict:
#                 dict[count]=0
#             dict[count]+=1
#         result = []
#         for value,count in dict.items():
#             result.append((count/len(self.data)*100,value))
#         return result


# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
# data = Statistics(ages)                    # create the object

# print('Count:', data.count())              # 25
# print('Sum: ', data.sum())                 # 744
# print('Min: ', data.min())                 # 24
# print('Max: ', data.max())                 # 38
# print('Range: ', data.range())             # 14
# print('Mean: ', data.mean())               # 30
# print('Median: ', data.median())           # 29
# print('Mode: ', data.mode())               # (26, 5)
# print('Variance: ', data.var())            # 17.5
# print('Standard Deviation: ', data.std())  # 4.2
# print('qrs: ',data.sqr())


# class PersonAccount:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.incomes = []                  # empty list, every object gets its own
#         self.expenses = []

#     def add_income(self, amount, description):
#         # save one income as a small dictionary inside the list
#         self.incomes.append({'amount': amount, 'description': description})

#     def add_expense(self, amount, description):
#         self.expenses.append({'amount': amount, 'description': description})

#     def total_income(self):
#         total = 0                          # start the total at 0
#         for income in self.incomes:        # go through every income
#             total += income['amount']      # add its amount
#         return total

#     def total_expense(self):
#         total = 0
#         for expense in self.expenses:
#             total += expense['amount']
#         return total

#     def account_balance(self):
#         # my own methods, called with self.
#         return self.total_income() - self.total_expense()

#     def account_info(self):
#         return f'{self.firstname} {self.lastname} has a balance of {self.account_balance()}'


# account = PersonAccount('Ali', 'Khan')     # create the object
# account.add_income(5000, 'Salary')
# account.add_income(200, 'Gift')
# account.add_expense(1000, 'Rent')

# print(account.total_income())      # 5200
# print(account.total_expense())     # 1000
# print(account.account_balance())   # 4200
# print(account.account_info())      # Ali Khan has a balance of 4200
