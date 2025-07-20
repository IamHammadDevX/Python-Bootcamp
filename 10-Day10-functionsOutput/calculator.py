


# addition
def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

operations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": division,
    "%": modulus
}


def calculation():
    num1 = float(input("Enter first number: "))
    for operator in operations:
        print(operator)   
    shouldContinue = True

    while shouldContinue:
        operatorSymbol = input("Pick an operatore from line above: ")
        num2 = float(input("Enter next number: "))
        calculationFunction = operations[operatorSymbol]
        result = calculationFunction(num1, num2)

        print(f"{num1} {operatorSymbol} {num2} = {result}")
        if input(f"Type 'y' to continue to calculate with {result}, or type 'n' to start new calculation: ") == "y":
            num1 = result
        else:
            shouldContinue = False
            calculation()   #recursion

calculation()