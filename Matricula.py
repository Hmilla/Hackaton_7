from pymongo.message import update
from config.connection import Connection
from bson.objectid import ObjectId
import Alumnos
import Profesores
import Cursos
import Periodos
import Salones
class Matricula:
    def __init__(self, alumno,grado, profesor, curso, salon, periodo):
        self.alumno = alumno
        self.grado=grado
        self.profesor=profesor
        self.curso=curso
        self.salon=salon
        self.periodo=periodo

    # __str__ | solo string
    def __repr__(self): # representation
        return self.modelo

conn = Connection('Hackaton_7')

def all_matriculas():
    # Traer todos los datos
    matriculas_all = conn.get_all('Matriculas', {
        '_id': {
            '$ne': ''
        }
    }, {
        'alumno': 1,
        'grado':1,
        'profesor':1,
        'curso':1,
        'salon':1,
        'periodo':1
   })

    return list(matriculas_all)

def Agregar_alumno():
    id_alumno=Alumnos.select_Alumno()
    lista_alumnos=Alumnos.all_alumnos()
    for alumno in lista_alumnos:
        if alumno["_id"]==id_alumno:
            alumno_seleccionado=alumno
    Alumnos.print_one_alumno(id_alumno)
    if alumno_seleccionado["estado"]=="Inactivo":
        print("El estado de este alumno es 'Inactivo'. ¿Deseas cambiarlo antes de agregarlo a la matrícula? (1 = si / 2 = no)")
        si_o_no=input("> ")
        if si_o_no=="1":
            Alumnos.actualizar_Alumnos(id_alumno,{"estado":"Activo"})
            alumno_seleccionado["estado"]="Activo"
            print(f'Se cambio el estado del alumno {alumno_seleccionado["nombre"]} a "Activo"')

    return alumno_seleccionado

def Agregar_profesor():
    id_profesor=Profesores.select_Profesor()
    lista_profesores=Profesores.all_profesores()
    for profesor in lista_profesores:
        if profesor["_id"]==id_profesor:
            profesor_seleccionado=profesor
    Profesores.print_one_profesor(id_profesor)
    if profesor_seleccionado["estado"]=="Inactivo":
        print("El estado de este profesor es 'Inactivo'. ¿Deseas cambiarlo antes de agregarlo a la matrícula? (1 = si / 2 = no)")
        si_o_no=input("> ")
        if si_o_no=="1":
            Profesores.actualizar_Profesores(id_profesor,{"estado":"Activo"})
            profesor_seleccionado["estado"]="Activo"
            print(f'Se cambio el estado del profesor {profesor_seleccionado["nombre"]} a "Activo"')

    return profesor_seleccionado

def Agregar_curso():
    id_curso=Cursos.select_curso()
    lista_cursos=Cursos.all_cursos()
    for curso in lista_cursos:
        if curso["_id"]==id_curso:
            curso_seleccionado=curso
    return curso_seleccionado

def Agregar_salon():
    id_salon=Salones.select_salon()
    lista_salones=Salones.all_salones()
    for salon in lista_salones:
        if salon["_id"]==id_salon:
            salon_seleccionado=salon
    return salon_seleccionado

def Agregar_periodo():
    id_periodo=Periodos.select_periodo()
    lista_periodos=Periodos.all_periodos()
    for periodo in lista_periodos:
        if periodo["_id"]==id_periodo:
            periodo_seleccionado=periodo
    return periodo_seleccionado



def agregar_matricula():

    alumno=Agregar_alumno()
    while True:
        try:
            print("Ingrese el grado del alumno")
            grado=int(input("> "))
            if grado>6 or grado<=0:
                print("El grado del alumno debe ser un número del 1 al 6")
            else:
                break
        except Exception as e:
            print("Escribe un número")   

    profesor=Agregar_profesor()

    curso=Agregar_curso()

    salon=Agregar_salon()

    periodo=Agregar_periodo()
    new_matricula=Matricula(alumno, grado, profesor, curso, salon, periodo)
    conn.insert_many('Matriculas', [
        new_matricula.__dict__

    ])
    print("Se agregó la matrícula")

def select_matricula():
    opcion=-1
    opciones=[]
    ids=[]
    print("Selecciona una matrícula")
    lista_matricula=all_matriculas()
    for matricula_1 in lista_matricula:
        opcion+=1
        print(f'''{opcion+1} = MATRICULA {opcion+1}
        Alumno: {matricula_1["alumno"]["nombre"]} {matricula_1["alumno"]["apellido"]}
        Grado: {matricula_1["grado"]}
        Profesor: {matricula_1["profesor"]["nombre"]} {matricula_1["profesor"]["apellido"]}
        Curso: {matricula_1["curso"]["nombre"]}
        Salon: {matricula_1["salon"]["nombre"]}
        Periodo: año={matricula_1["periodo"]["año"]} | bimestre = {matricula_1["periodo"]["bimestre"]}
----------------------------------------------------------------------------''')

        
        ids.append(matricula_1["_id"])
        opciones.append(opcion)

    while True:
        try:
            seleccion=int(input(">"))
            if seleccion-1 in opciones:
                id_seleccionado=lista_matricula[seleccion-1]["_id"]
                break
            else:
                print("Elija una opción valida")

        except Exception as e:
            print(e)
            print("Escriba un número")
    
    print(f'Se seleccionó la matrícula {seleccion}')
    return id_seleccionado

def listar_all_matriculas():
    opcion=-1
    print("LISTA DE MATRICULAS")
    lista_matricula=all_matriculas()
    for matricula_1 in lista_matricula:
        opcion+=1
        print(f''' MATRICULA {opcion+1}
        Alumno: {matricula_1["alumno"]["nombre"]} {matricula_1["alumno"]["apellido"]}
        Grado: {matricula_1["grado"]}
        Profesor: {matricula_1["profesor"]["nombre"]} {matricula_1["profesor"]["apellido"]}
        Curso: {matricula_1["curso"]["nombre"]}
        Salon: {matricula_1["salon"]["nombre"]}
        Periodo: año={matricula_1["periodo"]["año"]} | bimestre = {matricula_1["periodo"]["bimestre"]}
----------------------------------------------------------------------------------------''')


def delete_matricula():
    id_matricula = select_matricula()
    print("¿Estas seguro que quieres eliminar esta matrícula? (1 = si/ 2 = no)")
    while True:
        seleccion=input("> ")
        if seleccion =="1":
            conn.delete_many('Matriculas', {
                '_id': {
                    '$eq': id_matricula
                }
            })
            print(f'Se eliminó la matrícula')
            break
        elif seleccion=="2":
            print("Saliendo...")
            break
        else:
            print("Elija una opción válida")

def menu_matriculas():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = listar matrículas")
            print("2 = insertar matrícula")
            print("3 = eliminar matrícula")
            print("4 = volver a menu")
            seleccion=input("> ")
            if seleccion=="1":
                listar_all_matriculas()
            elif seleccion=="2":
                agregar_matricula()
            elif seleccion=="3":
                delete_matricula()
            elif seleccion=="4":
                break
            else:
                print("Ingrese una opción válida")

    except Exception as e:
        print(e)
