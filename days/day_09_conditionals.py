# 💻 Exercises: Day 9
# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# number=int(input('Enter your age: '))

# num = 18 - number
# if number >= 18:
#     print('feedback: You are old enough to drive.')
# else:
#     print('wait to become 18 year byby' , 'just allital time by by: ',num,'year even could to drive')
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# Enter your age: 30
# You are 5 years older than me.
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.


# number=int(input('Enter your age: '))
# my_age=23
# diffrint_age= abs(number - my_age)


# if number > my_age :
#     print ('you old than me',diffrint_age)
# elif number == my_age:
#     print('you have thr same my_age')

# else:
#     print(' I am old than you : ',diffrint_age)


# number_1=int(input('first number plase: '))
# number_2= int(input ('scond number plase: '))

# if number_1 > number_2:
#     print('your first number great than scound nuber')
# elif number_1 < number_2:
#     print('number_2 great than first number')
# else:
#     print('the same number here')


# choies=input('choies your firut plase:')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# # insied = []

# if choies not in  fruits:
#     fruits.append(choies)
#     print(list(fruits))


# else:
#     print('your friut here')


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# if 'skills' in person:
#     print(person['skills'][2])

# if'Python' in person['skills']:
#     print('yeeeeeees')

if 'JavaScript' in person['skills'] and 'Node' in person['skills']:

    print('front end developer')
