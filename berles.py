class Berles:
    def __init__(self, auto, datum: str):
        self.auto = auto
        self.datum = datum  # Pl. "2025-05-25"

    def info(self):
        return f"{self.auto.rendszam} - {self.auto.tipus} - Dátum: {self.datum} - Ár: {self.auto.berleti_dij} Ft"