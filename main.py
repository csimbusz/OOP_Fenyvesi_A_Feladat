from autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("UniCar")
    kolcsonzo.feltolt_alapadatok()

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Választás: ")

        if valasztas == "1":
            rendszam = input("Rendszám: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            print(kolcsonzo.berel(rendszam, datum))
        elif valasztas == "2":
            rendszam = input("Rendszám: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            print(kolcsonzo.lemond(rendszam, datum))
        elif valasztas == "3":
            print(kolcsonzo.listaz_berlesek())
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()