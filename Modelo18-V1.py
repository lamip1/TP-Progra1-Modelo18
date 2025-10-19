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
    
    # Solicitar y validar el DNI
    while True:
        dni = input("Ingrese el DNI del paciente (solo números): ")
        if dni.isdigit() and len(dni) >= 7:  # Verifica que sea numérico y tenga al menos 7 dígitos
            if dni in pacientes:
                print("\nYa existe un paciente con ese DNI.")
                return pacientes
            break
        else:
            print("DNI inválido. Intente nuevamente.")
    
    # Solicitar y validar el nombre
    while True:
        nombre = input("Ingrese el nombre del paciente: ").strip()
        if nombre.isalpha():  # Verifica que solo contenga letras
            break
        else:
            print("Nombre inválido. Intente nuevamente.")
    
    # Solicitar y validar el apellido
    while True:
        apellido = input("Ingrese el apellido del paciente: ").strip()
        if apellido.isalpha():  # Verifica que solo contenga letras
            break
        else:
            print("Apellido inválido. Intente nuevamente.")
    
    # Solicitar y validar el teléfono
    while True:
        telefono = input("Ingrese el teléfono del paciente (solo números): ")
        if telefono.isdigit() and len(telefono) >= 8:  # Verifica que sea numérico y tenga al menos 8 dígitos
            break
        else:
            print("Teléfono inválido. Intente nuevamente.")
    
    # Solicitar y validar el email
    while True:
        email = input("Ingrese el email del paciente: ").strip()
        if "@" in email and "." in email:  # Verifica que tenga un formato básico de email
            break
        else:
            print("Email inválido. Intente nuevamente.")
    
    # Solicitar y validar la fecha de nacimiento
    while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (AAAA-MM-DD): ")
        try:
            año, mes, día = map(int, fecha_nacimiento.split("-"))
            if len(fecha_nacimiento) == 10 and 1900 <= año <= 2025 and 1 <= mes <= 12 and 1 <= día <= 31:
                break
        except ValueError:
            print("Fecha de nacimiento inválida. Intente nuevamente.")
    
    # Solicitar y validar la dirección
    while True:
        calle = input("Ingrese la calle de la dirección: ").strip()
        if calle:
            break
        else:
            print("Calle inválida. Intente nuevamente.")
    
    while True:
        numero = input("Ingrese el número de la dirección: ")
        if numero.isdigit():  # Verifica que sea numérico
            break
        else:
            print("Número inválido. Intente nuevamente.")
    
    while True:
        ciudad = input("Ingrese la ciudad de la dirección: ").strip()
        if ciudad.isalpha():  # Verifica que solo contenga letras
            break
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
    ...

def listarPacientes(pacientes):
    """
    Explicacion: esta funcion imprime los pacientes.

    Entrada: la funcion recibe como parametro un diccionario de los pacientes.

    Salida: la funcion imprime el listado de los pacientes.
    """

    for k,v in pacientes.items():

        #Listado de los pacientes
        print(k,":")
        print("\t","DNI: ", v['dni'])
        print("\t","Nombre: ",v["nombre"])
        print("\t","Apellido: ",v["apellido"])
        print("\t","Telefono: ",v["telefono"])
        print("\t","Email: ",v["email"])
        print("\t","Fecha de nacimiento: ",v["fecha_nacimiento"])
        print("\t","Direccion: ")
        print("\t\t", "Calle:", v["direccion"]["calle"])
        print("\t\t", "Numero:", v["direccion"]["numero"])
        print("\t\t", "Ciudad:", v["direccion"]["ciudad"]) 

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
    ...

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    pacientes = {}
    doctores = {}

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            opciones = 2
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Paciente")
            print("[2] Gestión de Doctor")
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

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa

main()