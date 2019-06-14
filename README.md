# pythonProteco

Para interpretar los archivos:
    python3 "nombreArchivo.py"

    BÁSICO
    
    • Orientación a objetos:
    Todos son objetos en python.
    Type de función foo() => 
        Clase 4 (poo.py)

    Objeto: Abstracción de un objeto de la vida real en la programación
    
    Tiene 4 pilares: abstracción, encapsulamiento, herencia, polimorfismo
        - Abstracción: Seleccionar qué características y métodos sirven para el problema a solucionar.
            • Clase: Clase que genra los objetos. Los moldes. Upper Camel Case. (Empiezan con mayúsculas) y está en singular
            • El constructor se escribe así:
                def __init__(self):
                
                self se pone en todas las funciones utilizados en POO. Indica que si usamos esta
                función vamos a usarla con un objeto.
                
                Self es la referencia del objeto
                
                self.nombre = nombre
                Hace referencia al parámetro = lo renombras
                La característica del objeto = nombre que le pasamos como parámetro
                
                Instancia de las clases:
                #Instancia de la clase Persona
                aldo = Persona("Aldo","Vázquez",21)
            
            • Los decoradores son los equivalentes a métodos estáticos: Métodos que sirven para toda la clase
                
        - Encapsulamiento: Permite proteger los datos. En python hay público y privado.
            •Todos los métodos mágicos son métodos privados.
            •self.__telefono Indica que es privado (__)
            •Los getters y setters te permite acceder o poner un valor privado. 
                Sirven para tener una capa extra de seguridad
        - Herencia:
            •Si una clase hereda de otra se escribe como: (Vegetariano hereda de persona)
                class Vegetariano(Persona):
                
            •Herencia de varias clases; Persona -> Vegetariano -> Vegano
                Se pueden sobreescribir los métodos
                
            •super representa una instancia de la clase padre
            Para sobreescribir el constructor de la clase hija- le agrego dos atributos y hago super
            para con los atributos de las clase padre y después pongo sus dos nuevos parámetros.
            
            
        - Polimorfismo:
            •(Varias formas) Cuando una clase hija hereda de una padre y después hereda a otra,
            tiene varios comportamientos (como padre e hijo)
            •Multiherencia: Cuando quieres que herede de varias padres.
            PROBLEMAS: Problema de diamante; así que no es recomendable usarla.
                class ComeAire(CrudiVegano, Fantasma):
                
            

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        REPASO
            return termina una función
            break termina un ciclo
            
            self NO es una palabra reservada
            
            Las clases se escriben class Clase_Uno
            
            Dif (Función y método) El método va asociado a una clase y la función
            no necesariamente. El método tiene un objeto asociaado. Los métodos llevan self
            en el parámetro y las funciones no.
        
    
