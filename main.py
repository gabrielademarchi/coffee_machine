from art import logo
import os

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


def clear():
    return os.system('cls')


def show_report():
    print(
        f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${profit}')


def ask_for_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters ($0.25)?: "))
    dimes = int(input("How many dimes ($0.10)?: "))
    nickles = int(input("How many nickles ($0.05)?: "))
    pennies = int(input("How many pennies ($0.01)?: "))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return round(total, 2)


def get_cost(order):
    print(f'That would be ${MENU[order]["cost"]}')
    return MENU[order]["cost"]


def process_transaction(money, cost, order):
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        change = money - cost
        print(f"Here is ${change} in change.")
        print(f"Here is your {order} ☕. Enjoy!")
        return cost


def make_drink(order):
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]


def check_resources(order):
    for item in MENU[order]["ingredients"]:
        if resources[item] < MENU[order]["ingredients"][item]:
            print(f"​Sorry, there is not enough {item}.")
            break
        else:
            return True


def restock():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    return resources


print(logo)
is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'report':
        show_report()
    elif order == 'off':
        is_on = False
    elif order == 'restock':
        resources = restock()
    else:
        if check_resources(order) == True:
            cost = get_cost(order)
            money = ask_for_money()
            profit += process_transaction(money, cost, order)
            make_drink(order)
