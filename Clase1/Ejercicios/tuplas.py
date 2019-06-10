#Tuplas
x = ("a", "b", "c")
print(x[1])

#Transformar de tupla a lista
y = list(x)
print(type(y))

w = [1,2,4,5]
c = tuple(w)
print(type(c))
print(c)

print(c[2])
# No se puede porque las tuplas son inmutales
# c[2] = "Hola"
