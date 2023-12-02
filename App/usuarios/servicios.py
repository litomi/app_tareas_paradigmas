from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from base import connection

usuarios_servicios = Blueprint("usuarios_servicios", __name__, template_folder='templates_usu')


# Recupera los 'usuarios' de la base.
# Envía los datos recuperados a el archivo
# que contiene la tabla que muestra los usuarios.

@usuarios_servicios.route('/usuarios')
def listar_usuarios():
    datos = None #limpiando
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    return render_template('tabla_usuarios.html', usuarios = datos)

# Devuelve el archivo que contiene el formulario
# para cargar un usuario.
@usuarios_servicios.route('/usuarios/crear')
def crear_formulario():
    return render_template('form_usuarios_agregar.html')


# Recupera los datos recibidos por 'request' desde el formulario.
# Graba los datos recibidos en la base.
# Redirecciona
@usuarios_servicios.route('/usuarios/agregar_db', methods=['POST'])
def guardar_usuario():
    if request.method == 'POST':
        nombreCompleto = request.form['nombreCompleto']
        email = request.form['email']
        password = request.form['password']
        activo = 'activo' if 'activo' in request.form else 'inactivo'
        rol = int(request.form['rol'])

        sql = "INSERT INTO usuarios(nombreCompleto, email, password, activo, rol) \
            VALUES(%s, %s, %s, %s, %s)"

        cursor = connection.cursor()
        cursor.execute(sql, (nombreCompleto, email, password, activo, rol))
        connection.commit()
        cursor.close()

    return redirect(url_for('usuarios_servicios.listar_usuarios'))


# Recibe un 'id' de usuario.
# Recupera el usuario correspondiente desde la base.
# Envía los datos al formulario de edición de usuario.

@usuarios_servicios.route('/usuarios/editar/<int:id>')
def obtener_usuario(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = {}".format(id))
    datos = cursor.fetchall()
    cursor.close()
    return render_template('form_usuarios_editar.html', usuario = datos[0])


# Recibe un 'id' de usuario.
# Recupera los datos recibidos por 'request' desde el formulario.
# Actualiza en la base los datos del usuario correspondiente.
# Redirecciona a la tabla de usuarios.

@usuarios_servicios.route('/usuarios/editar_db/<int:id>', methods = ['POST'])
def editar_usuario(id):
    if request.method == 'POST':
        nombreCompleto = request.form['nombreCompleto']
        email = request.form['email']
        activo = 'activo' if 'activo' in request.form else 'inactivo'
        rol = int(request.form['rol'])

        sql = (
            "UPDATE usuarios SET "
            "nombreCompleto = %s, "
            "email = %s, "
            "activo = %s, "
            "rol = %s "
            "WHERE id = %s"
            )

        cursor = connection.cursor()
        cursor.execute(sql, (nombreCompleto, email, activo, rol, id))
        connection.commit()
        cursor.close()

    return redirect(url_for('usuarios_servicios.listar_usuarios'))

# Recibe un 'id' de usuario.
# Eliminar al usuario correspondiente de la base.
# Redirecciona a la tabla de usuarios.

@usuarios_servicios.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = {}".format(id))
    connection.commit()
    cursor.close()
    return redirect(url_for('usuarios_servicios.listar_usuarios'))
