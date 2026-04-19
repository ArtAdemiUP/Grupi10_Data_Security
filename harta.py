import random
import string
import os

def krijo_harten(fjalet):
    """Lidhim çdo shkronjë me pozicionet e fjalëve në libër."""
    harta = {}
    for i, fjala in enumerate(fjalet):
        shkronja = fjala[0].lower()
        if shkronja not in harta:
            harta[shkronja] = []
        harta[shkronja].append(i + 1)
    return harta
