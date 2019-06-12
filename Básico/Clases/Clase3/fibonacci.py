#Serie de Fibonacci
#1 1 2 3 5 8 

#i es la posición comenzando desde el 1
def fibonacci(i):
	if i==1 or i==2:
		return 1
	else:
		return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(4))

"""
fibonacci(4) = 3

finacci(3) + fibonacci(2)
finacci(2) + finacci(1) + fibonacci(2)
1 + 1 + 1

"""