# load.py (version verbosée)  
import pandas as pd  
from sqlalchemy import create_engine  
from pathlib import Path  
import sys  

def load_data():  
    try:  
        # 1. Vérifie que le CSV nettoyé existe  
        input_path = Path("data/cleaned_data.csv")  
        if not input_path.exists():  
            print("❌ Fichier 'cleaned_data.csv' introuvable. Exécute d'abord transform.py !")  
            sys.exit(1)  

        # 2. Charge les données  
        df = pd.read_csv(input_path)  
        print(f"✅ CSV chargé. Lignes trouvées : {len(df)}")  

        # 3. Connexion à SQLite (crée le .db si inexistant)  
        db_path = Path("data/clinical_data.db")  
        engine = create_engine(f'sqlite:///{db_path}')  
        print(f"🔌 Connexion à la base SQLite : {db_path.resolve()}")  

        # 4. Exporte les données  
        df.to_sql('patients', engine, if_exists='replace', index=False)  
        print(f"💾 Données exportées dans la table 'patients' !")  

    except Exception as e:  
        print(f"❌ Erreur : {str(e)}")  

if __name__ == "__main__":  
    load_data()  
