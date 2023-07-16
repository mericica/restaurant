from modelle.Beverage import Beverage
from repository.DataRepo import DataRepo
class DrinkRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, Liste):
        list_to_string = "\n".join(list(map(lambda el: str(el.id) + "," + str(el.name) + "," + str(el.price) + "," + str(el.alcohol_content) + "," + str(el.portion_size), Liste)))
        return list_to_string

    def convert_from_string(self, string):
        neue_liste = []
        if string != "":
            n = string.split("\n")
            neue_liste = list(map(lambda line: Beverage(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4]), n))
        return neue_liste