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
import time

#----------------------------------------------------------------------------------------------
# ESTRUCTURAS DE DATOS
#----------------------------------------------------------------------------------------------

# Estructura de datos para el sistema de centro de salud

# Entidad: Paciente
pacientes = {
    "dni": {  # Clave principal: DNI del paciente
        "activo": True,           # bool
        "nombre": "",           # str
        "apellido": "",         # str
        "email": "",            # str
        "fecha_nacimiento": "", # str
        "direccion": "",       # str (según diagrama)
        "telefonos": {           # dict de teléfonos
            "id_telefono_1": "",  # str
            "id_telefono_2": "",  # str
            "id_telefono_3": ""   # str
        }
    }
}

# Entidad: Doctor
doctores = {
    "matricula": {  # Clave principal: número de matrícula del doctor
        "activo": True,        # bool
        "nombre": "",        # str
        "apellido": "",      # str
        "email": "",         # str
        "honorarios": 0.0,     # float
        "telefonos": {        # dict de teléfonos
            "id_telefono_1": "",
            "id_telefono_2": "",
            "id_telefono_3": ""
        },
        "especialidades": {   # dict de especialidades
            "id_especialidad_1": "",
            "id_especialidad_2": "",
            "id_especialidad_3": ""
        }
    }
}

# Entidad: Consulta
consultas = {
    "id_consulta": {  # Clave principal: ID único de la consulta ("AAAA.MM.DD hh:mm:ss")
        "id_paciente": "",    # str (DNI del paciente)
        "id_doctor": "",      # str (Matrícula del doctor)
        "fecha_consulta": "", # str
        "hora_consulta": "",  # str
        "motivo": "",         # str
        "diagnostico": "",    # str
        "tratamiento": "",    # str
        "observaciones": "",  # str
        "estado": ""          # str
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
    
    direccion = input("Ingrese la dirección del paciente: ").strip()
    
    telefonos = {}
    for i in range(1, 4):
        telefono = input(f"Ingrese el teléfono {i} del paciente (deje vacío si no aplica): ").strip()
        telefonos[f"id_telefono_{i}"] = telefono
    
    # Crear el registro del paciente
    pacientes[dni] = {
        "activo": True,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": direccion,
        "telefonos": telefonos
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
        email = input(f"Email actual ({paciente['email']}): ") or paciente['email']
        fecha_nacimiento = input(f"Fecha nacimiento actual ({paciente['fecha_nacimiento']}): ") or paciente['fecha_nacimiento']
        direccion = input(f"Dirección actual ({paciente['direccion']}): ") or paciente['direccion']
        
        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({paciente['telefonos'][f'id_telefono_{i}']}): ") or paciente['telefonos'][f'id_telefono_{i}']

        # Permitir cambiar el estado 'activo' (solo S/N; deje vacío para mantener)
        activo_input = input(f"Activo actual ({paciente.get('activo', True)}) - (S/N, deje vacío para mantener): ").strip().lower()
        if activo_input == 's':
            activo = True
        elif activo_input == 'n':
            activo = False
        else:
            activo = paciente.get('activo', True)

        # Actualización del registro
        pacientes[dni] = {
            "activo": activo,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "telefonos": telefonos
        }

        print(f"\nPaciente con DNI {dni} modificado exitosamente.")
    else:
        print("\nEl DNI del paciente no existe.")
    
    return pacientes

def eliminarPaciente(pacientes):
    
    print("\n--- Eliminar Paciente ---")
    dni = input("Ingrese el DNI del paciente que desea eliminar: ")

    if dni in pacientes:
        pacientes[dni]["activo"] = False
        print(f"Paciente con DNI {dni} ha sido desactivado exitosamente.")
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

        if paciente["activo"] == True:

            print(f"DNI: {dni}")
            print(f"\tNombre: {paciente['nombre']}")
            print(f"\tApellido: {paciente['apellido']}")
            print(f"\tEmail: {paciente['email']}")
            print(f"\tFecha de nacimiento: {paciente['fecha_nacimiento']}")
            print(f"\tDirección: {paciente['direccion']}")
            print("\tTeléfonos:")
            for key, value in paciente['telefonos'].items():
                print(f"\t\t{key}: {value}")
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
        opcion = input("¿Desea modificar los datos? (S/N): ").upper()
        if opcion != "S":
            print("No se realizaron cambios.")
            return doctores
    
    # Solicitar datos nuevos o actualizados
    nombre = input("Ingrese el nombre del doctor: ")
    apellido = input("Ingrese el apellido del doctor: ")
    email = input("Ingrese el email del doctor: ")
    honorarios = float(input("Ingrese el monto de los honorarios: "))
    
    telefonos = {}
    for i in range(1, 4):
        telefonos[f"id_telefono_{i}"] = input(f"Ingrese el teléfono {i} del doctor (deje vacío si no aplica): ").strip()
    
    especialidades = {}
    for i in range(1, 4):
        especialidades[f"id_especialidad_{i}"] = input(f"Ingrese la especialidad {i} del doctor (deje vacío si no aplica): ").strip()
    
    doctores[matricula] = {
        "activo": True,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "honorarios": honorarios,
        "telefonos": telefonos,
        "especialidades": especialidades
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
        email = input(f"Email actual ({doctor['email']}): ") or doctor['email']
        honorarios = input(f"Honorarios actuales ({doctor['honorarios']}): ") or doctor['honorarios']
        
        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({doctor['telefonos'][f'id_telefono_{i}']}): ") or doctor['telefonos'][f'id_telefono_{i}']
        
        especialidades = {}
        for i in range(1, 4):
            especialidades[f"id_especialidad_{i}"] = input(f"Especialidad {i} actual ({doctor['especialidades'][f'id_especialidad_{i}']}): ") or doctor['especialidades'][f'id_especialidad_{i}']

        # Permitir cambiar el estado 'activo' (solo S/N; deje vacío para mantener)
        activo_input = input(f"Activo actual ({doctor.get('activo', True)}) - (S/N, deje vacío para mantener): ").strip().lower()
        if activo_input == 's':
            activo = True
        elif activo_input == 'n':
            activo = False
        else:
            activo = doctor.get('activo', True)

        # Actualización del registro
        doctores[matricula] = {
            "activo": activo,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "honorarios": float(honorarios),
            "telefonos": telefonos,
            "especialidades": especialidades
        }

        print(f"\nDoctor con matrícula {matricula} modificado exitosamente.")
    else:
        print("\nLa matrícula del doctor no existe.")
    
    return doctores

def eliminarDoctor(doctores):
    """
    Explicacion: esta funcion elimina un doctor.
    Entrada: la funcion recibe como parametro un diccionario con los datos de los doctores.
    Salida: la funcion retorna un mensaje de doctor eliminado o no eliminado.
    """

    matricula = input("Ingresar el numero de matricula del doctor que desea eliminar: ").strip()
    
    if not matricula:
        return "Error: debe ingresar un número de matrícula."
    
    if matricula in doctores:
        if not doctores[matricula].get("activo", True):
            return "El doctor ya está desactivado."
        doctores[matricula]["activo"] = False
        return "Doctor desactivado exitosamente."
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

        if doctor["activo"] == True:

            print(f"Matrícula: {matricula}")
            print(f"\tNombre: {doctor['nombre']}")
            print(f"\tApellido: {doctor['apellido']}")
            print(f"\tEmail: {doctor['email']}")
            print(f"\tHonorarios: {doctor['honorarios']}")
            print("\tTeléfonos:")
            for key, value in doctor['telefonos'].items():
                print(f"\t\t{key}: {value}")
            print("\tEspecialidades:")
            for key, value in doctor['especialidades'].items():
                print(f"\t\t{key}: {value}")
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
        id_paciente = input("Ingrese el DNI del paciente: ")
        if id_paciente in pacientes:
            dni_valido = True
        else:
            print("El DNI del paciente no está registrado. Intente nuevamente.")
    
    # Validar la matrícula del doctor
    matricula_valida = False
    while not matricula_valida:
        id_doctor = input("Ingrese la matrícula del doctor: ")
        if id_doctor in doctores:
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
        "id_paciente": id_paciente,
        "id_doctor": id_doctor,
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
            print(f"  Paciente (DNI): {datos['id_paciente']}")
            print(f"  Doctor (Matrícula): {datos['id_doctor']}")
            print(f"  Motivo: {datos['motivo']}")
            print(f"  Estado: {datos['estado']}")
            print("--------------------------------------------------")
        print(f"Total de consultas encontradas: {contador}")


def resumenAnualConsultasPorDoctorCantidades(consultas, doctores):
    """
    Explicación: muestra en formato matricial la cantidad de consultas por doctor y por mes en un año específico.
    
    Entrada: la función recibe como parámetro dos diccionarios, consultas y doctores.
    
    Salida: la función imprime una matriz con doctores en filas y meses en columnas.
    """
    print("\n--- Resumen Anual de Consultas por Doctor (Cantidades) ---")
    
    # Solicitar año
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)
    
    # Inicializar matriz: {id_doctor: [ene, feb, mar, ..., dic]}
    matriz_cantidades = {}
    
    # Inicializar contadores para cada doctor activo
    for id_doctor, datos_doctor in doctores.items():
        if datos_doctor.get("activo", True):
            matriz_cantidades[id_doctor] = [0] * 12  # 12 meses
    
    # Contar consultas por doctor y mes
    for id_consulta, datos_consulta in consultas.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        
        # Validar formato de fecha: AAAA-MM-DD
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit():
                año_c = int(partes[0])
                mes_c = int(partes[1])
                
                if año_c == año and 1 <= mes_c <= 12:
                    id_doctor = datos_consulta.get("id_doctor", "")
                    
                    # Si el doctor existe y está activo, incrementar contador
                    if id_doctor in matriz_cantidades:
                        matriz_cantidades[id_doctor][mes_c - 1] += 1
    
    # Verificar si hay datos para mostrar
    if not matriz_cantidades:
        print(f"\nNo hay doctores activos registrados.")
        return
    
    # Verificar si hay consultas en el año
    hay_consultas = any(sum(cantidades) > 0 for cantidades in matriz_cantidades.values())
    if not hay_consultas:
        print(f"\nNo hay consultas registradas para el año {año}.")
        return
    
    # Imprimir encabezado
    print(f"\n{'='*120}")
    print(f"CANTIDADES TOTALES POR MES - AÑO {año}")
    print(f"{'='*120}")
    
    # Nombres de meses abreviados
    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    
    # Imprimir encabezado de columnas
    print(f"{'Doctor':<25}", end="")
    for mes in meses:
        print(f"{mes}.{str(año)[2:]:>2}", end=" ")
    print()
    print(f"{'-'*120}")
    
    # Imprimir filas de datos
    for id_doctor, cantidades in matriz_cantidades.items():
        if id_doctor in doctores:
            doctor = doctores[id_doctor]
            nombre_completo = f"{doctor['nombre']} {doctor['apellido']}"
            
            # Truncar nombre si es muy largo
            if len(nombre_completo) > 23:
                nombre_completo = nombre_completo[:20] + "..."
            
            print(f"{nombre_completo:<25}", end="")
            
            # Imprimir cantidades de cada mes (alineadas a la derecha)
            for cantidad in cantidades:
                print(f"{cantidad:>4} ", end="")
            print()
    
    print(f"{'='*120}")


def resumenAnualConsultasPorDoctorHonorarios(consultas, doctores):
    """
    Explicación: muestra en formato matricial el total de honorarios por doctor y por mes en un año específico.

    Entrada: la función recibe como parámetro dos diccionarios, consultas y doctores.

    Salida: la función imprime una matriz con doctores en filas y meses en columnas mostrando honorarios.
    """
    print("\n--- Resumen Anual de Honorarios por Doctor ---")
    
    # Solicitar año
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)
    
    # Inicializar matriz: {id_doctor: [ene, feb, mar, ..., dic]}
    matriz_honorarios = {}
    
    # Inicializar contadores para cada doctor activo
    for id_doctor, datos_doctor in doctores.items():
        if datos_doctor.get("activo", True):
            matriz_honorarios[id_doctor] = [0.0] * 12  # 12 meses
    
    # Acumular honorarios por doctor y mes
    for id_consulta, datos_consulta in consultas.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        
        # Validar formato de fecha: AAAA-MM-DD
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit():
                año_c = int(partes[0])
                mes_c = int(partes[1])
                
                if año_c == año and 1 <= mes_c <= 12:
                    id_doctor = datos_consulta.get("id_doctor", "")
                    
                    # Si el doctor existe y está activo, acumular honorarios
                    if id_doctor in matriz_honorarios and id_doctor in doctores:
                        honorario = doctores[id_doctor].get("honorarios", 0.0)
                        matriz_honorarios[id_doctor][mes_c - 1] += honorario
    
    # Verificar si hay datos para mostrar
    if not matriz_honorarios:
        print(f"\nNo hay doctores activos registrados.")
        return
    
    # Verificar si hay consultas en el año
    hay_consultas = any(sum(honorarios) > 0 for honorarios in matriz_honorarios.values())
    if not hay_consultas:
        print(f"\nNo hay consultas registradas para el año {año}.")
        return
    
    # Imprimir encabezado
    print(f"\n{'='*160}")
    print(f"HONORARIOS TOTALES POR MES - AÑO {año} (en pesos)")
    print(f"{'='*160}")
    
    # Nombres de meses abreviados
    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    
    # Imprimir encabezado de columnas
    print(f"{'Doctor':<25}", end="")
    for mes in meses:
        print(f"{mes}.{str(año)[2:]:>2}", end="      ")
    print()
    print(f"{'-'*160}")
    
    # Imprimir filas de datos
    for id_doctor, honorarios in matriz_honorarios.items():
        if id_doctor in doctores:
            doctor = doctores[id_doctor]
            nombre_completo = f"{doctor['nombre']} {doctor['apellido']}"
            
            # Truncar nombre si es muy largo
            if len(nombre_completo) > 23:
                nombre_completo = nombre_completo[:20] + "..."
            
            print(f"{nombre_completo:<25}", end="")
            
            # Imprimir honorarios de cada mes (formato con separador de miles y 2 decimales)
            for honorario in honorarios:
                print(f"{honorario:>10,.2f}  ", end="")
            print()
    
    print(f"{'='*160}")

def rankingEspecialidadesMasConsultadas(consultas, doctores):
    """
    Explicación: muestra un ranking de las especialidades médicas más consultadas en un año específico.
    
    Entrada: la función recibe como parámetro dos diccionarios, consultas y doctores.
    
    Salida: la función imprime un ranking ordenado de especialidades por cantidad de consultas.
    """
    print("\n--- Ranking de Especialidades Más Consultadas ---")
    
    # Solicitar año
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)
    
    # Diccionario para contar consultas por especialidad
    especialidades_contador = {}
    
    # Recorrer todas las consultas del año
    for id_consulta, datos_consulta in consultas.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        
        # Validar formato de fecha: AAAA-MM-DD
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            if len(partes) == 3 and partes[0].isdigit():
                año_c = int(partes[0])
                
                if año_c == año:
                    id_doctor = datos_consulta.get("id_doctor", "")
                    
                    # Verificar que el doctor existe y está activo
                    if id_doctor in doctores and doctores[id_doctor].get("activo", True):
                        # Obtener todas las especialidades del doctor
                        especialidades_dict = doctores[id_doctor].get("especialidades", {})
                        
                        # Contar cada especialidad (si no está vacía)
                        for key, especialidad in especialidades_dict.items():
                            especialidad = especialidad.strip()
                            if especialidad:  # Solo contar si no está vacío
                                especialidades_contador[especialidad] = especialidades_contador.get(especialidad, 0) + 1
    
    # Verificar si hay datos
    if not especialidades_contador:
        print(f"\nNo hay consultas registradas para el año {año}.")
        return
    
    # Ordenar especialidades por cantidad de consultas (descendente)
    especialidades_ordenadas = sorted(especialidades_contador.items(), key=lambda x: x[1], reverse=True)
    
    # Calcular total de consultas
    total_consultas = sum(especialidades_contador.values())
    
    # Imprimir el ranking
    print(f"\n{'='*70}")
    print(f"RANKING DE ESPECIALIDADES MÁS CONSULTADAS - AÑO {año}")
    print(f"{'='*70}")
    print(f"{'Posición':<12}{'Especialidad':<35}{'Consultas':>10}{'%':>8}")
    print(f"{'-'*70}")
    
    posicion = 1
    for especialidad, cantidad in especialidades_ordenadas:
        porcentaje = (cantidad / total_consultas) * 100
        print(f"{posicion:<12}{especialidad:<35}{cantidad:>10}{porcentaje:>7.1f}%")
        posicion += 1
    
    print(f"{'-'*70}")
    print(f"{'TOTAL':<47}{total_consultas:>10}{100.0:>7.1f}%")
    print(f"{'='*70}")


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
    # Datos precargados - 10 PACIENTES
    pacientes = {
        "12345678": {
            "activo": True,
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "fecha_nacimiento": "1990-05-15",
            "direccion": "Av. Siempre Viva 123, Springfield",
            "telefonos": {
                "id_telefono_1": "123456789",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "87654321": {
            "activo": True,
            "nombre": "Ana",
            "apellido": "Gómez",
            "email": "ana.gomez@example.com",
            "fecha_nacimiento": "1985-10-20",
            "direccion": "Calle Falsa 456, Shelbyville",
            "telefonos": {
                "id_telefono_1": "987654321",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "23456789": {
            "activo": True,
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "email": "carlos.rodriguez@example.com",
            "fecha_nacimiento": "1978-03-12",
            "direccion": "Av. Libertador 789, Capital Federal",
            "telefonos": {
                "id_telefono_1": "1145678901",
                "id_telefono_2": "1156789012",
                "id_telefono_3": ""
            }
        },
        "34567890": {
            "activo": True,
            "nombre": "María",
            "apellido": "López",
            "email": "maria.lopez@example.com",
            "fecha_nacimiento": "1995-07-25",
            "direccion": "Calle San Martín 234, Quilmes",
            "telefonos": {
                "id_telefono_1": "1167890123",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "45678901": {
            "activo": True,
            "nombre": "Roberto",
            "apellido": "Fernández",
            "email": "roberto.fernandez@example.com",
            "fecha_nacimiento": "1982-11-30",
            "direccion": "Av. Corrientes 567, Buenos Aires",
            "telefonos": {
                "id_telefono_1": "1178901234",
                "id_telefono_2": "1189012345",
                "id_telefono_3": ""
            }
        },
        "56789012": {
            "activo": True,
            "nombre": "Laura",
            "apellido": "Martínez",
            "email": "laura.martinez@example.com",
            "fecha_nacimiento": "1988-02-14",
            "direccion": "Calle Belgrano 890, Berazategui",
            "telefonos": {
                "id_telefono_1": "1190123456",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "67890123": {
            "activo": True,
            "nombre": "Diego",
            "apellido": "Sánchez",
            "email": "diego.sanchez@example.com",
            "fecha_nacimiento": "1992-09-08",
            "direccion": "Av. Mitre 345, Avellaneda",
            "telefonos": {
                "id_telefono_1": "1101234567",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "78901234": {
            "activo": True,
            "nombre": "Sofía",
            "apellido": "Ramírez",
            "email": "sofia.ramirez@example.com",
            "fecha_nacimiento": "1998-06-19",
            "direccion": "Calle Rivadavia 678, Lanús",
            "telefonos": {
                "id_telefono_1": "1112345678",
                "id_telefono_2": "1123456789",
                "id_telefono_3": ""
            }
        },
        "89012345": {
            "activo": True,
            "nombre": "Javier",
            "apellido": "Torres",
            "email": "javier.torres@example.com",
            "fecha_nacimiento": "1975-12-03",
            "direccion": "Av. 9 de Julio 901, Buenos Aires",
            "telefonos": {
                "id_telefono_1": "1134567890",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        },
        "90123456": {
            "activo": True,
            "nombre": "Valentina",
            "apellido": "Díaz",
            "email": "valentina.diaz@example.com",
            "fecha_nacimiento": "2000-04-22",
            "direccion": "Calle Moreno 123, Florencio Varela",
            "telefonos": {
                "id_telefono_1": "1145678902",
                "id_telefono_2": "",
                "id_telefono_3": ""
            }
        }
    }

    # Datos precargados - 10 DOCTORES
    doctores = {
        "1208661": {
            "activo": True,
            "nombre": "Roberto",
            "apellido": "Martínez",
            "email": "roberto.martinez@example.com",
            "honorarios": 5000.0,
            "telefonos": {
                "id_telefono_1": "1122334455",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Cardiología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "1305782": {
            "activo": True,
            "nombre": "Ana",
            "apellido": "García",
            "email": "ana.garcia@example.com",
            "honorarios": 4500.0,
            "telefonos": {
                "id_telefono_1": "1133445566",
                "id_telefono_2": "1144556677",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Pediatría",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "1402893": {
            "activo": True,
            "nombre": "Miguel",
            "apellido": "Fernández",
            "email": "miguel.fernandez@example.com",
            "honorarios": 5500.0,
            "telefonos": {
                "id_telefono_1": "1155667788",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Traumatología",
                "id_especialidad_2": "Ortopedia",
                "id_especialidad_3": ""
            }
        },
        "1509104": {
            "activo": True,
            "nombre": "Clara",
            "apellido": "Ruiz",
            "email": "clara.ruiz@example.com",
            "honorarios": 4800.0,
            "telefonos": {
                "id_telefono_1": "1166778899",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Dermatología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "1601215": {
            "activo": True,
            "nombre": "Martín",
            "apellido": "López",
            "email": "martin.lopez@example.com",
            "honorarios": 6000.0,
            "telefonos": {
                "id_telefono_1": "1177889900",
                "id_telefono_2": "1188990011",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Neurología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "1708326": {
            "activo": True,
            "nombre": "Patricia",
            "apellido": "Gómez",
            "email": "patricia.gomez@example.com",
            "honorarios": 4200.0,
            "telefonos": {
                "id_telefono_1": "1199001122",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Ginecología",
                "id_especialidad_2": "Obstetricia",
                "id_especialidad_3": ""
            }
        },
        "1805437": {
            "activo": True,
            "nombre": "Fernando",
            "apellido": "Pérez",
            "email": "fernando.perez@example.com",
            "honorarios": 5200.0,
            "telefonos": {
                "id_telefono_1": "1100112233",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Gastroenterología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "1902548": {
            "activo": True,
            "nombre": "Lucía",
            "apellido": "Romero",
            "email": "lucia.romero@example.com",
            "honorarios": 4700.0,
            "telefonos": {
                "id_telefono_1": "1111223344",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Oftalmología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "2009659": {
            "activo": True,
            "nombre": "Gustavo",
            "apellido": "Silva",
            "email": "gustavo.silva@example.com",
            "honorarios": 5800.0,
            "telefonos": {
                "id_telefono_1": "1122334455",
                "id_telefono_2": "1133445566",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Cardiología",
                "id_especialidad_2": "",
                "id_especialidad_3": ""
            }
        },
        "2106760": {
            "activo": True,
            "nombre": "Marta",
            "apellido": "Vega",
            "email": "marta.vega@example.com",
            "honorarios": 4600.0,
            "telefonos": {
                "id_telefono_1": "1144556677",
                "id_telefono_2": "",
                "id_telefono_3": ""
            },
            "especialidades": {
                "id_especialidad_1": "Psiquiatría",
                "id_especialidad_2": "Psicología",
                "id_especialidad_3": ""
            }
        }
    }

    # Datos precargados - 10 CONSULTAS
    consultas = {
        "2025.10.21 10:30:00": {
            "id_paciente": "12345678",
            "id_doctor": "1208661",
            "fecha_consulta": "2025-10-21",
            "hora_consulta": "10:30",
            "motivo": "Chequeo general",
            "diagnostico": "Sin novedades",
            "tratamiento": "Ninguno",
            "observaciones": "Paciente en buen estado de salud",
            "estado": "Completada"
        },
        "2025.09.15 14:00:00": {
            "id_paciente": "87654321",
            "id_doctor": "1305782",
            "fecha_consulta": "2025-09-15",
            "hora_consulta": "14:00",
            "motivo": "Control pediátrico",
            "diagnostico": "Desarrollo normal",
            "tratamiento": "Vacunación al día",
            "observaciones": "Próximo control en 6 meses",
            "estado": "Completada"
        },
        "2025.08.10 09:15:00": {
            "id_paciente": "23456789",
            "id_doctor": "1402893",
            "fecha_consulta": "2025-08-10",
            "hora_consulta": "09:15",
            "motivo": "Dolor en rodilla izquierda",
            "diagnostico": "Tendinitis rotuliana",
            "tratamiento": "Antiinflamatorios y fisioterapia",
            "observaciones": "Reposo relativo por 2 semanas",
            "estado": "Completada"
        },
        "2025.07.22 16:45:00": {
            "id_paciente": "34567890",
            "id_doctor": "1509104",
            "fecha_consulta": "2025-07-22",
            "hora_consulta": "16:45",
            "motivo": "Lesión en la piel",
            "diagnostico": "Dermatitis de contacto",
            "tratamiento": "Crema con corticoides",
            "observaciones": "Evitar contacto con alérgenos",
            "estado": "Completada"
        },
        "2025.06.05 11:00:00": {
            "id_paciente": "45678901",
            "id_doctor": "1601215",
            "fecha_consulta": "2025-06-05",
            "hora_consulta": "11:00",
            "motivo": "Migrañas frecuentes",
            "diagnostico": "Cefalea tensional crónica",
            "tratamiento": "Analgésicos y técnicas de relajación",
            "observaciones": "Seguimiento en 1 mes",
            "estado": "Completada"
        },
        "2025.05.18 08:30:00": {
            "id_paciente": "56789012",
            "id_doctor": "1708326",
            "fecha_consulta": "2025-05-18",
            "hora_consulta": "08:30",
            "motivo": "Control ginecológico anual",
            "diagnostico": "Sin alteraciones",
            "tratamiento": "Ninguno",
            "observaciones": "Próximo control en 12 meses",
            "estado": "Completada"
        },
        "2025.04.12 15:30:00": {
            "id_paciente": "67890123",
            "id_doctor": "1805437",
            "fecha_consulta": "2025-04-12",
            "hora_consulta": "15:30",
            "motivo": "Dolor abdominal",
            "diagnostico": "Gastritis leve",
            "tratamiento": "Omeprazol y dieta blanda",
            "observaciones": "Evitar alimentos irritantes",
            "estado": "Completada"
        },
        "2025.03.25 10:00:00": {
            "id_paciente": "78901234",
            "id_doctor": "1902548",
            "fecha_consulta": "2025-03-25",
            "hora_consulta": "10:00",
            "motivo": "Revisión de la vista",
            "diagnostico": "Miopía leve",
            "tratamiento": "Prescripción de lentes",
            "observaciones": "Control anual recomendado",
            "estado": "Completada"
        },
        "2025.02.14 13:15:00": {
            "id_paciente": "89012345",
            "id_doctor": "2009659",
            "fecha_consulta": "2025-02-14",
            "hora_consulta": "13:15",
            "motivo": "Dolor en el pecho",
            "diagnostico": "Angina de pecho estable",
            "tratamiento": "Nitratos y betabloqueantes",
            "observaciones": "Control cardiológico mensual",
            "estado": "Completada"
        },
        "2025.01.30 17:00:00": {
            "id_paciente": "90123456",
            "id_doctor": "2106760",
            "fecha_consulta": "2025-01-30",
            "hora_consulta": "17:00",
            "motivo": "Ansiedad y estrés",
            "diagnostico": "Trastorno de ansiedad generalizada",
            "tratamiento": "Terapia cognitivo-conductual",
            "observaciones": "Sesiones semanales recomendadas",
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
                    print(eliminarDoctor(doctores))
                
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
                    print("[4] Ranking de Especialidades Más Consultadas")
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
                    rankingEspecialidadesMasConsultadas(consultas, doctores)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()
