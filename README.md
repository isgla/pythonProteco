# pythonProteco

Para interpretar los archivos:
    python3 "nombreArchivo.py"

BÁSICO:
    
    • Orientación a objetos:
    Todos son objetos en python.
    Type de función foo() => 
        Clase 4 (poo.py)

    Objeto: Abstracción de un objeto de la vida real en la programación.
    
    Tiene 4 pilares: abstracción, encapsulamiento, herencia, polimorfismo
        - Abstracción: Seleccionar qué características y métodos sirven para el problema a solucionar.
            • Clase: Clase que genera los objetos. Los moldes. Upper Camel Case. (Empiezan con mayúsculas) y está en singular
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
    
    Módulos:
        Tienen que estar en la misma carpeta
        
        Usar funciones de otro archivo de la siguientes maneras:
        
           • import modulo
            resultado = modulo.areaCuadrado(lado)
            
           • from modulo import areaCirculo
            print(areaCirculo(radio))
            
           • import modulo as mo
            resultado = mo.areaCuadrado(lado)
        
        ERRORES COMUNES
            Llamando el archivo igual que un módulo que ya existe
            Ejemplo: math.py
            
            import math
            print("La raiz cuadrada de 2 es: ", math.sqrt(2))
            """
            ERROR
            Traceback (most recent call last):
            File "math.py", line 1, in <module>
            import math
            File "/Users/cur01alu38/Desktop/pythonProteco/Básico/Clases/Clase5/math.py", line 3, in <module>
            print("La raiz cuadrada de 2 es: ", math.sqrt(2))
            AttributeError: module 'math' has no attribute 'sqrt'
            """
        
        NAME SPACES
            •Podemos acceder al atributo mediante name.
            
            Realizar ciertas acciones sólo si se está ejecutando el programa principal
            if __name__ == '__main__':
            
            Ejemplo (nombres.py): 
            sin: if __name__ == '__main__':
                Hola estoy dentro del modulo
                Hola soy Hannah
                
                
                con: if __name__ == '__main__':
                Hola soy Hannah
            
            •Para utilizar módulos externos en python:
            Instalar Pip:
                pip install nombre_paquete
                

        
        Todos los objetos heredan de Object y por eso todos los objetos tienen el atributo de nombre.

            
INTERMEDIO:                
    
    archivo = open("mi_archivo.txt","a")
    #La a es de append, para que empiece a escribir de donde se quedó el archivo
    
    archivo_json = open("clase.json", "r")
    #La r es de read
    
    json.dump() Convertir diccionarios a json
    json.load() Convertir json a diccionarios
    
    EJEMPLO: serialización.py
    csv: valores separados por comas
        - Writer es el método que primero convierte en lista y te permite ir agregando rows, append a la lista. 
        - Reader es el método que tiene el csv para convertir un archivo en una lista
            
    json: son como los diccionarios de los archivos
    
    • Serialización: Estándar para manejar formatos. Por ejemplo, para manejar json o csv.
    Converti,os los json o los csv en formatos que podamos manejar fácilmente. 
    En este caso en listas.
            

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        REPASO CURSO BÁSICO
            return termina una función
            break termina un ciclo
            
            self NO es una palabra reservada
            
            Las clases se escriben class Clase_Uno
            
            Dif (Función y método) El método va asociado a una clase y la función
            no necesariamente. El método tiene un objeto asociaado. Los métodos llevan self
            en el parámetro y las funciones no.
        
    
