#include <iostream>
#include <cmath>

using namespace std;

#define PI 3.14159265359

// Fonction pour calculer le volume d'un cône
double calculerVolumeCone(double r, double h)
{
    return (PI * pow(r, 2.0) * h) / 3.0;
}

int main(void)
{
    double rayon, hauteur;

    // Demande de saisie à l'utilisateur
    cout << "Entrez le rayon du cône (en mètres) : ";
    cin >> rayon;
    cout << "Entrez la hauteur du cône (en mètres) : ";
    cin >> hauteur;

    // Calcul du volume
    double volume = calculerVolumeCone(rayon, hauteur);

    // Affichage du résultat avec les unités
    cout << "Le volume du cône est : " << volume << " m³" << endl;
}
