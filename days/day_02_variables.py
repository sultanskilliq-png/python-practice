# # # age=int(input('wlcome to you:'))
# # # name=str(input('write your name:'))
# # # my_name= 'sultan'
# # # print(len(my_name))
# # # print(type(my_name))


# # # num_one=4
# # # num_two=5

# # # S = num_one * num_two
# # # k = (num_one**) * num_two


# # # π=3.7
# # # radius=int(input('write here:'))
# # # radiu= radius **2
# # # area = π * radiu
# # # Circumference=2*π*radiu
# # # circum_of_circle = Circumference
# # # print(circum_of_circle)


# # names = ["Ali", "Sara", "Ali", "Omar", "Sara", "Ali"]


# # o={}
# # for i in names:
# #     if i not in o:
# #         o[i]=0
# #     o[i]+=1
# # print(o)


# # students = {
# #     "Ali": "blue",
# #     "Sara": "red",
# #     "Omar": "blue",
# #     "Lina": "green",
# #     "Ahmed": "blue"
# # }


# # P={}
# # for k in students:
# #     if students[k]=='blue':

# #         P[k]=students[k]


# # print(P)


# # scores = {
# #     "Ali": 85,
# #     "Sara": 92,
# #     "Omar": 78,
# #     "Lina": 88,
# #     "Ahmed": 95
# # }


# # highest_score = 0
# # best_student = ""

# # for st in scores:
# #     if scores[st] > highest_score:
# #         best_student=st
# #         highest_score=scores[st]

# # print('b:',best_student,':h:',highest_score)


# # prices = {
# #      "apple": 2,
# #     "banana": 3,
# #      "orange": 4
# #  }

# # shopping = ["apple", "orange", "apple", "banana"]

# # L=0

# # for i in shopping:
# #     if i in prices:
# #         L+=prices[i]

# # I={}
# # for z in shopping :
# #     if z in prices:
# #         print(z, prices[z])


# # print(L)

# # print(I)


# names = ["Ali", "Sara", "Omar", "Lina"]

# scores = {
#     "Ali": 85,
#     "Sara": 55,
#     "Omar": 72,
#     "Lina": 60
# }


# # shopping = ["apple", "orange", "apple", "banana"]


# # Quntity={}
# # for Fre in shopping:
# #     if Fre not in Quntity:
# #         Quntity[Fre]=0
# #     Quntity[Fre]+=1
# # for Fre in Quntity:
# #     QU= Quntity[Fre]
# #     price=prices[Fre]
# #     total=QU*price
# #     print('Friuts:',Fre,'Qunt:',QU,'prics:',price,'total:',total)


# # def calculate_bill(shopping, prices):
# #     quantities = {}
# #     ruselt={}
# #     # Count each fruit
# #     for fruit in shopping:
# #         if fruit not in quantities:
# #             quantities[fruit] = 0
# #         quantities[fruit] += 1

# #     # Calculate and print the bill
# #     for fruit in quantities:
# #         quantity = quantities[fruit]
# #         price = prices[fruit]
# #         total = quantity * price

# #         P=(
# #             "Fruit:", fruit,
# #             "| Quantity:", quantity,
# #             "| Unit price:", price,
# #             "| Total:", total
# #         )
# #         return P


# # shopping = ["apple", "orange", "apple", "banana"]

# # R=calculate_bill(shopping, prices)
# # print(R)


# # def calculate_bill(shopping, prices):
# #     quantities = {}
# #     result = {}

# #     for fruit in shopping:
# #         if fruit not in quantities:
# #             quantities[fruit] = 0
# #         quantities[fruit] += 1

# #     for fruit in quantities:
# #         quantity = quantities[fruit]
# #         price = prices[fruit]
# #         total = quantity * price
# # ef low_stock(stock):
# #     M=[]

# #     for Y in stock:
# #         if stock[Y] < 5:
# #             M.append(stock[Y])

# #     return M

# # stock = {
# #     "apple": 12,
# #     "banana": 4,
# #     "orange": 9,
# #     "mango": 2,
# #     "grape": 7
# # }
# # P=low_stock(stock)
# # print(P)
# #         result[fruit] = {
# #             "quantity": quantity,
# #             "price": price,
# #             "total": total
# #         }

# #     return result


# # shopping = ["apple", "orange", "apple", "banana"]

# # bill = calculate_bill(shopping, prices)

# # print(bill)


# students = [
#     {"name": "Ali", "scores": [80, 90, 70]},
#     {"name": "Sara", "scores": [60, 55, 70]},
#     {"name": "Omar", "scores": [95, 88, 92]},
#     {"name": "Lina", "scores": [50, 65, 60]}
# ]
# def passed_students(students):
#     L=[]
#     for i in students:
#         avrage= sum(i['scores'])/len(i['scores'])

#         if avrage>70:

#             L.append((i['name'],avrage))
#     return L


# NN=passed_students(students)
# # print(NN)


# prices = {
#     "apple": 3,
#     "banana": 2,
#     "orange": 4
# }

# sold = ["apple", "orange", "apple", "banana", "orange"]

# W=0
# for i in sold :
#     if i in prices:
#         W+=prices[i]


# # print(W)


# # def custemrs_totel(orders, prices):
# #     totele = {}
# #     for order in orders:
# #         prder_totel=prices[order['product']] * order['quantity']

# #         customer=order['customer']

# #         if customer not in totele:
# #             totele[customer]=0

# #         totele[customer]+=prder_totel
# #     return totele

# orders = [
#     {"customer": "Ali", "product": "apple", "quantity": 2},
#     {"customer": "Sara", "product": "banana", "quantity": 3},
#     {"customer": "Ali", "product": "orange", "quantity": 1},
#     {"customer": "Omar", "product": "apple", "quantity": 4},
#     {"customer": "Sara", "product": "apple", "quantity": 2}
# ]

# prices = {
#     "apple": 3,
#     "banana": 2,
#     "orange": 4
# }
# O = custemrs_totel(orders,prices)
# # print(O)


# numbers = [4, 7, 2, 9, 6, 8]
# P=[i  for i in numbers if i >5 and i%2==0]
# # print('p',P)
# num=[]
# for i in numbers:
#     if i>5 and i %2==0:
#         num.append(i)
# # print('num:',num)


# products = [
#     {"name": "apple", "price": 3},
#     {"name": "banana", "price": 2},
#     {"name": "orange", "price": 4}
# ]

# j=[]

# for i in products:
#     if i["price"] >=3:
#         j.append(i)
# # print(j)


# orders = [
#     {"customer": "Ali", "amount": 5},
#     {"customer": "Sara", "amount": 7},
#     {"customer": "Ali", "amount": 4},
#     {"customer": "Omar", "amount": 3}
# ]

# total={}

# for i in orders:
#     customer=i["customer"]

#     if customer  not in total:
#         total[customer]=0
#     total[customer]+=i["amount"]
# # print(total)


# def top_customer(orders, prices):
#     totals = custemrs_totel(orders, prices)   # Step 1: total per customer

#     best_name = ""
#     best_total = 0
#     for name in totals:                       # Step 2: find the highest
#         if totals[name] > best_total:
#             best_name = name                  # the line that was missing
#             best_total = totals[name]

#     return best_name


# winner = top_customer(orders, prices)
# print(f"Top customer: {winner}")


# winner = "Sara"
# print(f"Top customer: {winner}")


stocks = {
    "apple": 12,
    "banana": 4,
    "orange": 9,
    "mango": 2,
    "grape": 7,
}
# def low_stock_names(stock):
#     low_names = []
#     for name in stock:
#         if stock[name] < 5:
#             low_names.append((name,stock[name]))
#     return low_names


# result = low_stock_names(stocks)
# print(result)
# print(f"Low stock: {result}")


def total_stock(stock):

    numbers=0
    for stoc in stock:
        if stock[stoc] not in numbers:
            numbers[stoc]=0
        numbers[stoc]+=stoc
    return numbers
