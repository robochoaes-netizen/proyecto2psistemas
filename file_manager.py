import os

# --- 1. PACIENTES ---
class FileManagerPaciente:
    def __init__(self, filename="data/pacientes.txt", counter_file="data/cont_pacientes.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Paciente
        pacientes = {}
        if not os.path.exists(self.filename): return pacientes
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Paciente.from_line(line)
                    # Cambiado de obj.datos['id'] a obj['id']
                    pacientes[obj['id']] = obj
        return pacientes

    def get_all(self):
        # Cambiado de p.datos a p
        return [p for p in self._read_file().values()]

    def _write_file(self, pacientes):
        with open(self.filename, "w") as f:
            for p in pacientes.values():
                f.write(p.to_line() + "\n")

    def insert(self, nombre, edad, cedula):
        from models import Paciente
        new_id = self._get_next_id()
        p = Paciente(new_id, nombre, edad, cedula)
        with open(self.filename, "a") as f:
            f.write(p.to_line() + "\n")
        return p.datos

    def update(self, id, nombre, edad, cedula):
        pacientes = self._read_file()
        if id in pacientes:
            pacientes[id].datos.update({"nombre": nombre, "edad": edad, "cedula": cedula})
            self._write_file(pacientes)
            return True
        return False

    def delete(self, id):
        pacientes = self._read_file()
        if id in pacientes:
            del pacientes[id]
            self._write_file(pacientes)
            return True
        return False


# --- 2. DOCTORES ---
class FileManagerDoctor:
    def __init__(self, filename="data/doctores.txt", counter_file="data/cont_doctores.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Doctor
        doctores = {}
        if not os.path.exists(self.filename): return doctores
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Doctor.from_line(line)
                    doctores[obj['id']] = obj 
        return doctores

    def get_all(self):
        return [d for d in self._read_file().values()]

    def _write_file(self, doctores):
        with open(self.filename, "w") as f:
            for d in doctores.values():
                f.write(d.to_line() + "\n")

    def insert(self, nombre, id_especialidad):
        from models import Doctor
        new_id = self._get_next_id()
        d = Doctor(new_id, nombre, id_especialidad)
        with open(self.filename, "a") as f:
            f.write(d.to_line() + "\n")
        return d.datos

    def update(self, id, nombre, id_especialidad):
        doctores = self._read_file()
        if id in doctores:
            doctores[id].datos.update({"nombre": nombre, "id_especialidad": id_especialidad})
            self._write_file(doctores)
            return True
        return False

    def delete(self, id):
        doctores = self._read_file()
        if id in doctores:
            del doctores[id]
            self._write_file(doctores)
            return True
        return False

 
# --- 3. ESPECIALIDADES ---
class FileManagerEspecialidad:
    def __init__(self, filename="data/especialidades.txt", counter_file="data/cont_especialidades.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Especialidad
        especialidades = {}
        if not os.path.exists(self.filename): return especialidades
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Especialidad.from_line(line)
                    especialidades[obj['id']] = obj 
        return especialidades

    def get_all(self):
        return [e for e in self._read_file().values()]

    def insert(self, nombre):
        from models import Especialidad
        new_id = self._get_next_id()
        e = Especialidad(new_id, nombre)
        with open(self.filename, "a") as f:
            f.write(e.to_line() + "\n")
        return e.datos


# --- 4. CITAS ---
class FileManagerCita:
    def __init__(self, filename="data/citas.txt", counter_file="data/cont_citas.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Cita
        citas = {}
        if not os.path.exists(self.filename): return citas
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Cita.from_line(line)
                    # CORRECCIÓN: Usamos obj['id'] porque es un diccionario
                    citas[obj['id']] = obj 
        return citas

    def get_all(self):
        # CORRECCIÓN: Se quita el .datos para que devuelva la lista de diccionarios
        return [c for c in self._read_file().values()]

    def _write_file(self, citas):
        with open(self.filename, "w") as f:
            for c in citas.values():
                # Construimos la línea manualmente usando las llaves del diccionario
                # Asegúrate de que el orden sea: id|id_paciente|id_doctor|fecha|hora|estado
                linea = f"{c['id']}|{c['id_paciente']}|{c['id_doctor']}|{c['fecha']}|{c['hora']}|{c['estado']}"
                f.write(linea + "\n")

    def insert(self, id_paciente, id_doctor, fecha, hora):
        from models import Cita
        actuales = self._read_file()
        
        # CORRECCIÓN: Validamos usando corchetes porque 'c' es un diccionario
        for c in actuales.values():
            if (c['id_doctor'] == id_doctor and 
                c['fecha'] == fecha and 
                c['hora'] == hora):
                return None # Ya existe una cita a esa hora
        
        new_id = self._get_next_id()
        # El estado inicial siempre es PENDIENTE
        estado = "PENDIENTE"
        
        # Guardamos en el archivo TXT (Formato: id|id_p|id_d|fecha|hora|estado)
        with open(self.filename, "a") as f:
            linea = f"{new_id}|{id_paciente}|{id_doctor}|{fecha}|{hora}|{estado}"
            f.write(linea + "\n")
            
        # Retornamos el diccionario para que el Action sepa que fue exitoso
        return {"id": new_id, "id_paciente": id_paciente, "id_doctor": id_doctor, 
                "fecha": fecha, "hora": hora, "estado": estado}

    def finalizar_cita(self, id_cita, diagnostico):
        citas = self._read_file()
        
        # Acceso con corchetes porque es un diccionario
        if id_cita in citas and citas[id_cita]['estado'] == "PENDIENTE":
            citas[id_cita]['estado'] = "FINALIZADA"
            
            # Aquí es donde se llama al _write_file que acabamos de corregir
            self._write_file(citas)
            
            # Guardamos en el historial
            fm_hist = FileManagerHistoriaClinica()
            fm_hist.insert(
                citas[id_cita]['id_paciente'],
                citas[id_cita]['fecha'],
                diagnostico,
                citas[id_cita]['id_doctor']
            )
            return True
        return False

# --- 5. HISTORIA CLÍNICA ---
class FileManagerHistoriaClinica:
    def __init__(self, filename="data/historias.txt", counter_file="data/cont_historias.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def insert(self, id_paciente, fecha, diagnostico, id_doctor):
        from models import HistoriaClinica
        new_id = self._get_next_id()
        h = HistoriaClinica(new_id, id_paciente, fecha, diagnostico, id_doctor)
        with open(self.filename, "a") as f:
            f.write(h.to_line() + "\n")
        return h.datos

    def _read_file(self):
        from models import HistoriaClinica
        historias = {}
        if not os.path.exists(self.filename): return historias
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = HistoriaClinica.from_line(line)
                    # CORRECCIÓN: Acceso directo al ID del diccionario
                    historias[obj['id']] = obj 
        return historias

    def get_all(self):
        # CORRECCIÓN: Se elimina el .datos
        return [h for h in self._read_file().values()]

    def obtener_datos_reporte(self):
        from file_manager import FileManagerPaciente, FileManagerDoctor
        
        fm_p = FileManagerPaciente()
        fm_d = FileManagerDoctor()
        
        # CORRECCIÓN: Como get_all ya devuelve diccionarios, 
        # accedemos con ['id'] y ['nombre']
        nombres_pacientes = {p['id']: p['nombre'] for p in fm_p.get_all()}
        nombres_doctores = {d['id']: d['nombre'] for d in fm_d.get_all()}
        
        historias = self.get_all()
        reporte_final = []
        
        for h in historias:
            reporte_final.append({
                "fecha": h['fecha'],
                "paciente": nombres_pacientes.get(h['id_paciente'], "Desconocido"),
                "doctor": nombres_doctores.get(h['id_doctor'], "Desconocido"),
                "diagnostico": h['diagnostico']
            })
        return reporte_final