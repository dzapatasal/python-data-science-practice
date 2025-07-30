import pandas as pd
import numpy as np

# ✅ Cargar un archivo CSV
def cargar_csv(ruta, encabezado=True):
    try:
        if encabezado:
            df = pd.read_csv(ruta)
        else:
            df = pd.read_csv(ruta, header=None)
        print("✅ Archivo cargado con éxito.")
        return df
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return None

# 🧼 Mostrar información básica del DataFrame
def resumen(df):
    print("🔍 Dimensiones:", df.shape)
    print("\n🔢 Tipos de datos:\n", df.dtypes)
    print("\n📋 Primeras filas:\n", df.head())
    print("\n📊 Descripción estadística:\n", df.describe(include='all'))

# 🔁 Transponer un DataFrame y guardar como CSV
def transponer_y_guardar(df, nombre_archivo, encabezado=False):
    transpuesto = df.transpose()
    transpuesto.to_csv(nombre_archivo, header=encabezado, index=False)
    print(f"📁 Archivo guardado como: {nombre_archivo}")
    return transpuesto

# 🎯 Cargar solo datos numéricos desde CSV (ignorando la primera fila si es texto)
def cargar_numeros_csv(ruta, saltar_fila=1):
    try:
        data = np.loadtxt(ruta, delimiter=',', skiprows=saltar_fila)
        print("✅ Datos numéricos cargados con éxito.")
        return data
    except Exception as e:
        print(f"❌ Error al cargar datos numéricos: {e}")
        return None

# 📈 Visualizar contenido completo del DataFrame sin truncar
def mostrar_completo(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
