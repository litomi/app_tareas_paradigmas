from flask import Flask, render_template, request, redirect, url_for, flash
from mysql import connector
from usuarios.servicios import usuarios_servicios


app = Flask(__name__)

@app.route('/')
def index():
    return "Hola"

app.register_blueprint(usuarios_servicios)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
