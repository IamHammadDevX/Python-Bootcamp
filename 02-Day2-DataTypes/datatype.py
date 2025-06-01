#DAY - 2: DATA TYPES
# PRIMITIVE DT
# string
print("HELLO"[3])
print("123" + "456")

# int
num = 23
print(num)
print(123+456)

# float
print(435.45)

# Boolean
check = False
print(check)

# typo errors
# print(len(345))
# type check
# chrCount = str(len(input("Enter Name: ")))
# # len() calc the int
# print("You name is containing " + chrCount + " letters!")

# print(type(chrCount))

print(100 + float("88.76"))

# Challenge add two num i.g: i/p => 39 = 3 + 9 =>  o/p: 12
ipTwoNum = input("Enter Two numbers i.g 89,12,34: ")
print(type(ipTwoNum))
print("Sum of " + ipTwoNum[0] + " + " + ipTwoNum[1] + " is: " + str(int(ipTwoNum[0])+int(ipTwoNum[1])))

# Mathematical Operators PEMDASLR
# priority
# (), **, */, +-
2 + 3
2 * 3
2 - 3
print(6/2)
print(2**5)
print(3 * 3 + 3 / 3 - 3)

# Number Manipulation
print(round(3.464644645, 3))
print(round(8 / 3, 2))
print(int(8 / 3))
# best approach
print(8 // 3)

# f-String
score = 10
height = 1.8
isWin = True

print(f"your score is {score} and height: {height} and you win {isWin}")