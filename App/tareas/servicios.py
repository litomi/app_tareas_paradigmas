from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from base import connection

tareas_servicios = Blueprint("tareas_servicios", __name__, template_folder='templates_tareas')

@tareas_servicios.route("/tareas")
def listar_tareas():
    datos = None
    cursor = connection.cursor()

    # sql = (    
    #     "SELECT "
    #         "t.id,"
    #         "t.titulo,"
    #         "t.descripcion,"
    #         "c.nombre,"
    #         "creador.nombreCompleto AS creada_por,"
    #         "asignado.nombreCompleto AS asignada_a,"
    #         "t.fecha_creacion,"
    #         "t.fecha_vencimiento,"
    #         "t.fecha_edicion,"
    #         "t.estado"
    #     " FROM "
    #         "tareas AS t"
    #     " INNER JOIN "
    #         "categorias AS c ON t.categoria = c.id"
    #     " INNER JOIN "
    #         "usuarios AS creador ON t.creada_por = creador.id"
    #     " INNER JOIN "
    #         "usuarios AS asignado ON t.asignada_a = asignado.id;"
    # )
    sql = "SELECT * FROM tareas"
    cursor.execute(sql)
    datos = cursor.fetchall()
    cursor.close()
    return render_template('/tabla_tareas.html', tareas = datos)
    #return jsonify(datos)

def listar_categorias():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categorias")
    datos = cursor.fetchall()
    cursor.close()
    return datos

def listar_usuarios():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    return datos

@tareas_servicios.route("/tareas/crear")
def crear_tarea():
    categorias = listar_categorias()
    usuarios = listar_usuarios()
    return render_template("/form_tareas_agregar.html", categorias = categorias, usuarios = usuarios)


