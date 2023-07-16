from modelle.Dish import Dish
class CookedDish(Dish):
    def __init__(self, id , name, price, prep_time, portion_size=350):
        self.prep_time = prep_time
        Dish.__init__(self, id, name, price, portion_size)

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name)

    def __str__(self):
        return f"{self.id} hat {type(self.id)}, {self.name}, hat {type(self.name)}, {self.price} hat {type(self.price)}"