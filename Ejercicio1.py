class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.fecha_consulta = None

class Secretaria:
    def __init__(self):
        self.pacientes_registrados = {}
        self.sala_espera = []

    def registrar_paciente(self, paciente):
        if paciente.nombre in self.pacientes_registrados:
            print(f"{paciente.nombre} ya tiene una consulta previa. Por favor, pase a la sala de espera.")
            self.sala_espera.append(paciente.nombre)
        else:
            self.pacientes_registrados[paciente.nombre] = paciente
            print(f"{paciente.nombre} ha sido registrado con éxito.")
            self.asignar_fecha_consulta(paciente)

    def asignar_fecha_consulta(self, paciente):
        paciente.fecha_consulta = "01/09/2024"
        print(f"Consulta asignada para {paciente.nombre} el {paciente.fecha_consulta}.")

    def mostrar_info(self):
        for nombre, paciente in self.pacientes_registrados.items():
            print(f"Nombre: {paciente.nombre}")
            print(f"Motivo de consulta: {paciente.motivo_consulta}")
            print(f"Fecha de consulta: {paciente.fecha_consulta}")
            print("-----------------------------")

    def mostrar_tiempo_espera(self):
        tiempo_por_paciente = 30  # Tiempo de espera en minutos por paciente
        tiempo_total = tiempo_por_paciente * len(self.sala_espera)
        if self.sala_espera:
            print("Pacientes en la sala de espera.")
            print(f"Tiempo aproximado de espera: {tiempo_total} minutos.")
        else:
            print("No hay pacientes en la sala de espera.")

# Ejemplo interactivo
secretaria = Secretaria()

while True:
    print("\n--- Consultorio Médico ---")
    print("1. Registrar un nuevo paciente")
    print("2. Ya tiene cita, pase a la sala de espera")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        motivo_consulta = input("Ingrese el motivo de la consulta: ")
        paciente = Paciente(nombre, motivo_consulta)
        secretaria.registrar_paciente(paciente)
    elif opcion == "2":
        print("Tiene una consulta previa. Por favor, espere en la sala de espera. El médico lo atenderá pronto.")
        secretaria.mostrar_tiempo_espera()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

# Imprimir la información de todos los pacientes registrados
print("--------------------------------------------------------------------------")
print("\n--- Resumen de pacientes registrados ---")
secretaria.mostrar_info()

