# import requests
# from bs4 import BeautifulSoup

# headers = {'user_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0'}

# url= 'https://www.bu.edu/president/boston-university-facts-stats/'

# respons = requests.get(url)
# soup = BeautifulSoup(respons.content,'html.parser')
# facts={}

# for h in soup.find_all('h3'):
#     title = h.get_text(strip=True)
#     number = h.find_next(string=lambda s: s.strip()).strip()   # next text that is not empty
#     if number[0].isdigit() or number[0] == '$':                # keep only numbers
#         facts[title] = number


# lines = [line.strip() for line in soup.get_text('\n').split('\n') if line.strip ]
# result = []
# for line in soup.get_text('\n').split('\n'):
#     clean = line.strip
#     if clean:
#         result.append(clean)
# for i,line in enumerate(result[:60]):
#     print(i,line)
# for i,n in enumerate(lines):
#     print()


# import re
# import json
# import requests
# from bs4 import BeautifulSoup

# url = 'http://www.bu.edu/president/boston-university-facts-stats/'   # redirects to https by itself
# headers = {'User-Agent': 'Mozilla/5.0'}          # look like a browser, some sites block plain code

# response = requests.get(url, headers=headers)
# print(response.status_code)                      # 200 = success

# soup = BeautifulSoup(response.text, 'html.parser')
# # get_text('\n') = all the page text, one piece per line; then remove empty lines
# lines = [line.strip() for line in soup.get_text('\n').split('\n') if line.strip()]

# # keep only the facts area: from 'Quick Facts' until the footer line 'Boston University'
# start = [i for i, line in enumerate(lines) if 'Quick Facts' in line][0]
# end = lines.index('Boston University', start) if 'Boston University' in lines[start:] else len(lines)

# VALUE = r'\$?\s?\d[\d,.:]*\s?[M+%]*'             # a number like 848, 38,093, $ 641 M, 10:1, 300+

# facts = {}
# label = None                                      # the last label line we saw
# for line in lines[start:end]:
#     if re.fullmatch(VALUE, line):                 # a line with ONLY a number
#         if label:
#             facts[label] = line                   # it belongs to the label before it
#             label = None
#     else:
#         both = re.fullmatch(r'(.+?)\s+(' + VALUE + ')', line)   # 'label number' on one line
#         if both:
#             facts[both.group(1)] = both.group(2)  # group(1) = label, group(2) = number
#         else:
#             label = line                          # a label alone, its number comes next

# print(facts)

# with open('bu_facts.json', 'w', encoding='utf-8') as f:     # 'w' creates the file
#     json.dump(facts, f, indent=4, ensure_ascii=False)       # indent=4 makes it easy to read


# import requests
# import json
# from bs4 import BeautifulSoup

# # --- Part 0: get the page ---
# url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

# facts = {}   # empty dictionary, we will fill it

# --- Part 1: the 8 boxes ---
# HTML: <article class="bu-stat-single ..."> ... </article>
# boxes = soup.find_all('article', class_='bu-stat-single')

# for box in boxes:
#     # HTML: <h3 class="bu-stat-title">Classrooms</h3>
#     title = box.find('h3', class_='bu-stat-title').get_text(strip=True)

#     # HTML: <div class="bu-stat-value-container"> has 3 small spans: $ , 641 , M
#     container = box.find('div', class_='bu-stat-value-container')

#     # stripped_strings gives each piece of text: '$', '641', 'M'
#     # ''.join(...) glues them together: '$641M'
#     value = ''.join(container.stripped_strings)

#     facts[title] = value

# --- Part 2: the 13 list items ---
# HTML: <li> <span class="stat-label">Student Body</span>
#            <span class="stat-figure">38,093</span> </li>


# facts = {}   # empty dictionary, we will fill it


#     facts[title] = value


# for li in items:
#     label = li.find('span', class_='stat-label')    # None if this li is a menu item
#     figure = li.find('span', class_='stat-figure')

#     if label and figure:                             # keep only the li that have both
#         facts[label.get_text(strip=True)] = figure.get_text(strip=True)

# # print(len(facts))
# # print(facts)

# # --- Part 3: save as JSON ---
# with open('bu_facts.json', 'w', encoding='utf-8') as f:
#     json.dump(facts, f, indent=4, ensure_ascii=False)


# # ---------- Part 0: get the page ----------
# url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# # print(response.status_code)                      # 200 = success
# soup = BeautifulSoup(response.text, 'html.parser')

# # the big div that holds Community, Campus and Academics
# content = soup.find('div', class_="facts-stats-content")


# # ---------- Part 1: Quick Facts (3 boxes, outside content) ----------
# quick = soup.find('div', class_="bu-stat-count-3")
# quick_boxes = quick.find_all('article', class_="bu-stat-single")
# print(len(quick_boxes))                          # expect 3

# quick_data = {}
# for box in quick_boxes:
#     title = box.find('h3', class_='bu-stat-title').get_text(strip=True)
#     value = box.find('div', class_='bu-stat-value-container').get_text(strip=True)
#     quick_data[title] = value                    # '$' + '641' + 'M' = '$641M'


# # ---------- Part 2: Community (first section) ----------
# sections = content.find_all('section', class_="stat-section")
# print(len(sections))                             # expect 2

# community_items = sections[0].find_all('li')
# print(len(community_items))                      # expect 7

# community_data = {}
# for li in community_items:
#     label = li.find('span', class_="stat-label").get_text(strip=True)
#     figure = li.find('span', class_="stat-figure").get_text(strip=True)
#     community_data[label] = figure


# # ---------- Part 3: Campus (5 boxes, inside content) ----------
# campus = content.find('div', class_="bu-stat-list")
# campus_boxes = campus.find_all('article', class_="bu-stat-single")
# print(len(campus_boxes))                         # expect 5

# campus_data = {}
# for box in campus_boxes:
#     title = box.find('h3', class_='bu-stat-title').get_text(strip=True)
#     value = box.find('span', class_='bu-stat-value-field').get_text(strip=True)
#     campus_data[title] = value


# # ---------- Part 4: Academics (second section) ----------
# academics_items = sections[1].find_all('li')
# print(len(academics_items))                      # expect 6

# academics_data = {}
# for li in academics_items:
#     label = li.find('span', class_="stat-label").get_text(strip=True)
#     figure = li.find('span', class_="stat-figure").get_text(strip=True)
#     academics_data[label] = figure


# # ---------- Part 5: join everything ----------
# facts = {}
# facts.update(quick_data)
# facts.update(community_data)
# facts.update(campus_data)
# facts.update(academics_data)

# print(len(facts))                                # expect 19
# print(facts)


# ---------- Part 6: save as JSON ----------
# with open('bu_facts.json', 'w', encoding='utf-8') as f:
#     json.dump(facts, f, indent=4, ensure_ascii=False)


# # ---------- Part 0: get the page ----------
# url = 'https://www.scrapethissite.com/pages/forms/'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# print(response.status_code)                      # 200 = success
# soup = BeautifulSoup(response.content, 'html.parser')


# tabel = soup.find('table',class_="table")

# rows = tabel.find_all('tr')

# table_th = []

# for th in rows[0].find_all('th'):
#     table_th.append(th.get_text(strip=True))
# print(len(table_th))


# date = []


# for row in rows[1:]:
#     calls = row.find_all('td')
#     if not calls:
#         continue
#     item={}
#     for i,j in enumerate(calls):
#         item[table_th[i]]=j.get_text(strip=True)
#     date.append(item)

# print(date[0])

# import json
# with open('hockey.json', 'w', encoding='utf-8') as f:
#     json.dump(date, f, indent=4, ensure_ascii=False)


# url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# # 1. the table (check the count, see the note below)
# print(len(soup.find_all('table', class_='wikitable')))
# table = soup.find('table', class_='wikitable')

# # 2. remove reference marks like [19]
# for sup in table.find_all('sup'):
#     sup.decompose()

# # 3. one dictionary for each president
# data = []
# for row in table.find_all('tr'):
#     th = row.find('th', scope='row')     # only the first row of each president
#     if not th:
#         continue
#     cells = row.find_all('td')
#     data.append({
#         'number': th.get_text(strip=True),
#         'name': cells[1].find('b').get_text(strip=True),
#         'term': cells[2].get_text(' ', strip=True),
#         'party': cells[4].get_text(strip=True)
#     })

# print(len(data))      # expect 47
# print(data[0])

# # 4. save
# with open('presidents.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)


# import requests
# from bs4 import BeautifulSoup
# # ---------- Part 0: get the page ----------
# url = 'https://books.toscrape.com/'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# print(response.status_code)                      # 200 = success
# soup = BeautifulSoup(response.text, 'html.parser')

# books = soup.find('ol',class_="row")
# rows = books.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# for row in rows:
#     name = row.find('h3').get_text(strip=True)
#     rating = row.find('p',class_="star-rating")['class'][1]
#     title = row.find('p',class_="price_color").get_text(strip=True)
#     print(f'book_name: {name}')
#     print(f'rating: {rating}')
#     print(f'title: {title}')
#     print('-'*30)


# table = soup.find('table',class_="table")
# rows = table.find_all('tr')
# key=[]
# sc=[]
# for rwo in rows:
#     th = rwo.find_all('th')
#     if  th:
#         key=[t.get_text(strip=True) for t in th]
#         continue
#     result_sc={}
#     cells = rwo.find_all('td')
#     for keyy,value in enumerate(cells):
#         result_sc[key[keyy]]=value.get_text(strip=True)
#     sc.append(result_sc)
# # print(sc[0])

# keys = []
# sc = []
# for rwo in rows:
#     if rwo.find('th'):                                 # the first row (it has th)
#         keys = rwo.get_text('|', strip=True).split('|')   # one line instead of the list
#         continue
#     cells = rwo.find_all('td')                         # data rows
#     result_sc = {}
#     for i, value in enumerate(cells):
#         result_sc[keys[i]] = value.get_text(strip=True)
#     sc.append(result_sc)


# for rwo in rows[:3]:
#     # print: how many th, how many td in this row
#     print(len(rwo.find_all('th')), len(rwo.find_all('td')))


# table = soup.find('table',class_="wikitable")

# infoo=[]
# for rwo in table.find_all('tr'):
#     th = rwo.find('th',scope="row")
#     if not th:
#         continue
#     calls = rwo.find_all('td')

#     infoo.append({
#         'number' : th.get_text(strip=True),
#         'Name' : calls[1].find('b').get_text().strip(),
#         'Term' : calls[2].get_text('',strip=True),
#         'Party' : calls[4].get_text(strip=True),
#         'election': calls[5].get_text(strip=True),

#     })

# t = table.find_all('a',rel="mw:WikiLink")
# print('hjhhhh',len(t))

# import json

# with open ('fack_prisedent.json','r') as f:
#      read = json.load(f)
#      print(read)


# # for chek:
# if not calls[5].find('a'):            # no <a> in this cell
#         print(th.get_text(strip=True), calls[5].get_text(strip=True))
# # import json

# with open ('fack_prisedent.json','w') as f:
#     json.dump(infoo,f,indent=4,ensure_ascii=False)


# soup = BeautifulSoup(html, 'html.parser')

# rows = soup.find_all('div', class_='row')

# for row in rows:
#     countries = row.find_all('div', class_='col-md-4 country')

#     for country in countries:
#         name = country.find('h3', class_='country-name').get_text(strip=True)

# countries = soup.find_all('div', class_='country')


#     capital = country.find('span', class_='country-capital').get_text(strip=True)

#     population = country.find('span', class_='country-population').get_text(strip=True)

#     area = country.find('span', class_='country-area').get_text(strip=True)

#     print(f"Country: {name}")
#     print(f"Capital: {capital}")
#     print(f"Population: {population}")
#     print(f"Area: {area} km²")
#     print("-" * 30)


# contires = soup.find_all('div',class_="col-md-4 country")

# for contry in contires:
#     contryy = contry.find('h3',class_="country-name").get_text(strip=True)
#     captil = contry.find('span',class_="country-capital").get_text(strip=True)
#     Population = contry.find('span',class_="country-population").get_text(strip=True)
#     print(f'contry : {contryy}')
#     print(f'captil : {captil}')
#     print(f'Population : {Population}')
#     print('-'*30)


# books = soup.find('ol',class_="row")
# rows = books.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# for row in rows:
#     name = row.find('h3').find('a')['title']
#     rating = row.find('p',class_="star-rating")['class'][1]
#     title = row.find('p',class_="price_color").get_text(strip=True)
#     url = row.find('a')['href']
#     print(f'book_name: {name}')
#     print(f'rating: {rating}')
#     print(f'title: {title}')
#     print(f'link: {url}')
#     print('-'*30)
# print(f'the count of books: {len(rows)}')

# from urllib.parse import urljoin
# url = urljoin('https://books.toscrape.com/', row.find('a')['href'])


import requests
import re

url = 'https://books.toscrape.com/'
response = requests.get(url)
html = response.text
price = re.findall(r'£\d+.\d+',html)
ratings = re.findall(r'<p class="star-rating (\w+)',html)
name_of_book = re.findall(r'title="([^"]+)',html)
link = re.findall(r'a href="([^"]+)',html)
random= re.findall(r'In stock',html)

result = dict(zip(name_of_book,ratings))


# print(result)
# for name, rating in zip(name_of_book, ratings):
    # print(f'name: {name} rating:{ratings}')
result = [float(pr.replace('£', '')) for pr in price]

cost = 0
for i in result:
    if i < 30:
        cost += 1

print(cost)
