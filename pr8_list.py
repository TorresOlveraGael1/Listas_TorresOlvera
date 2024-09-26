#En esta practica utilizaremos las listas

print (" ")
print ("Torres Olvera Gael")
print (" ")
thislist = ["apple", "banana", "cherry"]

#Muestra el miembro 1 y comienza en Cero 0
print(thislist[1])

#Muestra el ultimo miembro de la lista
print(thislist[-1])

print(" ")

# Ejemplo de uso de listas en Python

# Crear una lista
frutas = ["manzana", "banana", "cereza"]

# Imprimir la lista
print("Lista de frutas:", frutas)

# Agregar un elemento
frutas.append("naranja")
print("Después de agregar naranja:", frutas)

# Eliminar un elemento
frutas.remove("banana")
print("Después de eliminar banana:", frutas)

# Acceder a un elemento
print("Primera fruta:", frutas[0])

# Recorrer la lista
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

# Obtener la longitud de la lista
print("Número de frutas en la lista:", len(frutas))

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Sumar todos los elementos de la lista
suma = sum(numeros)
print("Suma de los números:", suma)