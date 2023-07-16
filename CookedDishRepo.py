from modelle.CookedDish import CookedDish
from repository.DataRepo import DataRepo
class CookedDishRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, Liste):
        list_to_string = "\n".join(list(map(lambda el: str(el.id) + "," + str(el.name) + "," + str(el.price) + "," + str(el.prep_time) + "," + str(el.portion_size), Liste)))
        return list_to_string

    def convert_from_string(self, string):
        new_list = []
        if string != "":
            n = string.split("\n")
            new_list = list(map(lambda line: CookedDish(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4]), n))
        return new_list