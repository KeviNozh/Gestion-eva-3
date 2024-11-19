from DAL.conexion import ConexionDB
from Clases.contrasena import Contrasena

def crear_usuario(nombre, correo, contrasena, rol_id=1):
    conexion_db = ConexionDB()
    conexion = conexion_db.conectar()
    if not conexion:
        return False

    cursor = conexion.cursor()
    contrasena_encriptada = Contrasena.encriptar(contrasena)
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, contrasena, rol_id) VALUES (%s, %s, %s, %s)",
            (nombre, correo, contrasena_encriptada, rol_id)
        )
        conexion.commit()
        print("Usuario creado exitosamente.")
        return True
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False
    finally:
        cursor.close()
        conexion_db.cerrar(conexion)
