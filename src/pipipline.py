# pipeline.py

from extract import extract_data
from transform import transform_data
from load import load_data
import sys 

def main():
    try:
        # Etape 1: Exctraction
        print("\nDémarrage de l'extraction...")
        extract_data()
        print("Extraction réussie ! Fichier CSV brut créé.")

        # Etape 2: Transformation
        print("\nNettoyage de données...")
        transform_data()
        print("Transformation réussie ! Données prêtes pour SQLite.")

        # Etape 3: Chargement
        print("\nChargement des données...")
        load_data()
        print("Chargement terminé ! Base de données mise à jour.\n")

    except Exception as e:
        print(f"\nErreur lors de l'exécution du pipeline: {str(e)}",
              file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()