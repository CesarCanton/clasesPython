import cmath

print("Hola mundo")

salario= float(input("Ingrese su salario\n"))

if salario>=5000:
    salario=+ salario*0.05
else:
    salario=+salario*0.15

print(f"Salario final es de:{salario} ")

#match case con numeros
puntuacion = int(input("Ingresa tu puntuación: "))

match puntuacion:
  case 100:
    print("Felicidades")
  case n if n>=80:
    print("Excelente")
  case n if n>=70:
    print("Muy bien")
  case n if n>=60:
    print("Aprobado")
  case _:
    print("Reprobado")

#Match case con texto
puntuacion = input("Ingresa tu puntuación: ").upper()

match puntuacion:
  case "A":
    print("Felicidades")
  case "B":
    print("Excelente")
  case "C":
    print("Muy bien")
  case "D":
    print("Aprobado")
  case _:
    print("Reprobado")


#Anidacion o If anidados
salario2 = float(input("Ingresa tu salario: "))
edad2 = int(input("Ingresa tu edad: "))

if salario2 < 1000:
  print("Tienes un descuento especial para comprar comida")
  if edad2 <= 25:
    print("Tienes un descuento especial para comprar ropa")
else:
  print("No tienes descuentos especiales")


#Ejercicio 5
n=0
while n<=100:
    
    if n%3==0 or n%13==0:
        print(f"{n}")  
    n+=1

#Ejercicio 2

print("Determinacion de tipo de triangulo segun sus lados")
x=float(input("Ingrese el valor del lado x: "))
y=float(input("Ingrese el valor del lado y: "))
z=float(input("Ingrese el valor del lado z: "))

#Considerando desigualdades
if x+y>z and x+z>y and y+z>x:
    if x==y and y==z:
        print("El triangulo es equilatero")
    elif x==y or y==z or x==z:
        print("El triangulo es isoceles")
    else:
        print("El triangulo es escaleno")
else:
    print("Los valores ingresados no forman un triangulo")
    
#Ejercicio 4
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c

x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
x2 = (-b - cmath.sqrt(discriminante)) / (2*a)

if discriminante.real >= 0:
    if discriminante > 0:
        print("Hay dos soluciones reales:")
    else:
        print("Hay una solución real doble:")
else:
    print("No hay soluciones reales, las soluciones son complejas:")

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")

#Ejercicio 7

print("Conteo y eliminacion de la letra")
oracion=input("Ingrese una oracion:\n")
letra=input("Ingrese la letra que quiere contar:\n")
oracionSinLetra=""

conteo=0
for i in range(len(oracion)):
  if oracion[i]==letra:
    conteo+=1
  else:
    oracionSinLetra+=oracion[i]
print(f"La letra {letra} se repite {conteo} veces")
print(f"La oracion sin la letra '{letra}' es: {oracionSinLetra}")

#Ejercicio 8
print("Numeros narcicistas")
entrada=input("Ingrese el numero narcicista\n")
# entrada="153"
numero=int(entrada)
print(f"{numero}")
sumatoria=0

for j in range(len(entrada)):
  sumatoria+=int(entrada[j])**len(entrada)
  print(f"Sumatoria {j}: {sumatoria}")

if numero == sumatoria:
  print(f"El numero ingresado es narcicista ya que el resultado es: {sumatoria}")
else:
  print(f"El numero ingresado no es narcicista ya que el resultado es: {sumatoria}")