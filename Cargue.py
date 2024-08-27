import pandas as pd

file_path = 'DETALLADO_AGOSTO27_2024.xlsx'
Nuevo = pd.read_excel(file_path, engine= 'openpyxl')

file_path2 = 'DETALLADO_FEBRERO29_2024.xlsx'
Original = pd.read_excel(file_path2, engine= 'openpyxl')

# Asegurarse de que la columna de ID tenga el mismo nombre en ambos DataFrames
id_columna = 'PER_ID'

# Buscar registros en Nuevo que no estén en Original
nuevos_registros = Nuevo[~Nuevo[id_columna].isin(Original[id_columna])]

# Agregar una columna de marcador en los nuevos registros
nuevos_registros['Es_Nuevo'] = True

# Insertar nuevos registros en Original
df_actualizado = pd.concat([Original, nuevos_registros], ignore_index=True)

# Para los registros que ya estaban en Original, asegurarse de que la columna de marcador esté en False
df_actualizado['Es_Nuevo'].fillna(False, inplace=True)

# Guardar el DataFrame actualizado en un nuevo archivo Excel o sobreescribir el existente
df_actualizado.to_excel('archivo_base_actualizado.xlsx', index=False)

print(f'Se han insertado {len(nuevos_registros)} registros nuevos en el archivo base.')

#print(Nuevo.head())




