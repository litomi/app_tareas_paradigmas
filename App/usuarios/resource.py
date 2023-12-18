from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from App.base import connection
from App.usuarios import ServiciosUsuarios
from App.roles import ServiciosRoles


usuarios_servicios = Blueprint("usuarios_servicios", __name__, template_folder='templates_usu')

servicioUsuario = ServiciosUsuarios()
serviciosRoles = ServiciosRoles()

@usuarios_servicios.route('/usuarios')
def usuarios():
    datos = servicioUsuario.listar_usuarios()
    return render_template('tabla_usuarios.html', usuarios = datos)

@usuarios_servicios.route('/usuarios/activos')
def usuarios_activos():
    usaurios = servicioUsuario.listar_usuarios()
    datos =  servicioUsuario.filtrar_usuarios_activos(usuarios)
    return render_template('tabla_usuarios_activos.html', usuarios = datos)

# Devuelve el archivo que contiene el formulario
# para cargar un usuario.
@usuarios_servicios.route('/usuarios/crear')
def crear_formulario():
    roles = serviciosRoles.listar_roles()
    return render_template('form_usuarios_agregar.html', roles)


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

        ServiciosUsuarios.guardar_usuario(nombreCompleto, email, activo, rol, id)

    return redirect(url_for('usuarios_servicios.listar_usuarios'))


# Recibe un 'id' de usuario.
# Recupera el usuario correspondiente desde la base.
# Envía los datos al formulario de edición de usuario.

@usuarios_servicios.route('/usuarios/editar/<int:id>')
def obtener_usuario(id):
    datos = servicioUsuario.obtener_usuario(id)
    roles = serviciosRoles.listar_roles()
    return render_template('form_usuarios_editar.html', usuario = datos[0], roles = roles)


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

        servicioUsuario.editar_usuario(nombreCompleto, email, activo, rol, id)

    return redirect(url_for('usuarios_servicios.usuarios'))

# Recibe un 'id' de usuario.
# Eliminar al usuario correspondiente de la base.
# Redirecciona a la tabla de usuarios.
@usuarios_servicios.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    return ServiciosUsuarios.eliminar_usuario(id)