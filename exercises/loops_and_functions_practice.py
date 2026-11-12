# numbers = [3, 7, 2, 9, 4, 6]

# for nu in numbers :
#      if nu > 5:
#        print(nu)


# def count_even(numberss):
#     count=0
#     for numm in  numberss:
#         if numm %2==0:
#             count+=1


#     return count


# countt = count_even ([1,2,4,5,6,7,8])
# print ('Q2:',countt)


# # #3:
numbersss = [1, 2, 3, 4, 5]
# Y = [S**2 for S in numbersss]
# print ('Q3:',Y)


# N = [4, 7, 4, 2, 7, 7, 9]
# C=0
# for NN in N :

#     if NN ==7:
#         C+=1
# print('Q4:',C)


# print ()
# def V(s):


#S= [scoerss for scoerss in s if scoerss >= 60]
#return S
# c= V([45, 80, 72, 90, 33, 65])
# print ('Q5:',c)


# def count_numbers(numbers):
#     key = {}

#     for number in numbers:
#         if number not in key:
#             key[number] = 0

#         key[number] += 1

#     return key


# G = count_numbers([4, 7, 4, 2, 7, 7, 9])
# # print('Q6',G)


# prices = {
#     "apple": 5,
#     "banana": 1,
#     "orange": 3
# }
# # for pri in prices:
# #     prices[pri]+=1

# # print(prices)
# result = {}
# for prii in prices:
#     if prices[prii] > 3:
#         result[prii]=prices[prii]
# # print(result)


# numbers = [2, 5, 2, 7, 5,1, 2, 7]
# K={}

# for r in numbers:
#     if r not in K:
#         K[r]=0
#     K[r]+=1
# # print (K)


# P={
#     'apple':1,
#     'banana':5,
#     'salad':4,
#     'bread':2

# }

# PP={}
# for O in P:
#     if P[O] >3:
#         PP[O]=P[O]
# # print(PP)


# number = [3, 8, 4, 7, 10, 5, 2]

# I = [M for M in number if M %2==0 ]
# co = len(I)
# # print(I)
# # print(co)


# L=[]
# count=0
# for i in number :
#     if i %2==0:
#      L.append(i)
#      count+=1
# # print(count)
# # print(L)


# numberss = [2, 7, 4, 9, 6, 1]
# E=[]
# for ii in numberss:
#     if ii > 5:
#         E.append(ii)
# # print (E)


# numbers_D = [1, 3, 3, 5, 1, 3, 7, 5]
# V= {}
# for number in numbers_D:
#     if number not in V:
#         V[number]=0
#     V[number]+=1
# print('hhhh',V)


# count={}
# for key in V:
#     if V[key]>1:
#        count[key]=V[key]
# print(count)


# numbers = [4, 9, 2, 7, 6, 1, 8]
# Q=[number  for number in numbers if number>4 and number %2==0]
# print(Q)
# U=[]
# for i in numbers:
#     if i % 2==0 and  i >4:
#         U.append(i)

# print(U)


# numbers = [1, 2, 3, 4, 5, 6]
# P = [Q**2 for Q in numbers if Q%2==0 ]
# print(P)

# W = []
# for r in P:
#     if r%2==0 and r**2:

#      W.append(r)
# print(W)


# scores = {
#     "Ali": 85,
#     "Sara": 62,
#     "Omar": 91,
#     "Lina": 68,
#     "Ahmed": 74
# }
# R={}

# for i in scores :
#     if  scores[i] > 70:
#         R[i]=scores[i]

# # print(R)

# X={i: scores[i] for i in scores if scores[i] >= 70}
# print(X)


# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# L = {}
# for i in words:
#     if i not in L:
#         L[i]=0
#     L[i]+=1
# print(L)
# J={}
# for i in L:
#     if L[i] >1:
#         J[i]=L[i]


# print(J)


# E= {word: words.count(word) for word in set(words) if words.count(word) > 1}
# print(E)


scores = {
    "Ali": 60,
    "Sara": 85,
    "Omar": 55,
    "Lina": 90
}

Y={key:scores[key]+10 if scores[key]<70 else  scores[key] for key in scores}
print(Y)

for S in scores:
    if scores[S] < 70:
        scores[S] += 10

print(scores)
distance = ((x₂ - x₁)² + (y₂ - y₁)²)
