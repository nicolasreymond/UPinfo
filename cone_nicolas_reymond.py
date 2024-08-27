import math

# Saisie du rayon et de la hauteur avec valeurs par défaut
rayon = float(input("Entrez le rayon du cône (r) [valeur par défaut 5] : ") or 5)
hauteur = float(input("Entrez la hauteur du cône (h) [valeur par défaut 10] : ") or 10)

# Calcul du volume du cône
volume = (1/3) * math.pi * rayon**2 * hauteur

# Affichage du résultat
print(f"Le volume du cône est de {volume:.2f} unités cubiques.")
