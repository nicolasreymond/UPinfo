#!/usr/bin/env python3
# File: ex_13_cone.py
# Brief: Calcul du volume d’un cône
# Author: Nicolas Reymond
# version:1.2
# Date: 27/08/2024

# Import
import math

# Saisie du rayon et de la hauteur avec valeurs par défaut
rayon = float(input("Entrez le rayon du cône (r) en [m] [valeur par défaut 5] : ") or 5)
hauteur = float(input("Entrez la hauteur du cône (h) en [m] [valeur par défaut 10] : ") or 10)

# Calcule surface
surface = 4 * math.pi * rayon**2

# Calcul volume
volume = surface * (rayon/3)

# Show result
print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}")