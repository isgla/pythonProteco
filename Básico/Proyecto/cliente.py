#Cliente
import getpass
import vuelo
from vuelo import *

class Cliente():
    
    def __init__(self, nombre, apellido, edad, usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.usuario = usuario
        self.contrasena = contrasena

    def __str__(self):
        s = """
        Nombre: {0}
        Apellido: {1}
        Edad: {2}
        Usuario: {3}
        """.format(self.nombre, self.apellido, self.edad, self.usuario)
        return s

    def get_usuario_cliente(self):
        return self.usuario

    def get_contra_cliente(self):
        return self.contrasena

    def cliente_func(self):
        flag = True
        while flag:
            men = """
            ----Bienvenid@ {0}----
            1. Ver vuelos disponibles
            2. Comprar vuelos
            3. Ver mi información
            4. Regresar
            """.format(self.get_usuario_cliente())
            print(men)

            opc = int(input("Ingrese la opción: "))
            if opc == 1:
                import administrador as ad
                i = 1
                #Checar lista vacia
                if not ad.vuelos:
                    print("No hay vuelos")
                else:
                    for vuelo in ad.vuelos:
                        print("Vuelo no.: " + str(i))
                        print(str(vuelo))
                        i += 1
                continue

            elif opc == 2:
                import administrador as ad
                i = 1
                #Checar lista vacia
                if not ad.vuelos:
                    print("No hay vuelos")
                else:
                    for vuelo in ad.vuelos:
                        print("Vuelo no.: " + str(i))
                        print(str(vuelo))
                        i += 1
                
                num_compra_vuelo = int(input("Ingrese el número del vuelo: "))
                import administrador as ad
                compra_v = ad.vuelos[num_compra_vuelo - 1]
                compra_v.m_compra()

            elif opc == 3:
                print(str(self))

            elif opc == 4:
                m_cliente()
                flag = False




clientes = []
c_ejemplo = Cliente("Ariana", "Fernandez", 18, "ari", "123a")
clientes.append(c_ejemplo)





def m_cliente():

    flag = True
    while flag:
        m_cliente = """
        ------------CLIENTE------------
        1. Ingresar
        2. Registrarse
        3. Regresar
        """
        print(m_cliente)
        opc = int(input("Ingrese la opción: "))

        if opc == 1:
            clie = input("Ingrese el cliente: ")
            password = getpass.getpass("Escriba su contraseña: ")
            for c in clientes:
                if (clie == c.get_usuario_cliente()) and (password == c.get_contra_cliente()):
                    c.cliente_func()
                    
                else:
                    print("Contraseña o usuario incorrecto")
                    continue

        elif opc == 2:
            print("Registro cliente")
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            ed = int(input("Edad: "))
            usr = input("Usuario: ")
            contra = getpass.getpass("Contraseña: ")
            cliente_nuevo = Cliente(nom, ape, ed, usr, contra)
            clientes.append(cliente_nuevo)
            continue

        elif opc == 3:
            import proyecto as pr
            pr.menu_princ()
            break

        else:
            print("Ingrese una opción válida")