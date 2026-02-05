# Heterogéneas: Pueden almancenar datos de diferentes tipos
# Mutables: Los elementos y el tamaño de la lista pueden ser modificados

mylist = ["Juan", 12e-2, False, 560 ]
type(mylist)

print(mylist[0])
print(mylist[-1]) #El último elemento

listaPrueba=[]
type(listaPrueba)

mylist = ["Clara",2,3,False,"Victoria","Celeste",8.5]

print(mylist[1:4]) #Selecciona del segundo al cuarto elemento
print(mylist[:3]) #Selecciona del principio al tercer elemento
print(mylist[4:]) #Selecciona del quinto elemento al final

print("\n", mylist[:]) #Selecciona todo
print(mylist[-2:]) #Selecciona los ultimos dos

mylist =  ["Juan", 12e-2, False, 560 ]
for i in mylist:
  print(i)
  
# Para cambiar un elemento 
mylist = ["Clara",2,3,False,"Victoria","Celeste",8.5]
mylist[0] = "María" #Cambia el valor del primer elemento
print(mylist)

#Agregar un valor al final
mylist.append("Nuevo valor")
print(mylist)

#Agregar un elemento dentro de la lista
mylist.insert(1, "Segundo elemento de la lista")
print(mylist)

print(mylist.pop()) #Elimina el último elemento y lo devuelve
print(mylist) #La lista con el elemento eliminado

mylist = ["Clara",2,3,False,"Victoria","Celeste",8.5]
mylist.remove("Celeste") #Elimina la primera aparición del valor
print(mylist)

del(mylist[0]) #Elimina el primer elemento
print(mylist)

# Vaciar lista
print(mylist)
mylist.clear()
print(mylist) #lista vacía

#Concatenacion de listas
l1 = ["Lista 1", 24]
l2 = [False, "Esto es parte de la segunda lista"]

print(l1 + l2) #Imprimimo la concatenación

print(list("Hola"))#Crea una lista con los caracteres
print(list(range(1,10)))#Crea una lista con los numeros del 1 al 9

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Recorriendo la matriz
for i in range(len(matrix[0])):
  for j in range(len(matrix)):
      print(j)
      print(matrix[i][j], end="")
    

#Diccionarios.

mydicctionary = dict()

mydicctionary["nombre"] = input("Ingresar nombre: ")
mydicctionary["edad"] =int( input("Ingrese la edad: "))
mydicctionary["numero"] = list(range(1,11))

print(mydicctionary)
print(len(mydicctionary))

diccionario = {"pos": 0, "neg": 0}
 
 
 
#Ejercicio 6
num = int(input("Ingrese un número: "))
 
while num != 0:
    if num > 0:
        diccionario["pos"] += 1
    else:
        diccionario["neg"] += 1
 
    num = int(input("Ingrese un número: "))
 
print(diccionario)

#Conjuntos
myset = {1,2,3,4,5}
print(myset)

myset = {1,2,3,3,3,3,4,5,5,5,5} #Si intentaramos almacenar multiples veces un mismo valor, solo se guardaría una vez
print(myset)

myset_from_list = set([1,2,3])
myset_from_string = set("hola")
myset_from_tuple = set((1,2,3))

print(myset_from_list)
print(myset_from_string)
print(myset_from_tuple)

#Operador de pertenencia "in"
palabra = input("Ingresa una palabra: ").lower()
vocales = {'a','e','i','o','u'}

for letra in palabra:
  if not (letra in vocales):
    print(letra, end ="")

#Modificacion
old_set = {"a","b","c"}
new_data = {"x","y","z"}

old_set.update(new_data)
print(old_set)

#Creacion de un conjunto

myset = set() #creando un set vacio
myset.add("hola")
myset.add("otro")
myset

#Eliminacion
myset = {"a",  "e", "i", "o", "u"}
myset.remove("a")
myset.discard("o")

print("a" in myset)
print("o" in myset)
print(myset)

#Tuplas

mytuple = ("Tito", 15, ["Matemática", "Historia"])
print(mytuple)

mytuple = "Juan", 20, ["Física", "Programación"] ##Una vez declarado no podremos modificarlo
print(mytuple)

mytuple = tuple(["Tito", 19, "estudiante", False])
print(mytuple)

mysingletuple = ("Tito",) #correcto
print(type(mysingletuple))

mysingletuple = ("Tito") #incorrecto
print(type(mysingletuple))


#Elementos de las tuplas
mytuple = 1, "2", 3, "4", 5, "6", 7
print(mytuple[0])
print(mytuple[-1])
print(mytuple[2:5])


#Para saber el tamaño de las tuplas 
mytuple = 1, 2, [3,4,5] , {6: "6", 7: "7"}
print(len(mytuple))

#Para modificar una tupla transformandola en una lista
mytuple = "Manza", "Pera", "Uvas"
tupleToList = list(mytuple)
tupleToList[0] = "Guayaba"
mytuple = tuple(tupleToList)
print(mytuple)

compras = "Jabon", "Cereal", "Pan", "Frutas"

item1, item2, item3, item4 = compras #puede hacerse con o sin paréntesis
(item5, item6, item7, item8) = compras

print(item1, item2, item3, item4)
print(item5, item6, item7, item8)

mytuple = 1,2,3,4,5,6,7,8,9,10,11,12,13,14
num1, num2, num3, *resto = mytuple #Desempaquetamos al final
print(num1, num2, num3, resto)

num1, *resto, num2, num3 = mytuple #Desempaquetamos hasta tantos alcance
print(num1, resto, num2, num3)

###########Iterando dos tuplas
mytuple = ("Manzana", 3.50), ("Pera", 1.00), ("Uva", 4.50)

for item, precio in mytuple:
  print(f"{item} vale {precio}")

