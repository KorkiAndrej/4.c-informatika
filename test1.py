class Vozilo():
    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena
    def info(self):
        print(f"Marka: {self.marka}, model: {self.model}, godina proizvodnje: {self.godina_proizvodnje}, cijena: {self.cijena})