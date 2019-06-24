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

