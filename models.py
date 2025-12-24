

class Paciente:
    def __init__(self, id, nombre, edad, cedula):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "edad": int(edad),
            "cedula": cedula
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['edad']}|{d['cedula']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {"id": int(p[0]), "nombre": p[1], "edad": int(p[2]), "cedula": p[3]}


class Especialidad:
    def __init__(self, id, nombre):
        self.datos = {
            "id": int(id),
            "nombre": nombre
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {"id": int(p[0]), "nombre": p[1]}


class Doctor:
    def __init__(self, id, nombre, id_especialidad):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "id_especialidad": int(id_especialidad)
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['id_especialidad']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {"id": int(p[0]), "nombre": p[1], "id_especialidad": int(p[2])}


class Cita:
    def __init__(self, id, id_paciente, id_doctor, fecha, hora, estado="PENDIENTE"):
        self.datos = {
            "id": int(id),
            "id_paciente": int(id_paciente),
            "id_doctor": int(id_doctor),
            "fecha": fecha,
            "hora": hora,
            "estado": estado
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_paciente']}|{d['id_doctor']}|{d['fecha']}|{d['hora']}|{d['estado']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {
            "id": int(p[0]), 
            "id_paciente": int(p[1]), 
            "id_doctor": int(p[2]), 
            "fecha": p[3], 
            "hora": p[4], 
            "estado": p[5]
        }


class HistoriaClinica:
    def __init__(self, id, id_paciente, fecha, diagnostico, id_doctor):
        self.datos = {
            "id": int(id),
            "id_paciente": int(id_paciente),
            "fecha": fecha,
            "diagnostico": diagnostico,
            "id_doctor": int(id_doctor)
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_paciente']}|{d['fecha']}|{d['diagnostico']}|{d['id_doctor']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {
            "id": int(p[0]), 
            "id_paciente": int(p[1]), 
            "fecha": p[2], 
            "diagnostico": p[3], 
            "id_doctor": int(p[4])
        }