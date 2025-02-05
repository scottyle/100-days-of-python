from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
profit_machine = MoneyMachine()

while coffee_machine_on: 
    customer_order = input(f"What would you like {menu.get_items()}: ").lower()

    if customer_order == "off":
        coffee_machine_on = False
    
    elif customer_order == "report":
        coffee_maker.report()
        profit_machine.report()
    
    else:
        drink = menu.find_drink(customer_order)
        if coffee_maker.is_resource_sufficient(drink):
            if profit_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                profit_machine.make_payment(drink.cost)
        else:
            coffee_maker.is_resource_sufficient(drink)



