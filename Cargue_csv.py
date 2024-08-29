import pandas as pd

file_path = 'DETALLADO_AGOSTO_27_2024.csv'
Nuevo = pd.read_csv(file_path ,delimiter=';')

file_path2 = 'DETALLADO_FEBRERO_29_2024.csv'
Original = pd.read_csv(file_path2  ,delimiter=';')

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
df_actualizado.to_csv('archivo_base_actualizado.csv', index=False)

print(f'Se han insertado {len(nuevos_registros)} registros nuevos en el archivo base.')


# Seleccionar columnas específicas para el nuevo DataFrame
columnas_a_conservar = ['INSTITUCION', 'CALENDARIO', 'SECTOR', 'ZONA_SEDE', 'JORNADA','GRADO_COD']
df_nuevo = df_actualizado[columnas_a_conservar]

# Guardar el nuevo DataFrame como archivo CSV
#archivo_csv = 'nuevo_dataframe.csv'
df_nuevo.to_csv('nuevo_dataframe.csv', index=False)

# Mostrar el nuevo DataFrame
print("\nNuevo DataFrame con columnas específicas:")
print(df_nuevo)
#print(Nuevo.head())

# Imprime los nombres de las columnas
print("Columnas en el DataFrame original:")
print(Original.columns)