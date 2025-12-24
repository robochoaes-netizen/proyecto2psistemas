import os
from file_manager import FileManagerPaciente, FileManagerDoctor, FileManagerHistoriaClinica

def ejecutar_reporte_medico():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Instanciamos los managers para obtener los datos
    fm_p = FileManagerPaciente()
    fm_d = FileManagerDoctor()
    fm_h = FileManagerHistoriaClinica()

    historias = fm_h.get_all()
    
    print("======================================================================")
    print("                REPORTE MÉDICO INTEGRAL (HISTORIAL)                   ")
    print("======================================================================")

    if not historias:
        print("\n[!] No existen registros médicos para generar el reporte.")
    else:
        # Creamos diccionarios de búsqueda rápida para no leer el archivo en cada vuelta del ciclo
        dict_pacientes = {p['id']: p['nombre'] for p in fm_p.get_all()}
        dict_doctores = {d['id']: d['nombre'] for d in fm_d.get_all()}

        # Encabezado de la tabla
        print(f"{'FECHA':<12} | {'PACIENTE':<18} | {'DOCTOR':<18} | {'DIAGNÓSTICO'}")
        print("-" * 70)

        for h in historias:
            nombre_p = dict_pacientes.get(h['id_paciente'], "Desconocido")
            nombre_d = dict_doctores.get(h['id_doctor'], "Desconocido")
            
            # Formateamos para que la tabla no se rompa si el texto es muy largo
            print(f"{h['fecha']:<12} | {nombre_p[:18]:<18} | {nombre_d[:18]:<18} | {h['diagnostico']}")

    print("======================================================================")
    input("\nPresione Enter para regresar al menú principal...")