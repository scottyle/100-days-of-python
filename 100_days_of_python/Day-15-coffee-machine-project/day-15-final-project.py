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

def check_resources(drink):
    """This function is used to check if there is enough resources to make the drink"""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return False
    return True

def make_drink(drink):
    """This function is used to make the drink"""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

machine_money = 0
coffee_machine_on = True

while coffee_machine_on:
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if customer_input in MENU:
        if check_resources(customer_input):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))*0.25
            dimes = float(input("How many dimes?: ")) * 0.10
            nickles = float(input("How many nickles?: ")) * 0.05
            pennies = float(input("How many pennies?: ")) * 0.01
            total_amount = quarters + dimes + nickles + pennies


            #logic to check if amount put in is > that cost of drink
            if total_amount > MENU[customer_input]["cost"]:
                change = total_amount - MENU[customer_input]["cost"]
                make_drink(customer_input)
                machine_money += MENU[customer_input]["cost"]
                print(f"Here is your ${change:.2f} in change.")
                print(f"Here is your {customer_input}, Enjoy.")
            else:
                print("Sorry, you don't have enough money. Money refunded.")
        else:
            print("Insufficient resources. Please fill the machine again")
            coffee_machine_on = False

    elif customer_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}\nMoney: ${machine_money}" )

    elif customer_input == "off":
        coffee_machine_on = False

    else:
        print("Sorry, I didn't understand that. Please try again.")



