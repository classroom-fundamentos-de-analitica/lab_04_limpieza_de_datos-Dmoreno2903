"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    # Leer el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    # Reemplazar caracteres "-" y "_" por espacios
    df.replace({"-": " ", "_": " "}, regex=True, inplace=True)

    # Normalización de las columnas "sexo", "tipo_de_emprendimiento" y "barrio"
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["barrio"] = df["barrio"].str.lower()

    # Limpieza de las columnas "idea_negocio" y "línea_crédito"
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip()
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()

    # Conversión de "comuna_ciudadano" a entero
    df["comuna_ciudadano"] = pd.to_numeric(df["comuna_ciudadano"], errors='coerce').fillna(0).astype(int)

    # Limpieza y conversión de la columna "fecha_de_beneficio"
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Limpieza de la columna "monto_del_credito" y conversión a float
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.replace(r"[,$]", "", regex=True)
        .str.replace(r"\.00$", "", regex=True)
        .astype(float)
    )

    # Eliminación de duplicados y valores nulos
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    return df
