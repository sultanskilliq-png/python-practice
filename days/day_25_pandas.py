import pandas as pd
import numpy as np

nums= [1,2,3,6,4,7]
result = pd.Series(nums,index=[1,2,3,4,5,6])
# print(result)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
# print(s)
# print(dct)

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
# result = pd.DataFrame(data,columns=['name','contry','city'])
# print(result)


data = [{'name':
    ['Asabeneh', 'Finland', 'Helsink'],
   'contry': ['David', 'UK', 'London'],
   'city': ['John', 'Sweden', 'Stockholm']
}]
# re = pd.DataFrame(data)


cv = pd.read_csv('data/hacker_news.csv')
# print(cv.head(1))

# print(cv.tail(1))

# print(cv.shape)
# print(cv.columns)
# print(cv['id'])
# print(cv['title'])
id = cv['id']
title = cv['title']
# print(len(id)==len(title))

# print(id.describe())
# print(id.info())


import pandas as pd
# import numpy as np
# data = [
#     {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
#     {"Name": "David", "Country":"UK","City":"London"},
#     {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
# df = pd.DataFrame(data)
# weights  = [30,40,50]
# df['weights'] = weights
# # print(df)

# heights= [170,160,200]
# df['heigts']=heights
# # print(df)

# df['heigts']=df['heigts']*0.01
# # print(df)
# # Using functions makes our code clean, but you can calculate the bmi without one
# def calculate_bmi ():
#     weights = df['weights']
#     heights = df['heigts']
#     bmi = []
#     for w,h in zip(weights, heights):
#         b = w/(h*h)
#         bmi.append(b)
#     return bmi

# bmi = calculate_bmi()

# df['BMI'] = bmi
# df['BMI']=round(df['BMI'],1)

# birth_year = ['1769', '1985', '1990']
# current_year = pd.Series(2020, index=[0, 1,2])
# df['Birth Year'] = birth_year
# df['Current Year'] = current_year
# # print(df.head())

# df['Birth Year'] = df['Birth Year'].astype('int')
# print(df['Birth Year'].dtype) # let's check the data type now

# age = df['Current Year']-df['Birth Year']
# df['age']=age
# print(df)

# print(df[df['age']>120])

cv = pd.read_csv('data/hacker_news.csv')
# print(cv.head)
# print(cv.tail())
# print(cv['title'])
# print(cv.columns)
# print(cv.rpow)
# print(cv.shape)
# py=cv['title']
# py.str.contains('python')


# p=cv['title'].str.contains('python')
# print(p)

# print(cv[cv['title'].str.contains('python',case=False,na=False)].sum())
result = cv[cv['title'].str.contains(r'[Pp]ython')]
# print(len(result))
# print(cv['title'].str.contains(r'[Pp]ython', na=False).sum())

# import re
# words = cv['title']
# result = []
# for word in words:
#     if re.findall(r'[Pp]ython',word):
#         result.append(word)
# print(len(result))
# print(len(cv[cv['title'].str.contains('JavaScript', na=False)]))
# print(cv.head())
# print(cv.info())
# print(cv.describe())
