#Proyecto
import sys

def menu_princ():
    flag = True

    while flag:
        m_principal = """
        ------------SISTEMA DE VENTAS------------
        1. Administrador
        2. Cliente
        3. Salir
        """
        print(m_principal)
        opc = int(input("Ingrese la opción: "))

        if opc == 1:
            import administrador as ad
            ad.m_admin()
            continue

        elif opc == 2:
            import cliente as cl
            cl.m_cliente()
            continue

        elif opc == 3:
            flag = False
            sys.exit()
            break

        else:
            print("\nIngrese una opcioón válida\n")
            continue


menu_princ()