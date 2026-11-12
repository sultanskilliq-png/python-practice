# import re

# txt = 'My dog likes your dog and my cat'
# # write the line with re.findall here, then print it
# # expected: ['dog', 'dog']
# result = re.findall('dog',txt)
# print(result)

# import re

# txt = 'Ali is 25 and Sara is 30 and the room is 101'
# # write the line with re.findall here, then print it
# # expected: ['25', '30', '101']
# print(re.findall(r'\d+',txt))

# import re

# txt = 'H*e*llo, I* am le*arning Py*thon'
# # write the line with re.sub here, then print it
# # expected: Hello, I am learning Python
# print(re.sub(r'\*','',txt))


# import re

# txt = 'Cat and cat and dog and Cats'
# # write the line with re.findall here, then print it
# # expected: ['Cat', 'cat', 'Cat']
# print(re.findall('[Cc]ats?',txt))

# result = re.findall('[Cc]at',txt)
# print(result)


# import re

# txt = 'red,green,;blue,:yellow'
# # write the line with re.split here, then print it
# # expected: ['red', 'green', 'blue', 'yellow']
# print(re.split(r'[,;:]+',txt))


import re
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# result_1 = re.findall(r'\w+',paragraph)
# det={}
# pair=[]
# for ser in result_1 :
#     if ser not in det:
#         det[ser]=0
#     det[ser]+=1
# for word,count in det.items():
#     pair.append((count,word))

# final_result = sorted(pair,reverse=True)
# print(f'what thr fuck: {final_result}')


# words = re.findall(r'\w+', paragraph)

# pairs = []
# for word in set(words):                   # each different word, once
#     pairs.append((words.count(word), word))   # (how many times, the word)

# print(sorted(pairs, reverse=True))        # same result as yours


# words = re.findall(r'\w+',paragraph)
# new=[]
# for word in set(words):
#     new.append((word,words.count(word)))
# result = sorted(new,key=lambda c:c[1],reverse=True)
# print(f'fuck man: {result}')


# txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

# step_1 = re.findall(r'-?\d+',txt)
# result=[]
# for p in step_1:
#     result.append(int(p))

# big= max(result)
# smal = min(result)
# resultt = big-smal
# print(f'yeeees man your the best:; {resultt}')


# def is_valid_variable(word):

#    pattern = r'^[a-zA-Z_]\w*$'
#    result = re.findall(pattern,word)
#    if result:
#       return True
#    return False
# print(is_valid_variable('first_name')) # True)


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re

def clean_text(sentence):
    # 3 separate values: pattern, replacement (empty text), the text
    return re.sub(r'[^a-zA-Z ]', '', sentence)

def most_frequent_words(cleaned_text):
    words = re.findall(r'\w+', cleaned_text)       # get the words only
    pairs = []
    for word in set(words):                        # each different word, once
        pairs.append((words.count(word), word))    # (how many times, the word)
    final_result = sorted(pairs, reverse=True)     # biggest count first
    return final_result[:3]                        # keep the first three

cleaned_text = clean_text(sentence)             # the name now matches the course line
print(cleaned_text)
print(most_frequent_words(cleaned_text))        # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]


print(clean_text(sentence));
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
