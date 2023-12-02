import flask
from mysql import connector

connection = connector.connect(
    user = 'root',
    password = '1002',
    host = '127.0.0.1',
    port = 3306,
    database = 'gestortareas_db'
)