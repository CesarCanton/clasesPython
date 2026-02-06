puntos = []

n = int(input("Ingrese el número de puntos 3D: "))

for i in range(n):
    print(f"\nPunto {i + 1}")
    x = float(input("Ingrese x: "))
    y = float(input("Ingrese y: "))
    z = float(input("Ingrese z: "))

    if x > 0 and y > 0 and z > 0:
        octante = 1
    elif x < 0 and y > 0 and z > 0:
        octante = 2
    elif x < 0 and y < 0 and z > 0:
        octante = 3
    elif x > 0 and y < 0 and z > 0:
        octante = 4
    elif x > 0 and y > 0 and z < 0:
        octante = 5
    elif x < 0 and y > 0 and z < 0:
        octante = 6
    elif x < 0 and y < 0 and z < 0:
        octante = 7
    elif x > 0 and y < 0 and z < 0:
        octante = 8
    else:
        octante = 0  # Punto en algún eje o plano

    punto = (x, y, z, octante)
    puntos.append(punto)

for punto in puntos:
    x, y, z, octante = punto
    print(f"El punto ({x}, {y}, {z}) pertenece al octante {octante}.")
