"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
import time


#----------------------------------------------------------------------------------------------
# ESTRUCTURAS DE DATOS
#----------------------------------------------------------------------------------------------

# Estructura de datos para el sistema de centro de salud

# Entidad: Paciente
pacientes = {
    "dni": {  # Clave principal: DNI del paciente
        "activo": True,  # bool
        "nombre": "",  # str
        "apellido": "",  # str
        "telefono": "",  # str
        "email": "",  # str
        "fecha_nacimiento": "",  # str
        "direccion": {
            "calle": "",  # str
            "numero": "",  # str
            "ciudad": ""  # str
        }
    }
}

# Entidad: Doctor
doctores = {
    "matricula": {  # Clave principal: número de matrícula del doctor
        "activo": True,  # bool
        "nombre": "",  # str
        "apellido": "",  # str
        "especialidad": "",  # str
        "telefono": "",  # str
        "email": "",  # str
        "honorarios": {
            "monto": 0.0,  # float
            "moneda": ""  # str
        }
    }
}

# Entidad: Consulta
consultas = {
    "id_consulta": {  # Clave principal: ID único de la consulta
        "dni_paciente": "",  # str (DNI del paciente)
        "matricula_doctor": "",  # str (Matrícula del doctor)
        "fecha_consulta": "",  # str
        "hora_consulta": "",  # str
        "motivo": "",  # str
        "diagnostico": "",  # str
        "tratamiento": "",  # str
        "observaciones": "",  # str
        "estado": ""  # str
    }
}


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def ingresarPaciente(pacientes):
    """
    Permite ingresar un nuevo paciente al sistema, verificando los datos ingresados.
    """
    print("\n--- Ingresar Paciente ---")
    
    # Validar el DNI
    dni_valido = False
    while not dni_valido:
        dni = input("Ingrese el DNI del paciente (solo números): ")
        if dni.isdigit() and len(dni) >= 7:  # Verifica que sea numerico y tenga al menos 7 dígitos
            if dni in pacientes:
                print("\nYa existe un paciente con ese DNI.")
                return pacientes
            dni_valido = True
        else:
            print("DNI inválido. Intente nuevamente.")
    
    # Validar el nombre
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Ingrese el nombre del paciente: ").strip()
        if nombre.isalpha():  # Verifica que solo tenga letras
            nombre_valido = True
        else:
            print("Nombre inválido. Intente nuevamente.")
    
    # Validar el apellido
    apellido_valido = False
    while not apellido_valido:
        apellido = input("Ingrese el apellido del paciente: ").strip()
        if apellido.isalpha():  # Verifica que solo contenga letras
            apellido_valido = True
        else:
            print("Apellido inválido. Intente nuevamente.")
    
    # Validar el telefono
    telefono_valido = False
    while not telefono_valido:
        telefono = input("Ingrese el teléfono del paciente (solo números): ")
        if telefono.isdigit() and len(telefono) >= 8:  # Verifica que sea numerico y tenga al menos 8 dígitos
            telefono_valido = True
        else:
            print("Teléfono inválido. Intente nuevamente.")
    
    # Validar el email
    email_valido = False
    while not email_valido:
        email = input("Ingrese el email del paciente: ").strip()
        if "@" in email and "." in email:  # Verifica que tenga un at y punto para que sea un mail
            email_valido = True
        else:
            print("Email inválido. Intente nuevamente.")
    
    # Validar la fecha de nacimiento
    fecha_valida = False
    while not fecha_valida:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (AAAA-MM-DD): ")
        if len(fecha_nacimiento) == 10 and fecha_nacimiento.count("-") == 2:
            partes = fecha_nacimiento.split("-")
            if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
                año, mes, día = int(partes[0]), int(partes[1]), int(partes[2])
                if 1900 <= año <= 2025 and 1 <= mes <= 12 and 1 <= día <= 31: # Verifica que el año sea razonable y los dias y meses no se pasen.
                    fecha_valida = True
        if not fecha_valida:
            print("Fecha de nacimiento inválida. Intente nuevamente.")
    
    # No hay nada por validar pero se hace strip igualmente para seguir con la estructura de los demas inputs
    calle_valida = False
    while not calle_valida:
        calle = input("Ingrese la calle de la dirección: ").strip()
        if calle:
            calle_valida = True
        else:
            print("Calle inválida. Intente nuevamente.")
    
    numero_valido = False
    while not numero_valido:
        numero = input("Ingrese el número de la dirección: ")
        if numero.isdigit():  # Verifica que sean solo numeros
            numero_valido = True
        else:
            print("Número inválido. Intente nuevamente.")
    
    ciudad_valida = False
    while not ciudad_valida:
        ciudad = input("Ingrese la ciudad de la dirección: ").strip()
        if ciudad.isalpha():  # Verifica que solo tenga letras
            ciudad_valida = True
        else:
            print("Ciudad inválida. Intente nuevamente.")
    
    # Crear el registro del paciente
    pacientes[dni] = {
        "activo": True,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": {
            "calle": calle,
            "numero": numero,
            "ciudad": ciudad
        }
    }
    
    print(f"\nPaciente ingresado exitosamente con DNI: {dni}")
    return pacientes

def modificarPaciente(pacientes):
    """
    Permite modificar los datos de un paciente existente.
    """
    print("\n--- Modificar Paciente ---")
    dni = input("Ingrese el DNI del paciente que desea modificar: ")

    if dni in pacientes:
        paciente = pacientes[dni]
        print("\nPaciente encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")

        nombre = input(f"Nombre actual ({paciente['nombre']}): ") or paciente['nombre']
        apellido = input(f"Apellido actual ({paciente['apellido']}): ") or paciente['apellido']
        telefono = input(f"Teléfono actual ({paciente['telefono']}): ") or paciente['telefono']
        email = input(f"Email actual ({paciente['email']}): ") or paciente['email']
        fecha_nacimiento = input(f"Fecha nacimiento actual ({paciente['fecha_nacimiento']}): ") or paciente['fecha_nacimiento']
        calle = input(f"Calle actual ({paciente['direccion']['calle']}): ") or paciente['direccion']['calle']
        numero = input(f"Número actual ({paciente['direccion']['numero']}): ") or paciente['direccion']['numero']
        ciudad = input(f"Ciudad actual ({paciente['direccion']['ciudad']}): ") or paciente['direccion']['ciudad']

        # Actualización del registro
        pacientes[dni] = {
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": {
                "calle": calle,
                "numero": numero,
                "ciudad": ciudad
            }
        }

        print(f"\nPaciente con DNI {dni} modificado exitosamente.")
    else:
        print("\nEl DNI del paciente no existe.")
    
    return pacientes

def eliminarPaciente(pacientes):
    
    print("\n--- Eliminar Paciente ---")
    dni = input("Ingrese el DNI del paciente que desea eliminar: ")

    if dni in pacientes:
        del pacientes[dni]
        print(f"Paciente con DNI {dni} eliminado exitosamente.")
    else:
        print("Paciente no encontrado.")
    
    return pacientes

def listarPacientes(pacientes):
    """
    Explicacion: esta funcion imprime los pacientes.

    Entrada: la funcion recibe como parametro un diccionario de los pacientes.

    Salida: la funcion imprime el listado de los pacientes.
    """
    print("\n--- Listado de Pacientes ---")
    for dni, paciente in pacientes.items():
        print(f"DNI: {dni}")
        print(f"\tNombre: {paciente['nombre']}")
        print(f"\tApellido: {paciente['apellido']}")
        print(f"\tTeléfono: {paciente['telefono']}")
        print(f"\tEmail: {paciente['email']}")
        print(f"\tFecha de nacimiento: {paciente['fecha_nacimiento']}")
        print("\tDirección:")
        print(f"\t\tCalle: {paciente['direccion']['calle']}")
        print(f"\t\tNúmero: {paciente['direccion']['numero']}")
        print(f"\t\tCiudad: {paciente['direccion']['ciudad']}")
        print()

def ingresarDoctor(doctores):
    """
    Permite ingresar o actualizar un doctor según la matrícula.
    """
    print("\n--- Ingresar Doctor ---")
    
    matricula = input("Ingrese la matrícula profesional del doctor: ")
    
    if matricula in doctores:
        print("\n Ya existe un doctor con esa matrícula.")
        doctor = doctores[matricula]
        print(f"Nombre actual: {doctor['nombre']} {doctor['apellido']}")
        print(f"Especialidad actual: {doctor['especialidad']}")
        opcion = input("¿Desea modificar los datos? (S/N): ").upper()
        if opcion != "S":
            print("No se realizaron cambios.")
            return doctores
    
    # Solicitar datos nuevos o actualizados
    nombre = input("Ingrese el nombre del doctor: ")
    apellido = input("Ingrese el apellido del doctor: ")
    especialidad = input("Ingrese la especialidad: ")
    telefono = input("Ingrese el teléfono del doctor: ")
    email = input("Ingrese el email del doctor: ")
    monto = float(input("Ingrese el monto de los honorarios: "))
    moneda = input("Ingrese la moneda (por ejemplo, ARS, USD): ")
    
    doctores[matricula] = {
        "activo": True,
        "matricula": matricula,
        "nombre": nombre,
        "apellido": apellido,
        "especialidad": especialidad,
        "telefono": telefono,
        "email": email,
        "honorarios": {
            "monto": monto,
            "moneda": moneda
        }
    }
    
    print(f"\nDoctor registrado/modificado exitosamente con matrícula: {matricula}")
    return doctores

def modificarDoctor(doctores):
    """
    Permite modificar los datos de un doctor existente en el sistema.
    """
    print("\n--- Modificar Doctor ---")
    matricula = input("Ingrese la matrícula del doctor que desea modificar: ")

    if matricula in doctores:
        doctor = doctores[matricula]
        print("\nDoctor encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")

        nombre = input(f"Nombre actual ({doctor['nombre']}): ") or doctor['nombre']
        apellido = input(f"Apellido actual ({doctor['apellido']}): ") or doctor['apellido']
        especialidad = input(f"Especialidad actual ({doctor['especialidad']}): ") or doctor['especialidad']
        telefono = input(f"Teléfono actual ({doctor['telefono']}): ") or doctor['telefono']
        email = input(f"Email actual ({doctor['email']}): ") or doctor['email']
        monto = input(f"Honorarios actuales ({doctor['honorarios']['monto']}): ") or doctor['honorarios']['monto']
        moneda = input(f"Moneda actual ({doctor['honorarios']['moneda']}): ") or doctor['honorarios']['moneda']

        # Actualización del registro
        doctores[matricula] = {
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "especialidad": especialidad,
            "telefono": telefono,
            "email": email,
            "honorarios": {
                "monto": float(monto),
                "moneda": moneda
            }
        }

        print(f"\nDoctor con matrícula {matricula} modificado exitosamente.")
    else:
        print("\nLa matrícula del doctor no existe.")
    
    return doctores

def eliminarDoctor(doctores):
    """
    Explicacion: esta funcion elimina un doctor.
    Entrada: esta funcion recibe como parametro el id del doctor junto con el diccionario de los doctores.
    Salida: eliminacion del doctor.
    """

    matricula = int(input("Ingresar el numero de matricula del doctor que desea eliminar: "))

    if matricula in doctores:

        doctores.pop(matricula)

        return "Doctor eliminado con exito."

    else:

        return "Doctor no encontrado."

def listarDoctores(doctores):
    """
    Explicacion: esta funcion imprime los doctores registrados.

    Entrada: la funcion recibe como parametro un diccionario de los doctores.

    Salida: la funcion imprime el listado de los doctores.
    """
    print("\n--- Listado de Doctores ---")
    for matricula, doctor in doctores.items():
        print(f"Matrícula: {matricula}")
        print(f"\tNombre: {doctor['nombre']}")
        print(f"\tApellido: {doctor['apellido']}")
        print(f"\tEspecialidad: {doctor['especialidad']}")
        print(f"\tTeléfono: {doctor['telefono']}")
        print(f"\tEmail: {doctor['email']}")
        print(f"\tHonorarios: {doctor['honorarios']['monto']} {doctor['honorarios']['moneda']}")
        print()

def registrarConsulta(consultas, pacientes, doctores):
    """
    Permite registrar una nueva consulta en el sistema.
    
    Entrada:
    - consultas: Diccionario de consultas existentes.
    - pacientes: Diccionario de pacientes registrados.
    - doctores: Diccionario de doctores registrados.
    
    Salida:
    - Actualiza el diccionario de consultas con la nueva consulta.
    """
    print("\n--- Registro de Consulta ---")
    
    # Validar el DNI del paciente
    dni_valido = False
    while not dni_valido:
        dni_paciente = input("Ingrese el DNI del paciente: ")
        if dni_paciente in pacientes:
            dni_valido = True
        else:
            print("El DNI del paciente no está registrado. Intente nuevamente.")
    
    # Validar la matrícula del doctor
    matricula_valida = False
    while not matricula_valida:
        matricula_doctor = input("Ingrese la matrícula del doctor: ")
        if matricula_doctor in doctores:
            matricula_valida = True
        else:
            print("La matrícula del doctor no está registrada. Intente nuevamente.")
    
    # Solicitar fecha de la consulta
    fecha_valida = False
    while not fecha_valida:
        fecha_consulta = input("Ingrese la fecha de la consulta (AAAA-MM-DD): ")
        if len(fecha_consulta) == 10 and fecha_consulta.count("-") == 2:
            partes = fecha_consulta.split("-")
            if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
                año, mes, día = int(partes[0]), int(partes[1]), int(partes[2])
                if 1900 <= año <= 2025 and 1 <= mes <= 12 and 1 <= día <= 31:
                    fecha_valida = True
        if not fecha_valida:
            print("Fecha inválida. Intente nuevamente.")
    
    # Solicitar hora de la consulta
    hora_valida = False
    while not hora_valida:
        hora_consulta = input("Ingrese la hora de la consulta (HH:MM): ")
        if len(hora_consulta) == 5 and hora_consulta.count(":") == 1:
            partes = hora_consulta.split(":")
            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                hora, minuto = int(partes[0]), int(partes[1])
                if 0 <= hora <= 23 and 0 <= minuto <= 59:
                    hora_valida = True
        if not hora_valida:
            print("Hora inválida. Intente nuevamente.")
    
    # Solicitar otros datos de la consulta
    motivo = input("Ingrese el motivo de la consulta: ").strip()
    diagnostico = input("Ingrese el diagnóstico (si aplica): ").strip()
    tratamiento = input("Ingrese el tratamiento (si aplica): ").strip()
    observaciones = input("Ingrese observaciones adicionales (si aplica): ").strip()
    estado = input("Ingrese el estado de la consulta (Ejemplo: 'Pendiente', 'Completada'): ").strip()
    
    # Generar un ID único para la consulta usando el timestamp
    id_consulta = time.strftime("%Y.%m.%d %H:%M:%S")
    
    # Crear el registro de la consulta
    consultas[id_consulta] = {
        "dni_paciente": dni_paciente,
        "matricula_doctor": matricula_doctor,
        "fecha_consulta": fecha_consulta,
        "hora_consulta": hora_consulta,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "observaciones": observaciones,
        "estado": estado
    }
    
    print(f"\nConsulta registrada exitosamente con ID: {id_consulta}")
    return consultas

def consultasDelMes(consultas):
    """
    Explicación:
    Muestra todas las consultas registradas en un mes y año específicos.

    Entrada:
    - consultas: diccionario de consultas existentes.

    Salida:
    - Imprime el listado de consultas del mes seleccionado.
    """
    print("\n--- Consultas del Mes ---")

    # Solicitar año
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)

    # Solicitar mes
    mes = input("Ingrese el mes (1-12): ").strip()
    if not (mes.isdigit() and 1 <= int(mes) <= 12):
        print("Mes inválido. Operación cancelada.")
        return
    mes = int(mes)

    # Filtrar consultas del mes
    consultas_filtradas = {}
    for id_consulta, datos in consultas.items():
        fecha = datos.get("fecha_consulta", "")

        # Validar formato de fecha: AAAA-MM-DD
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
                año_c, mes_c, dia_c = int(partes[0]), int(partes[1]), int(partes[2])
                if año_c == año and mes_c == mes:
                    consultas_filtradas[id_consulta] = datos

    # Mostrar resultados
    if len(consultas_filtradas) == 0:
        print(f"\nNo hay consultas registradas para {mes:02d}/{año}.")
    else:
        print(f"\nConsultas registradas en {mes:02d}/{año}:")
        print("--------------------------------------------------")
        contador = 0
        for id_consulta, datos in consultas_filtradas.items():
            contador += 1
            print(f"Consulta N° {contador}")
            print(f"ID: {id_consulta}")
            print(f"  Fecha: {datos['fecha_consulta']} - Hora: {datos['hora_consulta']}")
            print(f"  Paciente (DNI): {datos['dni_paciente']}")
            print(f"  Doctor (Matrícula): {datos['matricula_doctor']}")
            print(f"  Motivo: {datos['motivo']}")
            print(f"  Estado: {datos['estado']}")
            print("--------------------------------------------------")
        print(f"Total de consultas encontradas: {contador}")


def resumenAnualConsultasPorDoctorCantidades(consultas, doctores):
    ...

def resumenAnualConsultasPorDoctorHonorarios(consultas, doctores):
    ...

def listadoPacientesPorEspecialidad(pacientes, doctores):
    ...

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal del programa.
    """
    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    pacientes = {
        "12345678": {
            "activo": True,
            "nombre": "Juan",
            "apellido": "Pérez",
            "telefono": "123456789",
            "email": "juan.perez@example.com",
            "fecha_nacimiento": "1990-05-15",
            "direccion": {
                "calle": "Av. Siempre Viva",
                "numero": "123",
                "ciudad": "Springfield"
            }
        },
        "87654321": {
            "activo": True,
            "nombre": "Ana",
            "apellido": "Gómez",
            "telefono": "987654321",
            "email": "ana.gomez@example.com",
            "fecha_nacimiento": "1985-10-20",
            "direccion": {
                "calle": "Calle Falsa",
                "numero": "456",
                "ciudad": "Shelbyville"
            }
        }
    }

    doctores = {
        "1208661": {
            "activo": True,
            "nombre": "Dr. Roberto",
            "apellido": "Martínez",
            "especialidad": "Cardiología",
            "telefono": "1122334455",
            "email": "roberto.martinez@example.com",
            "honorarios": {
                "monto": 5000.0,
                "moneda": "ARS"
            }
        }
    }

    consultas = {
        "2025.10.21 10:30:00": {
            "dni_paciente": "12345678",
            "matricula_doctor": "1208661",
            "fecha_consulta": "2025-10-21",
            "hora_consulta": "10:30",
            "motivo": "Chequeo general",
            "diagnostico": "Sin novedades",
            "tratamiento": "Ninguno",
            "observaciones": "Paciente en buen estado de salud",
            "estado": "Completada"
        }
    }

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Paciente")
            print("[2] Gestión de Doctor")
            print("[3] Gestión de Consultas")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTIÓN DE PACIENTE")
                    print("---------------------------")
                    print("[1] Ingresar Paciente")
                    print("[2] Modificar Paciente")
                    print("[3] Eliminar Paciente")
                    print("[4] Listado de Pacientes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    pacientes = ingresarPaciente(pacientes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarPaciente(pacientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    eliminarPaciente(pacientes)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarPacientes(pacientes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTIÓN DE DOCTOR")
                    print("---------------------------")
                    print("[1] Ingresar Doctor")
                    print("[2] Modificar Doctor")
                    print("[3] Eliminar Doctor")
                    print("[4] Listado de Doctores")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    doctores = ingresarDoctor(doctores)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarDoctor(doctores)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    eliminarDoctor(doctores)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarDoctores(doctores)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > GESTIÓN DE CONSULTAS")
                    print("---------------------------")
                    print("[1] Registrar Consulta")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    consultas = registrarConsulta(consultas, pacientes, doctores)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > INFORMES")
                    print("---------------------------")
                    print("[1] Consultas del Mes")
                    print("[2] Resumen Anual de Consultas por Doctor (Cantidades)")
                    print("[3] Resumen Anual de Consultas por Doctor (Honorarios)")
                    print("[4] Listado de Pacientes por Especialidad")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    consultasDelMes(consultas)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    resumenAnualConsultasPorDoctorCantidades(consultas, doctores)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenAnualConsultasPorDoctorHonorarios(consultas, doctores)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listadoPacientesPorEspecialidad(pacientes, doctores)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()
