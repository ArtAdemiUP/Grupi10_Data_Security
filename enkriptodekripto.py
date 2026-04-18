def enkripto(mesazhi, harta):
    rezultati = []
    for shkronja in mesazhi.lower():
        if shkronja == " ": continue
        if shkronja in harta:
            rezultati.append(str(random.choice(harta[shkronja])))
        else:
            print(f"X Gabim: Shkronja '{shkronja}' nuk gjendet ne liber!")
    return ", ".join(rezultati)


def dekripto(shifra, fjalet_e_librit):
    indekset = [int(n.strip()) for n in shifra.split(",")]
    mesazhi = ""
    for i in indekset:
        mesazhi += fjalet_e_librit[i - 1][0].lower()
    return mesazhi