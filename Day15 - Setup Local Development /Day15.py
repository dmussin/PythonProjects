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
# money = 0
# profit = 0
# coffee_on = True
#
# #Function for resources and chosen menu
# def resources_check(resources, drink):
#     if resources['water'] < drink['ingredients']['water']:
#         print("Sorry, there is not enough water")
#         return False
#     elif resources['milk'] < drink['ingredients']['milk']:
#         print("Sorry, there is not enough milk")
#         return False
#     elif resources['coffee'] < drink['ingredients']['coffee']:
#         print("Sorry, there is not enough coffee")
#         return False
#     else:
#         print("All fine all resources filled!")
#         return True
#
# #Function coin sum
# def coin_sum(money):
#     print("Please insert coins.")
#     quarters = float(input("how many quarters?:")) * 0.25
#     dimes = float(input("how many dimes?:")) * 0.10
#     nickles = float(input("how many nickles?:")) * 0.05
#     pennies = float(input("how many pennies?:")) * 0.01
#     total_value = quarters + dimes + nickles + pennies
#     print(round((total_value), 1))
#     return total_value
#
#
# #Function Make coffee for deducting resources
# # def make_coffee():
#
#
#
# #Looping the coffee machine
# while coffee_on:
#
#     asking = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     drink = MENU[asking]
#
#     # TODO Print report
#     if asking == 'report':
#         print(f" Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${money}")
#     elif asking == 'end':
#         print("bye")
#         coffee_on = False
#
#
#     # TODO Check resources sufficient?
#     if resources_check(resources, drink) == True:
#         # TODO Process coins
#         money = coin_sum(money)
#
#     # TODO Check transaction successful
#     if money < drink['cost']:
#         print("Sorry that's not enough money. Money refunded.")
#     elif money > drink['cost']:
#         change = money - drink['cost']
#         print(f"Returning your change: {round(change, 2)}")
#         profit += drink['cost']
#         print(f"Profit is {profit}")
#     else:
#         print("Something went wrong!")
#         coffee_on = False
#
#
#
#     # TODO Make coffie (deducting resources)
#     resources['water'] -= drink['ingredients']['water']
#     resources['milk'] -= drink['ingredients']['milk']
#     resources['coffee'] -= drink['ingredients']['coffee']
#     print(f"Resources left: {resources}")



##############################################



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
coffee_on = True

#Function for resources and chosen menu
def resources_check(order_ingridients):
    is_enough = True
    for item in order_ingridients:
       if order_ingridients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_enough = False
    return is_enough

#Function coin sum
def coin_sum():
    print("Please insert coins.")
    quarters = float(input("how many quarters?:")) * 0.25
    dimes = float(input("how many dimes?:")) * 0.10
    nickles = float(input("how many nickles?:")) * 0.05
    pennies = float(input("how many pennies?:")) * 0.01
    total_value = quarters + dimes + nickles + pennies
    print(round((total_value), 1))
    return total_value


#Function to check transaction successful
def is_transaction_recieved(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Returning your change: ${change}")
        global profit
        profit += drink_cost
        return True
    elif money_recieved <= drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print("Something went wrong!")
        return False



#Function Make coffee for deducting resources
def make_coffee(drink_name, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name} ☕️")


#Looping the coffee machine
while coffee_on:

    asking = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO Print report
    if asking == 'report':
        print(f" Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${money}")
    elif asking == 'end':
        print("bye")
        coffee_on = False
    else:
        drink = MENU[asking]
        # TODO Check resources sufficient?
        if resources_check(drink['ingredients']):
            # TODO Process coins
            money = coin_sum()
            # TODO Check transaction successful
            if is_transaction_recieved(money, drink['cost']):
                # TODO Make coffie (deducting resources)
                make_coffee(asking, drink['ingredients'])



