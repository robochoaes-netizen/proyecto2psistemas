import os
import sys

# Forzamos a Python a reconocer la carpeta actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones directas de módulos
from menus.menu_principal import mostrar_menu_principal
from actions.acciones_pacientes import ejecutar_menu_pacientes
from actions.acciones_doctores import ejecutar_menu_doctores
from actions.acciones_especialidades import ejecutar_menu_especialidades
from actions.acciones_citas import ejecutar_menu_citas
from actions.acciones_historias import ejecutar_menu_historias
from actions.acciones_reportes import ejecutar_reporte_medico

def main():
    while True:
        # Limpiar pantalla
        os.system("cls" if os.name == "nt" else "clear")
        
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_menu_pacientes()
        elif opcion == "2":
            ejecutar_menu_especialidades()
        elif opcion == "3":
            ejecutar_menu_doctores()
        elif opcion == "4":
            # Transacción: Agendar Cita con validación
            ejecutar_menu_citas()
        elif opcion == "5":
            # Consulta de Historias Clínicas
            ejecutar_menu_historias()
        elif opcion == "6":
            ejecutar_reporte_medico()
        elif opcion == "7":
            print("\nSaliendo del SISTEMA MÉDICO. ¡Hasta pronto!")
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()