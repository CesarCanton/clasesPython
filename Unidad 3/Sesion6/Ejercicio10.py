# Ingreso de la primera lista
arr1 = []
print("Ingrese elementos para la Lista 1 (escriba 'fin' para terminar):")

while True:
    elemento = input("Elemento: ")
    if elemento.lower() == "fin":
        break
    if elemento not in arr1:
        arr1.append(elemento)
    else:
        print("El elemento ya existe en la Lista 1")

# Ingreso de la segunda lista
arr2 = []
print("\nIngrese elementos para la Lista 2 (escriba 'fin' para terminar):")

while True:
    elemento = input("Elemento:  ")
    if elemento.lower() == "fin":
        break
    if elemento not in arr2:
        arr2.append(elemento)
    else:
        print("El elemento ya existe en la Lista 2")

# Conversión a conjuntos
set1 = set(arr1)
set2 = set(arr2)
print("\nLista 1:", arr1)
print("Lista 2:", arr2)

# Operaciones
comunes = set1 & set2
solo_una = set1 ^ set2
restantes_arr1 = set1 - set2
restantes_arr2 = set2 - set1



# Resultados
print("\nResultados:")
print("Elementos presentes en ambas listas:", len(comunes))
print("Elementos presentes en una sola lista:", len(solo_una))
print("Elementos restantes en arr1:", len(restantes_arr1))
print("Elementos restantes en arr2:", len(restantes_arr2))
