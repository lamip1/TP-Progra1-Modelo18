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
    def modificarPaciente(pacientes):
    """
    Permite modificar los datos de un paciente existente.
    """
    print("\n--- Modificar Paciente ---")
    id_paciente = input("Ingrese el ID del paciente que desea modificar: ")

    if id_paciente in pacientes:
        paciente = pacientes[id_paciente]
        print("\nPaciente encontrado. Ingrese los nuevos datos (deje vacío para mantener el actual):")

        nombre = input(f"Nombre actual ({paciente['nombre']}): ") or paciente['nombre']
        apellido = input(f"Apellido actual ({paciente['apellido']}): ") or paciente['apellido']
        dni = input(f"DNI actual ({paciente['dni']}): ") or paciente['dni']
        telefono = input(f"Teléfono actual ({paciente['telefono']}): ") or paciente['telefono']
        email = input(f"Email actual ({paciente['email']}): ") or paciente['email']
        fecha_nacimiento = input(f"Fecha nacimiento actual ({paciente['fecha_nacimiento']}): ") or paciente['fecha_nacimiento']
        calle = input(f"Calle actual ({paciente['direccion']['calle']}): ") or paciente['direccion']['calle']
        numero = input(f"Número actual ({paciente['direccion']['numero']}): ") or paciente['direccion']['numero']
        ciudad = input(f"Ciudad actual ({paciente['direccion']['ciudad']}): ") or paciente['direccion']['ciudad']

        # Actualización del registro
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

        print(f"\nPaciente con ID {id_paciente} modificado exitosamente.")
    else:
        print("\nEl ID del paciente no existe.")
    
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
    ...

def modificarDoctor(doctores):
    """
    Permite modificar los datos de un doctor existente en el sistema.
    
    Entrada: doctores (diccionario con los datos de los doctores).
    Salida: Actualiza los datos del doctor seleccionado.
    """
    print("\n--- Modificar Doctor ---")
    
    # Solicitar el ID del doctor a modificar
    id_doctor = input("Ingrese el ID del doctor que desea modificar: ")
    
    if id_doctor in doctores:
        print("\nDoctor encontrado. Ingrese los nuevos datos (deje vacío para no modificar):")
        
        # Mostrar los datos actuales del doctor
        print(f"Nombre actual: {doctores[id_doctor]['nombre']}")
        nombre = input("Nuevo nombre: ")
        print(f"Apellido actual: {doctores[id_doctor]['apellido']}")
        apellido = input("Nuevo apellido: ")
        print(f"Matrícula actual: {doctores[id_doctor]['matricula']}")
        matricula = input("Nueva matrícula: ")
        print(f"Especialidad actual: {doctores[id_doctor]['especialidad']}")
        especialidad = input("Nueva especialidad: ")
        print(f"Teléfono actual: {doctores[id_doctor]['telefono']}")
        telefono = input("Nuevo teléfono: ")
        print(f"Email actual: {doctores[id_doctor]['email']}")
        email = input("Nuevo email: ")
        print(f"Honorarios actuales: {doctores[id_doctor]['honorarios']['monto']} {doctores[id_doctor]['honorarios']['moneda']}")
        monto = input("Nuevo monto de honorarios: ")
        moneda = input("Nueva moneda de honorarios: ")
        
        # Actualizar los datos del doctor
        if nombre:
            doctores[id_doctor]['nombre'] = nombre
        if apellido:
            doctores[id_doctor]['apellido'] = apellido
        if matricula:
            doctores[id_doctor]['matricula'] = matricula
        if especialidad:
            doctores[id_doctor]['especialidad'] = especialidad
        if telefono:
            doctores[id_doctor]['telefono'] = telefono
        if email:
            doctores[id_doctor]['email'] = email
        if monto:
            doctores[id_doctor]['honorarios']['monto'] = float(monto)
        if moneda:
            doctores[id_doctor]['honorarios']['moneda'] = moneda
        
        print("\nDoctor modificado exitosamente.")
    else:
        print("\nEl ID del doctor no existe.")

def eliminarDoctor(doctores):
    ...

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
