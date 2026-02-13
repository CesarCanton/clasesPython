
def saludo():
       print("Buenos días" )
 
saludo()

def saludar():
    nombre = input("Ingresa tu nombre ")
    print(f"Buenos días, {nombre}")
  
saludar()

def saludos(nombre):
      print(f"Buenos dias {nombre}")

saludos("Tito")

#############################################################
#FUNCIONES CON PARAMETROS

def division(dividendo, divisor):
  print(dividendo/divisor)

division(10,2)
division(dividendo = 10, divisor = 2)
division(divisor = 2, dividendo = 10) #Notaremos que con esta sintaxis no importa el orden

#Devolviendo varios valores
def remain_division(dividendo, divisor):
  q = dividendo // divisor
  r = dividendo % divisor
  return q, r

print(remain_division(10,2)) #imprime la tupla
q, r = remain_division(10,2)
print(f"El resultado es {q} y restan {r}")

#####################################################
#NUMERO INDEFINIDO DE PARAMETROS

def varios_args(*numeros):#Un * significa que sera almacenado en una tupla.
    print(numeros)

varios_args(10, 20, 30, 40)

def varios_args(**numeros):#En este caso significa que sera almacenado en un diccionario.
    print(numeros)

varios_args(n1 =10, n2 =20, n3= 30, n5 =40)

def buenos_dias(nombre = "Usuario"):#Parametro que tiene un valor por defecto
  print(f"Buenos días {nombre}")

buenos_dias()
buenos_dias("Tito")

def arithmetic_operations(x, y):
  sum = x + y
  diff = x - y
  prod = x * y
  div = x / y
  return {"sum": sum,
          "difference": diff,
          "product": prod,
          "division": div}

diff = 15
print(arithmetic_operations(4,5)) #diff aquí tiene otro valor
print(diff)

########################################
#Referencia vs copia


def double_value(n):
    n = n*2
    return n

num = 5
print(double_value(num))
print(num)

###############################3
#Referencia

def double_values(ns):
  for i, n in enumerate(ns):
    ns[i] *= 2

  return ns

nums = [5, 6, 7, 8, 9]
print(double_values(nums))
print(nums)


#Ejercicio 2
def contar_par_impar(palabras):
    resultado = {
        "pares": 0,
        "impares": 0
    }
 
    for palabra in palabras:
        if len(palabra) % 2 == 0:
            resultado["pares"] += 1
        else:
            resultado["impares"] += 1
 
    return resultado
lista = ["hola", "me", "gusta", "python"]
 
resultado = contar_par_impar(lista)
print(resultado)

###################################################3
#Recursividad


#Funciones lambda

#Ejercicios por hacer 3,5,7,8,9
 
