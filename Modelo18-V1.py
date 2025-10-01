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
paciente = {
    "id_paciente": {
        "activo": True,  # bool
        "dni": "",  # str
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
doctor = {
    "id_doctor": {
        "activo": True,  # bool
        "matricula": "",  # str
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
consulta = {
    "id_consulta": {
        "id_paciente": "",  # str
        "id_doctor": "",  # str
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
    Permite ingresar un nuevo paciente al sistema.
    Genera un id único para el paciente utilizando el módulo random.
    """
    print("\n--- Ingresar Paciente ---")
    
    # Generar un id único para el paciente
    id_paciente = f"P{random.randint(1000, 9999)}"
    while id_paciente in pacientes:  # Asegurarse de que el ID no esté duplicado
        id_paciente = f"P{random.randint(1000, 9999)}"
    
    # Solicitar datos del paciente
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    dni = input("Ingrese el DNI del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    email = input("Ingrese el email del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (AAAA-MM-DD): ")
    calle = input("Ingrese la calle de la dirección: ")
    numero = input("Ingrese el número de la dirección: ")
    ciudad = input("Ingrese la ciudad de la dirección: ")
    
    # Crear el registro del paciente
    pacientes[id_paciente] = {
        "activo": True,
        "dni": dni,
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
    
    print(f"\nPaciente ingresado exitosamente con ID: {id_paciente}")
    return pacientes

def modificarPaciente(pacientes):
    ...

def eliminarPaciente(pacientes):
    ...

def listarPacientes(pacientes):
    ...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    pacientes = {}

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            opciones = 1
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Paciente")
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

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()