# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']


# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruits[0]='anana'
# print(fruits)


# # # syntax
# # lst = ['item1', 'item2']
# # lst.pop()       # last item
# # lst.pop(index)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)       # ['banana', 'orange', 'mango']

# fruits.pop(0)
# print(fruits)       # ['orange', 'mango']


# num1 = [0, 1, 2, 3]
# num2= [4, 5, 6]
# num1.extend(num2)
# print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]


# ============================================================
# Day 5: Python Lists Practice
# ============================================================


# ------------------------------------------------------------
# Q1: Indexing
# Print: length, first company, middle company, last company
# ------------------------------------------------------------

# it_companies = [
#     "Facebook", "Google", "Microsoft",
#     "Apple", "IBM", "Oracle", "Amazon"
# ]

# print(len(it_companies))
# print(it_companies[0])
# print(it_companies[len(it_companies) // 2])
# print(it_companies[-1])


# # ------------------------------------------------------------
# # Q2: Slicing
# # Print: first 3, last 3, and middle company
# # ------------------------------------------------------------

# print(it_companies[:3])
# print(it_companies[-3:])
# print(it_companies[len(it_companies) // 2])


# # ------------------------------------------------------------
# # Q3: Reverse two ways
# # Way A: [::-1] creates a new reversed list
# # ------------------------------------------------------------

# reversed_companies = it_companies[::-1]

# print(reversed_companies)
# print(it_companies)   # Original is unchanged


# # Way B: .reverse() changes the list itself
# # Use a copy so the original stays safe

# companies = it_companies.copy()
# companies.reverse()

# print(companies)
# print(it_companies)   # Original is unchanged

# # Difference:
# # [::-1] creates a new reversed list.
# # .reverse() changes the list it is called on.


# # ------------------------------------------------------------
# # Q4: Add, insert, and change
# # ------------------------------------------------------------

# companies = it_companies.copy()

# # Add Netflix to the end
# companies.append("Netflix")

# # Insert Tesla in the middle
# middle = len(companies) // 2
# companies.insert(middle, "Tesla")

# # Change Google to uppercase
# google_index = companies.index("Google")
# companies[google_index] = "GOOGLE"

# print(companies)


# # ------------------------------------------------------------
# # Q5: Checking with "in"
# # ------------------------------------------------------------

# print("Google" in it_companies)
# print("Tesla" in it_companies)


# # ------------------------------------------------------------
# # Q6: Removing
# # ------------------------------------------------------------

# companies = it_companies.copy()

# # Remove the first company
# companies.pop(0)

# # Remove the last company
# companies.pop()

# # Remove IBM
# companies.remove("IBM")

# print(companies)


# # ------------------------------------------------------------
# # Q7: Joining and inserting
# # ------------------------------------------------------------

# front_end = ["HTML", "CSS", "JS", "React", "Redux"]
# back_end = ["Node", "Express", "MongoDB"]

# # a) Combine two lists with +
# full_stack = front_end + back_end

# print(len(full_stack))
# print(full_stack)


# # b) Combine lists using .extend()
# full_stack_2 = front_end.copy()
# full_stack_2.extend(back_end)

# print(full_stack_2)


# # c) Insert Python and SQL after Redux
# full_stack = full_stack_2.copy()

# redux_index = full_stack.index("Redux")

# full_stack.insert(redux_index + 1, "Python")
# full_stack.insert(redux_index + 2, "SQL")

# print(full_stack)


# # ------------------------------------------------------------
# # Q8: The copy trap
# # ------------------------------------------------------------

# a = [1, 2, 3]

# b = a
# b.append(4)

# print(a)

# c = a.copy()
# c.append(5)

# print(a)

# # a and b refer to the same list, but c is a separate copy.


# # ------------------------------------------------------------
# # Q9: sort() vs sorted()
# # ------------------------------------------------------------

# nums = [3, 1, 2]

# x = nums.sort()

# print(x)
# print(nums)

# y = sorted([3, 1, 2])

# print(y)

# # x is None because .sort() changes the original list
# # instead of returning a new sorted list.


# # ------------------------------------------------------------
# # Q10: Statistics with a list
# # ------------------------------------------------------------

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sorted_ages = sorted(ages)

# minimum = min(ages)
# maximum = max(ages)

# # There are 10 values, so take the two middle values
# middle_1 = sorted_ages[len(sorted_ages) // 2 - 1]
# middle_2 = sorted_ages[len(sorted_ages) // 2]

# median = (middle_1 + middle_2) / 2

# average = sum(ages) / len(ages)
# age_range = maximum - minimum

# min_distance = round(abs(minimum - average), 1)
# max_distance = round(abs(maximum - average), 1)

# print(sorted_ages)
# print(
#     f"min {minimum}, max {maximum}, "
#     f"median {median}, average {average}, range {age_range}"
# )
# print(min_distance, "and", max_distance)


# # ------------------------------------------------------------
# # Q11: Unpacking with *
# # ------------------------------------------------------------

# countries = [
#     "China", "Russia", "USA",
#     "Finland", "Sweden", "Norway", "Denmark"
# ]

# country1, country2, country3, *scandic = countries

# print(country1)
# print(country2)
# print(country3)
# print(scandic)


# # ------------------------------------------------------------
# # Q12: Middle and halves
# # ------------------------------------------------------------

# middle_index = len(countries) // 2

# middle_country = countries[middle_index]

# first_half_size = (len(countries) + 1) // 2

# first_half = countries[:first_half_size]
# second_half = countries[first_half_size:]

# print(middle_country)
# print(first_half)
# print(second_half)


# # Q10: Statistics

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# # 1. Find the sorted list
# storted_age=sorted(ages)
# print(storted_age)
# # 2. Find the minimum
# min=min(ages)
# print(min)

# # 3. Find the maximum
# max=max(ages)
# print(max)

# # 4. Find the median

# median= storted_age[len(storted_age)//2-1]
# # Remember: there are 10 numbers, so use the TWO middle numbers.


# # 5. Find the average
# average= sum(ages)/len(ages)


# # 6. Find the range
# range=max-min

# # 7. Find the distance between min and average
# disten_min=round(abs(average-min))
# disten_max=round(abs(average-max))


#    and max and average.

#    Round both to 1 decimal place.


it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print:

# The length of the list

# print(len(it_companies))

# # The first company
# print(it_companies[0])
# # The middle company
# # mideel=it_companies[len(it_companies)//2]
# print(it_companies[len(it_companies)//2])

# # The last company
# print(it_companies[-1])


# Next question — Q2

# Using the same it_companies list:


# Get the first 3 companies
# print(it_companies[:3])
# # Get the last 3 companies
# print(it_companies[-3:])

# # Get the middle company

# print(it_companies[len(it_companies)//2])


# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# My_all_companies=it_companies[::-1]
# print(My_all_companies)


# my_compine=it_companies.copy()
# my_compine.reverse()
# print(my_compine)
# print(it_companies)


# Q4 — Add, Insert, Change

# Using a fresh copy of it_companies:

# Add "Netflix" to the end.
my_copy_past=it_companies.copy()
# my_copy_past.append('Netflix')

# my_copy_past.insert(len(my_copy_past)//2, "Tesla")
# print(my_copy_past)
# my_copy_past.insert(2,'"Tesla"')
# print(my_copy_past)
# it_companies[it_companies.index("Google")] = "GOOGLE"
# print(it_companies)


# Q5 — Check membership

# Using it_companies, check whether:


# # "Google" is in the list.
# print('google' in it_companies)

# # "Tesla" is in the list.
# print('Tesla' in my_copy_past)


# # Q6 — Remove items

# # Starting with a fresh copy of it_companies:
# my_copy=it_companies.copy()

# # Remove the first company.
# my_copy.pop(0)
# print(my_copy)
# # Remove the last company.
# my_copy.pop()
# print(my_copy)

# # Remove "IBM".
# my_copy.remove('IBM')
# print(my_copy)


# Q7 — Combine Lists

# Using:


# Do three things:

# A. Combine them using + and print the new list and its length.
# concted=front_end+back_end
# print(concted)

# # B. Combine them using .extend() and print the result.
# front_end.extend(back_end)
# print(front_end)

# # C. Make a copy of the combined list and insert "Python" and "SQL" immediately after "Redux"
# my_copy_2=concted.copy()
# my_copy_2.insert(5, "Python")
# my_copy_2.insert(6, "SQL")
# print(my_copy_2)


# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# c = a.copy()
# c.append(5)
# print(a)


nums = [3, 1, 2]

x = nums.sort()
print(x)
print(nums)

y = sorted([3, 1, 2])
print(y)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_sorted = sorted(ages)

minimum = min(ages)
maximum = max(ages)

median = (ages_sorted[4] + ages_sorted[5]) / 2

average = sum(ages) / len(ages)

age_range = maximum - minimum

distance_min = abs(minimum - average)
distance_max = abs(maximum - average)

print(ages_sorted)
print(minimum)
print(maximum)
print(median)
print(average)
print(age_range)
print(round(distance_min, 1))
print(round(distance_max, 1))


countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
p,o,i,*s= countries
print(p)

# اكتب الحل


countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]

# # اكتب الحل هنااطبع الدولة الموجودة في المنتصف.

my_copy=countries.copy()

middle = len(my_copy) // 2
first_half = my_copy[:middle + 1]
second_half = my_copy[middle + 1:]

print(first_half)
print(second_half)
# إذا كان العدد فرديًا، النصف الأول يأخذ عنصرًا إضافيًا.
