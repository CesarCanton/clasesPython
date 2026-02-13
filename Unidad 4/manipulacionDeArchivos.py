import os
import csv


#Leyendo un archivo
with open("Ejemplo.txt")as f:
    print(f.read(7))
    print(f.readline())

#Creacion de un archivo
with open("NuevorArchivo.txt", mode="w") as f:
    f.write("Amo Python Foundations")


#Leyendo el archivo por medio de un ciclo for

with open("Ejemplo.txt") as f:
    for line in f:
        print(line + "Esto es agregado")


#Creacion de un archivo vacio
f=open("ArchivoVacio.txt","x")
f.close

#Modificando archivo de texto
with open("ArchivoVacio.txt","a") as f:
    f.write("Me gustan los archivos creados")

#Eliminando un archivo
if os.path.exists("ArchivoVacio"):
    os.remove("ArchivoVacio.txt")




#################################################################
#Manipulacion de CSV
#Lectura de archivos
with open("csv_example.csv","r")as f:
    print(f.read())


with open("csv_example.csv","r")as f:
    reader=csv.reader(f)
    print(reader)
    for row in reader:
        print(row)


with open("csv_delimiter_example.csv","r")as f:
    reader=csv.reader(f, delimiter="|")
    print(reader)
    for row in reader:
        print(row)


#Leer el archivo eliminando los espacios entre cada atributo
with open("csv_spaces_example.csv", "r") as f:
    reader= csv.reader(f,skipinitialspace=True)
    for row in reader:
        print(row)


with open("csv_quotation_example.csv", "r") as f:
    reader= csv.reader(f,csv.QUOTE_NONE)
    for row in reader:
        print(row)

#Con dialecto
csv.register_dialect("my_dialect",
                     delimiter="|",
                     skipinitialspace=True,
                     quoting=csv.QUOTE_NONNUMERIC)

# with open("csv_dialect_example,csv","r") as f:


#Abriendolo en forma de diccionario
with open("csv_spaces_example.csv", "r") as f:
    reader= csv.DictReader(f)
    for row in reader:
        print(row)


#Crear un csv

data = [["id", "Name", "City", "Age"],
        [1234, "Arturo", "Madrid", 22],
        [2345, "Beatriz", "Barcelona", 25],
        [3456, "Carlos", "Sevilla", 18],
        [4567, "Dolores", "Cuenca", 34]]

with open("csv_write.csv", "w") as f:
  writer = csv.writer(f)
  for row in data:
    writer.writerow(row)


data = [{"id": 1234, "Name": "Arturo", "City": "Madrid", "Age": 22},
        {"id": 2345, "Name": "Beatriz", "City": "Barcelona", "Age": 25},
        {"id": 3456, "Name": "Carlos", "City": "Sevilla", "Age": 18},
        {"id": 4567, "Name": "Dolores", "City": "Cuenca", "Age": 34}]

# La cabecera es la lista de las keys de cualquiera de las entradas de data
header = list(data[0].keys())
print(header)

with open("csv_write_dict.csv", "w") as f:
  writer = csv.DictWriter(f, fieldnames = header)

  writer.writeheader()
  for d in data:
    writer.writerow(d)




