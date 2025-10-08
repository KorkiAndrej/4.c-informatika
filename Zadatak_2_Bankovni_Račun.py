class BankovniRacun:
    def __init__(self, broj_racuna, vlasnik, stanje=0):
        self.broj_racuna = broj_racuna
        self.vlasnik = vlasnik
        self.stanje = stanje
    def uplatiti(self, iznos):
        if iznos > 0:
            self.stanje += iznos
            print(f'Uplata od {iznos} je uspješna. Novo stanje: {self.stanje}')
        else:
            print('Iznos uplate mora biti pozitivan.')
    def isplatiti(self, iznos):
        if 0 < iznos <= self.stanje:
            self.stanje -= iznos
            print(f'Isplata od {iznos} je uspješna. Novo stanje: {self.stanje}')
        else:
            print('Nedovoljno sredstava ili neispravan iznos isplate.')
    def prikaz_stanja(self):
        print(f'Stanje na računu {self.broj_racuna} vlasnika {self.vlasnik} je {self.stanje}.')

# Primjer korištenja klase BankovniRacun
if __name__ == "__main__":
    racun = BankovniRacun('HR1234567890123456789', 'Ivan Horvat', 1000)
    racun.prikaz_stanja()
    racun.uplatiti(500)
    racun.isplatiti(200)
    racun.isplatiti(2000)  # Pokušaj isplate većeg iznosa nego što je stanje
    racun.prikaz_stanja()