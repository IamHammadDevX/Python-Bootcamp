import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`', ']', '[', '{', '}', '.', '|', '<', '>', '"','?', '/', ':', '+', '-', '_', '=']

print("Welcome to the worlds most trustable Password Generator App")
numLet = int(input("Enter the number of letters: "))
numNums = int(input("Enter the number of Numbers: "))
numSym = int(input("Enter the number of Symbols: "))

# Easy Level
password = ""

for letter in range(1, numLet + 1):
    password += random.choice(letters)
for num in range(1, numNums + 1):
    password += random.choice(numbers)
for symbol in range(1, numSym + 1):
    password += random.choice(symbols)

print(f"The Easy Level password is: {password}")

password_lst = []
for letter in range(1, numLet + 1):
    password_lst.append(random.choice(letters))
for num in range(1, numNums + 1):
    password_lst.append(random.choice(numbers))
for symbol in range(1, numSym + 1):
    # also same addition of strings or rather append method/function
    password_lst += random.choice(symbols)

random.shuffle(password_lst)
pass2 = ""
for char in password_lst:
    pass2 += char



print(f"The Hardest Level strongest password is: {pass2}")