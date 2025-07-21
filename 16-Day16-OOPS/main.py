# from turtle import Turtle, Screen
# # --- Turtle graphics section ---
# # timmy = Turtle()
# # timmy.shape("turtle")
# # timmy.color("red", "blue")
# # timmy.forward(100)

# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()

# # --- PrettyTable section ---
# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"  # Align columns to the left
# # Display the table
# print(table)
# from prettytable import PrettyTable

from menu import Menu
from coffee_maker import CoffeeMaker
from monye_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)


