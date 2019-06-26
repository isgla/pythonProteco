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
    
    •Expresiones regulares
        Secuencia especial de caracteres que ayuda aencontrar otras cadenas o 
        conjuntos de cadenas utilizando una sintáxis mantenida en un patrón.
    
    match() Busca al inicio de la cadena
    search() Busca en toda la cadena
    
    •Redes:
        Cada computadora tiene una dirección IP.
        
        Puertos: Salida-Entrada 
            1 ~ 2^(32)
            Sockets comunes: 5000, 3000, 8000, 5555, 3333, 8888
    
    •BASE DE DATOS
        -Entidades: Cualquier objeto o conceptosobre el que se recoge información.
        Se representan con rectángulos.
            Fuertes: No dependen de otra para exisitir.
            Débiles: Dependen de otra para existir.
                Personas pueden existir sin brazos pero los brazos no sin la persona.
        -Atributos: Características de las entidades.
        -Relación: Correspondencia entre dos o más entidades.
        Se representa con rombos
            Cardinalidad: Número de correspondencias.
                1:N
            Reglas de negocio.
            MODELOS:
                -Peter Chen: 
                    •Refleja tan sólo la existencia de los datos.
                    •Independiente del sistema Gestor de Base de Datos.
                    -Relacional: Sirve para cualquier tipo de SGBD
                    -Modelo físico: Tablas
                    - Funciones básicas de una base de datos: CRUD Create, read, update, delete
                
        •CONCURRENCIA
            -Thread (Hilo): Ruta de ejecución independiente.
        
            -Proceso: Programa en ejecución, puede incluir múltiples threads.
        
            -Tarea: Se refiere al concepto abstracto de una actividad que necesita ser ejecutada.
            
            -Paralelismo: Ejecución de una tarea al mismo tiempo (HW). Ejecución de tareas al mismo tiempo. (HW -> Hardware es lo que requiere).
        
            -Concurrencia: Múltiples flujos de control que pueden o no ejecutarse paralelamente. Es la capacidad que tiene una tarea (o más tareas) de poderse ejecutar de manera independiente de otra tarea
            
            •Socket: Es como una computadora, hay un servidor-clientes, recibe información.
            Se compartan como hilos.
 
 AVANZADO
            
            Numpy (Clase1: numpyModulo.py):
            
            vector = np.array([2,3,4,5])
            vector2 = np.array([6,7,8,9])
                
            •Permite hacer suma de vectores.
                suma = vector + vector2
                
            •Permite hacer producto punto
                productoPunto = vector.dot(vector2)
            
            •Creando matrices con el método array
                m2 = np.array([[1],[2],[3]])
                
                    Matriz 3x1
                    [[1]
                    [2]
                    [3]]
            
            
            •Multiplicación de matrices usando array y método dot
            
                    m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
                    m2 = np.array([[1],[2],[3]])
                    
                    m1.dot(m2)
            
            •Array con un rango de valores
                arr1 = np.arange(10)
                #Imprime [0 1 2 3 4 5 6 7 8 9]
                
                arr2 = np.arange(2,20)
                #Imprime [ 2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
                
                arr3 = np.arange(4,20,3)
                #Imprime [ 4  7 10 13 16 19]
                
            •Arreglos especiales
                unos = np.ones((2,2)) #Le pasas como parámetro una tupla para definir la dimensión
                    #Imprime: 
                    [[1. 1.]
                    [1. 1.]]
                    
                ceros = np.zeros((3,5))
                    #Imprime: 
                    [[0. 0. 0. 0. 0.]
                    [0. 0. 0. 0. 0.]
                    [0. 0. 0. 0. 0.]]
                
                #Del 0 al 3 en 9 puntos
                lins = np.linspace(0,3,9)
                    #Imprime 
                    [0.    0.375 0.75  1.125 1.5   1.875 2.25  2.625 3.   ]
                    
                #Imprimiría cuartos
                    lins = np.linspace(0,1,6)
                    print(lins)
                    #[0.  0.2 0.4 0.6 0.8 1. ]
            •Matriz diagonal
                diagonal = np.eye(3)
                print(diagonal)
                    #Imprime:
                    [[1. 0. 0.]
                    [0. 1. 0.]
                    [0. 0. 1.]]
            
            •Matriz transpuesta, Hermitiana (Conjugado de los complejos), Inversa
            
            
            Sympy (Clase1: sympyModulo.py) Cálculo simbólico:
            
                #Forzar tipos de datos (Casteos)
                
                Números racionales, infinitos (zoo = complex infinity))
        
        
        Machine Learning: Es una herramiento de A.I. 
        Tiene limitantes porque no aprende de errores.
        
        Se basa en aprender para tomar decisiones.
        Hay tres tipos:
        •Aprendizaje supervisado: Vamos a tener ciertas características asociadas con una etiqueta. Ejemplo: Una flor tiene varias características, y dependendo de esas, podemos asignarle una etiqueta.
            -Árboles de decicón: Estructura de datos para establecer un conjunto de reglas de decisión. Sklearn
            
                Conjunto de entrenamiento
                
                Conjunto de prueba
        •Aprendizaje no supervisado
                
        •Aprendizaje refuerzo

            
            -Redes neuronales.
            Perceptrón: neurona artificial (Entrada y peso) 
                Los pesos se asignan solos
                Bias: Umbral que permite tener un resultado siempre
                Tendríamos una función de activación; hay varias, entre ellas Sigmoide(hay variaciones de 0-1)
                
                Cálculo de errores:
                
                δ = D -Y
                D -> Valor deseado
                Y -> Valor obtenido
                w-> Peso
                
                Δ1 = n * δ * x1
                Δ2 = n * δ * x2
                w1 = w1 + Δ1
                w2 = w2 + Δ2
                b = b-n*δ (Recta)
                
            
            Modelo matemático
            
            TensorFlow
            big head (air b&b)
            
            IBM: computacion cuantica; Watson
            
            
            PASOS PARA CREAR UN BOT EN TELEGRAM
                Cd Desktop 
                pip3 install pyTelegramBotAPI —user
                
                Bot father (buscar)
                /newbot 
                Name: hannahgl 
                Bot: hannahgl_bot
                Dar click en el link
                Start
                
                Copiar el token 
                Link rojo 
                
                Haces el programa en Python 
                Lo corres 
                Desde la web escríbele un mensaje a tu bot 
                Y ve tu terminal
                
                (Cambios en el programa)
                Escribes otro mensaje en el chat con tu bot 
                Y te imprimes el id y el mensaje
                
                Puedes mandarte un mensaje pidiendo el nombre del archivo y te lo manda si los nombres coinciden.
        
        
        http: hyper text transfer protocol
       
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        REPASO CURSO BÁSICO
            return termina una función
            break termina un ciclo
            
            self NO es una palabra reservada
            
            Las clases se escriben class Clase_Uno
            
            Dif (Función y método) El método va asociado a una clase y la función
            no necesariamente. El método tiene un objeto asociaado. Los métodos llevan self
            en el parámetro y las funciones no.
        
        
        REPASO CURSO INTERMEDIO
            En finally se encuentra el código que debe ejecutarse siempre, pase lo que pase.
            
            TypeError es cuando tratas de sumar una cadena 
            
            raise: forzar a que una excepción se lance
            
            Las excepciones ejecutan código en caso de haber caído ya en un error
            
            Módulo os nos otorga funcionalidad para conectar el sistema operativo
            
            Módulo sys: Conocer información de nuestro ejecutable
            
            Leer el zen de python es con this
            
            sys.path Regresa la lista de carpetas donde están los módulos importables
            
            Para crear una carpeta: os.mkdir("nombre")
            
            Codename del sistema operativo de mac: Darwin
            
            Modos de apertura de archivos: r,w,a
            
            csv.writerow()
            
            KeyboardInterruption error es con Crtl+C
            
            os.system
        
        
        
        
        
    
