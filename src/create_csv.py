import pandas as pd

# Leer el CSV descargado localmente
df = pd.read_csv("/Users/luiseduardogarciablanco/Desktop/bootcamp/EDA Project ABNB/EDA_project_ABNB/data/raw/AB_NYC_2019.csv")
print(df.head())






# Especifica la ruta y nombre del archivo CSV que quieres generar
output_file_path = '/Users/luiseduardogarciablanco/Desktop/bootcamp/EDA Project ABNB/EDA_project_ABNB/data/processed/AirBNB.csv'

# Guarda el DataFrame en un archivo CSV local
df.to_csv(output_file_path, index=False)
