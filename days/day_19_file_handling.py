# # with open('./files/reading_file_example.txt','w') as f:
# #     f.write('This text has to be appended at the end')

# import os

# if os.path.exists('./files/reading_file_exampl"e.txt'):
#     os.remove('./files/reading_file_exampl"e.txt')
# else:
#     print('not her my frind')


#     import json
# # JSON
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''
# # let's change JSON to dictionary
# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'],person_dct['country'])

# with open('speech.txt') as f:
#     text = f.read()
# print(text)


# import os

# print(os.getcwd())         # the folder where Python is looking right now
# print(os.listdir())        # the files Python sees in that folder


# with open('speech.txt','w') as f:
#     f.write('''Hello Python
# I am learning files
# This is line three''')

# with open ('speech.txt') as f:
#     text = f.read()

# def count_lines_words(filename):
#     lines = filename.splitlines()
#     words_count = filename.split()
#     count_lins = len(words_count)
#     return len(lines),count_lins
# print(count_lines_words(text))


# import json
# with open ('countries_data.json') as f:
#     date = json.load(f)


# def most_spoken_languages(date):

#     dec = {}

#     for contry in date:
#         for lang in contry['languages']:
#             if lang not in dec:
#                 dec[lang]=0
#             dec[lang]+=1
#     return dec
# dec = most_spoken_languages(date)
# result = sorted(dec.items(),key=lambda c:c[1] , reverse=True)

# for i in result[:2]:
#     print(i)


# def most_spoken_languages(date):

#     dec = {}

#     for contry in date:
#         for lang in contry['languages']:
#             if lang not in dec:
#                 dec[lang]=0
#             dec[lang]+=1
#     pair = []
#     for lang,count in dec.items():
#         pair.append((count,lang))
#     return sorted(pair,reverse=True)[:2]
# print (most_spoken_languages(date))


# def most_spoken_languages(date):

#     dec = []

#     for contry in date:
#         for lang in contry['languages']:
#                 dec.append(lang)
#     new_list=[]
#     for lang in set(dec):
#         new_list.append((dec.count(lang),lang))
#     return sorted(new_list,reverse=True)[:2]
# print(most_spoken_languages(date))


# def most_spoken_languages(data):
#     all_languages = []
#     for country in data:
#         for lang in country['languages']:
#             all_languages.append(lang)      # one long list, repeats included

#     pairs = []
#     for lang in set(all_languages):         # each language once
#         pairs.append((all_languages.count(lang), lang))   # (count, language)

#     return sorted(pairs, reverse=True)[:2]  # biggest first, keep the top 2

# print(most_spoken_languages(date))          # [(3,

# import json
# with open('population_data.json') as f:
#     date = json.load(f)

# def most_populated_countries(date,n):

#     rank=sorted(date,key=lambda c:c['population'],reverse=True)

#     top=rank[:n]
#     result=[]
#     for c in top:
#         result.append({'country': c['name'], 'population': c['population']})
#     return result

# print(most_populated_countries(date,2))


# def most_populated_countries(data, n):
#     remaining = data.copy()                  # a copy, so the original list is not changed
#     result = []

#     for i in range(n):                       # repeat n times
#         biggest = remaining[0]               # start with the first country
#         for c in remaining:                  # check every country
#             if c['population'] > biggest['population']:   # found a bigger one?
#                 biggest = c                  # then IT becomes the biggest

#         result.append({'country': biggest['name'], 'population': biggest['population']})
#         remaining.remove(biggest)            # take it out, so the next round finds the next biggest

#     return result

# print(most_populated_countries(date, 2))
# [{'country': 'Finland', 'population': 5530719}, {'country': 'Norway', 'population': 5379475}]


import re

text = '''From: ali@gmail.com
Please write to sara.k@yahoo.com or to omar_99@company.org
No email on this line.'''

# expected: ['ali@gmail.com', 'sara.k@yahoo.com', 'omar_99@company.org']


def reserch(text):
    return re.findall(r'[\w.]+@[\w.]+',text)

print(reserch(text))
def reserch(text):
    return re.findall(r'[\w.]+@[\w.]+', text)    # pattern in quotes, then a comma, then text

print(reserch(text))


text = 'the cat and the dog and the bird'

# def find_most_common_words(text,n):
#     taxt = re.findall(r'\w+',text)

#     top=taxt[:n]
#     for word in top:


# def find_most_common_words(text, n):
#     taxt = re.findall(r'\w+', text)
#     result_1 = {}

#     for word in taxt:
#         if word not in result_1:
#             result_1[word] = 0
#         result_1[word] += 1

#     result = []
#     for word, count in result_1.items():
#         result.append((count, word))

#     return sorted(result, reverse=True)[:n]

# print(find_most_common_words(text, 2))


# def find_most_common_words(text, n):
#     words = re.findall(r'\w+', text)               # all the words
#     pairs = []
#     for word in set(words):                        # each word once
#         pairs.append((words.count(word), word))    # (count, word), double brackets
#     return sorted(pairs, reverse=True)[:n]         # sort first, cut at the END

# print(find_most_common_words(text, 2))             # [(3, 'the'), (2, 'and')]


# with open ('speech.txt') as f:
#     date = f.read()

# import re
# def scerh_word(date,n):
    # words = re.findall(r'\w+', date)
    # result=[]
    # for word in set(words):
    #     result.append((word,words.count(word)))

    # return sorted(result,key=lambda x:x[1],reverse=True)[:n]

# print(scerh_word(date,3))

# import re

# with open ('michelle_obama_speech.txt') as f:
#     date_obama = f.read()


# with open ('melina_trump_speech.txt') as f:
#     date_melina = f.read()


# def michelle_obama_speech(date,n):
#     words = re.findall(r'\w+', date)
#     result=[]
#     for word in set(words):
#         result.append((word,words.count(word)))

#     return sorted(result,key=lambda x:x[1],reverse=True)[:n]


# def melina_trump_speech(date,n):
#     words = re.findall(r'\w+', date)
#     result=[]
#     for word in set(words):
#         result.append((word,words.count(word)))

#     return sorted(result,key=lambda x:x[1],reverse=True)[:n]


# def diffrint(date_1,date_2):

#     result=[]
#     for word_1 in michelle_obama_speech():
#         for word_2 in melina_trump_speech():
#             if word_1 in word_2:
#                 result.append(word_1)
#     return set(result)

# print(diffrint(date_obama,date_melina))


# def diffrint(date_1,date_2):

#     words_1 = re.findall(r'\w+', date_1)
#     words_2 = re.findall(r'\w+',date_2)
#     result=[]
#     for word_1 in set(words_1):
#         for word_2 in set(words_2):
#             if word_1 in word_2 :
#                 result.append((word_1,word_2))
#     return set(result)
# print(diffrint(date_obama,date_melina))


import re

with open('data/michelle_obama_speech.txt') as f:
    date_obama = f.read()

with open('data/melina_trump_speech.txt') as f:
    date_melina = f.read()


# def michelle_obama_speech(date, n):
#     words = re.findall(r'\w+', date)
#     result = []

#     for word in set(words):
#         result.append((words.count(word), word))

#     return sorted(result, reverse=True)[:n]


# def melina_trump_speech(date, n):
#     words = re.findall(r'\w+', date)
#     result = []


#     return sorted(result, reverse=True)[:n]


# def diffrint(date_1, date_2):
#     words_1 = set(re.findall(r'\w+', date_1))
#     words_2 = set(re.findall(r'\w+', date_2))

#     result = []

#     for word_1 in words_1:
#         for word_2 in words_2:
#             if word_1 == word_2:
#                 result.append(word_1)

#     return set(result)


# print(diffrint(date_obama, date_melina))


# import re

# with open('hacker_news.csv', encoding='utf-8') as f:
#     data = f.read()

# lines = data.splitlines()

# python_count = len([line for line in lines if re.search(r'[Pp]ython', line)])

# javascript_count = len([line for line in lines if re.search(r'[Jj]ava[Ss]cript', line)])

# java_count = len([
#     line for line in lines
#     if re.search(r'Java', line) and not re.search(r'JavaScript', line)
# ])

# print("Python:", python_count)
# print("JavaScript:", javascript_count)
# print("Java but not JavaScript:", java_count)
