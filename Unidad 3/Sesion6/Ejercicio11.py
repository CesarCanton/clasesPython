palabras = []

while True:
    palabra = input("Introduce una palabra (Enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)

# Convertimos la lista a tupla
palabras = tuple(palabras)

# Unpacking
primera, *_, ultima = palabras

print("Primera palabra:", primera)
print("Última palabra:", ultima)