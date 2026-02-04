num=0

try:
    num=int(input("Ingrese un numero: \n"))
except:
    print("Solo se pueden ingresar numeros")
else:
    print(f"Se ha ingresado correctamente el numero {num}")
finally:
    print("Fin de la ejecucion")