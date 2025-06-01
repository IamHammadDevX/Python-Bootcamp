# Leap Year is divisible by 4 with 0 remainder Except divisible by 100 and unless divisible by 400
year = int(input("Enter year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year!")
        else:
            print(f"{year} is not a Leap Year!")
    else:
        print(f"{year} is a Leap Year!")
else:
    print(f"{year} is not a Leap Year!")