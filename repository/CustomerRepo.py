from modelle.Customer import Customer
from repository.DataRepo import DataRepo
class CustomerRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, Liste):
        list_to_string = "\n".join(list(map(lambda el: str(el.id) + "," + str(el.name) + "," + str(el.address) , Liste)))
        return list_to_string

    def convert_from_string(self, string):
        neue_liste = []
        if string != "":
            n = string.split("\n")
            neue_liste = list(map(lambda line: Customer(line.split(",")[0], line.split(",")[1], line.split(",")[2]), n))
        return neue_liste