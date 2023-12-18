from flask import Flask, render_template, request, redirect, url_for, flash
from mysql import connector
from usuarios.resource import usuarios_servicios
from tareas.servicios import tareas_servicios
from estados.servicios import estados_servicios
from categorias.servicios import categorias_servicios


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('tareas_servicios.listar_tareas'))

app.register_blueprint(usuarios_servicios)
app.register_blueprint(tareas_servicios)
app.register_blueprint(estados_servicios)
app.register_blueprint(categorias_servicios)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
