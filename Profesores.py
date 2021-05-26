from config.connection import Connection
from bson.objectid import ObjectId


class  Profesor:
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

def insert_Profesor():
    try:
        
        print("ingrese el nombre del profesor")
        nombre=input("> ")
        print("ingrese el apellido del profesor")
        apellido=input("> ")
        print("ingrese el documento del profesor") 
        documento=input("> ")
        
        while True:
            try:
                print("Ingrese la fecha de nacimiento del profesor")
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

        print("ingrese el correo del profesor")
        correo=input(">")
        while True:
            print("Ingrese el estado del profesor (A=Activo I=Inactivo)")
            estado=input("> ")
            if estado=="A":
                estado="Activo"
                break
            elif estado=="I":
                estado="Inactivo"
                break
            else:
                print("Ingrese una opción válida")
        new_Profesor=Profesor(nombre, apellido, documento, fecha_nacimiento, correo, estado)
        conn.insert_many('Profesores', [
         new_Profesor.__dict__,
            ])
    
    except Exception as e:
        print(e)

def all_profesores():
    # Traer todos los datos
    profesores_all = conn.get_all('Profesores', {
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
    return list(profesores_all)

def print_all_profesores():
    all_profesor=all_profesores()
    for profesor in all_profesor:
        print(f'nombre: {profesor["nombre"]}')
        print(f'apellido: {profesor["apellido"]}')
        print(f'documento: {profesor["documento"]}')
        print(f'fecha de nacimiento: {profesor["fecha_nacimiento"]}')
        print(f'correo: {profesor["correo"]}')
        print(f'estado: {profesor["estado"]}')
        print("------------------------------------------")

def print_one_profesor(id):
    profesor_1 = conn.get_all('Profesores', {
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
    for profesor in profesor_1:
        print("------------------------------------------")
        print(f'nombre: {profesor["nombre"]}')
        print(f'apellido: {profesor["apellido"]}')
        print(f'documento: {profesor["documento"]}')
        print(f'fecha de nacimiento: {profesor["fecha_nacimiento"]}')
        print(f'correo: {profesor["correo"]}')
        print(f'estado: {profesor["estado"]}')
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

def select_Profesor():
    print("Elija un profesor")
    nombres=[]
    all_profesor=all_profesores()
    for profesor_1 in all_profesor:
        nombre=f'{profesor_1["nombre"]} {profesor_1["apellido"]}'
        nombres.append(nombre)

    repetidos=[]
    for profesor_2 in all_profesor:
        nombre_2=f'{profesor_2["nombre"]} {profesor_2["apellido"]}'
        num_rep=nombres.count(nombre_2)
        if num_rep>=2:
            repetidos.append(nombre_2)
        else:
            pass
    
    
    opcion=-1
    opciones=[]
    ids=[]
    documentos=[]
    for profesor in all_profesor:
        opcion+=1
        opciones.append(opcion)
        ids.append(profesor["_id"])
        documentos.append(profesor["documento"])
        seleccion=f'{profesor["nombre"]} {profesor["apellido"]}'
        if seleccion in repetidos:
            print(f'{opcion+1} = {profesor["nombre"]} {profesor["apellido"]} -> repetido (documento: {profesor["documento"]})')
        else:
            print(f'{opcion+1} = {profesor["nombre"]} {profesor["apellido"]}')
    while True:
        try:
            op_elegida=int(input("> "))
            op_validar=op_elegida-1
            if op_validar in opciones:
                if nombres[op_validar]in repetidos:
                    print(f'Se seleccionó al profesor/a {nombres[op_validar]} -> repetido (documento: {documentos[op_validar]})')
                else:
                    print(f'Se seleccionó al profesor/a {nombres[op_validar]}')
                id_seleccionado=ids[op_validar]
                break
            else:
                print("Ingrese una opción válida")

        except Exception as e:
            print(e)
            print("Ingrese un número")

    return id_seleccionado

def actualizar_Profesores(id, datos_cambio): 
    conn.update_many('Profesores', {
        '_id': {
            '$eq': id
        }
    }, datos_cambio)

def opciones_actualzar_profesor():
    id_profesor=select_Profesor()
    print("Datos actuales del profesor")
    print_one_profesor(id_profesor)
    
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
            print("ingrese el nuevo nombre del profesor")
            nombre=input("> ")
            actualizar_Profesores(id_profesor,{'nombre':nombre})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="2":
            print("ingrese el nuevo apellido del profesor")
            apellido=input("> ")
            actualizar_Profesores(id_profesor,{'apellido':apellido})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="3":
            print("ingrese el nuevo documento del profesor")
            documento=input("> ")
            actualizar_Profesores(id_profesor,{'documento':documento})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="4":
            while True:
                try:
                    print("Ingrese la nueva fecha de nacimiento del profesor")
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
            actualizar_Profesores(id_profesor,{'fecha_nacimiento':fecha_nacimiento})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="5":
            print("Ingrese el nuevo correo del profesor")
            correo=input("> ")
            actualizar_Profesores(id_profesor,{'correo':correo})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="6":
            while True:
                print("Ingrese el nuevo estado del profesor (A=Activo I=Inactivo)")
                estado=input("> ")
                if estado=="A":
                    estado="Activo"
                    break
                elif estado=="I":
                    estado="Inactivo"
                    break
                else:
                    print("Ingrese una opción válida")
            actualizar_Profesores(id_profesor,{'estado':estado})
            print("Nuevos datos del profesor")
            print_one_profesor(id_profesor)
        elif opcion=="7":
            break
        else:
            print("Escribe una opción válida")

def eliminar_profesor():
    id_profesor=select_Profesor()
    print("Datos del profesor")
    print_one_profesor(id_profesor)
    print("¿Estas seguro que quieres eliminar los datos de este profesor (1 = si / 2 = no)")
    while True:
        si_o_no=input("> ")
        if si_o_no=="1":
            conn.delete_many('Profesor', {
            '_id': {
            '$eq': id_profesor
            }
            })
            print("Se eliminaron los datos del profesor")
            break
        elif si_o_no=="2":
            print("saliendo...")
            break
        else:
            print("Error, ingresa una opcion válida")
        
def menu_profesor():
    try:
        while True:
            print("¿Que deseas hacer?")
            print("1 = Agregar profesor")
            print("2 = Ver datos de un profesor")
            print("3 = Ver datos de todos los profesores")
            print("4 = Actualizar datos de un profesor")
            print("5 = Eliminar datos de un profesor")
            print("6 = Volver a menu")
            opcion_menu_al=input("> ")
            if opcion_menu_al=="1":
                insert_Profesor()
            elif opcion_menu_al=="2":
                id_profesor=select_Profesor()
                print_one_profesor(id_profesor)
            elif opcion_menu_al=="3":
                print_all_profesores()
            elif opcion_menu_al=="4":
                opciones_actualzar_profesor()
            elif opcion_menu_al=="5":
                eliminar_profesor()
            elif opcion_menu_al=="6":
                break
            else:
                print("Ingresa una opción válida")
    except Exception as e:
        print (e)



