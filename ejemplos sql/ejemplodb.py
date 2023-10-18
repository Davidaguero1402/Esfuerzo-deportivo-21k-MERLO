import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')