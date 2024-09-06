import os
import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error



# Función para extraer datos del Excel (no es necesario cargar de nuevo, solo mostrar el DataFrame resultante)
def _display_dataframe(df):
    """Displays the DataFrame in the Streamlit interface."""
    st.write(df)  # Displays the dataframe

st.title("Visualización de Datos - Users y Roles")

# Cargar los DataFrames desde el sistema local
df1 = pd.read_excel('C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Users.xlsx')
df2 = pd.read_excel(r'C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Role table.xlsx')

# Unir los DataFrames por la columna 'ID'
df_merged = pd.merge(df1, df2, on='ID', how='inner')

# Mostrar el DataFrame resultante en la interfaz de Streamlit
st.write("Datos combinados (Users y Roles):")
_display_dataframe(df_merged)  

def get_all_the_courses():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    courses = []

    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT c.id, c.name FROM courses as c;
            """
            cursor.execute(query)
            courses = cursor.fetchall()
            print(courses)
        except Error as e:
            print(f"Error while getting courses from database: {e}")
        finally:
            cursor.close()
            return courses