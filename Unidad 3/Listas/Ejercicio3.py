columnas = int(input("Escriba la cantidad de columnas de la tabla\n"))
filas = int(input("Escriba la cantidad de filas de la tabla\n"))

# METODO CON PRELOCACION: crear todas las filas y columnas vacías
tabla = [[0 for _ in range(columnas)] for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        tabla[i][j] = int(input(f"Ingrese el numero de la fila {i+1} columna {j+1}: "))


print("\nTabla capturada:")
for row in tabla:
    print(row)   
     
sumatoria=[0 for _ in range(columnas)]

print((f"tamaño de la tabla {len(tabla)} X {len(tabla[0])}"))
  
for i in range(len(tabla[0])):
    for j in range(len(tabla)):
        sumatoria[i]+=tabla[j][i]

for i in range(len(sumatoria)):
    if sumatoria[i]>50:
        print(f"La columna {i+1} ha excedido la cantidad\n")
    else:
        print(f"{sumatoria[i]}")









#SE PUEDE HACER DE ESTA MANERA EN DONDE NO EXISTEN LA SUBLISTA
#######################################################################################
# tabla = []
# for i in range(filas):
#     print(f"FILA {i}")
#     fila = []
#     for j in range(columnas):
#         valor = int(input(f"\nIngrese el numero de la fila {i} columna {j}: "))
#         fila.append(valor)
#     tabla.append(fila)
########################################################################################
# for row in tabla:
#     print(row)