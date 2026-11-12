# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[0:4]         # all items
# all_items = tpl[0:]         # all items
# middle_two_items = tpl[-1:]
# print(middle_two_items)


# my_empty_file=()

# my_sister=('Malak','Jana')
# my_brothers=('oama','ALI')
# siblings=my_sister+my_brothers
# print(len(siblings))
# partiners=('mom','mom')
# co=siblings+partiners

# sister1,sistear2,*brothers_and_sister =co


# # Empty tuple
# my_empty_tuple = ()

# # Sisters and brothers
# my_sisters = ('Malak', 'Jana')
# my_brothers = ('Oama', 'ALI')

# # Join siblings
# siblings = my_sisters + my_brothers
# print(len(siblings))

# # Add parents
# parents = ('Dad', 'Mom')
# family_members = siblings + parents

# # Unpack family members
# sister1, sister2, brother1, brother2, father, mother = family_members

# print(sister1)
# print(sister2)
# print(brother1)
# print(brother2)
# print(father)
# print(mother)

# # Food tuple
# food_stuff_tp = ("apple", "banana", "carrot", "milk", "potato")

# # Convert tuple to list
# food_stuff_lt = list(food_stuff_tp)

# # Get middle item
# middle = food_stuff_lt[len(food_stuff_lt) // 2]
# print(middle)


# # First 3 and last 3 items
# print(food_stuff_lt[:3])
# print(food_stuff_lt[-3:])
# # Nordic countries
# nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# print('Sweden' in nordic_countries)


# name=(input('what is your name: '))
# age=int(input('your age: '))
# middele=100-age
# Data_Year=2026+middele

# appeard=int(input('clice the count of appeard: '))
# message=f'Welcome {name}, oh, you have a long time to live {Data_Year}\n'
# print(appeard*message)

# color=(input('write your coloer: '))
# # print(name ,'like',+ color)
# print(f'{name} like {color}')

# print('that a big age: '+str(age))


# numbers=int(input('what i your number: '))

# if numbers % 4 ==0:
#     print('I catch you ')
# elif numbers % 2==0:
#     print('that even number')
# else:
#     print('easy to me: that is ood numbers')


# num = int(input('numbeeer'))

# chaek=int(input("cheak your num: "))

# # if num % chaek ==0:
# #     print('niiiiiiies')
# # else:
# #     print('fuuuuuuck')


# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# # print(a[0:4])
# # last=[]
# # for s in a :
# #     if s < 5 :
# #         last.append(s)
# # print(last)

# # short=[F for F in a if F <5]
# # print(short)


# # number=int(input('what is your number: '))
# # result=[]
# # for num in a:
# #     if num < number:
# #         result.append(num)
# # print(result)

# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# # number = int(input("What is your number: "))

# # result = []

# # for num in a:
# #     if num < number:
# #         result.append(num)

# # print(result)


# # number = int(input("What's your number: "))

# # result = []

# # for num in range(1, number + 1):
# #     if number % num == 0:
# #         result.append(num)

# # print(result)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# result=[]

# # for i in a:
# #     []
# #     for n in b:
# #         if n == i :
# #             result.append(n)
# # print(result)


# # for i in a:
# #     if i in b:
# #         result.append(i)
# # print(set(result))


# # import random

# # randomm=[random.randint(1,20) for _ in range(10)]

# # print(randomm)


# # randommm=random.randint(1,20)
# # h=[]
# # for i in range(10):
# #      h.append(random.randint(1,20))
# # print(set(h))


# # =====================================================================
# # DICTIONARY REVIEW  (new data, new shapes, solve alone)
# # مراجعة القواميس: بيانات جديدة وأشكال جديدة، حلها وحدك
# #
# # RULES / القواعد
# # 1. For each question, write a FUNCTION with a good name.
# #    Inside the function, use ONLY the parameters (not outside variables).
# #    اكتب دالة لكل سؤال، واستخدم المعاملات فقط داخل الدالة.
# # 2. Before the code, write 3 comments: Input / Output / One item in my loop.
# # 3. Print your result and compare with "Expected".
# # 4. Stuck for 20 minutes? Skip it. Peek at the cheat sheet at the bottom
# #    ONLY after you tried.   علقت؟ لا تنظر للأسفل إلا بعد المحاولة.
# # 5. Tomorrow: rewrite Q1 and Q4 FROM MEMORY.   غدًا أعد كتابة Q1 وQ4 من الذاكرة.
# # =====================================================================

# # ---------- Data (do not change) ----------
# words = ["cat", "dog", "cat", "bird", "dog", "cat"]
# grades = {"Maya": 88, "Omar": 59, "Lina": 92, "Zaid": 71, "Noor": 45}
# sales = [
#     {"region": "north", "amount": 120},
#     {"region": "south", "amount": 80},
#     {"region": "north", "amount": 60},
#     {"region": "east", "amount": 50},
#     {"region": "south", "amount": 40},
# ]
# prices = {"pen": 2, "book": 10, "bag": 25}
# cart = ["pen", "bag", "pen", "book", "pen"]


# # ---------- Q1: Count (العدّ) ----------
# # Function count_words(words): how many times does each word appear?
# # Expected: {'cat': 3, 'dog': 2, 'bird': 1}

# def count_(words):

#     count={}
#     for word in words:
#         if word >count:
#             count[word]=0
#         count[word]+=1
#     return count


# # ---------- Q2: Filter into a dictionary (التصفية) ----------
# # Function passed(grades): return a DICTIONARY with only the students
# # who have 60 or more.  (Note: the output is a dict, not a list.)
# # Expected: {'Maya': 88, 'Lina': 92, 'Zaid': 71}

# def passed(grades):

#     result={}

#     for grade in grades:
#         if grades[grade] >= 60:
#             result[grade]=grades[grade]
#     return result


# # ---------- Q3: The LOWEST score (الأقل) ----------
# # Function lowest_student(grades): return the name and the score
# # of the student with the LOWEST score.
# # WARNING: this looks like "highest score", but one thing must change.
# # Think: what happens if you start with 0? Why does it fail for the lowest?
# # Expected: Noor 45
# def lowest_student(grades):
#     count=1000

#     for grade in grades:
#         if grades[grade] < count:
#             count[grade]=grades[grade]
#     return count


# # ---------- Q4: Total per key (المجموع لكل مفتاح) ----------
# # Function total_by_region(sales): the total amount for each region.
# # Here "sales" is a LIST of dictionaries, so one item in your loop is one dictionary.
# # Expected: {'north': 180, 'south': 120, 'east': 50}
# def total_by_region(sales):

#     count={}
#     for sale in sales:
#         if sale["region"] not in count:
#             count['amount']=sale
#         count['amount']+=sale['region']
#     return count

# # ---------- Q5: Two sources (قائمة وقاموس معًا) ----------
# # Function bill(cart, prices): return a dictionary with the total price for each item.
# # (first count the quantity of each item, then multiply by its price)
# # Then print the grand total of the bill.
# # Expected: {'pen': 6, 'bag': 25, 'book': 10}
# #           41
# def bill(cart, prices):
#     reult={}
#     for cart in prices:
#         if cart not in reult:
#             reult+=cart
#     return reult


# # ---------- Q6: Reuse your own function (إعادة استخدام دالتك) ----------
# # Function top_region(sales): return the name of the region with the highest total.
# # Call your Q4 function inside it. Do not rewrite the totals again.
# # Expected: north

# def top_region(sales):
#     count=0
#     for sale in sales:
#         if sale["amount"] not in count:
#             count['amount']=sale
#         count['amount']+=sale['region']
#     return count


# Dictionary review

# # ---------- Data ----------
# words = ["cat", "dog", "cat", "bird", "dog", "cat"]
# grades = {"Maya": 88, "Omar": 59, "Lina": 92, "Zaid": 71, "Noor": 45}
# sales = [
#     {"region": "north", "amount": 120},
#     {"region": "south", "amount": 80},
#     {"region": "north", "amount": 60},
#     {"region": "east", "amount": 50},
#     {"region": "south", "amount": 40},
# ]
# prices = {"pen": 2, "book": 10, "bag": 25}
# cart = ["pen", "bag", "pen", "book", "pen"]


# # ---------- Q1: Count ----------
# # Output: one number for EACH word -> a dictionary {}
# def count_words(words):
#     re={}
#     for i in words:
#         if words[i] not in re:
#             re[i]=0
#         re[i]+=1
#     print(re)


#     count={}
#     for word in words:
#         if word not in count:
#             count[word]=0
#         count[word]+=1
#     return count


# # ---------- Q2: Filter into a dictionary ----------
# def passed(grades):

#     res={}

#     for grade in grades:
#         if grades[grade] >= 60:
#             res[grade]=grades
# #     return res


# #     result={}


# # ---------- Q3: The lowest score ----------
# # Output: ONE name and ONE score -> two variables that we replace
# # The start value must be BIGGER than every score, so the first student wins.
# # def lowest_student(grades):


# #     lowest_name=""
# #     lowest_score=0

# #     for grade in grades:
# #         if grades[grade] > lowest_score:
# #             lowest_name=grade
# #             lowest_score=grades[grade]
# #     return lowest_name, lowest_score

# # J=lowest_student(grades = {"Maya": 88, "Omar": 59, "Lina": 92, "Zaid": 71, "Noor": 45}
# # )

# # print(J)


# # # # ---------- Q4: Total per region ----------
# # # # Key = the region. Value = the amount we add.
# # def total_by_region(sales):

# #     result={}

# #     for sale in sales:
# #         region=sale['region']
# #         if region not in result:
# #             result['region'] = 0
# #         result['region']+=sale['amount']

# #     return result

# # print(f'hillo bibi that is yoour result : {total_by_region(sales = [
# #     {"region": "north", "amount": 120},
# #     {"region": "south", "amount": 80},
# #     {"region": "north", "amount": 60},
# #     {"region": "east", "amount": 50},
# #     {"region": "south", "amount": 40},
# # ])}')


# #     result={}
# #     for sale in sales:
# #         region=sale["region"]
# #         if region not in result:
# #             result[region]=0
# #         result[region]+=sale["amount"]
# #     return result


# # # ---------- Q5: Bill ----------
# # # Step 1: count the quantity of each item. Step 2: multiply by the price.
# def bill(cart, prices):
#         quantities={}
#         for item in cart:
#           if item not in quantities:
#             quantities[item]=0
#         quantities[item]+=1

#         result={}
#         for item in quantities:
#           result[item]=quantities[item]*prices[item]
#         return result

#         print(f'hiiiiii {prices = {"pen": 2, "book": 10, "bag": 25},
# cart = ["pen", "bag", "pen", "book", "pen"]
#  }')


# # # ---------- Q6: Top region (reuses Q4) ----------
# def top_region(sales):


# # ---------- Tests ----------
# print(count_words(words))               # {'cat': 3, 'dog': 2, 'bird': 1}
# print(passed(grades))                   # {'Maya': 88, 'Lina': 92, 'Zaid': 71}
# name, score = lowest_student(grades)
# print(name, score)                      # Noor 45
# print(total_by_region(sales))           # {'north': 180, 'south': 120, 'east': 50}
# my_bill = bill(cart, prices)
# print(my_bill)                          # {'pen': 6, 'bag': 25, 'book': 10}
# print(sum(my_bill.values()))            # 41
# print(top_region(sales))


def total_by_region(sales):

    result = {}

    for reg in sales:
        region = reg['region']

        if region not in result:
            result[region] = 0

        result[region] += reg['amount']

    return result


def top_region(sales):

    total = total_by_region(sales)

    best_item = ''
    best_total = 0

    for item in total:
        if total[item] > best_total:
            best_item = item
            best_total = total[item]

    return best_item, best_total


sales = [
    {"region": "north", "amount": 120},
    {"region": "south", "amount": 80},
    {"region": "north", "amount": 60},
    {"region": "east", "amount": 50},
    {"region": "south", "amount": 40},
]


rs = total_by_region(sales=sales)

rs_2 = top_region(sales=sales)


print(f'Q_1: {rs}, Q_2: {rs_2}')
