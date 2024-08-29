import pandas as pd

def leer_csv(file_path, delimiter=';'):
    """Lee un archivo CSV y retorna un DataFrame."""
    try:
        return pd.read_csv(file_path, delimiter=delimiter)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
        return None

def encontrar_nuevos_registros(df_nuevo, df_original, id_columna):
    """Encuentra registros en df_nuevo que no están en df_original."""
    if df_nuevo is not None and df_original is not None:
        return df_nuevo[~df_nuevo[id_columna].isin(df_original[id_columna])]
    return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def agregar_columna_marcador(df, columna_marcador):
    """Agrega una columna de marcador con valor True."""
    if df is not None:
        df[columna_marcador] = True
    return df

def actualizar_dataframe(df_original, df_nuevos_registros):
    """Actualiza el DataFrame original con nuevos registros y ajusta la columna de marcador."""
    if df_original is not None and df_nuevos_registros is not None:
        df_actualizado = pd.concat([df_original, df_nuevos_registros], ignore_index=True)
        df_actualizado['Es_Nuevo'].fillna(False, inplace=True)
        return df_actualizado
    return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def guardar_csv(df, file_path):
    """Guarda el DataFrame en un archivo CSV."""
    try:
        df.to_csv(file_path, index=False)
        print(f"El DataFrame se ha guardado correctamente en {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo {file_path}: {e}")

def seleccionar_columnas(df, columnas_a_conservar):
    """Selecciona columnas específicas para el nuevo DataFrame."""
    if df is not None:
        return df[columnas_a_conservar]
    return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def main():
    # Rutas de los archivos
    file_path_nuevo = 'DETALLADO_AGOSTO_27_2024.csv'
    file_path_original = 'DETALLADO_FEBRERO_29_2024.csv'
    file_path_actualizado = 'archivo_base_actualizado.csv'
    file_path_nuevo_dataframe = 'nuevo_dataframe.csv'

    # Leer DataFrames
    df_nuevo = leer_csv(file_path_nuevo)
    df_original = leer_csv(file_path_original)

    if df_nuevo is not None and df_original is not None:
        # Encontrar nuevos registros
        id_columna = 'PER_ID'
        nuevos_registros = encontrar_nuevos_registros(df_nuevo, df_original, id_columna)

        # Agregar columna de marcador
        nuevos_registros = agregar_columna_marcador(nuevos_registros, 'Es_Nuevo')

        # Actualizar DataFrame original
        df_actualizado = actualizar_dataframe(df_original, nuevos_registros)

        # Guardar DataFrame actualizado
        guardar_csv(df_actualizado, file_path_actualizado)

        # Seleccionar columnas específicas y guardar nuevo DataFrame
        columnas_a_conservar = ['INSTITUCION', 'CALENDARIO', 'SECTOR', 'ZONA_SEDE', 'JORNADA', 'GRADO_COD']
        df_nuevo_dataframe = seleccionar_columnas(df_actualizado, columnas_a_conservar)
        guardar_csv(df_nuevo_dataframe, file_path_nuevo_dataframe)

        # Mostrar nuevo DataFrame
        print("\nNuevo DataFrame con columnas específicas:")
        print(df_nuevo_dataframe)

        # Imprimir columnas del DataFrame original
        print("Columnas en el DataFrame original:")
        print(df_original.columns)

if __name__ == "__main__":
    main()