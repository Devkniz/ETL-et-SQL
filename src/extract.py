"""
ETL - Étape 1 : Extraction des données depuis le CSV
"""

from pathlib import Path  
import pandas as pd  
import sys  

def extract_data():  
    try:  
        # Chemin ABSOLU plus robuste  
        current_dir = Path(__file__).parent.parent  # Suppose que extract.py est dans src/  
        csv_source = current_dir / "data" / "Data Sample for Sanofi(Feuil1).csv"  

        # Vérifie que le fichier source existe  
        if not csv_source.exists():  
            print(f"⛔ Fichier source introuvable : {csv_source}")  
            sys.exit(1)  

        # Lit et sauvegarde  
        df = pd.read_csv(csv_source, sep=';', encoding='latin1')  
        output_path = current_dir / "data" / "clinical_data.csv"  
        df.to_csv(output_path, index=False)  
        print(f"📥 Fichier brut généré : {output_path}")  

    except Exception as e:  
        print(f"🔥 Erreur lors de l'extraction : {str(e)}", file=sys.stderr)  
        sys.exit(1)  

if __name__ == "__main__":  
    extract_data()  
