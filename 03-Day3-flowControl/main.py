print("DAY - 3 Topic: CONTROL FLOW & LOGICAL OPERATORS")

height = int(input("Enter your height in cm? "))

if height >= 120:
    print("You can ride rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Ticke rate is 5$ Pay it!")
    elif age >= 12 and age <= 18:
        print("Ticket rate is 7$ Pay it!")
    else:
        print("Ticket rate is 12$ Pay it!")
else:
    print("You can't ride rollercoaster bcz your height not met the condition")

# EVEN ODD CHALLENGE
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even!")
else:
    print("Odd")