# import requests

# url = 'https://api.thecatapi.com/v1/breeds'

# response = requests.get(url)
# print(response.status_code)          # expected: 200
# print(response.json()[0]['name'])    # json() turns the data into a Python list; this prints the first cat breed


# import requests

# response = requests.get('https://api.thecatapi.com/v1/breeds')
# cats = response.json()

# print(len(cats))     # how many breeds
# print(cats[0])       # the first breed, as a dictionary
# import re
# import requests

# # 1) the working function
# def find_most_common_words(text, n):
#     words = re.findall(r'\w+', text)
#     pairs = []
#     print(f'total of words{len(words)}')
#     for word in set(words):
#         pairs.append((words.count(word), word))
#     return sorted(pairs, reverse=True)[:n]

# # 2) get the book
# url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
# response = requests.get(url)
# text = response.text

# # 3) the ONE new line: count the words in the book, keep the top 10
# # print(f'total of words{len(words)}')
# print(find_most_common_words(text, 10))


cats = [
    {'name': 'Abyssinian', 'weight': {'metric': '3 - 5'}, 'life_span': '14 - 15', 'origin': 'Egypt'},
    {'name': 'Bengal',     'weight': {'metric': '3 - 7'}, 'life_span': '12 - 15', 'origin': 'United States'},
    {'name': 'Birman',     'weight': {'metric': '4 - 6'}, 'life_span': '14 - 15', 'origin': 'France'},
    {'name': 'Persian',    'weight': {'metric': '3 - 5'}, 'life_span': '14 - 15', 'origin': 'Iran'},
    {'name': 'Siamese',    'weight': {'metric': '2 - 5'}, 'life_span': '12 - 15', 'origin': 'Thailand'},
]

# print(cats[0]['weight']['metric'])   # '3 - 5'
import re
def search_numbers(cats):
    result=[]

    for cat in cats:
        text = cat['weight']['metric']
        num = re.findall(r'\d+', text)
        a = int(num[0])
        b = int(num[1])
        result.append((a + b) / 2)
    return result
# print(search_numbers(cats))
# weights = search_numbers(cats)

# print(max(weights))
# print(min(weights))
# print((sum(weights)/len(weights)))

# middiel = sorted(weights)
# result = len(middiel)// 2
# print(middiel[result])

# import statistics

# print(statistics.median(weights))    # 4.0   (does the median for you, even or odd)
# print(statistics.pstdev(weights))    # 0.6   (the standard deviation)
# def search_numbers(cats):
#     result = []
#     for cat in cats:
#         num = cat['weight']['metric'].split(' - ')   # '3 - 5' becomes ['3', '5']
#         result.append((int(num[0]) + int(num[1])) / 2)
#     return result

# print(search_numbers(cats))   # [4.0, 5.0, 5.0, 4.0, 3.5]


# def cat_ (cats):
#     words=[]

#     for cat in cats:
#         text = cat['life_span']      # '14 - 15'
#         num = re.findall(r'\d+',text)
#         a = int(num[0])
#         b = int(num[1])
#         words.append((a+b)/2)
#     return words
# print(cat_(cats))

# words = cat_(cats)

# print(max(words))
# print(min(words))
# import statistics
# print(statistics.mean(words))
# print(statistics.pstdev(words))


cats = [
    {'name': 'Abyssinian', 'origin': 'Egypt'},
    {'name': 'Aegean',     'origin': 'Greece'},
    {'name': 'Chausie',    'origin': 'Egypt'},
    {'name': 'Mau',        'origin': 'Egypt'},
    {'name': 'Birman',     'origin': 'France'},
    {'name': 'Chartreux',  'origin': 'France'},
]

# expected: {'Egypt': 3, 'Greece': 1, 'France': 2}


def count_by_country(cats):
    new_list = {}
    for cat in cats:
        country = cat['origin']              # the value, like 'Egypt'
        if country not in new_list:
            new_list[country] = 0            # first time we see this country
        new_list[country] += 1               # always add 1
    return new_list

print(count_by_country(cats))
# {'Egypt': 3, 'Greece': 1, 'France': 2}


import re      # the RegEx tool, we need it to search inside text

# The "web page". It is just a long text made of 3 rows (one row = one dataset)
html = '''
<table>
<tr><td><a href="/dataset/iris">Iris</a></td><td>150</td></tr>
<tr><td><a href="/dataset/wine">Wine</a></td><td>178</td></tr>
<tr><td><a href="/dataset/adult">Adult</a></td><td>48842</td></tr>
</table>
'''

# ---- TASK 1: get the names ----
# The pattern has 5 pieces, from left to right:
#   <a        the start of the opening tag (written exactly like this)
#   [^>]*     any characters that are NOT '>', as many as needed.
#             This skips the part  href="/dataset/iris"
#   >         the end of the opening tag
#   ( [^<]+ ) the ( ) means: "KEEP only this part".
#             [^<]+ = one or more characters that are NOT '<'. This catches: Iris
#   </a>      the closing tag
names = re.findall(r'<a[^>]*>([^<]+)</a>', html)
print(names)           # ['Iris', 'Wine', 'Adult']   <- only the parts inside ( )

# ---- TASK 2: how many datasets ----
print(len(names))      # 3   <- len counts the items in the list

# ---- TASK 3: the number of rows ----
#   <td>      the opening tag
#   (\d+)     KEEP this: one or more digits
#   </td>     the closing tag
# Only the 2nd <td> of each row has digits only, so the 1st <td> (with the name) is skipped
rows = re.findall(r'<td>(\d+)</td>', html)
print(rows)            # ['150', '178', '48842']


from bs4 import BeautifulSoup   # install name: beautifulsoup4, import name: bs4

# (use the same html text from above)

# BeautifulSoup reads the text and understands the tags.
# 'html.parser' tells it that the text is HTML
soup = BeautifulSoup(html, 'html.parser')

# ---- TASK 1: get the names ----
names = []                         # an empty basket
for a in soup.find_all('a'):       # find_all('a') gives a list of ALL the <a> tags
    names.append(a.text)           # a.text is what sits BETWEEN <a ...> and </a>
print(names)                       # ['Iris', 'Wine', 'Adult']

# ---- TASK 2: how many datasets ----
print(len(names))                  # 3

# ---- TASK 3: the number of rows ----
rows = []                          # an empty basket
for td in soup.find_all('td'):     # find_all('td') gives ALL the <td> tags (6 of them)
    if td.text.isdigit():          # isdigit() is True when the text is only digits ('150' yes, 'Iris' no)
        rows.append(td.text)       # keep only the number cells
print(rows)                        # ['150', '178', '48842']
