from pymongo.message import update
from config.connection import Connection
from bson.objectid import ObjectId
class Salon:
    def __init__(self, nombre):
        self.nombre = nombre

    # __str__ | solo string
    def __repr__(self): # representation
        return self.modelo

conn = Connection('Hackaton_7')

def all_salones():
    # Traer todos los datos
    cursos_all = conn.get_all('Salones', {
        '_id': {
            '$ne': ''
        }
    }, {
        'nombre': 1,
   })

    return list(cursos_all)


def listar_salones():
    lista_salones=all_salones()
    
    for salon_1 in lista_salones:
        print(f'- {salon_1["nombre"]}')

def agregar_salon():
    print("Escribe el nombre del salon")
    nombre=input("> ")
    new_salon=Salon(nombre)
    conn.insert_many('Salones', [
        new_salon.__dict__

    ])
    print("Se agregó el salon ", nombre)

def select_salon():
    opcion=-1
    opciones=[]
    ids=[]
    print("Selecciona un salon")
    lista_salones=all_salones()
    for salon_1 in lista_salones:
        opcion+=1
        print(f'{opcion+1} = {salon_1["nombre"]}')
        ids.append(salon_1["_id"])
        opciones.append(opcion)

    while True:
        try:
            seleccion=int(input(">"))
            if seleccion-1 in opciones:
                id_seleccionado=lista_salones[seleccion-1]["_id"]
                break
            else:
                print("Elija una opción valida")

        except Exception as e:
            print(e)
            print("Escriba un número")
    
    print(f'Se seleccionó el salon {lista_salones[seleccion-1]["nombre"]}')
    return id_seleccionado

def update_salon():
    id_salon = select_salon()
    print("Cual va a ser el nuevo nombre del salon")
    nombre=input("> ")
    conn.update_many('Salones', {
        '_id': {
            '$eq': id_salon
        }
    }, {
        'nombre': nombre
    })
    print(f'Se cambió el nombre del salon a {nombre}')


def delete_salon():
    id_salon = select_salon()
    print("¿Estas seguro que quieres eliminar este salon? (1 = si/ 2 = no)")
    while True:
        seleccion=input("> ")
        if seleccion =="1":
            conn.delete_many('Salones', {
                '_id': {
                    '$eq': id_salon
                }
            })
            print(f'Se eliminó el salon')
            break
        elif seleccion=="2":
            print("Saliendo...")
            break
        else:
            print("Elija una opción válida")

def menu_salones():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = listar salons")
            print("2 = insertar salon")
            print("3 = actualizar nombre de salon")
            print("4 = eliminar salon")
            print("5 = volver a menu")
            seleccion=input("> ")
            if seleccion=="1":
                listar_salones()
            elif seleccion=="2":
                agregar_salon()
            elif seleccion=="3":
                update_salon()
            elif seleccion=="4":
                delete_salon()
            elif seleccion=="5":
                break
            else:
                print("Ingrese una opción válida")

    except Exception as e:
        print(e)


