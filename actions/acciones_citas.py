import os
from file_manager import FileManagerCita, FileManagerPaciente, FileManagerDoctor
from menus.menu_citas import mostrar_menu_citas

def ejecutar_menu_citas():
    fm_cita = FileManagerCita()
    fm_pac = FileManagerPaciente()
    fm_doc = FileManagerDoctor()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_citas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # LISTAR CITAS
            citas = fm_cita.get_all()
            # Diccionarios rápidos para mostrar nombres
            pacs = {p['id']: p['nombre'] for p in fm_pac.get_all()}
            docs = {d['id']: d['nombre'] for d in fm_doc.get_all()}
            
            print("\n" + "-"*75)
            print(f"{'ID':<4} | {'PACIENTE':<15} | {'DOCTOR':<15} | {'FECHA':<10} | {'HORA':<6} | {'ESTADO'}")
            print("-" * 75)
            for c in citas:
                nom_p = pacs.get(c['id_paciente'], "N/A")
                nom_d = docs.get(c['id_doctor'], "N/A")
                print(f"{c['id']:<4} | {nom_p[:15]:<15} | {nom_d[:15]:<15} | {c['fecha']:<10} | {c['hora']:<6} | {c['estado']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            # INSERTAR (AGENDAR)
            try:
                # Mostrar pacientes y doctores para referencia
                print("\n--- Pacientes ---")
                for p in fm_pac.get_all(): print(f"ID: {p['id']} - {p['nombre']}")
                id_p = int(input("\nID del Paciente: "))
                
                print("\n--- Doctores ---")
                for d in fm_doc.get_all(): print(f"ID: {d['id']} - {d['nombre']}")
                id_d = int(input("\nID del Doctor: "))
                
                fecha = input("Fecha (DD/MM/AAAA): ")
                hora = input("Hora (HH:MM): ")
                
                resultado = fm_cita.insert(id_p, id_d, fecha, hora)
                if resultado:
                    print("\n[!] Cita agendada con éxito.")
                else:
                    print("\n[!] ERROR: El doctor ya tiene una cita en esa fecha y hora.")
            except ValueError:
                print("\n[!] Error: Ingrese IDs válidos.")
            input("Presione Enter...")

        elif opcion == "3":
            # FINALIZAR (TRANSACCIÓN)
            try:
                id_c = int(input("ID de la cita a finalizar: "))
                diag = input("Ingrese el Diagnóstico Médico: ")
                
                if fm_cita.finalizar_cita(id_c, diag):
                    print("\n[!] Cita finalizada. Se ha generado la Historia Clínica automáticamente.")
                else:
                    print("\n[!] Error: La cita no existe o ya estaba finalizada.")
            except ValueError:
                print("\n[!] Error: ID inválido.")
            input("Presione Enter...")

        elif opcion == "4":
            break