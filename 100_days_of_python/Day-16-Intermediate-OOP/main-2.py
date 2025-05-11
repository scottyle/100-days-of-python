from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker() 
menu = Menu()
money_machine = MoneyMachine()

coffee_machine_on = True 

while coffee_machine_on: 
    order = input(f"What would you like? {menu.get_items()} ").lower()
    if order == "off": 
        coffee_machine_on = False 
    elif order == "report":
        coffee_machine.report() 
        money_machine.report() 
    elif menu.find_drink(order):
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
