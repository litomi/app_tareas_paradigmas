from flask import Flask as flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from App import connection

usuarios_servicios = Blueprint("roles_servicios", __name__, template_folder='templates_roles')

class ServiciosRoles:
    def listar_roles(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roles")
        datos = cursor.fetchall()
        cursor.close()
        return datos;
