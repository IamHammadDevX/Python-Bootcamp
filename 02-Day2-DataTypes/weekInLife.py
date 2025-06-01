# Weeks left in life before 90 years old challenge
age = int(input("Enter Age: "))
yearsRem = 90 - age
daysRem = yearsRem * 356
weeksRem = yearsRem * 52
monthRem = yearsRem * 12

print(f"You have days {daysRem}, weeks {weeksRem}, and months {monthRem} left to reachout 90 years old!")