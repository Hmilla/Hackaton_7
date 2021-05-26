from pymongo.message import update
from config.connection import Connection
from bson.objectid import ObjectId
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

    # __str__ | solo string
    def __repr__(self): # representation
        return self.modelo

conn = Connection('Hackaton_7')

def all_cursos():
    # Traer todos los datos
    cursos_all = conn.get_all('Cursos', {
        '_id': {
            '$ne': ''
        }
    }, {
        'nombre': 1,
   })

    return list(cursos_all)


def listar_cursos():
    lista_cursos=all_cursos()
    
    for curso_1 in lista_cursos:
        print(f'- {curso_1["nombre"]}')

def agregar_curso():
    print("Escribe el nombre del curso")
    nombre=input("> ")
    new_curso=Curso(nombre)
    conn.insert_many('Cursos', [
        new_curso.__dict__

    ])
    print("Se agregó el curso ", nombre)

def select_curso():
    opcion=-1
    opciones=[]
    ids=[]
    print("Selecciona un curso")
    lista_cursos=all_cursos()
    for curso_1 in lista_cursos:
        opcion+=1
        print(f'{opcion+1} = {curso_1["nombre"]}')
        ids.append(curso_1["_id"])
        opciones.append(opcion)

    while True:
        try:
            seleccion=int(input(">"))
            if seleccion-1 in opciones:
                id_seleccionado=lista_cursos[seleccion-1]["_id"]
                break
            else:
                print("Elija una opción valida")

        except Exception as e:
            print(e)
            print("Escriba un número")
    
    print(f'Se seleccionó el curso {lista_cursos[seleccion-1]["nombre"]}')
    return id_seleccionado

def update_curso():
    id_curso = select_curso()
    print("Cual va a ser el nuevo nombre del curso")
    nombre=input("> ")
    conn.update_many('Cursos', {
        '_id': {
            '$eq': id_curso
        }
    }, {
        'nombre': nombre
    })
    print(f'Se cambió el nombre del curso a {nombre}')


def delete_curso():
    id_curso = select_curso()
    print("¿Estas seguro que quieres eliminar este curso? (1 = si/ 2 = no)")
    while True:
        seleccion=input("> ")
        if seleccion =="1":
            conn.delete_many('Cursos', {
                '_id': {
                    '$eq': id_curso
                }
            })
            print(f'Se eliminó el curso')
            break
        elif seleccion=="2":
            print("Saliendo...")
            break
        else:
            print("Elija una opción válida")

def menu_cursos():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = listar cursos")
            print("2 = insertar curso")
            print("3 = actualizar nombre de curso")
            print("4 = eliminar curso")
            print("5 = volver a menu")
            seleccion=input("> ")
            if seleccion=="1":
                listar_cursos()
            elif seleccion=="2":
                agregar_curso()
            elif seleccion=="3":
                update_curso()
            elif seleccion=="4":
                delete_curso()
            elif seleccion=="5":
                break
            else:
                print("Ingrese una opción válida")

    except Exception as e:
        print(e)

