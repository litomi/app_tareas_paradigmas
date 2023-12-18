-- +-------------------+--------------+------+-----+-------------------+-----------------------------------------------+
-- | Field             | Type         | Null | Key | Default           | Extra                                         |
-- +-------------------+--------------+------+-----+-------------------+-----------------------------------------------+
-- | id                | int          | NO   | PRI | NULL              | auto_increment                                |
-- | titulo            | varchar(40)  | NO   |     | NULL              |                                               |
-- | descripcion       | varchar(100) | NO   |     | NULL              |                                               |
-- | categoria         | int          | NO   |     | NULL              |                                               |
-- | creada_por        | int          | NO   |     | NULL              |                                               |
-- | asignada_a        | int          | NO   |     | NULL              |                                               |
-- | fecha_creacion    | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
-- | fecha_vencimiento | timestamp    | YES  |     | NULL              |                                               |
-- | fecha_edicion     | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
-- | estado            | int          | NO   |     | NULL              |                                               |
-- +-------------------+--------------+------+-----+-------------------+-----------------------------------------------+

sql = (
"SELECT "
"    t.id,"
"    t.titulo,"
"    t.descripcion,"
"    c.nombre,"
"    creador.nombreCompleto AS creada_por,"
"    asignado.nombreCompleto AS asignada_a,"
"    t.fecha_creacion,"
"    t.fecha_vencimiento,"
"    t.fecha_edicion,"
"    t.estado"
"FROM "
"    tareas AS t"
"INNER JOIN "
"    categorias AS c ON t.categoria = c.id"
"INNER JOIN"
"    usuarios AS creador ON t.creada_por = creador.id"
"INNER JOIN"
"    usuarios AS asignado ON t.asignada_a = asignado.id;"
)

-- +----------------+-------------+------+-----+-------------------+-------------------+
-- | Field          | Type        | Null | Key | Default           | Extra             |
-- +----------------+-------------+------+-----+-------------------+-------------------+
-- | id             | int         | NO   | PRI | NULL              | auto_increment    |
-- | nombre         | varchar(20) | NO   |     | NULL              |                   |
-- | descripcion    | varchar(50) | YES  |     | NULL              |                   |
-- | color          | varchar(10) | YES  |     | NULL              |                   |
-- | fecha_creacion | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
-- +----------------+-------------+------+-----+-------------------+-------------------+


INSERT INTO estados(nombre, descripcion, color) VALUES
("Por hacer", "Tarea pendiente de realización.", "red"),
("En progreso", "Tarea en proceso de realización.", "yellow"),
("Completado", "Tarea finalizada con éxito.", "green" ),


-- +-------+-------------+------+-----+---------+-------+
-- | Field | Type        | Null | Key | Default | Extra |
-- +-------+-------------+------+-----+---------+-------+
-- | color | varchar(15) | NO   | PRI | NULL    |       |
-- | rgb   | varchar(7)  | NO   | UNI | NULL    |       |
-- +-------+-------------+------+-----+---------+-------+

CREATE TABLE colores(
    color VARCHAR(15) NOT NULL UNIQUE,
    rgb VARCHAR(7) NOT NULL UNIQUE
);

INSERT INTO colores VALUES
("Rojo", "#FF0000"),
("Verde", "#00FF00"),
("Azul", "#0000FF"),
("Amarillo", "#FFFF00"),
("Naranja", "#FFA500");


mysql> DESC categorias;
+----------------+-------------+------+-----+-------------------+-------------------+
| Field          | Type        | Null | Key | Default           | Extra             |
+----------------+-------------+------+-----+-------------------+-------------------+
| id             | int         | NO   | PRI | NULL              | auto_increment    |
| nombre         | varchar(20) | NO   |     | NULL              |                   |
| descripcion    | varchar(50) | YES  |     | NULL              |                   |
| color          | varchar(10) | YES  |     | NULL              |                   |
| fecha_creacion | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+----------------+-------------+------+-----+-------------------+-------------------+

INSERT INTO categorias(nombre, descripcion, color) VALUES
("Planificación", "Definición de objetivos y estrategias. Asignación de tareas y recursos", "#000000"),
("Desarrollo", "Creación o realización de tareas", "#ffffff"),
("Revisión", "Evaluación de progreso. Corrección de desviaciones", "#00ff00"),
("Entrega/Implementación", "Finalización y entrega de resultados. Cierre del proyecto o tarea", "#ff0000");