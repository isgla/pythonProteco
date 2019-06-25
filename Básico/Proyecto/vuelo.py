
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
	            x = input("Ingrese el nuevo destino del vuelo: ")
	            #Es método propio de la clase, como si fuera statico en java
	            self.set_destino(x)
	            continue
	        elif opcm == 2:
	            x = input("Ingrese la nueva hora de salida del vuelo: ")
	            self.set_sal(x)
	            continue
	        elif opcm == 3:
	            x = input("Ingrese la nueva hora de llegada del vuelo: ")
	            self.set_lleg(x)
	            continue
	        elif opcm == 4:
	            x = int(input("Ingrese el nuevo costo clase Turista: "))
	            self.set_tur(x)
	            continue
	        elif opcm == 5:
	            x = int(input("Ingrese el nuevo costo clase Negocios: "))
	            self.set_neg(x)
	            continue
	        elif opcm == 6:
	            x = int(input("Ingrese el nuevo costo de primera clase:  "))
	            self.set_prim(x)
	            continue
	        elif opcm == 7:
	            x = int(input("Ingrese el nuevo número de lugares en la clase turista: "))
	            self.set_l_tur(x)
	            continue
	        elif opcm == 8:
	            x = int(input("Ingrese el nuevo número de lugares en la clase de negocios: "))
	            self.set_l_neg(x)
	            continue
	        elif opcm == 9:
	            x = int(input("Ingrese el nuevo número de lugares en primera clase: "))
	            self.set_l_prim(x)
	            continue
	        elif opcm == 10:
	            x = input("Ingrese la nueva fecha de salida: ")
	            self.set_f_sal(x)
	            continue
	        elif opcm == 11:
	            regresar_admin()
	            break


def regresar_admin():
	import administrador as ad
	ad.admin_func()



