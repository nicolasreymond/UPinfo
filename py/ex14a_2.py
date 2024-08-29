#!/usr/bin/env python3
# File: ex_13_cone.py
# Brief: Calcul du volume d’un cône
# Author: Nicolas Reymond
# version:1.2
# Date: 27/08/2024

import math

# Saisie du rayon et de la hauteur avec valeurs par défaut
rayon = float(input("Entrez le rayon du cône (r) en [m] [valeur par défaut 5] : ") or 5)

# Calculer la surface du cône
def calcule_surface(rayon):
    """Calcule de la surface selon le <rayon>"""
    return 4 * math.pi * rayon**2

# Calculer le volume du cône
def calcule_volume(rayon):
    """Calcule du volume selon le <rayon>"""
    surface = calcule_surface(rayon)
    return surface * (rayon/3) 

# Calculs et affichage des résultats
surface = calcule_surface(rayon)
volume = calcule_volume(rayon)
print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}")

