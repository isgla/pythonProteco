# Administrador
import getpass
import vuelo
from vuelo import *

adm = "Rodrigo"
contra = "abc123!"

def admin_func():
    flag = True
    while flag:
        ventas = """
        ------------SISTEMA DE VENTAS------------
                1. Ingresar no. máximo de vuelos
                2. Ingresar vuelos
                3. Listar vuelos
                4. Cancelar vuelos
                5. Actualizar vuelos
                6. Estadísticas de pago
                7. Estadísticas de clases
                8. Información administrador
                9. Regresar
        """
        print(ventas)
        opc = int(input("Ingrese la opción: "))
        if opc == 1:
            max_vuelos = int(input("Ingrese el número máximo de vuelos que el aeropuerto tendrá disponible para dar de alta en el sistema: "))
            continue

        if opc == 2:
            vuelos = []
            num_vuelos = int(input("¿Cuántos vuelos desea agregar?: "))
            if num_vuelos<= max_vuelos:
                for i in range(num_vuelos):
                    dest = input("Ingrese el destino del vuelo: ")
                    sal = input("Ingrese la hora de salida: ")
                    lleg = input("Ingrese la hora de llegada: ")
                    tur = int(input("Ingrese el costo del viaje de turista: "))
                    neg = int(input("Ingrese el costo del viaje de negocios: "))
                    prim = int(input("Ingrese el costo del viaje de primera clase: "))
                    l_tur = int(input("Ingrese los lugares disponibles para clase de turista: "))
                    l_neg = int(input("Ingrese los lugares disponibles para clase de negocios: "))
                    l_prim = int(input("Ingrese los lugares disponibles para primera clase: "))
                    f_sal = input("Ingrese la fecha de salida: ")

                    v = Vuelo(dest, sal, lleg, tur, neg, prim, l_tur, l_neg, l_prim, f_sal)
                    
                    vuelos.append(v)
            else:
                print("Debe ingresar un número menor a la que ingresó como mayor cantidad de vuelos.")

        if opc == 3:
            i = 1
            for vuelo in vuelos:
                print("Vuelo no.: " + str(i))
                print(str(vuelo))
                i += 1

        if opc == 4:
            
            for vuelo in vuelos:
                print("-"*15)
                print(vuelo.dest)
            
            elim = input("¿Cuál es el destino del vuelo que quiere eliminar?: ")

            for vuelo in vuelos:
                if elim == vuelo.dest:
                    vuelos.remove(vuelo)
                else:
                    print("No se encontró ningún vuelo con ese destino.")
                    continue

        if opc == 5:
            pass
        if opc == 6:
            pass
        if opc == 7:
            pass
        if opc == 8:
            pass
        if opc == 9:
            m_admin()
        



def m_admin():

    flag = True
    while flag:
        m_admin = """
        ------------ADMINISTRADOR------------
        1. Ingresar
        2. Regresar
        """
        print(m_admin)
        opc = int(input("Ingrese la opción: "))

        if opc == 1:
            admin = input("Ingrese el administrador: ")
            password = getpass.getpass("Escriba su contraseña: ")
            if (admin!=adm)|(password!=contra):
                print("Contraseña o usuario incorrecto")
                continue
            else:
                admin_func()

        if opc == 2:
            import proyecto as pr
            pr.menu_princ()
            break



        
    