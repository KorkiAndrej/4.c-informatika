class Ucenik:
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []

    def dodaj_ocjenu(self, ocjena):
            self.ocjene.append(ocjena)
    
    def izracunaj_prosjek(self):
        if len(self.ocjene) == 0:
            return 0.0
        else:
            return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        prosjek = self.izracunaj_prosjek()
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        print(f"Ocjene: {self.ocjene}")
        print(f"Prosjek ocjena: {round(prosjek, 2)}")
        print("-" * 30)

ucenik1 = Ucenik("Miranda", "Šarenić", "1.b")
ucenik2 = Ucenik("Marko", "Vasilić", "2.a")
ucenik3 = Ucenik("Andrej", "Korelić", "4.c")

ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(4)
ucenik1.dodaj_ocjenu(5)

ucenik2.dodaj_ocjenu(3)
ucenik2.dodaj_ocjenu(4)

ucenik3.dodaj_ocjenu(5)
ucenik3.dodaj_ocjenu(5)
ucenik3.dodaj_ocjenu(5)
ucenik3.dodaj_ocjenu(5)

ucenik1.info()
ucenik2.info()
ucenik3.info()

