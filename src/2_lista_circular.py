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


# ====Definicion de la clase lista circular====
class lista_cirular:
    def __init__(self):
        self.primero = None

    def insertar(self, receta):
        if self.primero is None:
            self.primero = nodo(receta=receta)
            self.primero.siguiente = self.primero  # apunta a el mismo
        else:
            # declaración de actual
            actual = nodo(receta=receta, siguiente=self.primero.siguiente)
            self.primero.siguiente = actual

    def recorrer(self):
        if self.primero is None:
            return

        actual = self. primero
        print("Paciente: ", actual.receta.paciente,
              "| Fecha de nacimiento: ", actual.receta.fecha_nac,
              "| Doctor: ", actual.receta.doctor,
              "| Colegiado: ", actual.receta.colegiado,
              "| Fecha de cita: ", actual.receta.fecha_cita,
              "| Hora cita: ", actual.receta.hora_cita,
              "| Tipo de consulta: ", actual.receta.tipo_consulta,
              "| Tratamiento: ", actual.receta.tipo_consulta)

        while actual.siguiente != self.primero:
            actual = actual.siguiente
            print("Paciente: ", actual.receta.paciente,
                  "| Fecha de nacimiento: ", actual.receta.fecha_nac,
                  "| Doctor: ", actual.receta.doctor,
                  "| Colegiado: ", actual.receta.colegiado,
                  "| Fecha de cita: ", actual.receta.fecha_cita,
                  "| Hora cita: ", actual.receta.hora_cita,
                  "| Tipo de consulta: ", actual.receta.tipo_consulta,
                  "| Tratamiento: ", actual.receta.tipo_consulta)

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                print("NO encontrado")
                break

        if not no_encontrado:
            if anterior is not None:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
            else:
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente

    def modificar(self, paciente, fecha_nueva_cita, hora__nueva_cita):
        actual = self.primero
        while actual is not None:
            if actual.receta.paciente == paciente:
                actual.receta.fecha_cita = fecha_nueva_cita
                actual.receta.hora_cita = hora__nueva_cita
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

lista_c = lista_cirular()
lista_c.insertar(r1)
lista_c.insertar(r2)
lista_c.insertar(r3)


# ==== Recorrer la lista====

lista_c.recorrer()

print("==== Eliminar de la lista ====")
# Eliminar karen
lista_c.eliminar(8567, "31-01-2023", "09:00")
lista_c.recorrer()

# === Modificar ===
print("\n=== Modificar ===")
lista_c.modificar("German López", "19-01-2023", "09:30")
lista_c.recorrer()
