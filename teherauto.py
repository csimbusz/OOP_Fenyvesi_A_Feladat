from auto import Auto

class Teherauto(Auto):
    def info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft"