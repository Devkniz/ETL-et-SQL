"""
ETL - Étape 2 : Nettoyage des données
"""

from pathlib import Path  
import pandas as pd  

def transform_data():  
    input_csv = Path("data/clinical_data.csv") 
    output_csv = Path("data/cleaned_data.csv") 
    df = pd.read_csv(input_csv)  

    # Supprime les lignes avec des erreurs  
    cleaned_df = df[df["errors"].isna()].copy() 

    # Convertit les dates  
    cleaned_df["treatment_date"] = pd.to_datetime(cleaned_df["treatment_date"], dayfirst=True)  
    cleaned_df.to_csv(Path("data/cleaned_data.csv"), index=False)  
    print(f"✅ Fichier nettoyé généré : {output_csv.resolve()}")  

if __name__ == "__main__":  
    transform_data()  
