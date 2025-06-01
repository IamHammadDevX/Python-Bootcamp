import random

nameStr = input("Enter names: ")

names = nameStr.split(", ")

totalPersons = len(names)
randChoice = random.randint(0, totalPersons-1)
perWhoPay = names[randChoice]

print(perWhoPay + " Will Pay for meal today!")