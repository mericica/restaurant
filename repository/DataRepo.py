import csv

f = "dishes.csv"

with open("../Customer.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
with open("../beverages.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
with open("../dishes.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
with open("../Ordner.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)


class DataRepo:
    def __init__(self, datei):
        self.datei = datei


    """
    saves a list of objects in a file
    """
    def save(self, Liste):
        string = self.convert_to_string(Liste)
        self.write_to_file(string)



    """
    reads a list of objects from a file
    """
    def load(self):
        string = self.read_file()
        return self.convert_from_string(string)


    """
    reads the contents of a file and returns it
    """
    def read_file(self):
        with open(self.datei) as f:
            inhalt = f.read()

        return inhalt


    """
    writes a string to a file and overwrites the file
    """
    def write_to_file(self, string):
        with open(self.datei, "w") as f:
            f.write(string)



    """
    receives as argument a list of objects, which need to be converted to a string and later saved to the file.
    """
    def convert_to_string(self, Liste):
        pass



    """
    takes a string and converts it to a list of objects previously read from a file.
    """
    def convert_from_string(self, string):
        pass