import os
from file_manager import FileManagerPaciente
from menus.menu_pacientes import mostrar_menu_pacientes

def ejecutar_menu_pacientes():
    fm = FileManagerPaciente()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_pacientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # LISTAR
            pacientes = fm.get_all()
            print("\n" + "-"*50)
            print(f"{'ID':<5} | {'NOMBRE':<20} | {'EDAD':<5} | {'CÉDULA'}")
            print("-"*50)
            if not pacientes:
                print("No hay pacientes registrados.")
            else:
                for p in pacientes:
                    print(f"{p['id']:<5} | {p['nombre']:<20} | {p['edad']:<5} | {p['cedula']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            # INSERTAR
            try:
                nombre = input("Nombre completo: ")
                edad = int(input("Edad: "))
                cedula = input("Cédula/DNI: ")
                fm.insert(nombre, edad, cedula)
                print("\n[!] Paciente registrado con éxito.")
            except ValueError:
                print("\n[!] Error: La edad debe ser un número.")
            input("Presione Enter...")

        elif opcion == "3":
            # ACTUALIZAR
            try:
                id_mod = int(input("ID del paciente a modificar: "))
                nombre = input("Nuevo nombre: ")
                edad = int(input("Nueva edad: "))
                cedula = input("Nueva cédula: ")
                if fm.update(id_mod, nombre, edad, cedula):
                    print("\n[!] Datos actualizados correctamente.")
                else:
                    print("\n[!] Error: No se encontró el paciente con ese ID.")
            except ValueError:
                print("\n[!] Error: Ingrese datos válidos.")
            input("Presione Enter...")

        elif opcion == "4":
            # ELIMINAR
            try:
                id_del = int(input("ID del paciente a eliminar: "))
                confirmar = input(f"¿Seguro que desea eliminar al ID {id_del}? (s/n): ")
                if confirmar.lower() == 's':
                    if fm.delete(id_del):
                        print("\n[!] Paciente eliminado satisfactoriamente.")
                    else:
                        print("\n[!] Error: ID no encontrado.")
            except ValueError:
                print("\n[!] Error: ID inválido.")
            input("Presione Enter...")

        elif opcion == "5":
            # SALIR
            break
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter...")