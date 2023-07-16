from modelle.Identifizierbar import Identifizierbar
class Dish(Identifizierbar):
    def __init__(self, id, name, price, portion_size=350):
        self.name = name
        self.portion_size = portion_size
        self.price = price
        Identifizierbar.__init__(self, id)