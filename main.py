import Alumnos
import Profesores
import Salones
import Cursos
import Periodos
import Matricula
import Registro

print("BIENVENIDO AL MENU DEL COLEGIO")
while True:
    try:
        print("Elija una opción")
        print("1 = Alumnos")
        print("2 = Profesores")
        print("3 = Salones")
        print("4 = Cursos")
        print("5 = Periodos")
        print("6 = Matriculas")
        print("7 = Registros")
        print("8 = Salir")
        opcion=input("> ")
        if opcion=="1":
            Alumnos.menu_alumno()
        elif opcion=="2":
            Profesores.menu_profesor()
        elif opcion=="3":
            Salones.menu_salones()
        elif opcion=="4":
            Cursos.menu_cursos()
        elif opcion=="5":
            Periodos.menu_periodos()
        elif opcion=="6":
            Matricula.menu_matriculas()
        elif opcion=="7":
            Registro.menu_registros()
        elif opcion=="8":
            break
        else:
            print("Ingresa una opción válida")

    except Exception as e :
        print(e)