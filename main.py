from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------
# Ruta del menú principal
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -------------------------
# Ejercicio 1: Cálculo de Compras
# -------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        tarros = int(request.form.get('tarros'))

        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario

        # Calcular descuento según edad
        if 18 <= edad <= 30:
            descuento_porcentaje = 0.15
        elif edad > 30:
            descuento_porcentaje = 0.25
        else:
            descuento_porcentaje = 0.0

        monto_descuento = int(total_sin_descuento * descuento_porcentaje)
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "monto_descuento": monto_descuento,
            "total_con_descuento": total_con_descuento
        }

        return render_template('ejercicio1.html', resultado=resultado)

    return render_template('ejercicio1.html')


# -------------------------
# Ejercicio 2: Inicio de Sesión
# -------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')

        mensaje = "Usuario o contraseña incorrectos"  # Valor por defecto

        # Validaciones específicas
        if nombre == "juan" and password == "admin":
            mensaje = f"Bienvenido Administrador {nombre}"
        elif nombre == "pepe" and password == "user":
            mensaje = f"Bienvenido Usuario {nombre}"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


# -------------------------
# Arranque de la aplicación
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)