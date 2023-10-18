import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Definir el nombre de la tabla como una variable
nombre_tabla = 'zapatos'

# Crear la tabla con el nombre de la tabla especificado
create_table_sql = f'''
    CREATE TABLE {nombre_tabla} (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
'''

cursor.execute(create_table_sql)

# Guardar los cambios
conn.commit()
