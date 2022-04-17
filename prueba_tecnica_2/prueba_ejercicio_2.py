import pickle

lista_usuarios = []
class Usuario():
    def __init__(self,):
        self.id = ("")
        self.nombre = ("")
        self.apellido = ("")
        self.edad = ()
        self.email = ("")
        


def menu():
    opcion = 0
    while opcion != 5:
        print("-----Bienvenido al programa de usuarios-----")
        print()
        print("*****Elija una de las opciones*****")
        print("""
        OP.(1): Agregar usuario
        OP.(2): Actualizar usuario
        OP.(3): Eliminar usuario
        OP.(4): Listar usuarios
        OP.(5): Salir""")
        try:
            opcion=int(input("Ingrese opcion: "))
        except ValueError:
            print("`\\\\\\\\\\\\\Caracter invalido//////////////")
        if opcion == 1:
            agregar()
        elif opcion == 2:
            actualizar()
        elif opcion == 3:
            Eliminar()
        elif opcion == 4:
            Listar()
        elif opcion == 5:
            print("########Gracias por usar este programa#######")
        else:

            print("Por favor ingrese opcion valida")
        

def agregar():
    print("++++++Estas en la pestaña agregar++++++")
    print()
    usuario=Usuario()
    usuario.id = input("Ingrese la identificacion: ")
    usuario.nombre = input("Ingrese el nombre: ")
    usuario.apellido = input("Ingrese el apellido: ")
    usuario.edad = input("Ingrese la edad: ")
    usuario.email = input("Ingrese el imeil: ")
    lista_usuarios.append(usuario)
    print("¡¡¡¡¡¡¡¡Se agrego con exito!!!!!!!!")


def actualizar():
    print("++++++Estas en la pestaña actualizar+++++")
    buscar()
    print("Que dato desea actualizar?")
    print("""
    OP.1): Identificacion
    OP.2): Nombre
    OP.3): Apellido
    OP.4): Edad
    OP.5): Email""")
    try:
        opc=int(input("Ingrese opcion: "))
    except ValueError:
            print("`\\\\\\\\\\\\\Caracter invalido//////////////")
    if opc == 1:
        nueva_id = input("Nueva identificacion: ")
        for u in lista_usuarios:
            u.id = nueva_id
            print(u.id)
        print("Se cambio la identificacion")
    
    elif opc == 2:
        nuevo_nombre = input("Nueva nombre: ")
        for u in lista_usuarios:
            u.nombre = nuevo_nombre
            print(u.nombre)
        print("Se cambio el nombre")
    
    elif opc == 3:
        nuevo_apellido = input("Nuevo apellido: ")
        for u in lista_usuarios:
            u.apellido = nuevo_apellido
            print(u.apellido)
        print("Se cambio el apellido")
    
    elif opc == 4:
        nueva_edad = input("Nueva edad: ")
        for u in lista_usuarios:
            u.edad = nueva_edad
            print(u.edad)
        print("Se cambio la edad")
    
    elif opc == 5:
        nuevo_imeil = input("Nuevo imeil: ")
        for u in lista_usuarios:
            u.imeil = nuevo_imeil
            print(u.imeil)
        print("Se cambio el imeil")
    
    else:

        print("Por favor ingrese opcion valida")


def Eliminar():
    print("++++++Estas en la pestaña eliminar++++++")
    u = buscar()
    lista_usuarios.remove(u)
    print(f"Se elimino el usuario{u.nombre}")

def Listar():
    print("++++++Estas en la pestaña listar++++++")
    for u in lista_usuarios:
        datos=(f"Identificacion: {u.id}\nNombre: {u.nombre} {u.apellido}\nEdad: {u.edad}\nEmail: {u.email}")
        print(datos)
        print()


def buscar():
    busc = input("Ingrese su identificacion o su nombre: ")
    for usuario in lista_usuarios:
        if usuario.id == busc or usuario.nombre == busc:
            return usuario
            


menu()
    
#     def __str__(self):
#         return f"{self.nombre} {self.apellido} {self.edad} {self.email}"

# # 

# class Lista_Usuarios:
#     usuarios = []

#     def __init__(self):
#         lista_de_usuarios = open("ficheroExterno", "ab+")
#         lista_de_usuarios.seek(0)

#         try:
#            self.usuarios = pickle.load(lista_de_usuarios)
#            print(f"Se cargaron {len(self.usuarios)} usuarios del fichero externo")
#         except:
#             print("El fichero esta vacio")
#         finally:
#             lista_de_usuarios.close()
#             del(lista_de_usuarios)
    
#     def agregar_Usuarios(self, u):
#         self.usuarios.append(u)
#         self.guardar_usuarios_en_fichero_externo()
    
#     def listar_Personas(self):
#         for u in self.usuarios:
#             print(u)
#     def guardar_usuarios_en_fichero_externo(self):
#         lista_de_usuarios=open("ficheroExterno", "wb")
#         pickle.dump(self.usuarios, lista_de_usuarios)
#         lista_de_usuarios.close()
#         del(lista_de_usuarios)
        

    


    