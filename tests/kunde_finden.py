from modelle.Customer import Customer
from repository.CustomerRepo import CustomerRepo
from controller.controller import Controller
kunde1 = Customer(id=1, name="Flavius", address="strada sttrazilor")
kunde2 = Customer(id=2, name="Adina", address="strada nucului")
liste_kunden = [kunde1, kunde2]
repo = CustomerRepo("Customer.csv")
repo.save([kunde1, kunde2])


def finde_nach_name():
    controller1 = Controller("Customer.csv", "dishes.csv", "beverages.csv", "Order.csv")
    c1 = controller1.suche("fla", liste_kunden)[0]
    try:
        assert c1 == kunde1
        print("Alles gut")
    except:
        print("Falsch")
finde_nach_name()



def finde_nach_adresse():
    controller1 = Controller("Customer.csv", "dishes.csv", "beverages.csv", "Order.csv")
    c1 = controller1.suche("uc", liste_kunden)[0]
    try:
        assert c1 == kunde2
        print("Alles gut")
    except:
        print("Falsch")
finde_nach_adresse()








