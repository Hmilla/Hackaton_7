from pymongo.message import update
from config.connection import Connection
from bson.objectid import ObjectId
import Matricula
class Registro:
    def __init__(self, matricula, nota):
        self.matricula=matricula
        self.nota=nota
    # __str__ | solo string
    def __repr__(self): # representation
        return self.modelo

conn = Connection('Hackaton_7')

def all_registros():
    # Traer todos los datos
    registros_all = conn.get_all('Registros', {
        '_id': {
            '$ne': ''
        }
    }, {
        'matricula': 1,
        'nota':1
   })

    return list(registros_all)

def agregar_registro():
    matricula=agregar_matricula()
    print("Escriba la nota del alumno")
    while True:
        try:
            nota=int(input("> "))
            if nota<0 or nota>20:
                print("La nota no puede ser menor a 0 ni mayor a 20")
            else:
                break
        except Exception as e:
            print(e)
            print("Escribe un número")
    new_registro=Registro(matricula, nota)
    conn.insert_many('Registros', [
        new_registro.__dict__

    ])
    print("Se inserto el registro")
def listar_registros():
    lista_registos=all_registros()
    opcion=0
    
    for registro_1 in lista_registos:
        opcion+=1
        print(f'REGISTRO {opcion}')
        matricula_1=registro_1["matricula"]
        print(f'''MATRICULA {opcion}
        Alumno: {matricula_1["alumno"]["nombre"]} {matricula_1["alumno"]["apellido"]}
        Grado: {matricula_1["grado"]}
        Profesor: {matricula_1["profesor"]["nombre"]} {matricula_1["profesor"]["apellido"]}
        Curso: {matricula_1["curso"]["nombre"]}
        Salon: {matricula_1["salon"]["nombre"]}
        Periodo: año={matricula_1["periodo"]["año"]} | bimestre = {matricula_1["periodo"]["bimestre"]}''')
        print("")
        print(f'NOTA {registro_1["nota"]}')
        print("----------------------------------------------------------------------")

def agregar_matricula():
    id_matricula=Matricula.select_matricula()
    lista_matricula=Matricula.all_matriculas()
    for matricula in lista_matricula:
        if matricula["_id"]==id_matricula:
            matricula_seleccionada=matricula
    
    return matricula_seleccionada

def select_Registro():
    opcion=-1
    opciones=[]
    ids=[]
    print("Selecciona un registro")
    lista_registros=all_registros()
    for registro_1 in lista_registros:
        opcion+=1
        print(f'{opcion+1} = REGISTRO {opcion+1}')
        matricula_1=registro_1["matricula"]
        print(f'''MATRICULA {opcion+1}
        Alumno: {matricula_1["alumno"]["nombre"]} {matricula_1["alumno"]["apellido"]}
        Grado: {matricula_1["grado"]}
        Profesor: {matricula_1["profesor"]["nombre"]} {matricula_1["profesor"]["apellido"]}
        Curso: {matricula_1["curso"]["nombre"]}
        Salon: {matricula_1["salon"]["nombre"]}
        Periodo: año={matricula_1["periodo"]["año"]} | bimestre = {matricula_1["periodo"]["bimestre"]}''')
        print("")
        print(f'NOTA {registro_1["nota"]}')
        print("----------------------------------------------------------------------")
        ids.append(registro_1["_id"])
        opciones.append(opcion)

    while True:
        try:
            seleccion=int(input(">"))
            if seleccion-1 in opciones:
                id_seleccionado=lista_registros[seleccion-1]["_id"]
                break
            else:
                print("Elija una opción valida")

        except Exception as e:
            print(e)
            print("Escriba un número")
    
    print(f'Se seleccionó el registro')
    return id_seleccionado


def delete_registro():
    id_registro = select_Registro()
    print("¿Estas seguro que quieres eliminar este registro? (1 = si/ 2 = no)")
    while True:
        seleccion=input("> ")
        if seleccion =="1":
            conn.delete_many('Registros', {
                '_id': {
                    '$eq': id_registro
                }
            })
            print(f'Se eliminó el registro')
            break
        elif seleccion=="2":
            print("Saliendo...")
            break
        else:
            print("Elija una opción válida")


def menu_registros():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = listar registros")
            print("2 = insertar registro")
            print("3 = eliminar registro")
            print("4 = volver a menu")
            seleccion=input("> ")
            if seleccion=="1":
                listar_registros()
            elif seleccion=="2":
                agregar_registro()
            elif seleccion=="3":
                delete_registro()
            elif seleccion=="4":
                break
            else:
                print("Ingrese una opción válida")

    except Exception as e:
        print(e)

