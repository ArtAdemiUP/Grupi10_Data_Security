import random
import string
import os
def ngarko_dhe_pastro_librin(emri_fajllit):
    """Lexon librin dhe heq shenjat e pikësimit."""
    if not os.path.exists(emri_fajllit):
        with open(emri_fajllit, "w", encoding="utf-8") as f:
            f.write("Siguria e te dhenave eshte nje lende shume interesante. "
                    "Ne po mesojmë se si te kodojme mesazhe sekrete duke perdorur "
                    "metoda te vjetra por efikase si kjo e Beale cipher.")
        print(f"[!] U krijua nje skedar provizor '{emri_fajllit}' per testim.")
          with open(emri_fajllit, 'r', encoding='utf-8') as f:
        teksti = f.read()

    tabela = str.maketrans('', '', string.punctuation)
    fjalet = teksti.translate(tabela).split()
    return fjalet
