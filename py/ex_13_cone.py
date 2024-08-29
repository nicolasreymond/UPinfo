"""
Exercice 13
Program to calculate the volume (V) of a cone.
The formula used is: V = (pi * radius^2 * height) / 3
The user needs to input the radius (r) and height (h) of the cone.
"""

# File: ex_13_cone.py
# Brief: Calcul du volume d’un cône
# Author: Nicolas Reymond
# version:1.3
# Date: 27/08/2024

from math import pi

# Get the cone's radius and height
radius = float(input("Enter radius (r) in [m] : "))
height = float(input("Enter height (h) in [m] : "))

# Calculate and print the volume"
volume = pi * radius ** 2 * height / 3
print(f"Le volume du cône est de {volume}m3.")