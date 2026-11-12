# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# # # output
# # I hope every one is enjoying the Python Challenge.
# # Are you ?
# # Days  Topics  Exercises
# # Day 1	5	    5
# # Day 2	6	    20
# # Day 3	5	    23
# # Day 4	1	    35
# # This is a backslash  symbol (\)
# # In every programming language it starts with "Hello, World!"


# company='Coding For All'

# print(len(company))
# print(company.lower())
# print(company.upper())
# print(company.[start:end])
# fuck='Coding For All'
# print(fuck.find('coding'))
# print(fuck.replace('coding','pyhoen'))

# print(company.split(' '))
# print(company[0])
# Trans=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# print('# '.join(Trans))


# radius = 10
# area = 3.14 * radius ** 2

# print('This My radius{}, and this the area{}'.format(radius,area))


# def count_vowels(text):

#     count=[]

#     for letter in text:
#         if letter in 'aeuio':
#             count.append(letter)

#     return count

# print(f'volum: {count_vowels('python is very very fun')}')


# def is_palindrome(word):

#     words = ''
#     for letter in word:
#         words = letter + words
#     if words == word:
#         return True
#     else:
#         return False


# print(f"python: {is_palindrome('python')}")
# print(f"level: {is_palindrome('level')}")


# def is_palindrome(word):

#     return word == word [::1]
# print(f'ruselt:{is_palindrome('python')}')
# print(f"level: {is_palindrome('level')}")


# name=input('write your name: ')

# age=int(input('write your age: '))
# years_left= 100-age

# Data_Year=2026+years_left

# copies=int(input('how many copies? '))
# message=f'Welcome {name}, oh, you have a long time to live {Data_Year}\n'

# print(copies*message)

# color=input('write your favorite color: ')

# print(name + ' likes ' + color)
# print(f'{name} likes {color}')
# print("You are " + str(age))

# print('hi'+'llo')

# print(f'')    # prints an empty line


# number=int(input('write your number: '))
# if number % 4 == 0:
#     print('yeeeeeees')
# elif number % 2 == 0:
#     print(number,'is even')
# else:
#     print(number,'is odd')


# num=int(input('write the number to check: '))
# check=int(input('write the number to divide by: '))
# if num % check == 0:
#     print(f'{check} divides evenly into {num}')
# else:
#     print(f'{check} does not divide evenly into {num}')
