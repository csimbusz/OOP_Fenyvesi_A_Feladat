from auto import Auto

class Szemelyauto(Auto):
    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft"