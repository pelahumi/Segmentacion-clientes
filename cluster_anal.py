import pandas as pd 



df = pd.read_csv('data/Client_segment_MODIFICADO.csv', sep=';', encoding='ISO-8859-1')

dict_prov = {'i\x81vila': 'Avila', 'Almeri\xada': 'Almeria', 'i\x81lava': 'Alava', 'La Corui±a': 'La Coruña', 'Guipiºzcoa': 'Guipuzcoa'}

for key, value in dict_prov.items():
    df['Provincia'] = df['Provincia'].replace(key, value)

df.to_csv('data/cleaned/Client_segment_cleaned.csv', sep=';', encoding='ISO-8859-1', index=False)

# print(df.head())