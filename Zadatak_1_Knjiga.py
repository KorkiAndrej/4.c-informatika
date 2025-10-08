class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja

    def __str__(self):
        return f"'{self.naslov}' by {self.autor} ({self.godina_izdanja})"

knjiga1 = Knjiga("Gospodar prstenova", "J.R.R. Tolkien", 1954)
print(knjiga1)

