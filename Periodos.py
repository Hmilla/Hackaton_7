from pymongo.message import update
from pymongo.topology import _is_stale_error_topology_version
from config.connection import Connection
from bson.objectid import ObjectId
class Periodo:
    def __init__(self, año, bimestre):
        self.año = año
        self.bimestre=bimestre

    # __str__ | solo string
    def __repr__(self): # representation
        return self.modelo

conn = Connection('Hackaton_7')

def all_periodos():
    # Traer todos los datos
    periodos_all = conn.get_all('Periodos', {
        '_id': {
            '$ne': ''
        }
    }, {
        'año': 1,
        'bimestre':1
   })

    return list(periodos_all)


def listar_periodos():
    lista_periodos=all_periodos()
    
    for periodo_1 in lista_periodos:
        print(f'año: {periodo_1["año"]}')
        print(f'bimestre: {periodo_1["bimestre"]}')
        print("--------------------------------")

def agregar_periodo():
    while True:
        try:
            print("Ingresa el año del periodo")
            año=int(input("> "))
            break
        except Exception as e :
            print(e)
            print("Escribe un número")
    while True:
        try:

            print("Ingresa el bimestre del periodo")
            bimestre=int(input("> "))
            if bimestre<=0 or bimestre>4:
                print("El bimestre debe ser un número del 1 al 4")
            else:
                break
        except Exception as e :
            print(e)
            print("Escribe un número")
    new_curso=Periodo(año,bimestre)
    conn.insert_many('Periodos', [
        new_curso.__dict__
    ])
    print("Se agregó el periodo")


def select_periodo():
    opcion=-1
    opciones=[]
    ids=[]
    print("Selecciona un periodo")
    lista_periodos=all_periodos()
    for periodo_1 in lista_periodos:
        opcion+=1
        print(f'{opcion+1} = periodo {opcion+1} (año: {periodo_1["año"]}|bimestre: {periodo_1["bimestre"]})')
        ids.append(periodo_1["_id"])
        opciones.append(opcion)

    while True:
        try:
            seleccion=int(input(">"))
            if seleccion-1 in opciones:
                id_seleccionado=lista_periodos[seleccion-1]["_id"]
                break
            else:
                print("Elija una opción valida")

        except Exception as e:
            print(e)
            print("Escriba un número")
    
    print(f'Se seleccionó el periodo con año = {lista_periodos[seleccion-1]["año"]} y bimestre = {lista_periodos[seleccion-1]["bimestre"]}')
    return id_seleccionado

def update_periodo():
    id_periodo = select_periodo()
    while True:
        print("¿Que deseas hacer?")
        print("1 = Actualizar año")
        print("2 = Actualizar bimestre")
        print("3 = Salir")
        seleccion=input("> ")
        if seleccion=="1":
            while True:
                try:
                    print("Ingresa el nuevo año del periodo")
                    año=int(input("> "))
                    update_id(id_periodo,{"año":año})
                    break
                except Exception as e :
                    print(e)
                    print("Escribe un número")
        elif seleccion=="2":
            while True:
                try:
                    print("Ingresa el nuevo bimestre del periodo")
                    bimestre=int(input("> "))
                    if bimestre<=0 or bimestre>4:
                        print("El bimestre debe ser un número del 1 al 4")
                    else:
                        update_id(id_periodo,{"bimestre":bimestre})
                        break
                except Exception as e :
                    print(e)
                    print("Escribe un número")
        elif seleccion =="3":
            break
        else:
            print("Ingresa una opción válida")



def update_id(id, datos_nuevos):

    conn.update_many('Periodos', {
        '_id': {
            '$eq': id
        }
    }, datos_nuevos)



def delete_periodo():
    id_periodo = select_periodo()
    print("¿Estas seguro que quieres eliminar este periodo? (1 = si/ 2 = no)")
    while True:
        seleccion=input("> ")
        if seleccion =="1":
            conn.delete_many('Periodos', {
                '_id': {
                    '$eq': id_periodo
                }
            })
            print(f'Se eliminó el periodo')
            break
        elif seleccion=="2":
            print("Saliendo...")
            break
        else:
            print("Elija una opción válida")

def menu_periodos():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = listar periodos")
            print("2 = insertar periodo")
            print("3 = actualizar nombre de periodo")
            print("4 = eliminar periodo")
            print("5 = volver a menu")
            seleccion=input("> ")
            if seleccion=="1":
                listar_periodos()
            elif seleccion=="2":
                agregar_periodo()
            elif seleccion=="3":
                update_periodo()
            elif seleccion=="4":
                delete_periodo()
            elif seleccion=="5":
                break
            else:
                print("Ingrese una opción válida")

    except Exception as e:
        print(e)
    

