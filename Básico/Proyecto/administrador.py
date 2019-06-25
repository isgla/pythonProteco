# Administrador
import getpass
import vuelo
from vuelo import *

adm = "ro"
contra = "1"

def modifica_vuelo(v):
    flag = True
    while flag:
        mod_vuelo = """
            -----Modificar vuelo-----
            1. Destino
            2. Hora Salida
            3. Hora Llegada
            4. Costo clase Turista
            5. Costo clase Negocios
            6. Costo Primera Clase
            7. Lugares clase Turista
            8. Lugares clase Negocios
            9. Lugares Primera Clase
            10. Fecha salida
            11. Regresar
            """
        print(mod_vuelo)
        opcm = int(input("Ingrese la opción: "))
        if opcm == 1:
            x = input("Ingrese el nuevo destino del vuelo: ")
            v.set_destino(x)
            continue
        elif opcm == 2:
            x = input("Ingrese la nueva hora de salida del vuelo: ")
            v.set_sal(x)
            continue
        elif opcm == 3:
            x = input("Ingrese la nueva hora de llegada del vuelo: ")
            v.set_lleg(x)
            continue
        elif opcm == 4:
            x = int(input("Ingrese el nuevo costo clase Turista: "))
            v.set_tur(x)
            continue
        elif opcm == 5:
            x = int(input("Ingrese el nuevo costo clase Negocios: "))
            v.set_neg(x)
            continue
        elif opcm == 6:
            x = int(input("Ingrese el nuevo costo de primera clase:  "))
            v.set_prim(x)
            continue
        elif opcm == 7:
            x = int(input("Ingrese el nuevo número de lugares en la clase turista: "))
            v.set_l_tur(x)
            continue
        elif opcm == 8:
            x = int(input("Ingrese el nuevo número de lugares en la clase de negocios: "))
            v.set_l_neg(x)
            continue
        elif opcm == 9:
            x = int(input("Ingrese el nuevo número de lugares en primera clase: "))
            v.set_l_prim(x)
            continue
        elif opcm == 10:
            x = input("Ingrese la nueva fecha de salida: ")
            v.set_f_sal(x)
            continue
        elif opcm == 11:
            admin_func()

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

        elif opc == 2:
            vuelos = []
            num_vuelos = int(input("¿Cuántos vuelos desea agregar?: "))
            if num_vuelos<= max_vuelos:
                for i in range(num_vuelos):
                    dest = input("\nIngrese el destino del vuelo: ")
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

        elif opc == 3:
            i = 1
            for vuelo in vuelos:
                print("Vuelo no.: " + str(i))
                print(str(vuelo))
                i += 1

        elif opc == 4:
            
            for vuelo in vuelos:
                print("-"*15)
                print(vuelo.dest)
            
            elim = input("\n¿Cuál es el destino del vuelo que quiere eliminar?: ")

            for vuelo in vuelos:
                if elim == vuelo.dest:
                    vuelos.remove(vuelo)
                else:
                    print("No se encontró ningún vuelo con ese destino.")
                    continue

        elif opc == 5:
            for vuelo in vuelos:
                print("-"*15)
                print(vuelo.dest)

            m = input("¿Cuál es el destino del vuelo que quiere modificar?: ")

            for v in vuelos:
                if m == vuelo.dest:
                    v.modifica_vuelo()
                    continue
                else:
                    print("No se encontró ningún vuelo con ese destino.")
                    continue

        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
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

        elif opc == 2:
            import proyecto as pr
            pr.menu_princ()
            break



        
    