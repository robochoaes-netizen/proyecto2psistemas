import os
from file_manager import FileManagerHistoriaClinica, FileManagerPaciente, FileManagerDoctor
from menus.menu_historias import mostrar_menu_historias

def ejecutar_menu_historias():
    fm_h = FileManagerHistoriaClinica()
    fm_p = FileManagerPaciente()
    fm_d = FileManagerDoctor()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_historias()
        opcion = input("Seleccione una opción: ")

        # Diccionarios de búsqueda rápida para nombres
        pacs = {p['id']: p['nombre'] for p in fm_p.get_all()}
        docs = {d['id']: d['nombre'] for d in fm_d.get_all()}

        if opcion == "1":
            # LISTAR TODO
            historias = fm_h.get_all()
            print("\n" + "-"*80)
            print(f"{'FECHA':<12} | {'PACIENTE':<15} | {'DOCTOR':<15} | {'DIAGNÓSTICO'}")
            print("-" * 80)
            
            for h in historias:
                nom_p = pacs.get(h['id_paciente'], "Desconocido")
                nom_d = docs.get(h['id_doctor'], "Desconocido")
                print(f"{h['fecha']:<12} | {nom_p[:15]:<15} | {nom_d[:15]:<15} | {h['diagnostico']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            # FILTRAR POR PACIENTE
            try:
                print("\n--- Seleccione el Paciente ---")
                for p_id, p_nom in pacs.items():
                    print(f"ID: {p_id} - {p_nom}")
                
                target = int(input("\nIngrese el ID del paciente: "))
                historias = fm_h.get_all()
                filtradas = [h for h in historias if h['id_paciente'] == target]

                if not filtradas:
                    print("\n[!] No se encontraron registros para este paciente.")
                else:
                    print(f"\nHistorial de: {pacs.get(target, 'Paciente ID '+str(target))}")
                    for h in filtradas:
                        nom_d = docs.get(h['id_doctor'], "Desconocido")
                        print(f"[{h['fecha']}] Dr. {nom_d}: {h['diagnostico']}")
                
            except ValueError:
                print("\n[!] Error: ID inválido.")
            input("\nPresione Enter...")

        elif opcion == "3":
            break