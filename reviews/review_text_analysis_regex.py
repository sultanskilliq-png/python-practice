# with open ('obama_speech.txt','r') as f:

#     data = f.read()
import re
# # def compute(data):
# #     result = re.findall(r'\w+',data)
# #     count = {}
# #     for i in result :
# #         if i not in count:
# #             count[i]=0
# #         count[i]+=1
# #     numbers=[]
# #     for key,value in count.items():
# #         numbers.append((key,value))
# #     return sorted(numbers, key=lambda c: c[1], reverse=True)[:10]

# # print(compute(data))

# def compute(data):
#     result = re.findall(r'\w+', data)
#     resultt = []

#     for word in result:
#         resultt.append((result.count(word), word))

#     word = sorted(set(resultt), reverse=True)[:10]
#     return word

# print(compute(data))


# # print(compute(data))


# def compute(data):
#     words = re.findall(r'\w+',data)
#     result={}
#     for word in words:
#         if word not in result:
#             result[word]=0
#         result[word]+=1
#     final_result = []
#     for count,number in result.items():
#         final_result.append((number,count))
#     key=sorted(final_result,reverse=True)[:10]
#     return key

# print(compute(data))


# with open ('hacker_news.csv','r') as f:
#     data= f.read()

# import re

# def compute(data):
#     lines = data.splitlines()

#     python_count = 0
#     javascript_count = 0
#     java_count = 0

#     for line in lines:
#         if re.search(r'\b[Pp]ython\b', line):
#             python_count += 1

#         if re.search(r'\b[Jj]ava[Ss]cript\b', line):
#             javascript_count += 1

#         if re.search(r'\bJava\b', line) and not re.search(r'\bJavaScript\b', line):
#             java_count += 1

#     return (
#         f'Python lines: {python_count}, '
#         f'JavaScript lines: {javascript_count}, '
#         f'Java but not JavaScript lines: {java_count}'
#     )

# with open('hacker_news.csv', 'r', encoding='utf-8') as f:
#     data = f.read()

# def clean(data):
#     word = re.sub(r'[^\w\s]', '', data)
#     return word.lower()
# print(clean(data))


# import re

# def clean_text(text):
#     text = re.sub(r'[^\w\s]', '', text)
#     return text.lower()


# def remove_support_words(text, support_words):
#     words = text.split()
#     result = []

#     for word in words:
#         if word not in support_words:
#             result.append(word)

#     return ' '.join(result)


# def check_text_similarity(text1, text2):
#     words1 = set(text1.split())
#     words2 = set(text2.split())

#     common_words = words1.intersection(words2)
#     all_words = words1.union(words2)

#     return len(common_words) / len(all_words) if all_words else 0


# with open('michelle_obama_speech.txt', 'r', encoding='utf-8') as f:
#     michelle = f.read()

# with open('melina_trump_speech.txt', 'r', encoding='utf-8') as f:
#     melina = f.read()

# michelle = clean_text(michelle)
# melina = clean_text(melina)

# # Add the support words here.
# support_words = set()

# michelle = remove_support_words(michelle, support_words)
# melina = remove_support_words(melina, support_words)

# print(check_text_similarity(michelle, melina))


# nums = [1,2,3,4,5]


# paragraph = """I love teaching. If you do not love teaching what else can you love.
# I love Python if you do not love something which can give you all the capabilities
# to develop an application what else can you love."""
# import re
# def search(data,n):
#     words = re.findall(r'\w+',data)
#     result = []
#     for word in words:
#         if word not in [item[1]for item in result]:
#             result.append((words.count(word),word))
#     return sorted(result,reverse=True)[:n]
# print(search(paragraph,5))


# import re
# def search(data,n):
#     words = re.findall(r'\w+',data)
#     result = {}
#     for word in words:
#         if word not in result:
#             result[word]=0
#         result[word]+=1
#     resultt=[]
#     for count,wordd in result.items():
#         resultt.append((wordd,count))

#     return sorted(resultt,reverse=True)[:n]
# print(search(paragraph,5))


# text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
# def find(data):
#     numbers = re.findall(r'-?\d+',data)
#     result = [int(num)for num in numbers]
#     return result
# result = find(text)
# print(result)
# min = min(result)
# max = max(result)
# res = max-min
# print(res)


# def is_valid_variable(name):

#     words = re.fullmatch(r'[a-zA-Z_]\w*',name)
#     return bool(words)


# # print(is_valid_variable('first_name')) # True
# # print(is_valid_variable('first-name')) # False
# # print(is_valid_variable('1first_name')) # False
# # print(is_valid_variable('firstname')) # True

# def is_valid_variable(name):

#     words = r'[a-zA-Z_]\w*'
#     result = re.findall(words,name)
#     if result:
#         return True
#     return 'fauck to you'
# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True


# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
# There $is nothing; &as& mo@re rewarding as educa@ting
# &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re
# interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate
# yo@u to be a tea@cher!?'''
# def clean(data):
#     words = re.sub(r'[^a-zA-Z\s]','',data)
#     return words
# def freq(data,n):
#     words = re.findall(r'\w+',clean(data))
#     words = clean(data).split()
#     result=[]
#     for word in words:
#         if word not in [item[1]for item in result]:
#             result.append((words.count(word),word))
#     return sorted(result,reverse=True)[:n]
# print(freq(sentence,3))


# try:
#     age = int('hello')
# except ValueError:
#     print('congaralahin you answor is coorect')

# # def number(a,s,d,f,g):
# #     return a+s+d+f+g
# # num = [1,3,4,7,7]
# # print(number(*num))

# def number(*num):
#     return sum(num)
# print(number(1,2,3,4))


# names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
# *nordic_countries, es, ru = names
# print(nordic_countries)


import numpy as np


x = np.array([10,20,30,40,50])
y = np.array([100, 200, 300, 400, 500])

# print(f'x.shape:{x.shape}, x.dtype:{x.dtype}, x.size:{x.size}')
# z=x+5
# print(z)
# print(z*2)
# print(x[0])
# print(x[-1])
# print(x[2:5])
# print(x[-3:])
# print(x[1,2])
# try:
#   print(x[1,3])
# except IndexError:
#     print('your answor is coorect')

# u = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(u.reshape(3,4))
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.hstack((a,b)))
# print(np.hstack([a,b]))

# import random
# print(np.random.randint(1,50,size=5))
c=np.random.randint(1,100,size=10)

# a = np.mean(u)
# b = np.std(u)


x = np.array([10, 25, 30, 45, 50, 65])

# print(x[x>40])

a = np.array([[1, 2], [3, 4]])
# print(a.T)


import numpy as np

x = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(x[0:,0])

print("Column minimum:", np.min(x, axis=0))
print("Column maximum:", np.max(x, axis=0))
print("Row minimum:", np.min(x, axis=1))
print("Row maximum:", np.max(x, axis=1))
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]
# plt.plot(x,y)
# plt.scatter(x,y)
# import matplotlib.pyplot as plt

# plt.hist(normal_data, bins=21, color="grey")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Normal Distribution")
# plt.show()


url=''
