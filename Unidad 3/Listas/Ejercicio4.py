filas=int(input("Ingrese la canitdad de filas que desea ver en la matriz: "))
columnas=int(input("Ingrese la canitdad de columnas que desea ver en la matriz: "))

tabla = [[0 for _ in range(columnas)] for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        if i==j:
            tabla[i][j]=1
        else:
            tabla[i][j]=0

for identidad in tabla:
    print(identidad)