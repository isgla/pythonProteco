#Estadísticas de pago
import vuelo
from vuelo import *

def est_pago():
    global efectivo
    global tarjeta
    global num_efectivo
    global num_tarjeta
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
            print(str(efectivo))
        elif opc == 2:
            print(str(tarjeta))
        elif opc == 3:
            total = efectivo + tarjeta
            print(str(total))
        elif opc == 4:
            print(str(num_efectivo))
        elif opc == 5:
            print(str(num_tarjeta))
        elif opc == 6:
            import administrador as ad
            ad.admin_func()
            flag = False



def est_clase():
    global num_tur
    global num_neg
    global num_prim
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
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            print(str(num_tur))
        elif opc == 2:
            print(str(num_neg))
        elif opc == 3:
            print(str(num_prim))
        elif opc == 4:
            print(str(max(num_tur, num_neg, num_prim)))
        elif opc == 5:
            import administrador as ad
            ad.admin_func()
            flag = False