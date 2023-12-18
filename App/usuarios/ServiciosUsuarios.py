from App import connection

class ServiciosUsuarios:
    def __init__(self):
        pass

   
    def filtrar_usuarios_activos(self, datos):
        activos = filter(lambda usuario: usuario[4] == "activo", datos)
        return list(activos)

   
    def listar_usuarios(self):
        datos = None #limpiando
        cursor = connection.cursor()

        sql = (
            "SELECT "
            "usr.id,"
            "usr.nombreCompleto,"
            "usr.email,"
            "usr.password,"
            "usr.activo,"
            "rol.nombre,"
            "usr.fecha_creacion,"
            "usr.fecha_edicion "
            "FROM usuarios AS usr "
            "INNER JOIN roles AS rol ON usr.rol = rol.id"
        )

        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        return datos
    
   
    def eliminar_usuario(self, id):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = {}".format(id))
        connection.commit()
        cursor.close()
        return redirect(url_for('usuarios_servicios.listar_usuarios'))
        
       
    def guardar_usuario(self):
        sql = "INSERT INTO usuarios(nombreCompleto, email, password, activo, rol) \
            VALUES(%s, %s, %s, %s, %s)"

        cursor = connection.cursor()
        cursor.execute(sql, (nombreCompleto, email, password, activo, rol))
        connection.commit()
        cursor.close()

    def obtener_usuario(self, id):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = {} LIMIT 1".format(id))
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def editar_usuario(self, nombreCompleto, email, activo, rol, id):
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
