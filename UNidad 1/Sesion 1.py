entero = 23
print(type(entero))

calculo= (((2-1/5)**2)/((3-2/9)**-1))/(((6/7*5/4-2/7*1/2)**3)/(1/2-1/3-1/4/1/5))-5*1/7
print(calculo)



#ejercicio 4
print('"\tSeria un crimen para el sabio\nno ser sabio"')

#ejercicio 5
frase1= "Quiero comer hamburguesas"
frase2="Ayer hice pupusas"

con1= frase1[:12]
con2= frase2[10:]

print(con1,con2)


#Entrada de valores por medio de la consola
print("¿Cómo te llamas?")
nombre = input() #Pedimos el nombre y asignamos a la variable nombre
print(nombre)

print("¿Cuántos años tienes?")
edad = int(input()) #Pedimos la edad y la convertimos a entero

#Ejercicio 6
datazo="Sali a correr esta mañana"
# print(datazo[:14].upper(), datazo[14:].lower())
print(datazo[:len(datazo)//2].upper() + datazo[len(datazo)//2:].lower())#Para buenas practicas ya que es algo relativo al tamaño de la cadena y no algo fijo
print(datazo.count("a"))
print(datazo.title())


#Ejercicio guiado:
dui=0
correo=""
correo=input("Ingrese su correo")
dui=input("Ingrese su dui")

arroba=correo.find("@")
correCensurado=correo[0:2]+"*"*len(correo[2:arroba-2])+correo[arroba-2:]
duiCensurado=dui[0:2]+"*"*6+"-"+dui[-1]

print(f"Gracias por ingresar, ¿Podrías confirmar que el correo {correCensurado} y el DUI {duiCensurado} corresponden a ti?")



#Ejercicio 7

oracion=input("\tIngrese la oracion a evaluar\n")
palabra=input("\tIngrese la palabra a identificar\n")


print("Oracion original: "+oracion)
oracion=oracion.title()
print("Oracion como titulo: "+oracion)

palabraSwap=palabra.swapcase()
oracion=oracion.replace(palabra,palabraSwap)
print("Oracion con la palabra modificada: "+oracion)


primeraIndex=oracion.index(" ")
ultimaIndex=oracion.rindex(" ")
print(f"{oracion[0:primeraIndex].upper()}{oracion[primeraIndex:ultimaIndex]}{oracion[ultimaIndex:].upper()} ")

#Ejercicio 8
carnet=input("Ingresa un carnet\n")
validacion= carnet[0:2].isalpha() and carnet[2:7].isdecimal()
print(f"El resultado es: {validacion} ")


