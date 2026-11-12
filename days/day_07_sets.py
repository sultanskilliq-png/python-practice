# # sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]


# it_companies.add('Twiteer')
# print(it_companies)

# C=A.update(B)
# print(C)

# it_companies.discard('Facebook')
# print(it_companies)

# A.isdisjoint(B)
# print(A)

# A.intersection(B)
# print(A.intersection(age))

# A.difference(B)
# print(A)


# if len(age) > len(B):
#     print ('yeees is bigeer')

# else:
#     print('no infortnaly')


# sentence = "I am a teacher and I love to inspire and teach people."

# R = sentence.split()

# print(set(R))


# # 💻 Exercises: Day 8
# # Create an empty dictionary called dog
# dog={}
# # Add name, color, breed, legs, age to the dog dictionary
# dog.update({
#     'name':None,'breed':None,'legs':None
# })
# # {
# #     dog['name']=None
# # }

# DEC=['name','age','dog']
# dog= dict.fromkeys(DEC)


# # Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# student={
#     'first name':'','last name':''
#     ,'gender':'' , 'age':'',' marital status':'', 'skills':('python','java'),"lokichin":{
#         'city':''
#         , 'addres':''

#     }
# }
# # Get the length of the student dictionary
# print(len(student))
# print(type(len(student)))
# # Get the value of skills and check the data type, it should be a list
# print(student.get('skills'))
# print(type(student.get('skills')))
# # Modify the skills values by adding one or two skills
# student['skills']= 'java scribt'
# student['skills'].append ('javaaaaaa')
# print(student)
# # Get the dictionary keys as a list
# print(list(student.keys()))
# # Get the dictionary values as a list
# print(list(student.values   ()))

# # Change the dictionary to a list of tuples using items() method
# list_=list(dog.items())
# print(list_)
# # Delete one of the items in the dictionary
# del dog['name']
# dog.pop('breed')
# # Delete one of the dictionaries
# dog.popitem()
# # 🎉 CONGRATULATIONS !


# # 💻 Exercises: Day 8

# # 1. Create an empty dictionary called dog
# dog = {}

# # 2. Add name, color, breed, legs, age to the dog dictionary
# dog.update({
#     'name': None,
#     'color': None,
#     'breed': None,
#     'legs': None,
#     'age': None
# })


# # 3. Create a student dictionary
# student = {
#     'first name': '',
#     'last name': '',
#     'gender': '',
#     'age': '',
#     'marital status': '',
#     'skills': ['python', 'java'],
#     'country': '',
#     'city': '',
#     'address': ''
# }

# # 4. Get the length of the student dictionary
# print(len(student))

# # 5. Get the value of skills and check the data type
# print(student.get('skills'))
# print(type(student.get('skills')))

# # 6. Modify the skills values by adding one or two skills
# student['skills'].append('javascript')
# student['skills'].append('html')

# print(student)

# # 7. Get the dictionary keys as a list
# print(list(student.keys()))

# # 8. Get the dictionary values as a list
# print(list(student.values()))

# # 9. Change the dictionary to a list of tuples using items()
# items_list = list(dog.items())
# print(items_list)

# # 10. Delete one of the items in the dictionary
# del dog['name']
# dog.pop('breed')

# # 11. Delete the dictionary
# del dog


# number=int(input('writ your: '))
# result=[]
# for num in range(1,number +1):
#     if number % num ==0:
#         result.append(num)
# print(result)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result=[]

# for aa in a:
#     if aa in b:
#         result.append(aa)
# print(set(result),'yeeeeeeees')


# import random
# # number = int(input('what\'s your name: '))

# result=[]
# randomm=random.randint(1,20)

# for i in range(10):
#     result.append(random.randint(1,20))

# print(result)

# rs=[random.randint(1,50) for _ in range(10)]
# print(rs)


# a=[]
# b=[]
# for i in range(10):
#     a.append(random.randint(1,10))
#     b.append(random.randint(1,10))
# print(a,b)

# result=[]

# for i in a:
#     if i in b:

#         result.append(i)

# print(result)


# print('last: ', list(set(a) & set(b)))


# string=input('write your word: ')

# word= string[::-1]
# print(word)


# string = input('write your word: ')

# word = string[::-1]

# if string == word:
#     print('fintaaaaactik')
# else:
#     print('fuuuuuck')


# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# re=[num**2 for num in a if num%2==0]
# print(re)
# re=[]

# for i in a:
#     if i %2==0:
#         re.append(i)
# print('it\'s even number: ',re)


# while True:
#     player_1 = input("Player 1 (rock/paper/scissors): ")
#     player_2 = input("Player 2 (rock/paper/scissors): ")

#     if player_1 == player_2:
#         print("It's a tie!")

#     elif player_1 == "rock" and player_2 == "scissors":
#         print("Player 1 wins!")

#     elif player_1 == "scissors" and player_2 == "paper":
#         print("Player 1 wins!")

#     elif player_1 == "paper" and player_2 == "rock":
#         print("Player 1 wins!")

#     else:
#         print("Player 2 wins!")

#     again = input("Do you want to play again? (yes/no): ")

#     if again != "yes":
#         break


#     wins = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }

#     if p1 == p2:
#         print("Tie!")
#     elif wins[p1] == p2:
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")

#     if input("Play again? yes/no: ") != "yes":
#         break

while True:
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")

    win={
        'rock':'scissors',
        'scissors':'paper',
        'paper': 'rock'
    }


    if p1 == p2 :
        print('tie')
    if win[p1] == p2:
        print('player_1 win')
    else:
        print('player_2 win')

    agin=input('are you want to play agin? (yes / no) :  ')

    if agin != 'yes':
        break
