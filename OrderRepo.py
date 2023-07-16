from modelle.Order import Order
from repository.DataRepo import DataRepo
class OrderRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, Liste):
        list_to_string = "\n".join(list(map(lambda el: str(el.id) + ":" + str(el.customer_id) + ":" + str(",".join(el.dishes_ids)) + ":" + str(",".join(el.beverages_ids)) + ":"+ str(el.total_cost), Liste)))
        return list_to_string

    def convert_from_string(self, string):
        neue_liste = []
        if string != "":
            n = string.split("\n")
            neue_liste = list(map(lambda line: Order(line.split(":")[0], line.split(":")[1], list(line.split(":")[2].split(",")), list(line.split(":")[3].split(",")), float(line.split(":")[4])), n))
        return neue_liste