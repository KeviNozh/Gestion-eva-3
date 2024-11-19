from DAL.conexion import ConexionDB
from Clases.contrasena import Contrasena

def autenticar(correo, contrasena):
    conexion_db = ConexionDB()
    conexion = conexion_db.conectar()
    if not conexion:
        return False

    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT contrasena FROM usuarios WHERE correo = %s", (correo,))
        usuario = cursor.fetchone()
        if usuario and Contrasena.verificar(contrasena, usuario['contrasena']):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al autenticar usuario: {e}")
        return False
    finally:
        cursor.close()
        conexion_db.cerrar(conexion)
