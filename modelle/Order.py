from modelle.Identifizierbar import Identifizierbar
import functools
import datetime
class Order(Identifizierbar):
    def __init__(self, id, customer_id, dishes_ids, beverages_ids, total_cost=0 ):
        self.customer_id = customer_id
        self.dishes_ids = dishes_ids
        self.beverages_ids = beverages_ids
        self.total_cost = total_cost
        Identifizierbar.__init__(self, id)

    def __eq__(self, other):
        return (self.id == other.id and self.customer_id == other.customer_id and self.dishes_ids == other.dishes_ids and self.beverages_ids == other.beverages_ids and self.total_cost == other.total_cost)

    def __str__(self):
        return f"id:{self.id}, Customer:{self.customer_id}, dish:{self.dishes_ids}, Beverage:{self.beverages_ids}"

    def berechnung(self, dishe, beverages):
        def function(id):
            for dish in dishe:
                if dish.id == id:
                    return float(dish.price)

        dishes_cost = list(map(function, self.dishes_ids))

        def function2(id):
            for Beverage in beverages:
                if Beverage.id == id:
                    return float(Beverage.price)
        beverages_cost = list(map(function2, self.beverages_ids))

        total = beverages_cost + dishes_cost
        self.total_cost = functools.reduce(lambda a, b: a + b, total)

    def __generierungRechnung(self, dishes, beverages):
        def function(id):
            for dish in dishes:
                if dish.id == id:
                    return f"{dish.price}: {dish.name}"
        gerichte_mit_preis = "\n".join(list(map(function, self.dishes_ids)))
        def function2(id):
            for Beverage in beverages:
                if Beverage.id == id:
                    return f"{Beverage.price}: {Beverage.name}"
        getranke_mit_preis = "\n". join(list(map(function2, self.beverages_ids)))

        def function3(id):
            for dish in dishes:
                if dish.id == id:
                    return float(dish.prep_time)

        delivery_time = sum(list(map(function3, self.dishes_ids)))
        time = datetime.datetime.now()
        delivered = (time + datetime.timedelta(minutes = delivery_time)).strftime("%d.%m.%Y %H.%M")
        urhzeit_print = time.strftime("%d.%m.%Y %H.%M")
        return f"""
         !!!!!!!!!!!!!!!!!!!!Bill!!!!!!!!!!!!!!!
         Time of order: {urhzeit_print}
         ID of order: {self.id}
         Total cost: {self.total_cost}
         Ordered dishes + costs: {gerichte_mit_preis}
         Ordered bevereges + costs: {getranke_mit_preis}
         Time: {time.strftime("%d.%m.%Y %H.%M")}
         Delivery time: {delivered}
        """
    def generierung_Rechnung(self, dishes, beverages , customer):
        print(self.__generierungRechnung(dishes, beverages, customer))

