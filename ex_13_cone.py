"""
Exercice 13
Programme qui, à partir de la saisie d’un rayon (r) et d’une hauteur (h), calcule le
volume (V) d’un cône droit en utilisant la formule (pi * rayon^2 * hauteur / 3)
"""

# File:    ex_13_cone.py
# Brief:   Calcul du volume d’un cône
# Author:  Nicolas Reymond
# version: 1.0
# Date:    27/08/2024

from math import pi

# Get the cone's radius and height
radius = float(input("Entrez le rayon du cône (r) en [m] : "))
height = float(input("Entrez la hauteur du cône (h) en [m] : "))

# Calculate and print the volume"
volume = pi * radius**2 * height / 3
print(f"Le volume du cône est de {volume:.2f}m³.")