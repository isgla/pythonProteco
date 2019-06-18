#RAISE: invoca excepciones de python
while True:
	mejorCurso = input("Ingresa cual es el mejor curso de proteco: ")

	mejorCursoConMinusculas = mejorCurso.lower()

	if mejorCursoConMinusculas != "python am sala a":
		raise ValueError
	else:
		print("Felicidades, Python AM sala A es el mejor curso")
		break