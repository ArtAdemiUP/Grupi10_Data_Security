def main():
    fajlli_librit = "libri.txt"
    fjalet = ngarko_dhe_pastro_librin(fajlli_librit)
    harta = krijo_harten(fjalet)

    print("=== PROJEKTI: BEALE CIPHER ===")

    while True:
        print("\nZgjidhni: 1 (Enkripto), 2 (Dekripto), 3 (Dil)")
        zgjedhja = input("> ")

        if zgjedhja == "1":
            teksti = input("Shkruaj mesazhin: ")
            shifra = enkripto(teksti, harta)
            print(f"Mesazhi i koduar: {shifra}")
        elif zgjedhja == "2":
            kodi = input("Jep numrat (te ndare me presje): ")
            try:
                origjinali = dekripto(kodi, fjalet)
                print(f"Mesazhi i zbuluar: {origjinali}")
            except:
                print("Gabim ne formatin e numrave!")
        elif zgjedhja == "3":
            break


if __name__ == "__main__":
    main()
