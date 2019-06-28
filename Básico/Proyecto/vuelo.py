
#Vuelos
efectivo = 0
tarjeta = 0
num_efectivo = 0
num_tarjeta = 0
num_tur = 0
num_neg = 0
num_prim = 0

class Vuelo:

    def __init__(self, dest, sal, lleg, tur, neg, prim, l_tur, l_neg, l_prim, f_sal):
        self.dest = dest
        self.sal = sal
        self.lleg = lleg
        self.tur = tur
        self.neg = neg
        self.prim = prim
        self.l_tur = l_tur
        self.l_neg = l_neg
        self.l_prim = l_prim
        self.f_sal = f_sal

    def __str__(self):
        s = """
        Destino:  {0}
        Hora de salida: {1}
        Hora de Llegada: {2}
        Costo de viaje Turista: {3}
        Costo de viaje Negocios: {4}
        Costo de viaje Primera Clase: {5}
        Lugares disponibles clase Turista: {6}
        Lugares disponibles clase Negocios: {7}
        Lugares disponibles Primera Clase: {8}
        Fecha de salida: {9}
        """.format(self.dest, self.sal, self.lleg, self.tur, self.neg, self.prim, self.l_tur, self.l_neg, self.l_prim, self.f_sal)
        return s

    def get_destino(self):
        return self.dest

    def get_sal(self):
        return self.sal

    def get_lleg(self):
        return self.lleg
    
    def get_tur(self):
        return self.tur
    
    def get_neg(self):
        return self.neg
    
    def get_prim(self):
        return self.prim

    def get_l_tur(self):
        return self.l_tur
    
    def get_l_neg(self):
        return self.l_neg

    def get_l_prim(self):
        return self.l_prim

    def get_f_sal(self):
        return self.f_sal
    
    def set_destino(self, dest):
        self.dest = dest

    def set_sal(self, sal):
        self.sal = sal

    def set_lleg(self, lleg):
        self.lleg = lleg

    def set_tur(self, tur):
        self.tur = tur

    def set_neg(self, neg):
        self.neg = neg

    def set_prim(self, prim):
        self.prim = prim

    def set_l_tur(self, l_tur):
        self.l_tur = l_tur
    
    def set_l_neg(self, l_neg):
        self.l_neg = l_neg

    def set_l_prim(self, l_prim):
        self.l_prim = l_prim

    def set_f_sal(self, f_sal):
        self.f_sal = f_sal


    def modifica_vuelo(self):
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
                print("Destino: " + self.get_destino())
                x = input("Nuevo destino: ")
                #Es método propio de la clase, como si fuera statico en java
                self.set_destino(x)
                continue
            elif opcm == 2:
                print("Hora de salida del vuelo: " + self.get_sal())
                x = input("Ingrese la nueva hora de salida del vuelo: ")
                self.set_sal(x)
                continue
            elif opcm == 3:
                print("Hora de llegada del vuelo: " + self.get_lleg())
                x = input("Ingrese la nueva hora de llegada del vuelo: ")
                self.set_lleg(x)
                continue
            elif opcm == 4:
                print("Costo clase Turista: " + str(self.get_tur()))
                x = int(input("Ingrese el nuevo costo clase Turista: "))
                self.set_tur(x)
                continue
            elif opcm == 5:
                print("Costo clase Negocios: " + str(self.get_neg()))
                x = int(input("Ingrese el nuevo costo clase Negocios: "))
                self.set_neg(x)
                continue
            elif opcm == 6:
                print("Costo de primera clase: " + str(self.get_prim()))
                x = int(input("Ingrese el nuevo costo de primera clase:  "))
                self.set_prim(x)
                continue
            elif opcm == 7:
                print("Número de lugares en la clase turista: " + str(self.get_l_tur()))
                x = int(input("Ingrese el nuevo número de lugares en la clase turista: "))
                self.set_l_tur(x)
                continue
            elif opcm == 8:
                print("Número de lugares en la clase de negocios: " + str(self.get_l_neg()))
                x = int(input("Ingrese el nuevo número de lugares en la clase de negocios: "))
                self.set_l_neg(x)
                continue
            elif opcm == 9:
                print("Número de lugares en primera claseo: " + str(self.get_l_prim()))
                x = int(input("Ingrese el nuevo número de lugares en primera clase: "))
                self.set_l_prim(x)
                continue
            elif opcm == 10:
                print("Fecha de salida: " + self.get_f_sal())
                x = input("Ingrese la nueva fecha de salida: ")
                self.set_f_sal(x)
                continue
            elif opcm == 11:
                regresar_admin()
                flag = False

    def m_compra(self):
        global num_tur
        global num_neg
        global num_prim
        global tarjeta
        global num_tarjeta
        global efectivo
        global num_efectivo

        flag = True
        while flag:
            print("-----COMPRAR BOLETOS DE VUELO-----")
            boletos = int(input("Ingrese el número de boletos: "))
            s = """
            Número de boletos: {0}
            Clase:
            \t1. Turista
            \t2. Negocios
            \t3. Primera Clase
            """.format(str(boletos))
            print(s)
            clase = int(input("Ingrese la opción de la clase que desea comprar: "))
            if clase == 1:
                num_tur += boletos
            elif clase == 2:
                num_neg += boletos
            elif clase == 3:
                num_prim += boletos
            else:
                print("Ingresa una opción válida")
                continue

            s2 = """
            Forma de pago:
            \t1. Tarjeta de credito
            \t2. Efectivo
            """
            print(s2)
            pag = int(input("Ingrese la opción de forma de pago: "))
            #Tarjeta de credito
            
            if pag == 1:
                #Costo clase Turista
                #global tarjeta
                #global num_tarjeta
                if clase == 1:
                    tarjeta = ((tarjeta + self.get_tur()) * boletos)
                    num_tarjeta += 1
                #Costo clase Negocios
                elif clase == 2:
                    tarjeta = ((tarjeta + self.get_neg())*boletos)
                    num_tarjeta += 1
                #Costo clase Primera clase
                elif clase == 3:
                    tarjeta = ((tarjeta + self.get_prim())*boletos)
                    num_tarjeta += 1
                else:
                    print("Ingresa una opción válida")
                    continue
            
            #Efectivo
            elif pag == 2:
                #Costo clase Turista
                #global efectivo
                #global num_efectivo
                if clase == 1:
                    efectivo = ((efectivo + self.get_tur()) * boletos)
                    num_efectivo += boletos
                #Costo clase Negocios
                elif clase == 2:
                    efectivo = ((efectivo + self.get_neg()) * boletos)
                    num_efectivo += boletos
                #Costo clase Primera clase
                elif clase == 3:
                    efectivo = ((efectivo + self.get_prim()) * boletos)
                    num_efectivo += boletos
                else:
                    print("Ingresa una opción válida")
                    continue
            
            else:
                print("Ingrese una opción válida")
                continue

            print("Tu compra ha sido registrada")
            flag = False
        
                


def regresar_admin():
    import administrador as ad
    ad.admin_func()



