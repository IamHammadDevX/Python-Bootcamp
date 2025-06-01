# tip calculator
print("WELCOME TO THE TIP CALCULATOR!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? i.g 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))
tipPercent = tip / 100
totalTipAmount = bill * tipPercent
totalBill = bill + totalTipAmount
billPerPeople = totalBill / persons
# finalAmount = round(billPerPeople, 2)
finalAmount = "{:.3f}".format(billPerPeople)
print(f"Each Person should pay: ${finalAmount}")