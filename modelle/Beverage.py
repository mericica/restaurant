from modelle.Dish import Dish

class Beverage(Dish):
    def __init__(self, id , name, price, alcohol_content, portion_size=350):
        self.alcohol_content = alcohol_content
        Dish.__init__(self, id, name, price, portion_size)