
nekretnine = []


class Nekretnina:
    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izracunaj_cijenu(self):
        print("Ukupna cijena nekretnine iznosi ",self.kvadratura*self.bazna_cijena," Eura")

    def ispisi_info(self):
        print(f"Adresa: {self.adresa}, kvadratura: {self.kvadratura} metara kvadratnih, cijena: {self.izracunaj_cijenu}")
    
class Stan(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, kat, ima_lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.ima_lift = ima_lift
    
    def izracunaj_cijenu(self):
        if self.kat >= 2 and self.ima_lift == False:
            print("Ukupna cijena nekretnine iznosi ",self.kvadratura*self.bazna_cijena*0.9," Eura")
        elif self.ima_lift == True:
            print("Ukupna cijena nekretnine iznosi ",self.kvadratura*self.bazna_cijena*1.05," Eura")
        else: 
            print("Ukupna cijena nekretnine iznosi ",self.kvadratura*self.bazna_cijena," Eura")

    def ispisi_info(self):
        if self.ima_lift == True:
            print(super().ispisi_info())
            print(f"kat: {self.kat}, ima lift")
        if self.ima_lift == False:
            print(super().ispisi_info())
            print(f"kat: {self.kat}, nema lift")

class Kuca(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.povrsina_okucnice = povrsina_okucnice
    
    def izracunaj_cijenu(self):
        print(f"Ukupna cijena nekretnine iznosi ",{self.kvadratura*self.bazna_cijena}+{self.povrsina_okucnice *100}," Eura")
    
    def ispisi_info(self):
        print(super().ispisi_info())
        print(f"površina okućnice: {self.povrsina_okucnice}")
    
def ispisi_izbornik():
        print("------------------------")
        print("1.    Unos stana")
        print("2.     Unos kuće")
        print("3. Ispis svih nekretnina")
        print("4. Prodaja nekretnine ")
        print("5.       Izlaz")
        print("------------------------")

def unos_stana():
    print("Unos stana...")
    adresa = input("Unesi adresu stana: ")
    while True:
        try:
            kvadratura = int(input("Unesite kvadraturu stana: "))
            bazna_cijena = int(input("Unesite baznu cijenu stana: "))
            kat = int(input("Unesite kat stana: "))
            ima_lift = bool("Ima li stan u pitanju lift (True/Flase): ")
            break
        except ValueError:
            print("Pogrešan unos podataka.")
    return Stan(adresa, kvadratura, bazna_cijena, kat, ima_lift)

def unos_kuce():
    print("Unos kuće...")
    adresa = input("Unesi adresu kuće: ")
    while True:
        try:
            kvadratura = int(input("Unesite kvadraturu kuće: "))
            bazna_cijena = int(input("Unesite baznu cijenu kuće: "))
            povrsina_okucnice = int(input("Unesite površinu okućnice: "))
            break
        except ValueError:
            print("Pogrešan unos podataka.")
    return Kuca(adresa, kvadratura, bazna_cijena, povrsina_okucnice)

def ispis_svih_nekretnina():
    for nekretnina in nekretnine:
        if not nekretnine:
            print("Nema nekretnina")
            return None
        else:
            for i in nekretnine:
                return nekretnina.ispisi_info()
        
def prodaja_nekretnine():
    if not nekretnine:
        print("Nema nekretnina")
        return None
    else:
        for nekretnina in nekretnine:
            if nekretnina.lower() == Nekretnina.adresa.lower():
                nekretnine.remove[nekretnina]
                print("Nekretnina uklonjenja iz liste")

def main():
        
    while True:
        ispisi_izbornik()
        
        try:
            izbor = int(input("Odaberite opciju: "))
        except ValueError:
            print("Pogrešan unos! Molimo unesite broj između 1 i 5")
            continue
        
        if izbor == 1:
            novi_stan = unos_stana()
            nekretnine.append(novi_stan)
            print("Stan je dodan")
            
        elif izbor == 2:
            nova_kuca = unos_kuce()
            nekretnine.append(nova_kuca)
            print("Kuća uspješno dodana")  

        elif izbor == 3:
            return ispis_svih_nekretnina()
                        
        elif izbor == 4:
            return prodaja_nekretnine()
        
        elif izbor == 5:
            print("Hvala što ste koristili sustav evidencije autosalona!")
            break
            
        else:
            print("Pogrešan odabir! Molimo odaberite opciju između 1 i 5.")


if __name__ == "__main__":
    main()

