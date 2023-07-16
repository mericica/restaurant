from repository import *
from modelle import *
from controller import *
def fields():
    field1 = input("ID:")
    field2 = input("name:")
    field3 = input("Price:")
    field4 = input("Preparation time:")
    Liste = [field1, field2, field3, field4]
    return Liste
def fields2():
    field1 = input("Geben sie den ID ein:")
    field2 = input("Geben sie den name ein:")
    field3 = input("Geben sie den price ein:")
    field4 = input("Geben sie den alcohol_content ein:")
    Liste = [field1, field2, field3, field4]
    return Liste
def gericht_hinzufugen():
    print("Wahlen sie, was sie hinfugen wollen: \n"
          "1. Gekochtes dish\n"
          "2. Beverage")
def gericht_anzeigen():
    print("What do you wish to see?: \n"
          "a. List of dishes \n"
          "b. List of beverages")
def gericht_aktualisieren():
    print("What do you wish to update?: \n"
          "a. Dish \n"
          "b. Beverage")
def neue_daten_gericht(dish):
    dish.name = input("New name:")
    dish.price = input("New price:")
    dish.prep_time = input("New preparation time:")
    dish.portion_size = dish.portion_size
    Liste = [dish.name, dish.price, dish.prep_time, dish.portion_size]
    return Liste
def neue_daten_getrank(beverage):
    beverage.name = input("New name:")
    beverage.price = input("New price:")
    beverage.alcohol_content = input("New alcohol content:")
    beverage.portion_size = beverage.portion_size
    Liste = [beverage.name, beverage.price, beverage.alcohol_content, beverage.portion_size]
    return Liste
def gericht_loschen():
    print("What do you wish to delete?: \n"
          "a. Dish \n"
          "b. Beverage ")

def menu_auswahl():
    print("""Choose a subprogram: \n
           1. Add a new dish
           2. Show a certain dish with its attributes
           3. Change a dish
           4. Delete a dish
    
           5. Add a new customer
           6. Show a certain customer with its details
           7. Change something about a customer
           8. Delete a customer
    
           9. Make and order
    
          """)
