
nekretnine = []


class Nekretnina:
    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izracunaj_cijenu(self):
        return("Ukupna cijena nekretnine iznosi ",self.kvadratura*self.bazna_cijena," Eura")

    def ispisi_info(self):
        cijena = self.izracunaj_cijenu
        return(f"Adresa: {self.adresa}, kvadratura: {self.kvadratura} metara kvadratnih, cijena: {cijena}")
    
class Stan(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, kat, ima_lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.ima_lift = ima_lift
    
    def izracunaj_cijenu(self):
        osnovna_cijena = self.kvadratura * self.bazna_cijena
        
        if self.kat >= 2 and not self.ima_lift:
            return osnovna_cijena * 0.9
        elif self.ima_lift:
            return osnovna_cijena * 1.05
        else: 
            return osnovna_cijena

    def ispisi_info(self):
        cijena = self.izracunaj_cijenu()
        ima_lift = "ima lift" if self.ima_lift else "nema lift"
        print(f"Adresa: {self.adresa}, kvadratura: {self.kvadratura} metara kvadratnih, kat: {self.kat}, {ima_lift}, cijena: {cijena} Eura")

class Kuca(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.povrsina_okucnice = povrsina_okucnice
    
    def izracunaj_cijenu(self):
        return (self.kvadratura * self.bazna_cijena) + (self.povrsina_okucnice * 100)
        
    def ispisi_info(self):
        cijena = self.izracunaj_cijenu()
        print(f"Adresa: {self.adresa}, kvadratura: {self.kvadratura} metara kvadratnih, površina okućnice: {self.povrsina_okucnice} m², cijena: {cijena} Eura")

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
            ima_lift = bool(input("Ima li stan u pitanju lift (True/Flase): "))
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
    if not nekretnine:
        print("Nema nekretnina")
        return
    print("-----------Sve nekretnine------------")
    for nekretnina in nekretnine:
        nekretnina.ispisi_info()
        
def prodaja_nekretnine():
    if not nekretnine:
        print("Nema nekretnina")
        return
        
    adresa = input("Unesite adresu nekretnine: ")
    for nekretnina in nekretnine:
        if nekretnina.adresa == adresa:
            nekretnine.remove(nekretnina)
            print("Nekretnina prodana")
        else:
            print("Nepostojeća nekretnina")

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
            ispis_svih_nekretnina()
                        
        elif izbor == 4:
            prodaja_nekretnine()
        
        elif izbor == 5:
            print("Hvala što ste koristili sustav evidencije autosalona!")
            break
            
        else:
            print("Pogrešan odabir! Molimo odaberite opciju između 1 i 5.")


if __name__ == "__main__":
    main()
