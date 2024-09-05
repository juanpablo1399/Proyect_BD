import pandas as pd

# Usar doble backslash para evitar problemas con rutas en Windows
df1 = pd.read_excel('C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Users.xlsx')

# Mostrar el DataFrame para asegurarse de que se haya leído correctamente
print(df1)

# Mostrar las primeras 5 filas del DataFrame para verificar
print(df1.head())


df2 = pd.read_excel(r'C:\\Users\\juanp\\OneDrive\\Escritorio\\Semestre 6\\D_proyectOne\\Role table.xlsx')

# Mostrar el DataFrame
print(df2)

print(df2.head())
