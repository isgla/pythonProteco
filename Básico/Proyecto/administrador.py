# Administrador
import getpass
import vuelo
from vuelo import *

class Administrador:
    def __init__(self, nombre, apellido, sueldo, usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.usuario = usuario
        self.contrasena = contrasena
        
    def __str__(self):
        admin = """
        Nombre: {0}
        Apellido: {1}
        Usuario: {2}
        Sueldo: {3}
        """.format(self.nombre, self.apellido, self.usuario, self.sueldo)
        return admin

    def get_user(self):
        return self.usuario

    def get_pass(self):
        return self.contrasena

administrador = Administrador("Hannah", "Gonzalez", 50000, "han", "12")

adm = administrador.get_user()
contra = administrador.get_pass()

vuelos = []

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
            #Checar lista vacia
            if not vuelos:
                print("No hay vuelos")
            else:
                for vuelo in vuelos:
                    print("Vuelo no.: " + str(i))
                    print(str(vuelo))
                    i += 1

        elif opc == 4:
            print("Los vuelos son: ")
            i = 1
            for vuelo in vuelos:
                print("-"*15)
                print(str(i) + " " + str(vuelo.dest))
                i += 1

            num_vuelo = int(input("Número de vuelo a eliminar: "))
            del vuelos[num_vuelo - 1]
            """
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
            """

        elif opc == 5:
            print("Los vuelos son: ")
            i = 1
            for vuelo in vuelos:
                print("-"*15)
                print(str(i) + " " + str(vuelo.dest))
                i += 1

            num_vuelo = int(input("Número de vuelo a modificar: "))
            v = vuelos[num_vuelo - 1]
            v.modifica_vuelo()
            continue

        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            print(str(administrador))
            continue
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



        
    