from modelle.Identifizierbar import Identifizierbar
class Customer(Identifizierbar):
    def __init__(self, id, name, address):
        self.name = name
        self.address = address
        Identifizierbar.__init__(self, id)

