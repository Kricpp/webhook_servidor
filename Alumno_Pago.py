import sqlite3

conn = sqlite3.connect('Alumno_Pago')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alumno_Pago (
        id_alumno varchar(10) PRIMARY KEY ,
        estado bit ,
        Concepto_pago varchar(250)
    )
''')

conn.commit()
conn.close()


