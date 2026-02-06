#Crear dos diccionarios con tantas claves y valores que desee el usuario y al final los comnbine en un solo diccionario de resultados
# Las claves de los diccionarios dados pueden superponerse. En ese caso, debe combinar todos los valores de origen en una lista. Los valores duplicados deben conservarse.

diccionario1 = {}
diccionario2 = {}
n = int(input("Ingrese el número de claves para el primer diccionario: "))
for i in range(n):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario1[clave] = valor
m = int(input("Ingrese el número de claves para el segundo diccionario: "))
for i in range(m):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario2[clave] = valor
resultado = {}

for clave in diccionario1:
    if clave in diccionario2:
        resultado[clave] = [diccionario1[clave], diccionario2[clave]]
    else:
        resultado[clave] = diccionario1[clave]
for clave in diccionario2:
    if clave not in resultado:
        resultado[clave] = diccionario2[clave]
print("Diccionario combinado:", resultado)
