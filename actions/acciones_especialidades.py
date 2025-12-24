import os
from file_manager import FileManagerEspecialidad
from menus.menu_especialidades import mostrar_menu_especialidades

def ejecutar_menu_especialidades():
    fm = FileManagerEspecialidad()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_especialidades()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # LISTAR
            especialidades = fm.get_all()
            print("\n" + "-"*30)
            print(f"{'ID':<5} | {'NOMBRE'}")
            print("-"*30)
            if not especialidades:
                print("No hay especialidades registradas.")
            else:
                for e in especialidades:
                    print(f"{e['id']:<5} | {e['nombre']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            # INSERTAR
            nombre = input("Nombre de la nueva especialidad (ej. Pediatría): ")
            if nombre.strip():
                fm.insert(nombre)
                print("\n[!] Especialidad registrada con éxito.")
            else:
                print("\n[!] Error: El nombre no puede estar vacío.")
            input("Presione Enter...")

        elif opcion == "3":
            # SALIR AL MAIN
            break
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter...")