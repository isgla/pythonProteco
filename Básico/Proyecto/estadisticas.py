#Estadísticas de pago
import cliente
from cliente import *

def est_pago():
    flag = True
    while flag:
        pago = """
        --------Estadísticas de Pago--------
        1. Efectivo total en cajas
        2. Saldo de pagos por tarjeta
        3. Saldo total de ventas
        4. Número de pagos realizados en efectivo
        5. Número de pagos realizados con tarjeta
        6. Regresar
        """
        print(pago)
        opc = int(input("Ingrese una opción: "))
        if opc == 1:

        elif opc == 2:

        elif opc == 3:

        elif opc == 4:

        elif opc == 5:

        elif opc == 6:
            import administrador as ad
            ad.admin_func()
            flag = False



def est_clase():
    flag = True
    while flag:
        clase = """
        --------Estadísticas de Clase--------
        1. Boletos vendidos de la clase turista
        2. Boletos vendidos de la clase Negocios
        3. Boletos vendidos de Primera Clase
        4. Clase con mayor número de ventas
        5. Regresar
        """
        print(clase)