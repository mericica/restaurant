from ui import ui
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo

from modelle.Order import Order
from modelle.CookedDish import CookedDish
from modelle.Beverage import Beverage
from modelle.Customer import Customer
class Controller:

    def __init__(self, Kundendatei, Getrankdatei, dishdatei, Orderdatei):
        self.kundendatei = Kundendatei
        self.getrankdatei = Getrankdatei
        self.gerichtdatei = dishdatei
        self.orderdatei = Orderdatei


    """
    adding a dish/ or a beverage to the menu (in the csv file)
    """
    def add_dish(self):
        ui.gericht_hinzufugen()
        n = int(input())
        if n == 1:
            CookedDishRepo1 = CookedDishRepo("dishes.csv")
            disheliste = CookedDishRepo1.load()
            disheliste_id = [objekt.id for objekt in disheliste]
            field1 = ui.fields()
            """
            id must stay unique for all dishes and beverages
            """
            if field1[0] in disheliste_id:
                raise ValueError("ID ist schon benutzt")
            neues_dish = CookedDish(field1[0], field1[1], field1[2], field1[3])
            disheliste.append(neues_dish)
            CookedDishRepo1.save(disheliste)
        if n == 2:
            DrinkRepo1 = DrinkRepo("beverages.csv")
            Getrankeliste = DrinkRepo1.load()
            Getrankeliste_id = [objekt.id for objekt in Getrankeliste]
            field1 = ui.fields2()
            if field1[0] in Getrankeliste_id:
                raise ValueError("ID ist schon benutzt")
            neues_Getrank = Beverage(field1[0], field1[1], field1[2], field1[3])
            Getrankeliste.append(neues_Getrank)
            DrinkRepo1.save(Getrankeliste)



    def show_dish(self):

        ui.gericht_anzeigen()
        n = input()
        if n == "a":
            CookedDishRepo1 = CookedDishRepo("dishes.csv")
            disheliste = CookedDishRepo1.load()
            for dish in disheliste:
                print(dish.id, dish.name, dish.price, dish.prep_time, dish.portion_size)

            while len(disheliste) > 1:
                substring = input("Geben sie den ID des dishes ein:")

                def function(CookedDish):
                    if substring in CookedDish.id:
                        return True
                    else:
                        return False

                disheliste = list(filter(function, disheliste))
                for obj in disheliste:
                    print(obj.name, obj.price, obj.prep_time, obj.portion_size)
            return disheliste[0]
        if n == "b":

            DrinkRepo1 = DrinkRepo("beverages.csv")
            Getrankeliste = DrinkRepo1.load()
            for Beverage in Getrankeliste:
                print(Beverage.id, Beverage.name, Beverage.price, Beverage.alcohol_content, Beverage.portion_size)
            while len(Getrankeliste) > 1:
                substring = input("Geben sie den ID des Getrankes ein:")

                def function(Beverage):
                    if substring in Beverage.id:
                        return True
                    else:
                        return False

                Getrankeliste = list(filter(function, Getrankeliste))
                for obj in Getrankeliste:
                    print(obj.name, obj.price, obj.alcohol_content, obj.portion_size)
            return Getrankeliste[0]



    def update_dish(self):
        ui.gericht_aktualisieren()
        n = input()
        if n == "a":
            CookedDishRepo1 = CookedDishRepo("dishes.csv")
            disheliste = CookedDishRepo1.load()
            Ausgewahlter_dish = self.show_dish()
            for dish in disheliste:
                if dish.id == Ausgewahlter_dish.id:
                    ui.neue_daten_gericht(dish)
            CookedDishRepo1.save(disheliste)
        if n == "b":
            DrinkRepo1 = DrinkRepo("beverages.csv")
            Getrankeliste = DrinkRepo1.load()
            Ausgewahlter_Getrank = self.show_dish()
            for Beverage in Getrankeliste:
                if Beverage.id == Ausgewahlter_Getrank.id:
                    ui.neue_daten_getrank(Beverage)
            DrinkRepo1.save(Getrankeliste)

    def delete_dish(self):
        ui.gericht_loschen()
        n = input()
        if n == "a":
            CookedDishRepo1 = CookedDishRepo("dishes.csv")
            disheliste = CookedDishRepo1.load()
            Ausgewahlter_dish = self.show_dish()

            def loschen(dish):
                if dish.id == Ausgewahlter_dish.id:
                    return False
                else:
                    return True

            disheliste = list(filter(loschen, disheliste))
            CookedDishRepo1.save(disheliste)
        if n == "b":
            DrinkRepo1 = DrinkRepo("beverages.csv")
            Getrankeliste = DrinkRepo1.load()
            Ausgewahlter_Getrank = self.show_dish()

            def loschen(Beverage):
                if Beverage.id == Ausgewahlter_Getrank.id:
                    return False
                else:
                    return True

            Getrankliste = list(filter(loschen, Getrankeliste))
            DrinkRepo1.save(Getrankliste)


    """
    now the same functions for the customers
    """
    def add_customer(self):
        CustomerRepo1 = CustomerRepo("Customer.csv")
        Kundenliste = CustomerRepo1.load()
        Kundenliste_id = [objekt.id for objekt in Kundenliste ]
        field1 = input("Geben sie den ID ein:")
        if field1 in Kundenliste_id:
            raise ValueError("ID ist schon benutzt")
        field3 = input("Geben sie den name ein:")
        field4 =  input("Geben sie die address ein:")
        neuer_Kunde = Customer(field1, field3, field4)
        Kundenliste.append(neuer_Kunde)
        CustomerRepo1.save(Kundenliste)
        return neuer_Kunde


    def show_customer(self):
        CustomerRepo1 = CustomerRepo("Customer.csv")
        Kundenliste = CustomerRepo1.load()
        while len(Kundenliste) > 1:
            substring = input("Geben sie name oder address des Kunden ein:")
            Kundenliste = self.suche(substring, Kundenliste)
            for obj in Kundenliste:
                print(obj.name, obj.address)
        return Kundenliste[0]


    """
    subfunction to find the customer by substring
    """
    def suche(self, substring, Kundenliste):
        def function(Customer):
            if substring.casefold() in Customer.name.casefold() or substring.casefold() in Customer.address.casefold():
                return True
            else:
                return False

        Kundenliste = list(filter(function, Kundenliste))
        return Kundenliste

    def update_customer(self):
        CustomerRepo1 = CustomerRepo("Customer.csv")
        Kundenliste = CustomerRepo1.load()
        Ausgewahlter_Kunde = self.show_customer()
        for Customer in Kundenliste:
            if Customer.id == Ausgewahlter_Kunde.id:
                Customer.name = input("Geben sie den name ein:")
                Customer.address = input("Geben sie die address ein:")
        CustomerRepo1.save(Kundenliste)


    def delete_customer(self):
        CustomerRepo1 = CustomerRepo("Customer.csv")
        Kundenliste = CustomerRepo1.load()
        Ausgewahlter_Kunde = self.show_customer()
        def loschen(Customer):
            if Customer.id == Ausgewahlter_Kunde.id:
                return False
            else:
                return True
        Kundenliste = list(filter(loschen, Kundenliste))
        CustomerRepo1.save(Kundenliste)


    def info_Bestellung(self):
        CustomerRepo1 = CustomerRepo("Customer.csv")
        DrinkRepo1 = DrinkRepo("beverages.csv")
        CookedDishRepo1 = CookedDishRepo("dishes.csv")
        OrderRepo1 = OrderRepo("Ordner.csv")
        Orderliste = OrderRepo1.load()
        dishes_list = CookedDishRepo1.load()
        beverages_list = DrinkRepo1.load()
        print("Drucken sie 1 fur neuer Customer und 2 fur ein Customer der schon existiert")
        n = int(input())
        customer_id = None
        if n == 1:
            customer_id = self.add_customer()
        if n == 2:
            customer_id = self.show_customer()
        getrankeliste = DrinkRepo1.read_file()
        print("Wahlen sie die gewunschte beverages. Um die Speisekarte zu sehen, drucken sie 0.")
        beverages_ids = []
        id = 0
        while True:
            print(getrankeliste)
            id = input()
            if id == "0":
                break
            beverages_ids.append(id)

        print("Wahlen sie das Essen. Um die Order abzuschliessen, drucken sie 0 ")
        disheliste = CookedDishRepo1.read_file()
        dishes_ids = []
        idd = 0
        while True:
            print(disheliste)
            idd = input()
            if idd == "0":
                break
            dishes_ids.append(idd)


        id = input("Die Id der Order ist:")
        new_order = Order(id=id, customer_id=customer_id, dishes_ids=dishes_ids, beverages_ids=beverages_ids)
        new_order.berechnung(dishes_list, beverages_list)
        Orderliste.append(new_order)
        OrderRepo1.save(Orderliste)
        new_order.generierung_Rechnung(dishes_list, beverages_list, Customer)

    def run(self):
        n = int(input("Wahl:"))
        if n == 1:
            self.add_dish()

        if n == 2:
            self.show_dish()

        if n == 3:
            self.update_dish()

        if n == 4:
            self.delete_dish()

        if n == 5:
            self.add_customer()

        if n == 6:
            self.show_customer()

        if n == 7:
            self.update_customer()

        if n == 8:
            self.delete_customer()

        if n == 9:
            self.info_Bestellung()
