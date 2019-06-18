#Aquì declararemos nuestra propia excepciòn que herede de la clase Exception

class miExcepcion(Exception):
	def __init__(self, mensaje):
		self.mensaje= mensaje

def unaFuncion(parametro=None):
	if parametro == None:
		raise miExcepcion("Mi excepcion ha sido invocada")

unaFuncion()