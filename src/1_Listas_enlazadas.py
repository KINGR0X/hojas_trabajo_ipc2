class receta:
    def __init__(self, paciente, fecha_nac,
                 doctor, colegiado, fecha_cita, hora_cita, tipo_consulta, tratamiento):

        self.paciente = paciente
        self.fecha_nac = fecha_nac
        self.doctor = doctor
        self.colegiado = colegiado
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        self.tipo_consulta = tipo_consulta
        self. tratamiento = tratamiento


# Se le coloca None, para que al momento de crear un nodo con los valores por defecto no tenga un valor verdadero.
class nodo:
    def __init__(self, receta=None, siguiente=None):
        self.receta = receta
        self.siguiente = siguiente


# ====Definición de la clase de Lista Enlazada====
class lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, receta):
        # Si es el primer nodo, por eso el none, porque no tiene a donde apuntar
        if self.primero is None:
            self.primero = nodo(receta=receta)
            return
        actual = self.primero

        # Mientra siguiente no sea null
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(receta=receta)

    def recorrer(self):
        actual = self.primero

        while actual != None:
            print("Paciente: ", actual.receta.paciente,
                  "| Fecha de nacimiento: ", actual.receta.fecha_nac,
                  "| Doctor: ", actual.receta.doctor,
                  "| Colegiado: ", actual.receta.colegiado,
                  "| Fecha de cita: ", actual.receta.fecha_cita,
                  "| Hora cita: ", actual.receta.hora_cita,
                  "| Tipo de consulta: ", actual.receta.tipo_consulta,
                  "| Tratamiento: ", actual.receta.tipo_consulta)
            actual = actual.siguiente

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None

        while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def modificar(self, paciente, nueva_fecha_cita, nueva_hora_cita):
        actual = self.primero
        while actual is not None:
            if actual.receta.paciente == paciente:
                actual.receta.fecha_cita = nueva_fecha_cita
                actual.receta.hora_cita = nueva_hora_cita
                break
            actual = actual.siguiente


# ====Creación de objetos receta====

r1 = receta("German López", "03-10-1990", "Melvin Ortiz", 20156, "17-01-23",
            "11:30", "Medicina general", "2 pildoras de acetaminofen cada 6 horas")

r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023",
            "09:00", "Medicina interna", "Tylenol de 20 ml cada 4 horas")

r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20156, "02-02-2023", "12:00",
            "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

# ==== Inserción ====

lista_e = lista_enlazada()
lista_e.insertar(r1)
lista_e.insertar(r2)
lista_e.insertar(r3)

# ==== Eliminar ====
lista_e.eliminar(8567, "18-01-2023", "09:00")

# === Recorrer ===
lista_e.recorrer()

# === Modificar ===
print("\n=== Modificar ===")
lista_e.modificar("German López", "19-01-2023", "09:30")
lista_e.recorrer()
