import usuarios.conexion as conexion
import datetime

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Notas:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, fecha)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]
