from Usuario.crear_usuario import CrearUsuario
from Usuario.autenticar_usuario import AutenticarUsuario

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    CrearUsuario.crear(nombre, correo, contrasena)
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    if AutenticarUsuario.autenticar(correo, contrasena):
        print("Inicio de sesión exitoso.")
    else:
        print("Correo o contraseña incorrectos.")

if __name__ == "__main__":
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    else:
        print("Opción no válida.")
