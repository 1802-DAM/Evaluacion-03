from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET' , 'POST'])
def ejercicio1():


    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = None
    longitud_maxima = 0
    if request.method =='POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        longitud_maxima = max(len(nombre) for nombre in nombres)
        nombre_mas_largo = next(nombre for nombre in nombres if len(nombre) == longitud_maxima)

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud_maxima=longitud_maxima)





if __name__ == '__main__':
    app.run(debug=True)
