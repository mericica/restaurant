
from modelle.Order import Order
from modelle.Customer import Customer
from modelle.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from modelle.Beverage import Beverage

order = Order(id="1", customer_id="2", dishes_ids=["1", "2", "3"], beverages_ids=["4", "5", "6"], total_cost=0)
customer_repo = CustomerRepo("Customer.csv")



Customer = Customer(id="1", name="Ana", address="Bucuresti")
customer_repo.save([Customer])

CookedDishRepo1 = CookedDishRepo("dishes.csv")
dishes = [CookedDish(id="1", name="Sushi" , price=60 , prep_time="55" , portion_size="350")]
CookedDishRepo1.save(dishes)
dishes_list = CookedDishRepo1.load()
DrinkRepo1 = DrinkRepo("beverages.csv")
beverages = [Beverage(id="3", name="Cola", price=4, alcohol_content="0", portion_size="350")]
DrinkRepo1.save(beverages)
beverages_list = DrinkRepo1.load()


"""
Generation of the string representing the invoice
"""

def string_generieren():

    order2 = Order(id="1", customer_id="5", dishes_ids=["1"], beverages_ids=["3"], total_cost=[60, 4])
    field2 = order2.generierung_Rechnung(dishes_list, beverages_list, Customer)

    result = """
    !!!!!!!!!!!!!!!!!!!!Rechnung!!!!!!!!!!!!!!!
         Zeit der Order ist: 12.01.2023 18.54
         ID der Order ist: 1
         Die total_cost sind: [60, 4]
         Die dishe und Preise sind: 60: Sushi
         Die beverages und Preise sind: 4: Cola
         Kundeninformationen: ('Ana', 'Bucuresti')
         Uhrzeit: 12.01.2023 18.54
         Lieferzeit 12.01.2023 19.49
    
    """

    try:
        assert field2 == result
    except AssertionError:
        print("Alles gut")
    else:
        print("Schlecht")



string_generieren()

"""
Conversion and saving of an order instance in a file
"""

def bestellungsinstanz():
    repo = OrderRepo("Order.csv")

    repo.save([order])
    order2 = repo.load()[0]

    try:
        assert order == order2
        print("Test passed")
    except:
        print("Converting and saving an order instance to a file fails")

bestellungsinstanz()


"""
Reading and converting an order instance from a file
"""
def test():
    repo2 = OrderRepo("Order.csv")
    repo2.save([order])
    inhalt = repo2.read_file().strip()
    string = "1:2:1,2,3:4,5,6:0"
   # print(inhalt)
    try:
        assert inhalt == string
        print("Test passed")
    except:
        print("Reading and converting an order instance from a file fails")

test()




