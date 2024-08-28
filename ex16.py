import math


def menu():
    print("choose an option")
    print(" 1. Calculate the volume of a cone")
    print(" 2. Calculate the surface and the volume of a sphere")
    print(" 3. Exit")
    choise = input("> ")
    return choise

def calcule_cone():
    radius = float(input("Enter radius (r) in [m] : "))
    height = float(input("Enter height (h) in [m] : "))
    volume = math.pi * radius**2 * height / 3
    print(f"Le volume du cône est de {volume:.2f}m3.\n\n")
    return

def calcule_sphere():
    """Calculate and print <rayon>"""
    radius = float(input("Enter radius (r) in [m] : "))
    surface = 4 * math.pi * radius**2
    volume = surface * (radius/3) 
    print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}\n\n")
    return

choise = 0
while(choise != 3):
    try:
        choise = int(menu())
    except:
        print("Invalid input")
        choise = int(menu())

    if choise == 1:
        calcule_cone() 

    elif choise == 2:
        calcule_sphere() 

    elif choise != 3:
        print("Invalid input")


print("So long :)") 