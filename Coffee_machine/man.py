# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# coins = {
#     "penny"     : 0.01,
#     "nickle"    : 0.05,
#     "dime"      : 0.10,
#     "quarter"   : 0.25
# }
#
# from sys import exit
#
# # TODO 3 - Print report.
#
# def print_report(profit):
#     ''' Print a report of the available items in the inventory'''
#     for item in resources:
#         print(f"{item}    :    {resources[item]}\n")
#
#     print(f"Money    :   {round(profit,2)}")
#
# # TODO 4 - Check resources sufficient?
#
# def check_item_availability(drink):
#     for ingredient in MENU[drink]["ingredients"]:
#         if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
#             print(f"Sorry, There is not enough {ingredient}.")
#             return False
#
#         return True
#
# # TODO 5 - Process coins
#
# def get_coins():
#     pennies = int(input("Please insert pennies:\n"))
#     nickles = int(input("Please insert nickles:\n"))
#     dimes = int(input("Please insert dimes:\n"))
#     quarters = int(input("Please insert quarters:\n"))
#     total = (pennies * coins["penny"]) + (nickles * coins["nickle"]) + (dimes * coins["dime"]) +(quarters * coins["quarter"])
#     return total
#
# # TODO 6 - Check transaction successful?
# # TODO 7 - Make Coffee.
# def deduct_from_stock(ingredient, amount):
#     resources[ingredient] -= amount
#
# def prepare_drink(drink):
#     for ingredient in MENU[drink]["ingredients"]:
#         deduct_from_stock(ingredient,MENU[drink]["ingredients"][ingredient])
#     return f"“Here is your {drink}. Enjoy!”"
#
# # TODO 1 - Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# profit = 0
# cont = True
# while cont:
#     order = input("What would you like? (espresso/latte/cappuccino)\n").lower()
#     go_ahead = False
#
#     while not go_ahead:
#         if order == "espresso" or order == "latte" or order == "cappuccino":
#             go_ahead = True
#         elif order == "report":
#             print_report(profit)
#             order = input("What would you like? (espresso/latte/cappuccino)\n").lower()
#         elif order == "off":
#             cont = False
#             exit()
#         else:
#             order = input("The only beverages available are (espresso/latte/cappuccino)\n").lower()
#
#     if check_item_availability(order):
#         price = MENU[order]["cost"]
#         money_received = get_coins()
#         change = money_received - price
#         if change >= 0:
#             if change > 0:
#                 print(f"Here is ${round(change,2)} dollars change.\n")
#             profit += price
#             print(prepare_drink(order))
#         else:
#             print("Sorry that's not enough money. Money refunded\n")
#
#
# # TODO 2 - Turn off the Coffee Machine by entering “off” to the prompt.
#

