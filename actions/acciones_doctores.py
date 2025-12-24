import os
from file_manager import FileManagerDoctor, FileManagerEspecialidad
from menus.menu_doctores import mostrar_menu_doctores

def ejecutar_menu_doctores():
    fm_doc = FileManagerDoctor()
    fm_esp = FileManagerEspecialidad() 
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_doctores()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # LISTAR
            doctores = fm_doc.get_all()
            especialidades = {e['id']: e['nombre'] for e in fm_esp.get_all()}
            
            print("\n" + "-"*60)
            print(f"{'ID':<5} | {'NOMBRE':<20} | {'ESPECIALIDAD'}")
            print("-"*60)
            if not doctores:
                print("No hay doctores registrados.")
            else:
                for d in doctores:
                    nombre_esp = especialidades.get(d['id_especialidad'], "N/A")
                    print(f"{d['id']:<5} | {d['nombre']:<20} | {nombre_esp}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            # INSERTAR
            try:
                nombre = input("Nombre del doctor: ")
                print("\nEspecialidades disponibles:")
                for e in fm_esp.get_all():
                    print(f"ID: {e['id']} - {e['nombre']}")
                
                id_esp = int(input("\nID de la especialidad: "))
                fm_doc.insert(nombre, id_esp)
                print("\n[!] Doctor registrado con éxito.")
            except ValueError:
                print("\n[!] Error: El ID de especialidad debe ser un número.")
            input("Presione Enter...")

        elif opcion == "3":
            # ACTUALIZAR
            try:
                id_mod = int(input("ID del doctor a modificar: "))
                nombre = input("Nuevo nombre: ")
                id_esp = int(input("Nuevo ID de especialidad: "))
                if fm_doc.update(id_mod, nombre, id_esp):
                    print("\n[!] Datos actualizados correctamente.")
                else:
                    print("\n[!] Error: No se encontró el doctor.")
            except ValueError:
                print("\n[!] Error: Datos inválidos.")
            input("Presione Enter...")

        elif opcion == "4":
            # ELIMINAR
            try:
                id_del = int(input("ID del doctor a eliminar: "))
                confirmar = input(f"¿Seguro que desea eliminar al doctor {id_del}? (s/n): ")
                if confirmar.lower() == 's':
                    if fm_doc.delete(id_del):
                        print("\n[!] Doctor eliminado del sistema.")
                    else:
                        print("\n[!] Error: ID no encontrado.")
            except ValueError:
                print("\n[!] Error: ID inválido.")
            input("Presione Enter...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter...")