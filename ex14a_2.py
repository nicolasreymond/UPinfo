#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Created By  : Nicolas Reymond
# Created Date: 27/08/2024
# version ='2.0'
# ---------------------------------------------------------------------------

import math

# Saisie du rayon et de la hauteur avec valeurs par défaut
rayon = float(input("Entrez le rayon du cône (r) en [m] [valeur par défaut 5] : ") or 5)

# Calculer la surface du cône
def calcule_surface(rayon):
    return 4 * math.pi * rayon**2

# Calculer le volume du cône
def calcule_volume(rayon):
    surface = calcule_surface(rayon)
    return surface * (rayon/3) 

# Calculs
surface = calcule_surface(rayon)
volume = calcule_volume(rayon)

# Affichage des résultats
print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}")
