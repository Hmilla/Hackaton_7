from config.connection import Connection
from bson.objectid import ObjectId


class  Alumno:
    def __init__(self, nombre,apellido, documento, fecha_nacimiento, correo, estado):
        self.nombre=nombre
        self.apellido=apellido
        self.documento=documento
        self.fecha_nacimiento=fecha_nacimiento
        self.correo=correo
        self.estado=estado


    # __str__ | solo string
    def __repr__(self): # representation
        return self.nombre
    
conn = Connection('Hackaton_7')    

def insert_Alumno():
    try:
        
        print("ingrese el nombre del alumno")
        nombre=input("> ")
        print("ingrese el apellido del alumno")
        apellido=input("> ")
        print("ingrese el documento del alumno") 
        documento=input("> ")
        
        while True:
            try:
                print("Ingrese la fecha de nacimiento del alumno")
                print("Año")
                año=int(input("> "))
                while True:
                    print("Mes")
                    mes=int(input("> "))
                    if mes<=0 or mes>12:
                        print("Ingresa un mes válido")
                    else:
                        break
                while True:
                    print("Dia")
                    dia=int(input("> "))
                    if dia<=0 or dia>31:
                        print("Ingresa un día válido")
                    else:
                        break
                fecha_nacimiento=(f'{dia}/{mes}/{año}')
                break

            except Exception as e:
                print(e)
                print("Error, debes escribir un número")

        print("ingrese el correo del alumno")
        correo=input(">")
        while True:
            print("Ingrese el estado del alumno (A=Activo I=Inactivo)")
            estado=input("> ")
            if estado=="A":
                estado="Activo"
                break
            elif estado=="I":
                estado="Inactivo"
                break
            else:
                print("Ingrese una opción válida")
        new_Alumno=Alumno(nombre, apellido, documento, fecha_nacimiento, correo, estado)
        conn.insert_many('Alumnos', [
         new_Alumno.__dict__,
            ])
    
    except Exception as e:
        print(e)

def all_alumnos():
    # Traer todos los datos
    alumnos_all = conn.get_all('Alumnos', {
    '_id': {
        '$ne': ''
    }
    }, {
        'nombre': 1,
        'apellido':1,
        'documento': 1,
        'fecha_nacimiento':1,
        'correo':1,
        'estado':1
    })
    return list(alumnos_all)

def print_all_alumnos():
    all_alumno=all_alumnos()
    for alumno in all_alumno:
        print(f'nombre: {alumno["nombre"]}')
        print(f'apellido: {alumno["apellido"]}')
        print(f'documento: {alumno["documento"]}')
        print(f'fecha de nacimiento: {alumno["fecha_nacimiento"]}')
        print(f'correo: {alumno["correo"]}')
        print(f'estado: {alumno["estado"]}')
        print("------------------------------------------")

def print_one_alumno(id):
    alumno_1 = conn.get_all('Alumnos', {
    '_id': {
        '$eq': id
    }
    }, {
        'nombre': 1,
        'apellido':1,
        'documento': 1,
        'fecha_nacimiento':1,
        'correo':1,
        'estado':1
    })
    for alumno in alumno_1:
        print("------------------------------------------")
        print(f'nombre: {alumno["nombre"]}')
        print(f'apellido: {alumno["apellido"]}')
        print(f'documento: {alumno["documento"]}')
        print(f'fecha de nacimiento: {alumno["fecha_nacimiento"]}')
        print(f'correo: {alumno["correo"]}')
        print(f'estado: {alumno["estado"]}')
        print("------------------------------------------")

#Traer un dato
#mobile = conn.get_one('alumno', {
#    'nombre': {
#        '$eq': 'Heber'
#    }
#}, {
#    'nombre': 1,
#    'documento': 1
#})
#print(mobile)

def select_Alumno():
    print("Elija un alumno")
    nombres=[]
    all_alumno=all_alumnos()
    for alumno_1 in all_alumno:
        nombre=f'{alumno_1["nombre"]} {alumno_1["apellido"]}'
        nombres.append(nombre)

    repetidos=[]
    for alumno_2 in all_alumno:
        nombre_2=f'{alumno_2["nombre"]} {alumno_2["apellido"]}'
        num_rep=nombres.count(nombre_2)
        if num_rep>=2:
            repetidos.append(nombre_2)
        else:
            pass
    
    
    opcion=-1
    opciones=[]
    ids=[]
    documentos=[]
    for alumno in all_alumno:
        opcion+=1
        opciones.append(opcion)
        ids.append(alumno["_id"])
        documentos.append(alumno["documento"])
        seleccion=f'{alumno["nombre"]} {alumno["apellido"]}'
        if seleccion in repetidos:
            print(f'{opcion+1} = {alumno["nombre"]} {alumno["apellido"]} -> repetido (documento: {alumno["documento"]})')
        else:
            print(f'{opcion+1} = {alumno["nombre"]} {alumno["apellido"]}')
    while True:
        try:
            op_elegida=int(input("> "))
            op_validar=op_elegida-1
            if op_validar in opciones:
                if nombres[op_validar]in repetidos:
                    print(f'Se seleccionó al alumno/a {nombres[op_validar]} -> repetido (documento: {documentos[op_validar]})')
                else:
                    print(f'Se seleccionó al alumno/a {nombres[op_validar]}')
                id_seleccionado=ids[op_validar]
                break
            else:
                print("Ingrese una opción válida")

        except Exception as e:
            print(e)
            print("Ingrese un número")

    return id_seleccionado

def actualizar_Alumnos(id, datos_cambio): 
    conn.update_many('Alumnos', {
        '_id': {
            '$eq': id
        }
    }, datos_cambio)

def opciones_actualzar_alumno():
    id_alumno=select_Alumno()
    print("Datos actuales del alumno")
    print_one_alumno(id_alumno)
    
    while True:
        print("¿Que deseas hacer?")
        print("1 = actualizar nombre")
        print("2 = actualizar apellido")
        print("3 = actualizar documento")
        print("4 = actualizar fecha de nacimiento")
        print("5 = actualizar correo")
        print("6 = actualizar estado")
        print("7 = Salir")
        opcion=input(">")
        if opcion=="1":
            print("ingrese el nuevo nombre del alumno")
            nombre=input("> ")
            actualizar_Alumnos(id_alumno,{'nombre':nombre})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="2":
            print("ingrese el nuevo apellido del alumno")
            apellido=input("> ")
            actualizar_Alumnos(id_alumno,{'apellido':apellido})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="3":
            print("ingrese el nuevo documento del alumno")
            documento=input("> ")
            actualizar_Alumnos(id_alumno,{'documento':documento})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="4":
            while True:
                try:
                    print("Ingrese la nueva fecha de nacimiento del alumno")
                    print("Año")
                    año=int(input("> "))
                    while True:
                        print("Mes")
                        mes=int(input("> "))
                        if mes<=0 or mes>12:
                            print("Ingresa un mes válido")
                        else:
                            break
                    while True:
                        print("Dia")
                        dia=int(input("> "))
                        if dia<=0 or dia>31:
                            print("Ingresa un día válido")
                        else:
                            break
                    fecha_nacimiento=(f'{dia}/{mes}/{año}')
                    break

                except Exception as e:
                    print(e)
                    print("Error, debes escribir un número")
            actualizar_Alumnos(id_alumno,{'fecha_nacimiento':fecha_nacimiento})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="5":
            print("Ingrese el nuevo correo del alumno")
            correo=input("> ")
            actualizar_Alumnos(id_alumno,{'correo':correo})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="6":
            while True:
                print("Ingrese el nuevo estado del alumno (A=Activo I=Inactivo)")
                estado=input("> ")
                if estado=="A":
                    estado="Activo"
                    break
                elif estado=="I":
                    estado="Inactivo"
                    break
                else:
                    print("Ingrese una opción válida")
            actualizar_Alumnos(id_alumno,{'estado':estado})
            print("Nuevos datos del alumno")
            print_one_alumno(id_alumno)
        elif opcion=="7":
            break
        else:
            print("Escribe una opción válida")

def eliminar_alumno():
    id_alumno=select_Alumno()
    print("Datos del alumno")
    print_one_alumno(id_alumno)
    print("¿Estas seguro que quieres eliminar los datos de este alumno (1 = si / 2 = no)")
    while True:
        si_o_no=input("> ")
        if si_o_no=="1":
            conn.delete_many('Alumnos', {
            '_id': {
            '$eq': id_alumno
            }
            })
            print("Se eliminaron los datos del alumno")
            break
        elif si_o_no=="2":
            print("saliendo...")
            break
        else:
            print("Error, ingresa una opcion válida")
        
def menu_alumno():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = Agregar alumno")
            print("2 = Ver datos de un alumno")
            print("3 = Ver datos de todos los alumnos")
            print("4 = Actualizar datos de un alumno")
            print("5 = Eliminar datos de un alumno")
            print("6 = Volver a menu")
            opcion_menu_al=input("> ")
            if opcion_menu_al=="1":
                insert_Alumno()
            elif opcion_menu_al=="2":
                id_alumno=select_Alumno()
                print_one_alumno(id_alumno)
            elif opcion_menu_al=="3":
                print_all_alumnos()
            elif opcion_menu_al=="4":
                opciones_actualzar_alumno()
            elif opcion_menu_al=="5":
                eliminar_alumno()
            elif opcion_menu_al=="6":
                break
            else:
                print("Ingresa una opción válida")
    except Exception as e:
        print(e)
