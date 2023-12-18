from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from base import connection

estados_servicios = Blueprint("estados_servicios", __name__, template_folder='templates_est')


def listar_colores():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM colores")
    datos = cursor.fetchall()
    cursor.close()
    return datos

@estados_servicios.route('/estados')
def listar_estados():
    datos = None
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM estados")
    datos = cursor.fetchall()
    cursor.close()    
    return render_template('tabla_estados.html', estados = datos)

@estados_servicios.route('/estados/crear')
def crear_formulario():
    datos = listar_colores()
    return render_template('form_estados_agregar.html', colores=datos)

@estados_servicios.route('/estados/agregar_db', methods=['POST'])
def guardar_estados():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        color = request.form['color']

        sql = "INSERT INTO estados(nombre, descripcion, color) \
            VALUES(%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql,(nombre,descripcion,color))
        connection.commit()
        cursor.close()
        return redirect(url_for('estados_servicios.listar_estados'))

@estados_servicios.route('/estados/editar/<int:id>')
def obtener_estado(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM estados WHERE id = {}".format(id))
    datos = cursor.fetchall()
    cursor.close()
    return render_template('form_estados_editar.html', estado = datos[0], colores = listar_colores())

@estados_servicios.route('/estados/editar_db/<int:id>', methods = ['POST'])
def editar_estado(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        color = request.form['color']

        sql = (
            "UPDATE estados SET "
            "nombre = %s, " 
            "descripcion = %s, "
            "color = %s "  
            "WHERE id = %s"
            )

        cursor = connection.cursor()
        cursor.execute(sql, (nombre, descripcion, color, id))
        connection.commit()
        cursor.close()

    return redirect(url_for('estados_servicios.listar_estados'))

@estados_servicios.route('/estados/eliminar/<int:id>')
def eliminar_estado(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM estados WHERE id = {}".format(id))
    connection.commit()
    cursor.close()
    return redirect(url_for('estados_servicios.listar_estados'))
