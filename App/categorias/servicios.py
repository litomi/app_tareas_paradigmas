from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from base import connection

categorias_servicios = Blueprint("categorias_servicios", __name__, template_folder='templates_cat')


# Recupera las 'categorias' de la base.
# Envía los datos recuperados a el archivo
# que contiene la tabla que muestra las categorias.

@categorias_servicios.route('/categorias')
def listar_categorias():
    datos = None #limpiando
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categorias")
    datos = cursor.fetchall()
    cursor.close()
    return render_template('tabla_categorias.html', categorias = datos)


@categorias_servicios.route('/categorias/crear')
def crear_formulario():
    return render_template('form_categorias_agregar.html')

@categorias_servicios.route('/categorias/agregar_db', methods=['POST'])
def guardar_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        color = request.form['color']

        sql = "INSERT INTO categorias(nombre, descripcion, color) \
            VALUES(%s, %s, %s, %s, %s)"

        cursor = connection.cursor()
        cursor.execute(sql, (nombre, descripcion, color))
        connection.commit()
        cursor.close()

    return redirect(url_for('categorias_servicios.listar_categorias'))


@categorias_servicios.route('/categorias/editar/<int:id>')
def obtener_categoria(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categorias WHERE id = {}".format(id))
    datos = cursor.fetchall()
    cursor.close()
    return render_template('form_categorias_editar.html', categoria = datos[0])



@categorias_servicios.route('/categorias/editar_db/<int:id>', methods = ['POST'])
def editar_categoria(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        color = request.form["color"]

        sql = (
            "UPDATE categoria SET "
            "nombre = %s, "
            "descripcion = %s, "
            "color = %s, "
            "WHERE id = %s"
            )

        cursor = connection.cursor()
        cursor.execute(sql, (nombre, descripcion, color, id))
        connection.commit()
        cursor.close()

    return redirect(url_for('categoria_servicios.listar_categoria'))


@categorias_servicios.route('/categorias/eliminar/<int:id>')
def eliminar_categoria(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = {}".format(id))
    connection.commit()
    cursor.close()
    return redirect(url_for('categorias_servicios.listar_categorias'))
   
