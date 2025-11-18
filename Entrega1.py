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
import json

# Rutas de archivos (constantes de módulo) - usan nombres relativos
PACIENTES_PATH = 'pacientes.json'
DOCTORES_PATH = 'doctores.json'
CONSULTAS_PATH = 'consultas.json'

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
    # Cargar datos localmente (load-on-demand)
    pacientes_local = cargarJson(PACIENTES_PATH, {})

    print("\n--- Ingresar Paciente ---")
    try:
        dni_valido = False
        while not dni_valido:
            dni = input("Ingrese el DNI del paciente (solo números): ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                continue
            if not dni.isdigit() or len(dni) < 7:
                print("DNI inválido. Intente nuevamente.")
                continue
            if dni in pacientes_local:
                print("\nYa existe un paciente con ese DNI.")
                return pacientes_local
            dni_valido = True

        nombre = input("Ingrese el nombre del paciente: ").strip()
        apellido = input("Ingrese el apellido del paciente: ").strip()
        email = input("Ingrese el email del paciente: ").strip()
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (AAAA-MM-DD): ").strip()
        direccion = input("Ingrese la dirección del paciente: ").strip()

        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Ingrese el teléfono {i} del paciente (deje vacío si no aplica): ").strip()

        pacientes_local[dni] = {
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "telefonos": telefonos
        }

        # Guardar inmediatamente (save-after-change)
        guardarJson(PACIENTES_PATH, pacientes_local)
        print(f"\nPaciente ingresado exitosamente con DNI: {dni}")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al ingresar paciente: {e}")

    return pacientes_local

def modificarPaciente(pacientes):
    pacientes_local = cargarJson(PACIENTES_PATH, {})
    print("\n--- Modificar Paciente ---")
    try:
        dni = input("Ingrese el DNI del paciente que desea modificar: ").strip()
        if not dni:
            print("Error: Debe ingresar un DNI.")
            return pacientes_local
        if dni not in pacientes_local:
            print("\nEl DNI del paciente no existe.")
            return pacientes_local

        paciente = pacientes_local[dni]
        print("\nPaciente encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")

        nombre = input(f"Nombre actual ({paciente.get('nombre','')}): ").strip() or paciente.get('nombre','')
        apellido = input(f"Apellido actual ({paciente.get('apellido','')}): ").strip() or paciente.get('apellido','')
        email = input(f"Email actual ({paciente.get('email','')}): ").strip() or paciente.get('email','')
        fecha_nacimiento = input(f"Fecha nacimiento actual ({paciente.get('fecha_nacimiento','')}): ").strip() or paciente.get('fecha_nacimiento','')
        direccion = input(f"Dirección actual ({paciente.get('direccion','')}): ").strip() or paciente.get('direccion','')

        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({paciente.get('telefonos',{}).get(f'id_telefono_{i}','')}): ").strip() or paciente.get('telefonos',{}).get(f'id_telefono_{i}','')

        activo_input = input(f"Activo actual ({paciente.get('activo', True)}) - (S/N, deje vacío para mantener): ").strip().lower()
        if activo_input == 's':
            activo = True
        elif activo_input == 'n':
            activo = False
        else:
            activo = paciente.get('activo', True)

        pacientes_local[dni] = {
            "activo": activo,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "telefonos": telefonos
        }

        guardarJson(PACIENTES_PATH, pacientes_local)
        print(f"\nPaciente con DNI {dni} modificado exitosamente.")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al modificar paciente: {e}")

    return pacientes_local

def eliminarPaciente(pacientes):
    pacientes_local = cargarJson(PACIENTES_PATH, {})
    print("\n--- Eliminar Paciente ---")
    dni = input("Ingrese el DNI del paciente que desea eliminar: ").strip()

    if dni in pacientes_local:
        pacientes_local[dni]["activo"] = False
        print(f"Paciente con DNI {dni} ha sido desactivado exitosamente.")
        guardarJson(PACIENTES_PATH, pacientes_local)
    else:
        print("Paciente no encontrado.")

    return pacientes_local

def listarPacientes(pacientes):
    pacientes_local = cargarJson(PACIENTES_PATH, {})
    print("\n--- Listado de Pacientes ---")
    for dni, paciente in pacientes_local.items():
        if paciente.get("activo", True):
            print(f"DNI: {dni}")
            print(f"\tNombre: {paciente.get('nombre','')}")
            print(f"\tApellido: {paciente.get('apellido','')}")
            print(f"\tEmail: {paciente.get('email','')}")
            print(f"\tFecha de nacimiento: {paciente.get('fecha_nacimiento','')}")
            print(f"\tDirección: {paciente.get('direccion','')}")
            print("\tTeléfonos:")
            for key, value in paciente.get('telefonos',{}).items():
                print(f"\t\t{key}: {value}")
            print()

def ingresarDoctor(doctores):
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Ingresar Doctor ---")
    try:
        matricula = input("Ingrese la matrícula profesional del doctor: ").strip()
        if not matricula:
            print("Error: La matrícula no puede estar vacía.")
            return doctores_local
        if matricula in doctores_local:
            print("\nYa existe un doctor con esa matrícula.")
            opcion = input("¿Desea modificar los datos? (S/N): ").upper()
            if opcion != "S":
                print("No se realizaron cambios.")
                return doctores_local

        nombre = input("Ingrese el nombre del doctor: ").strip()
        apellido = input("Ingrese el apellido del doctor: ").strip()
        email = input("Ingrese el email del doctor: ").strip()

        honorarios = 0.0
        while True:
            try:
                honorarios_input = input("Ingrese el monto de los honorarios: ").strip()
                honorarios = float(honorarios_input)
                if honorarios < 0:
                    print("Los honorarios no pueden ser negativos")
                    continue
                break
            except ValueError:
                print("Valor inválido. Intente nuevamente.")

        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Ingrese el teléfono {i} del doctor (deje vacío si no aplica): ").strip()

        especialidades = {}
        for i in range(1, 4):
            especialidades[f"id_especialidad_{i}"] = input(f"Ingrese la especialidad {i} del doctor (deje vacío si no aplica): ").strip()

        doctores_local[matricula] = {
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "honorarios": honorarios,
            "telefonos": telefonos,
            "especialidades": especialidades
        }

        guardarJson(DOCTORES_PATH, doctores_local)
        print(f"\nDoctor registrado/modificado exitosamente con matrícula: {matricula}")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al ingresar doctor: {e}")

    return doctores_local

def modificarDoctor(doctores):
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Modificar Doctor ---")
    try:
        matricula = input("Ingrese la matrícula del doctor que desea modificar: ").strip()
        if not matricula:
            print("Error: Debe ingresar una matrícula.")
            return doctores_local
        if matricula not in doctores_local:
            print("\nLa matrícula del doctor no existe.")
            return doctores_local

        doctor = doctores_local[matricula]
        print("\nDoctor encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")

        nombre = input(f"Nombre actual ({doctor.get('nombre','')}): ").strip() or doctor.get('nombre','')
        apellido = input(f"Apellido actual ({doctor.get('apellido','')}): ").strip() or doctor.get('apellido','')
        email = input(f"Email actual ({doctor.get('email','')}): ").strip() or doctor.get('email','')

        honorarios_input = input(f"Honorarios actuales ({doctor.get('honorarios',0.0)}): ").strip()
        try:
            honorarios = float(honorarios_input) if honorarios_input else float(doctor.get('honorarios',0.0))
            if honorarios < 0:
                print("Advertencia: Honorarios negativos no permitidos. Se mantendrá el actual.")
                honorarios = float(doctor.get('honorarios',0.0))
        except ValueError:
            print("Advertencia: Valor inválido. Se mantendrá el actual.")
            honorarios = float(doctor.get('honorarios',0.0))

        telefonos = {}
        for i in range(1, 4):
            telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({doctor.get('telefonos',{}).get(f'id_telefono_{i}','')}): ").strip() or doctor.get('telefonos',{}).get(f'id_telefono_{i}','')

        especialidades = {}
        for i in range(1, 4):
            especialidades[f"id_especialidad_{i}"] = input(f"Especialidad {i} actual ({doctor.get('especialidades',{}).get(f'id_especialidad_{i}','')}): ").strip() or doctor.get('especialidades',{}).get(f'id_especialidad_{i}','')

        activo_input = input(f"Activo actual ({doctor.get('activo', True)}) - (S/N, deje vacío para mantener): ").strip().lower()
        if activo_input == 's':
            activo = True
        elif activo_input == 'n':
            activo = False
        else:
            activo = doctor.get('activo', True)

        doctores_local[matricula] = {
            "activo": activo,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "honorarios": float(honorarios),
            "telefonos": telefonos,
            "especialidades": especialidades
        }

        guardarJson(DOCTORES_PATH, doctores_local)
        print(f"\nDoctor con matrícula {matricula} modificado exitosamente.")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al modificar doctor: {e}")

    return doctores_local

def eliminarDoctor(doctores):
    doctores_local = cargarJson(DOCTORES_PATH, {})
    matricula = input("Ingresar el numero de matricula del doctor que desea eliminar: ").strip()
    if not matricula:
        print("Error: debe ingresar un número de matrícula.")
        return doctores_local
    if matricula in doctores_local:
        if not doctores_local[matricula].get("activo", True):
            print("El doctor ya está desactivado.")
            return doctores_local
        doctores_local[matricula]["activo"] = False
        guardarJson(DOCTORES_PATH, doctores_local)
        print("Doctor desactivado exitosamente.")
    else:
        print("Doctor no encontrado.")
    return doctores_local

def listarDoctores(doctores):
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Listado de Doctores ---")
    for matricula, doctor in doctores_local.items():
        if doctor.get("activo", True):
            print(f"Matrícula: {matricula}")
            print(f"\tNombre: {doctor.get('nombre','')}")
            print(f"\tApellido: {doctor.get('apellido','')}")
            print(f"\tEmail: {doctor.get('email','')}")
            print(f"\tHonorarios: {doctor.get('honorarios',0.0)}")
            print("\tTeléfonos:")
            for key, value in doctor.get('telefonos',{}).items():
                print(f"\t\t{key}: {value}")
            print("\tEspecialidades:")
            for key, value in doctor.get('especialidades',{}).items():
                print(f"\t\t{key}: {value}")
            print()

def registrarConsulta(consultas, pacientes, doctores):
    pacientes_local = cargarJson(PACIENTES_PATH, {})
    doctores_local = cargarJson(DOCTORES_PATH, {})
    consultas_local = cargarJson(CONSULTAS_PATH, {})

    print("\n--- Registro de Consulta ---")
    try:
        id_paciente = input("Ingrese el DNI del paciente: ").strip()
        if not id_paciente or id_paciente not in pacientes_local:
            print("DNI no registrado.")
            return consultas_local

        id_doctor = input("Ingrese la matrícula del doctor: ").strip()
        if not id_doctor or id_doctor not in doctores_local:
            print("Matrícula no registrada.")
            return consultas_local

        fecha_consulta = input("Ingrese la fecha de la consulta (AAAA-MM-DD): ").strip()
        hora_consulta = input("Ingrese la hora de la consulta (HH:MM): ").strip()
        motivo = input("Ingrese el motivo de la consulta: ").strip()
        diagnostico = input("Ingrese el diagnóstico (si aplica): ").strip()
        tratamiento = input("Ingrese el tratamiento (si aplica): ").strip()
        observaciones = input("Ingrese observaciones adicionales (si aplica): ").strip()
        estado = input("Ingrese el estado de la consulta (Ejemplo: 'Pendiente', 'Completada'): ").strip()

        try:
            id_consulta = time.strftime("%Y.%m.%d %H:%M:%S")
        except Exception:
            id_consulta = f"{fecha_consulta}_{hora_consulta}"

        consultas_local[id_consulta] = {
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

        guardarJson(CONSULTAS_PATH, consultas_local)
        print(f"\nConsulta registrada exitosamente con ID: {id_consulta}")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al registrar consulta: {e}")

    return consultas_local

def consultasDelMes(consultas):
    consultas_local = cargarJson(CONSULTAS_PATH, {})
    print("\n--- Consultas del Mes ---")
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)
    mes = input("Ingrese el mes (1-12): ").strip()
    if not (mes.isdigit() and 1 <= int(mes) <= 12):
        print("Mes inválido. Operación cancelada.")
        return
    mes = int(mes)

    consultas_filtradas = {}
    for id_consulta, datos in (consultas_local or {}).items():
        try:
            fecha = datos.get("fecha_consulta", "")
            if len(fecha) == 10 and fecha.count("-") == 2:
                partes = fecha.split("-")
                año_c = int(partes[0])
                mes_c = int(partes[1])
                if año_c == año and mes_c == mes:
                    consultas_filtradas[id_consulta] = datos
        except Exception:
            continue

    if len(consultas_filtradas) == 0:
        print(f"\nNo hay consultas registradas para {mes:02d}/{año}.")
        return

    print(f"\nConsultas registradas en {mes:02d}/{año}:")
    print("--------------------------------------------------")
    contador = 0
    for id_consulta, datos in consultas_filtradas.items():
        contador += 1
        fecha = datos.get('fecha_consulta', '')
        hora = datos.get('hora_consulta', '')
        paciente = datos.get('id_paciente', '')
        doctor = datos.get('id_doctor', '')
        motivo = datos.get('motivo', '')
        estado = datos.get('estado', '')
        print(f"Consulta N° {contador}")
        print(f"ID: {id_consulta}")
        print(f"  Fecha: {fecha} - Hora: {hora}")
        print(f"  Paciente (DNI): {paciente}")
        print(f"  Doctor (Matrícula): {doctor}")
        print(f"  Motivo: {motivo}")
        print(f"  Estado: {estado}")
        print("--------------------------------------------------")
    print(f"Total de consultas encontradas: {contador}")

def resumenAnualConsultasPorDoctorCantidades(consultas, doctores):
    consultas_local = cargarJson(CONSULTAS_PATH, {})
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Resumen Anual de Consultas por Doctor (Cantidades) ---")
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)

    matriz_cantidades = {}
    for id_doctor, datos_doctor in doctores_local.items():
        if datos_doctor.get("activo", True):
            matriz_cantidades[id_doctor] = [0] * 12

    for id_consulta, datos_consulta in consultas_local.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            año_c = int(partes[0])
            mes_c = int(partes[1])
            if año_c == año and 1 <= mes_c <= 12:
                id_doctor = datos_consulta.get("id_doctor", "")
                if id_doctor in matriz_cantidades:
                    matriz_cantidades[id_doctor][mes_c - 1] += 1

    if not matriz_cantidades:
        print(f"\nNo hay doctores activos registrados.")
        return
    if not any(sum(cantidades) > 0 for cantidades in matriz_cantidades.values()):
        print(f"\nNo hay consultas registradas para el año {año}.")
        return

    print(f"\n{'='*120}")
    print(f"CANTIDADES TOTALES POR MES - AÑO {año}")
    print(f"{'='*120}")
    meses = ["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
    print(f"{'Doctor':<25}", end="")
    for mes in meses:
        print(f"{mes}.{str(año)[2:]:>2}", end=" ")
    print(); print(f"{'-'*120}")

    for id_doctor, cantidades in matriz_cantidades.items():
        if id_doctor in doctores_local:
            doctor = doctores_local[id_doctor]
            nombre_completo = f"{doctor.get('nombre','')} {doctor.get('apellido','')}"
            if len(nombre_completo) > 23:
                nombre_completo = nombre_completo[:20] + "..."
            print(f"{nombre_completo:<25}", end="")
            for cantidad in cantidades:
                print(f"{cantidad:>4} ", end="")
            print()
    print(f"{'='*120}")

def resumenAnualConsultasPorDoctorHonorarios(consultas, doctores):
    consultas_local = cargarJson(CONSULTAS_PATH, {})
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Resumen Anual de Honorarios por Doctor ---")
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)

    matriz_honorarios = {}
    for id_doctor, datos_doctor in doctores_local.items():
        if datos_doctor.get("activo", True):
            matriz_honorarios[id_doctor] = [0.0] * 12

    for id_consulta, datos_consulta in consultas_local.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            año_c = int(partes[0])
            mes_c = int(partes[1])
            if año_c == año and 1 <= mes_c <= 12:
                id_doctor = datos_consulta.get("id_doctor", "")
                if id_doctor in matriz_honorarios and id_doctor in doctores_local:
                    honorario = doctores_local[id_doctor].get("honorarios", 0.0)
                    matriz_honorarios[id_doctor][mes_c - 1] += honorario

    if not matriz_honorarios:
        print(f"\nNo hay doctores activos registrados.")
        return
    if not any(sum(honorarios) > 0 for honorarios in matriz_honorarios.values()):
        print(f"\nNo hay consultas registradas para el año {año}.")
        return

    print(f"\n{'='*160}")
    print(f"HONORARIOS TOTALES POR MES - AÑO {año} (en pesos)")
    print(f"{'='*160}")
    meses = ["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
    print(f"{'Doctor':<25}", end="")
    for mes in meses:
        print(f"{mes}.{str(año)[2:]:>2}", end="      ")
    print(); print(f"{'-'*160}")

    for id_doctor, honorarios in matriz_honorarios.items():
        if id_doctor in doctores_local:
            doctor = doctores_local[id_doctor]
            nombre_completo = f"{doctor.get('nombre','')} {doctor.get('apellido','')}"
            if len(nombre_completo) > 23:
                nombre_completo = nombre_completo[:20] + "..."
            print(f"{nombre_completo:<25}", end="")
            for honorario in honorarios:
                print(f"{honorario:>10,.2f}  ", end="")
            print()
    print(f"{'='*160}")

def rankingEspecialidadesMasConsultadas(consultas, doctores):
    consultas_local = cargarJson(CONSULTAS_PATH, {})
    doctores_local = cargarJson(DOCTORES_PATH, {})
    print("\n--- Ranking de Especialidades Más Consultadas ---")
    año = input("Ingrese el año (AAAA): ").strip()
    if not (año.isdigit() and 1900 <= int(año) <= 2025):
        print("Año inválido. Operación cancelada.")
        return
    año = int(año)

    especialidades_contador = {}
    for id_consulta, datos_consulta in consultas_local.items():
        fecha = datos_consulta.get("fecha_consulta", "")
        if len(fecha) == 10 and fecha.count("-") == 2:
            partes = fecha.split("-")
            año_c = int(partes[0])
            if año_c == año:
                id_doctor = datos_consulta.get("id_doctor", "")
                if id_doctor in doctores_local and doctores_local[id_doctor].get("activo", True):
                    especialidades_dict = doctores_local[id_doctor].get("especialidades", {})
                    for key, especialidad in especialidades_dict.items():
                        especialidad = especialidad.strip()
                        if especialidad:
                            especialidades_contador[especialidad] = especialidades_contador.get(especialidad, 0) + 1

    if not especialidades_contador:
        print(f"\nNo hay consultas registradas para el año {año}.")
        return

    especialidades_ordenadas = sorted(especialidades_contador.items(), key=lambda x: x[1], reverse=True)
    total_consultas = sum(especialidades_contador.values())

    print(f"\n{'='*70}")
    print(f"RANKING DE ESPECIALIDADES MÁS CONSULTADAS - AÑO {año}")
    print(f"{'='*70}")
    print(f"{ 'Posición':<12}{'Especialidad':<35}{'Consultas':>10}{'%':>8}")
    print(f"{'-'*70}")
    posicion = 1
    for especialidad, cantidad in especialidades_ordenadas:
        porcentaje = (cantidad / total_consultas) * 100
        print(f"{posicion:<12}{especialidad:<35}{cantidad:>10}{porcentaje:>7.1f}%")
        posicion += 1
    print(f"{'-'*70}")
    print(f"{'TOTAL':<47}{total_consultas:>10}{100.0:>7.1f}%")
    print(f"{'='*70}")

# Funciones para manejo de archivos JSON
def cargarJson(path, default=None):
    """Carga un JSON desde la ruta indicada. Retorna default en caso de error."""
    if default is None:
        default = {}
    try:
        f = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        return default
    except Exception:
        return default

    try:
        data = json.load(f)
        f.close()
        return data
    except Exception:
        try:
            f.close()
        except:
            pass
        return default


def guardarJson(path, data):
    """Guarda el diccionario en formato JSON en la ruta indicada."""
    try:
        f = open(path, 'w', encoding='utf-8')
    except Exception as e:
        print(f"Error abriendo {path} para escritura: {e}")
        return
    try:
        json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error guardando {path}: {e}")
    finally:
        try:
            f.close()
        except:
            pass


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal del programa.
    """
    #-------------------------------------------------
    # Inicialización de variables: no cargamos los diccionarios globalmente aquí
    # Las funciones usan load-on-demand y guardan después de modificar (save-after-change)
    #-------------------------------------------------
    # rutas relativas (usar constantes del módulo)
    pacientes_path = PACIENTES_PATH
    doctores_path = DOCTORES_PATH
    consultas_path = CONSULTAS_PATH

    # No cargamos los datos acá para no mantenerlos en memoria ni realizar I/O redundante.
    pacientes = None
    doctores = None
    consultas = None

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
            # No es necesario guardar aquí: cada función guarda sus cambios inmediatamente.
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
                    pacientes = modificarPaciente(pacientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    pacientes = eliminarPaciente(pacientes)
                
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
                    doctores = modificarDoctor(doctores)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resultado = eliminarDoctor(doctores)
                    print(resultado)
                
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
