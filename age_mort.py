# init var and ask for data (or init with default data)
birth_year = int(input("Saisir l'année de naissance: ") or 1868)
death_year = int(input("Saisir l'année de mort: ") or 1921)
# Calculate death age
death_age = death_year - birth_year
# Print result
print("\ndate de naissance : " + str(birth_year) + "\ndate de mort : " + str(death_year) + "\nage de mort : " + str(death_age))
