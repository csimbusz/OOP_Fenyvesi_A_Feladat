from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def berel(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Nincs ilyen autó!"
        if any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek):
            return "Ez az autó ezen a napon már ki van bérelve!"
        berles = Berles(auto, datum)
        self.berlesek.append(berles)
        return f"Bérlés sikeres! Ár: {auto.berleti_dij} Ft"

    def lemond(self, rendszam, datum):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                self.berlesek.remove(b)
                return "Bérlés lemondva."
        return "Nincs ilyen bérlés."

    def listaz_berlesek(self):
        if not self.berlesek:
            return "Nincs aktív bérlés."
        return "\n".join(b.info() for b in self.berlesek)

    def feltolt_alapadatok(self):
        self.hozzaad_auto(Szemelyauto("ABC-123", "Toyota Corolla", 10000))
        self.hozzaad_auto(Szemelyauto("XYZ-789", "Honda Civic", 11000))
        self.hozzaad_auto(Teherauto("TGH-456", "Ford Transit", 15000))
        self.berlesek.append(Berles(self.autok[0], "2025-05-25"))
        self.berlesek.append(Berles(self.autok[1], "2025-05-26"))
        self.berlesek.append(Berles(self.autok[2], "2025-05-27"))
        self.berlesek.append(Berles(self.autok[0], "2025-05-28"))