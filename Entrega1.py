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
import os

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
    Incluye manejo de excepciones para mayor robustez.
    """
    print("\n--- Ingresar Paciente ---")
    
    try:
        # Validar el DNI
        dni_valido = False
        while not dni_valido:
            try:
                dni = input("Ingrese el DNI del paciente (solo números): ").strip()
                if not dni:
                    print("El DNI no puede estar vacío.")
                    continue
                if not dni.isdigit():
                    raise ValueError("El DNI debe contener solo números.")
                if len(dni) < 7:
                    raise ValueError("El DNI debe tener al menos 7 dígitos.")
                if dni in pacientes:
                    print("\nYa existe un paciente con ese DNI.")
                    return pacientes
                dni_valido = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado al validar DNI: {e}")
        
        # Validar el nombre
        nombre_valido = False
        while not nombre_valido:
            try:
                nombre = input("Ingrese el nombre del paciente: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                if not nombre.replace(" ", "").isalpha():
                    raise ValueError("El nombre solo puede contener letras.")
                nombre_valido = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado al validar nombre: {e}")
        
        # Validar el apellido
        apellido_valido = False
        while not apellido_valido:
            try:
                apellido = input("Ingrese el apellido del paciente: ").strip()
                if not apellido:
                    raise ValueError("El apellido no puede estar vacío.")
                if not apellido.replace(" ", "").isalpha():
                    raise ValueError("El apellido solo puede contener letras.")
                apellido_valido = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado al validar apellido: {e}")
        
        # Validar el email
        email_valido = False
        while not email_valido:
            try:
                email = input("Ingrese el email del paciente: ").strip()
                if not email:
                    raise ValueError("El email no puede estar vacío.")
                if "@" not in email or "." not in email:
                    raise ValueError("El email debe contener '@' y '.'")
                if email.count("@") != 1:
                    raise ValueError("El email debe contener exactamente un '@'")
                email_valido = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado al validar email: {e}")
        
        # Validar la fecha de nacimiento
        fecha_valida = False
        while not fecha_valida:
            try:
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (AAAA-MM-DD): ").strip()
                if len(fecha_nacimiento) != 10 or fecha_nacimiento.count("-") != 2:
                    raise ValueError("Formato incorrecto. Use AAAA-MM-DD")
                
                partes = fecha_nacimiento.split("-")
                if len(partes) != 3:
                    raise ValueError("La fecha debe tener año, mes y día separados por '-'")
                
                año = int(partes[0])
                mes = int(partes[1])
                día = int(partes[2])
                
                if not (1900 <= año <= 2025):
                    raise ValueError("El año debe estar entre 1900 y 2025")
                if not (1 <= mes <= 12):
                    raise ValueError("El mes debe estar entre 1 y 12")
                if not (1 <= día <= 31):
                    raise ValueError("El día debe estar entre 1 y 31")
                
                fecha_valida = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado al validar fecha: {e}")
        
        # Dirección (sin validación estricta)
        try:
            direccion = input("Ingrese la dirección del paciente: ").strip()
        except Exception as e:
            print(f"Error al ingresar dirección: {e}")
            direccion = ""
        
        # Teléfonos
        telefonos = {}
        for i in range(1, 4):
            try:
                telefono = input(f"Ingrese el teléfono {i} del paciente (deje vacío si no aplica): ").strip()
                telefonos[f"id_telefono_{i}"] = telefono
            except Exception as e:
                print(f"Error al ingresar teléfono {i}: {e}")
                telefonos[f"id_telefono_{i}"] = ""
        
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
        
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al ingresar paciente: {e}")
    
    return pacientes


def modificarPaciente(pacientes):
    """
    Permite modificar los datos de un paciente existente.
    Incluye manejo de excepciones.
    """
    print("\n--- Modificar Paciente ---")
    
    try:
        dni = input("Ingrese el DNI del paciente que desea modificar: ").strip()
        
        if not dni:
            print("Error: Debe ingresar un DNI.")
            return pacientes
        
        if dni not in pacientes:
            print("\nEl DNI del paciente no existe.")
            return pacientes
        
        paciente = pacientes[dni]
        print("\nPaciente encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")
        
        try:
            # Nombre
            nombre_input = input(f"Nombre actual ({paciente['nombre']}): ").strip()
            if nombre_input and not nombre_input.replace(" ", "").isalpha():
                print("Advertencia: El nombre contiene caracteres inválidos. Se mantendrá el actual.")
                nombre = paciente['nombre']
            else:
                nombre = nombre_input or paciente['nombre']
            
            # Apellido
            apellido_input = input(f"Apellido actual ({paciente['apellido']}): ").strip()
            if apellido_input and not apellido_input.replace(" ", "").isalpha():
                print("Advertencia: El apellido contiene caracteres inválidos. Se mantendrá el actual.")
                apellido = paciente['apellido']
            else:
                apellido = apellido_input or paciente['apellido']
            
            # Email
            email_input = input(f"Email actual ({paciente['email']}): ").strip()
            if email_input and ("@" not in email_input or "." not in email_input):
                print("Advertencia: El email es inválido. Se mantendrá el actual.")
                email = paciente['email']
            else:
                email = email_input or paciente['email']
            
            # Fecha de nacimiento
            fecha_input = input(f"Fecha nacimiento actual ({paciente['fecha_nacimiento']}): ").strip()
            if fecha_input:
                try:
                    if len(fecha_input) == 10 and fecha_input.count("-") == 2:
                        partes = fecha_input.split("-")
                        año, mes, día = int(partes[0]), int(partes[1]), int(partes[2])
                        if 1900 <= año <= 2025 and 1 <= mes <= 12 and 1 <= día <= 31:
                            fecha_nacimiento = fecha_input
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                except:
                    print("Advertencia: Fecha inválida. Se mantendrá la actual.")
                    fecha_nacimiento = paciente['fecha_nacimiento']
            else:
                fecha_nacimiento = paciente['fecha_nacimiento']
            
            # Dirección
            direccion = input(f"Dirección actual ({paciente['direccion']}): ").strip() or paciente['direccion']
            
            # Teléfonos
            telefonos = {}
            for i in range(1, 4):
                try:
                    telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({paciente['telefonos'][f'id_telefono_{i}']}): ").strip() or paciente['telefonos'][f'id_telefono_{i}']
                except Exception:
                    telefonos[f"id_telefono_{i}"] = paciente['telefonos'].get(f'id_telefono_{i}', "")
            
            # Estado activo
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
            
        except KeyError as e:
            print(f"Error: Campo faltante en los datos del paciente: {e}")
        except Exception as e:
            print(f"Error al modificar datos: {e}")
            
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al modificar paciente: {e}")
    
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
    Incluye manejo de excepciones.
    """
    print("\n--- Ingresar Doctor ---")
    
    try:
        matricula = input("Ingrese la matrícula profesional del doctor: ").strip()
        
        if not matricula:
            print("Error: La matrícula no puede estar vacía.")
            return doctores
        
        if matricula in doctores:
            print("\nYa existe un doctor con esa matrícula.")
            doctor = doctores[matricula]
            print(f"Nombre actual: {doctor['nombre']} {doctor['apellido']}")
            opcion = input("¿Desea modificar los datos? (S/N): ").upper()
            if opcion != "S":
                print("No se realizaron cambios.")
                return doctores
        
        try:
            # Solicitar datos
            nombre = input("Ingrese el nombre del doctor: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            
            apellido = input("Ingrese el apellido del doctor: ").strip()
            if not apellido:
                raise ValueError("El apellido no puede estar vacío")
            
            email = input("Ingrese el email del doctor: ").strip()
            if not email or "@" not in email or "." not in email:
                raise ValueError("Email inválido")
            
            # Honorarios con validación
            honorarios_valido = False
            while not honorarios_valido:
                try:
                    honorarios_input = input("Ingrese el monto de los honorarios: ").strip()
                    honorarios = float(honorarios_input)
                    if honorarios < 0:
                        raise ValueError("Los honorarios no pueden ser negativos")
                    honorarios_valido = True
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")
            
            # Teléfonos
            telefonos = {}
            for i in range(1, 4):
                try:
                    telefonos[f"id_telefono_{i}"] = input(f"Ingrese el teléfono {i} del doctor (deje vacío si no aplica): ").strip()
                except Exception:
                    telefonos[f"id_telefono_{i}"] = ""
            
            # Especialidades
            especialidades = {}
            for i in range(1, 4):
                try:
                    especialidades[f"id_especialidad_{i}"] = input(f"Ingrese la especialidad {i} del doctor (deje vacío si no aplica): ").strip()
                except Exception:
                    especialidades[f"id_especialidad_{i}"] = ""
            
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
            
        except ValueError as e:
            print(f"Error de validación: {e}")
        except Exception as e:
            print(f"Error al procesar datos del doctor: {e}")
            
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al ingresar doctor: {e}")
    
    return doctores


def modificarDoctor(doctores):
    """
    Permite modificar los datos de un doctor existente en el sistema.
    Incluye manejo de excepciones.
    """
    print("\n--- Modificar Doctor ---")
    
    try:
        matricula = input("Ingrese la matrícula del doctor que desea modificar: ").strip()
        
        if not matricula:
            print("Error: Debe ingresar una matrícula.")
            return doctores
        
        if matricula not in doctores:
            print("\nLa matrícula del doctor no existe.")
            return doctores
        
        doctor = doctores[matricula]
        print("\nDoctor encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")
        
        try:
            nombre = input(f"Nombre actual ({doctor['nombre']}): ").strip() or doctor['nombre']
            apellido = input(f"Apellido actual ({doctor['apellido']}): ").strip() or doctor['apellido']
            
            # Email con validación
            email_input = input(f"Email actual ({doctor['email']}): ").strip()
            if email_input and ("@" not in email_input or "." not in email_input):
                print("Advertencia: Email inválido. Se mantendrá el actual.")
                email = doctor['email']
            else:
                email = email_input or doctor['email']
            
            # Honorarios con validación
            honorarios_input = input(f"Honorarios actuales ({doctor['honorarios']}): ").strip()
            if honorarios_input:
                try:
                    honorarios = float(honorarios_input)
                    if honorarios < 0:
                        print("Advertencia: Honorarios negativos no permitidos. Se mantendrá el actual.")
                        honorarios = doctor['honorarios']
                except ValueError:
                    print("Advertencia: Valor inválido. Se mantendrá el actual.")
                    honorarios = doctor['honorarios']
            else:
                honorarios = doctor['honorarios']
            
            # Teléfonos
            telefonos = {}
            for i in range(1, 4):
                try:
                    telefonos[f"id_telefono_{i}"] = input(f"Teléfono {i} actual ({doctor['telefonos'][f'id_telefono_{i}']}): ").strip() or doctor['telefonos'][f'id_telefono_{i}']
                except Exception:
                    telefonos[f"id_telefono_{i}"] = doctor['telefonos'].get(f'id_telefono_{i}', "")
            
            # Especialidades
            especialidades = {}
            for i in range(1, 4):
                try:
                    especialidades[f"id_especialidad_{i}"] = input(f"Especialidad {i} actual ({doctor['especialidades'][f'id_especialidad_{i}']}): ").strip() or doctor['especialidades'][f'id_especialidad_{i}']
                except Exception:
                    especialidades[f"id_especialidad_{i}"] = doctor['especialidades'].get(f'id_especialidad_{i}', "")
            
            # Estado activo
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
            
        except KeyError as e:
            print(f"Error: Campo faltante en los datos del doctor: {e}")
        except Exception as e:
            print(f"Error al modificar datos: {e}")
            
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al modificar doctor: {e}")
    
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
    Incluye manejo de excepciones robusto.
    """
    print("\n--- Registro de Consulta ---")
    
    try:
        # Validar el DNI del paciente
        dni_valido = False
        while not dni_valido:
            try:
                id_paciente = input("Ingrese el DNI del paciente: ").strip()
                if not id_paciente:
                    raise ValueError("El DNI no puede estar vacío")
                if id_paciente not in pacientes:
                    raise KeyError("El DNI del paciente no está registrado")
                dni_valido = True
            except (ValueError, KeyError) as e:
                print(f"Error: {e}. Intente nuevamente.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        # Validar la matrícula del doctor
        matricula_valida = False
        while not matricula_valida:
            try:
                id_doctor = input("Ingrese la matrícula del doctor: ").strip()
                if not id_doctor:
                    raise ValueError("La matrícula no puede estar vacía")
                if id_doctor not in doctores:
                    raise KeyError("La matrícula del doctor no está registrada")
                matricula_valida = True
            except (ValueError, KeyError) as e:
                print(f"Error: {e}. Intente nuevamente.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        # Solicitar fecha de la consulta
        fecha_valida = False
        while not fecha_valida:
            try:
                fecha_consulta = input("Ingrese la fecha de la consulta (AAAA-MM-DD): ").strip()
                if len(fecha_consulta) != 10 or fecha_consulta.count("-") != 2:
                    raise ValueError("Formato incorrecto. Use AAAA-MM-DD")
                
                partes = fecha_consulta.split("-")
                año, mes, día = int(partes[0]), int(partes[1]), int(partes[2])
                
                if not (1900 <= año <= 2025):
                    raise ValueError("Año fuera de rango (1900-2025)")
                if not (1 <= mes <= 12):
                    raise ValueError("Mes debe estar entre 1 y 12")
                if not (1 <= día <= 31):
                    raise ValueError("Día debe estar entre 1 y 31")
                
                fecha_valida = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        # Solicitar hora de la consulta
        hora_valida = False
        while not hora_valida:
            try:
                hora_consulta = input("Ingrese la hora de la consulta (HH:MM): ").strip()
                if len(hora_consulta) != 5 or hora_consulta.count(":") != 1:
                    raise ValueError("Formato incorrecto. Use HH:MM")
                
                partes = hora_consulta.split(":")
                hora, minuto = int(partes[0]), int(partes[1])
                
                if not (0 <= hora <= 23):
                    raise ValueError("Hora debe estar entre 0 y 23")
                if not (0 <= minuto <= 59):
                    raise ValueError("Minutos deben estar entre 0 y 59")
                
                hora_valida = True
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        # Solicitar otros datos de la consulta
        try:
            motivo = input("Ingrese el motivo de la consulta: ").strip()
            diagnostico = input("Ingrese el diagnóstico (si aplica): ").strip()
            tratamiento = input("Ingrese el tratamiento (si aplica): ").strip()
            observaciones = input("Ingrese observaciones adicionales (si aplica): ").strip()
            estado = input("Ingrese el estado de la consulta (Ejemplo: 'Pendiente', 'Completada'): ").strip()
        except Exception as e:
            print(f"Error al ingresar datos adicionales: {e}")
            motivo = diagnostico = tratamiento = observaciones = estado = ""
        
        # Generar un ID único para la consulta
        try:
            import time
            id_consulta = time.strftime("%Y.%m.%d %H:%M:%S")
        except Exception as e:
            print(f"Error al generar ID: {e}")
            id_consulta = f"{fecha_consulta}_{hora_consulta}"
        
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
        
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado al registrar consulta: {e}")
    
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
    try:    
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
        for id_consulta, datos in (consultas or {}).items():
            try:
                if not isinstance(datos, dict):
                    continue
                fecha = datos.get("fecha_consulta", "")
                # Validar formato de fecha: AAAA-MM-DD
                if len(fecha) == 10 and fecha.count("-") == 2:
                    partes = fecha.split("-")
                    if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
                        año_c = int(partes[0])
                        mes_c = int(partes[1])
                        if año_c == año and mes_c == mes:
                            consultas_filtradas[id_consulta] = datos
            except Exception as e:
                # Ignorar registro malformado y continuar
                print(f"Advertencia: se omitió la consulta '{id_consulta}' por error: {e}")
                continue

        # Mostrar resultados
        if len(consultas_filtradas) == 0:
            print(f"\nNo hay consultas registradas para {mes:02d}/{año}.")
            return
        else:
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

    except Exception as e:
        print(f"\nError inesperado en consultasDelMes: {e}")
        return

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


def guardarTodo(pacientes, doctores, consultas, pacientes_path='pacientes.json', doctores_path='doctores.json', consultas_path='consultas.json'):
    """Guarda los tres diccionarios en sus archivos JSON correspondientes.
    Usa rutas relativas (archivos en el directorio de trabajo).
    """
    guardarJson(pacientes_path, pacientes)
    guardarJson(doctores_path, doctores)
    guardarJson(consultas_path, consultas)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal del programa.
    """
    #-------------------------------------------------
    # Inicialización de variables: cargar desde JSON
    #-------------------------------------------------
    # rutas relativas (archivos en la carpeta de trabajo)
    pacientes_path = 'pacientes.json'
    doctores_path = 'doctores.json'
    consultas_path = 'consultas.json'

    pacientes = cargarJson(pacientes_path, {})
    doctores = cargarJson(doctores_path, {})
    consultas = cargarJson(consultas_path, {})

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
            guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
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
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    pacientes = modificarPaciente(pacientes)
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    pacientes = eliminarPaciente(pacientes)
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                
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
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    doctores = modificarDoctor(doctores)
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resultado = eliminarDoctor(doctores)
                    print(resultado)
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)
                
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
                    guardarTodo(pacientes, doctores, consultas, pacientes_path, doctores_path, consultas_path)

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
