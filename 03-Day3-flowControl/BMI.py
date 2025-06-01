# BMI UPDATED VERSION
height = float(input("Enter Height in meters: "))
weight = int(input("Enter Weight in kg: "))

bmiCalc = weight / height**2
resultBmi = round(bmiCalc, 2)
print("Your Body Mass index is: ", resultBmi)

if resultBmi < 18.5:
    print("You are Underweight!")
elif resultBmi >= 18.5 and resultBmi < 25:
    print("You have Normal weight!")
elif resultBmi >= 25 and resultBmi < 30:
    print("You are Overweight!")
elif resultBmi >= 30 and resultBmi < 35:
    print("You are Obese!")
else:
    print("You are clinically Obese")