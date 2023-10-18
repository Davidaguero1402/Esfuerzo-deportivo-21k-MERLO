import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Realizar una consulta SQL para seleccionar todos los registros de la tabla 'usuarios'
cursor.execute('SELECT * FROM usuarios')

# Obtener todos los registros como una lista de tuplas
filas = cursor.fetchall()

# Imprimir los datos
for fila in filas:
    print(fila)

# Cerrar la conexión
conn.close()
