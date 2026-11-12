# My Python exercises


# ---------- Exercise 1: customers total and top customer ----------
def customers_total(orders, prices):
    totals = {}
    for order in orders:
        order_total = prices[order["product"]] * order["quantity"]
        customer = order["customer"]
        if customer not in totals:
            totals[customer] = 0
        totals[customer] += order_total
    return totals


def top_customer(orders, prices):
    totals = customers_total(orders, prices)   # Step 1: total per customer
    best_name = ""
    best_total = 0
    for name in totals:                        # Step 2: find the highest
        if totals[name] > best_total:
            best_name = name
            best_total = totals[name]
    return best_name


# ---------- Exercise 2: low stock names ----------
def low_stock_names(stock):
    low_names = []
    for name in stock:
        if stock[name] < 5:
            low_names.append(name)
    return low_names


# ---------- Exercise 3: total stock ----------
def total_stock(stock):
    total = 0
    for name in stock:
        total += stock[name]
    return total


# ---------- Exercise 4: vowels ----------
def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def find_vowels(text):
    vowels_found = []
    for letter in text.lower():
        if letter in "aeiou":
            vowels_found.append(letter)
    return vowels_found


# ---------- Exercise 5: palindrome ----------
def is_palindrome(word):          # way A: with a loop
    word = word.lower()
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word == word


def is_palindrome_short(word):    # way B: with the slice
    word = word.lower()
    return word == word[::-1]


# ---------- Exercise 6: turn 100 years old (with Extra 1 and Extra 2) ----------
def age_100_program():
    name = input("Write your name: ")
    age = int(input("Write your age: "))      # int(input(...)), in this order
    years_left = 100 - age
    year_100 = 2026 + years_left
    copies = int(input("How many copies? "))
    message = f"Welcome {name}, you will turn 100 in the year {year_100}\n"
    print(copies * message)                   # \n puts each copy on its own line

    color = input("Write your favorite color: ")
    print(name + " likes " + color)           # joining with +
    print(f"{name} likes {color}")            # joining with an f-string
    print("You are " + str(age))              # str() turns the number into text


# ---------- Tests (they print the answers) ----------
orders = [
    {"customer": "Ali", "product": "apple", "quantity": 2},
    {"customer": "Sara", "product": "banana", "quantity": 3},
    {"customer": "Ali", "product": "orange", "quantity": 1},
    {"customer": "Omar", "product": "apple", "quantity": 4},
    {"customer": "Sara", "product": "apple", "quantity": 2},
]
prices = {"apple": 3, "banana": 2, "orange": 4}
stock = {"apple": 12, "banana": 4, "orange": 9, "mango": 2, "grape": 7}

print(f"Totals: {customers_total(orders, prices)}")        # Ali 10, Sara 12, Omar 12
print(f"Top customer: {top_customer(orders, prices)}")     # Sara
print(f"Low stock: {low_stock_names(stock)}")              # ['banana', 'mango']
print(f"Total stock: {total_stock(stock)}")                # 34
print(f"Vowels: {count_vowels('Python is fun')}")          # 3
print(f"Vowels list: {find_vowels('Hello World')}")        # ['e', 'o', 'o']
print(f"level: {is_palindrome('level')}")                  # True
print(f"python: {is_palindrome('python')}")                # False
print(f"Madam: {is_palindrome_short('Madam')}")            # True

print()
age_100_program()   # this one asks you questions
