#!/usr/bin/env python3
# File: ex_13_cone.py
# Brief: Calcul du volume d’un cône
# Author: Nicolas Reymond
# version:1.2
# Date: 27/08/2024

import math

# Saisie du rayon et de la hauteur avec valeurs par défaut
rayon = float(input("Entrez le rayon du cône (r) en [m] [valeur par défaut 5] : ") or 5)

# Calculer la surface et du volume du cône
def calcule(rayon):
    """Calcule de la surface selon le <rayon>"""
    surface = 4 * math.pi * rayon**2
    volume = surface * (rayon/3) 
    return surface, volume 

# Calculs et affichage des résultats
surface, volume = calcule(rayon)
print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}")

