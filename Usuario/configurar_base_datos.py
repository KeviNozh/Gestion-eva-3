import mysql.connector

def configurar_base_datos():
    host = "127.0.0.1"
    user = "tu_usuario_mysql"
    password = "tu_contraseña"

    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conexion.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS gestion;")
        print("Base de datos 'gestion' verificada o creada exitosamente.")

        cursor.execute("USE gestion;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                correo VARCHAR(100) UNIQUE NOT NULL,
                contrasena VARCHAR(255) NOT NULL,
                rol_id INT NOT NULL DEFAULT 1
            );
        """)
        print("Tabla 'usuarios' verificada o creada exitosamente.")

    except mysql.connector.Error as e:
        print(f"Error al configurar la base de datos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

if __name__ == "__main__":
    configurar_base_datos()
