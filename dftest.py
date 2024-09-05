import pandas as pd

# Cargar los dos archivos Excel en dos DataFrames separados
df1 = pd.read_excel('C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Users.xlsx')
df2 = pd.read_excel(r'C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Role table.xlsx')

# Unir los DataFrames por filas (apilar uno debajo del otro)
df_combined = pd.concat([df1, df2], ignore_index=True)

# Mostrar el DataFrame combinado
print(df_combined)
