import os
from Entities.Usuario import Usuario
from DAOs.UsuarioDAO import UsuarioDAO
from Logger.logger_base import log

op = 0



def menu():
    #borrarPantalla()
    print("LABORATORIO DB Usuarios".center(60,"*"))
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")
    try:
        return int(input("Ingrese la opción deseada (1-5): "))
    except Exception as e:
        print(e)


def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")


while op != 5:
    op = menu()
    #log.info(f"Opción seleccionada: {op}")
    if op == 1:
        #borrarPantalla()

        usuarios = UsuarioDAO.seleccionar()
        log.info("Lista de Usuarios".center(60, "*"))
        for u in usuarios:
            log.debug(u)


    elif op == 2:
        #borrarPantalla()
        #log.info("Insertar usuario".center(60, "*"))
        usuario = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        u = Usuario(usuario=usuario, password=password)

        u_i = UsuarioDAO.insertar(u)
        log.info(f"Usuarios insertados: {u_i}")

        #borrarPantalla()
    elif op == 3:
        #borrarPantalla()
        #log.info("Actualizar usuario".center(60, "*"))
        id_usuario = input("Ingrese el ID de usuario: ")
        usuario = input("Ingrese el nuevo nombre de usuario: ")
        password = input("Ingrese la nueva contraseña: ")

        u = Usuario(id_usuario, usuario, password)

        u_a = UsuarioDAO.actualizar(u)
        log.info(f"Usuarios actualizados: {u_a}")

    elif op == 4:
        #borrarPantalla()
        #log.debug("Eliminar usuario".center(60, "*"))
        id_usuario = input("Ingrese el ID de usuario a eliminar: ")

        u = Usuario(id_usuario=id_usuario)
        u_e = UsuarioDAO.eliminar(u)
        log.debug(f"Usuarios eliminados: {u_e}")
    elif op == 5:
        pass
    else:
        print("Opción desconocida")


