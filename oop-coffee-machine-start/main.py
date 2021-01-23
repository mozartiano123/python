from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from sys import exit

#instantiating objects

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

#variable to control the loop.
is_on = True

while is_on:
# # TODO 1 - Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    options = menu.get_items()
    order = input(f"What would you like? ({options}): \n").lower()
# # TODO 2 - Turn off the Coffee Machine by entering “off” to the prompt.
    if order == 'off':
        is_on = False
        exit()
    elif order == 'report':
# # TODO 3 - Print report.
        coffee_machine.report()
        money.report()
    elif (order == 'espresso') or (order == 'latte') or (order == 'cappuccino'):
# # TODO 4 - Check resources sufficient?
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
# # TODO 5 - Process coins
# # TODO 6 - Check transaction successful?
            if money.make_payment(drink.cost):
# # TODO 7 - Make Coffee.
                coffee_machine.make_coffee(drink)