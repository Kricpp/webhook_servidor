import sqlite3
def conexion():
    conn = sqlite3.connect('Alumno_Pago')
    cursor = conn.cursor()
    return conn, cursor



def insertar_pago(cursor, conn, alumno_id, estado_pago, concepto_pago):
    cursor.execute("INSERT INTO Alumno_Pago (id_alumno, estado, Concepto_pago) VALUES (?, ?, ?)", (alumno_id, estado_pago, concepto_pago))
    conn.commit()


def actualizar_pago(cursor,conn, alumno_id, estado_pago, concepto_pago=None):
    cursor.execute("UPDATE Alumno_Pago SET estado = ?, Concepto_pago = ? WHERE id_alumno = ?", (estado_pago, concepto_pago, alumno_id))
    conn.commit()



def obtener_pagos(cursor):
    cursor.execute("SELECT * FROM Alumno_Pago")
    return cursor.fetchall()

def obtener_estado(cursor, id_alumno):
    cursor.execute("SELECT estado FROM Alumno_Pago where id_alumno= ? ", (id_alumno,))
    return cursor.fetchall()
def obtener_alumnos(cursor, dato: str):
    cursor.execute("SELECT * FROM Alumno_Pago where id_alumno = ?",(dato,),)
    return cursor.fetchall()


'''
import sqlite3

conn = sqlite3.connect('Alumno_Pago')

cursor = conn.cursor()


alumno_id = '0020210149'
estado_pago = 1  # 1 para indicar un pago realizado (o 0 para no realizado)
concepto_pago = 'Matrícula'

# Insertar datos en la tabla
cursor.execute("INSERT INTO Alumno_Pago (id_alumno, estado, Concepto_pago) VALUES (?, ?, ?)", (alumno_id, estado_pago, concepto_pago))
cursor.execute("select * from Alumno_Pago")

filas = cursor.fetchall()
for row in filas : 
    print(row)


conn.commit()
conn.close()

con, cursor = conexion()
insertar_pago(cursor,con,"0020210165",0, "MATRICULA")
insertar_pago(cursor,con,"0020210166",0, "MATRICULA")
insertar_pago(cursor,con,"0020210167",0, "CARNET")
insertar_pago(cursor,con,"0020210168",0, "COMEDOR")
insertar_pago(cursor,con,"0020210169",0, "MATRICULA")
insertar_pago(cursor,con,"0020210170",0, "MATRICULA")

historial = obtener_pagos(cursor)
for row in historial:
    print(row)
    '''