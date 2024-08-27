import pandas as pd

file_path = 'DETALLADO_AGOSTO27_2024.xlsx'
Nuevo = pd.read_excel(file_path, engine= 'openpyxl')

file_path2 = 'DETALLADO_FEBRERO29_2024.xlsx'
Original = pd.read_excel(file_path2, engine= 'openpyxl')

# Asegurarse de que la columna de ID tenga el mismo nombre en ambos DataFrames
id_columna = 'PER_ID'

# Buscar registros en df_comparar que no estén en df_base
nuevos_registros = Nuevo[~Nuevo[id_columna].isin(Original[id_columna])]

# Insertar nuevos registros en Original
df_actualizado = pd.concat([Original, nuevos_registros], ignore_index=True)

# Guardar el DataFrame actualizado en un nuevo archivo Excel o sobreescribir el existente
df_actualizado.to_excel('archivo_base_actualizado.xlsx', index=False)

print(f'Se han insertado {len(nuevos_registros)} registros nuevos en el archivo base.')

#print(Nuevo.head())




