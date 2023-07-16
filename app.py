from controller.controller import Controller
from ui import ui
def main():
    ui.menu_auswahl()
    while True:
        Controller1 = Controller("Customer.csv", "dishes.csv", "beverages.csv", "Order.csv")

        Controller1.run()

main()