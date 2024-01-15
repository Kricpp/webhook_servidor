
from flask import Flask , request
import Hacer_pago

con, cursor= Hacer_pago.conexion()

app = Flask(__name__)

@app.route('/pagos', methods=['POST'])  
def pagos():
    datos = request.json
    print("Datos Recibidos", datos)
    alumno = datos[0][1]
    concepto = datos[0][3]
    print("Alumno", alumno)
    conn, cursor= Hacer_pago.conexion()
    historial =Hacer_pago.obtener_pagos(cursor)
    print (historial)
    Hacer_pago.actualizar_pago(cursor,conn, alumno, True, concepto)
    print("-----------")
    historial =Hacer_pago.obtener_pagos(cursor)
    print (historial)
    return "pago exitoso"







@app.route('/confirmarExistencia', methods=['POST']) 
def confirmarExistencia():
    datos = str(request.json)
    print("Datos Recibidos", datos)
    con, cursor= Hacer_pago.conexion()
    estado = Hacer_pago.obtener_alumnos(cursor, datos)
    print(estado)
    if estado == []:
        return "0"
    else:
        return "1"

if __name__ == "__main__":
    pepe =Hacer_pago.obtener_pagos(cursor)
    print("Pago recibido por webhook", pepe)
    app.run(host="192.168.43.141",port=5000)



