from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#This is a coffee maker program
#I am using this as practice for OOP

cm = CoffeeMaker()
mu = Menu()
mm = MoneyMachine()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/):")
    if choice == "off":
        break
    elif choice == "report":
        print(cm.resources)
    else:
        drink = mu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)