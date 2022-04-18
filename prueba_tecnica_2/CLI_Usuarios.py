import argparse
import json


class Usuario():
    def __init__(self, id, nombres, apellidos, edad, email):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.email = email

    def crear(self):
        with open('data.json', 'a') as f:
            json.dump(self.__dict__, f)

    @classmethod
    def listar(self):
        f = open('data.json', 'r')
        return f.read()

    def buscar(self):
        pass

parser = argparse.ArgumentParser(description = "Operaciones con usuarios")

parser.add_argument("-c", "--crear", nargs = '*', metavar = "Id, Nombres, Apellidos, Edad, Email", type = str,
                     help = "Información del usuario a crear")
parser.add_argument("-l", "--listar", nargs = '*', metavar = "num", type = str,
                     help = "Se muestran todos los usuarios creados")
parser.add_argument("-m", "--modificar", nargs = '*', metavar = "num", type = str,
                     help = "Ingrese el ID del usuario a modificar")
parser.add_argument("-e", "--eliminar", nargs = '*', metavar = "num", type = str,
                     help = "All the numbers separated by spaces will be added.")

args = parser.parse_args()



if args.crear != None:
    if len(args.crear) == 0:
        print("Por favor suministre la información del usuario a crear: (e.g. --crear 1234 John Doe 25 john@doe.com )")
    else:
        user = Usuario(int(args.crear[0]), args.crear[1], args.crear[2], args.crear[3], args.crear[4])
        user.crear()
        print("Usuario creado exitosamente!!")


if args.listar != None:
    print(Usuario.listar())



if args.modificar != None:
    if len(args.modificar) == 0:
        print("Por favor suministre el ID del usuario a modificar (e.g. --modificar 1234).")
    else:
        id = args.modificar[0]
        id = input('Ingrese qué campo quiere modificar: (id, nombres, apellidos, edad, email:) ')
        print(id)



if args.eliminar != None:
    print("Eliminando clase")
