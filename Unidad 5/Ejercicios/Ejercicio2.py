import os

listaEstudiantes=[]

class Estudiante():
    def __init__(self, carnet, nombre, apellidos,carrera):
        self.carnet=carnet
        self.nombre=nombre
        self.apellidos=apellidos
        self.carrera=carrera
    
    def __str__(self):
        return(f"\nCarnet: {self.carnet}\nNombre: {self.nombre}\nApellidos:{self.apellidos}\nCarrera:{self.carrera}")


with open("estudiantes_practica.txt","r")as archivo:
    for linea in archivo:
        datos=linea.split(",")

        estudiante=Estudiante(datos[0],datos[1],datos[2],datos[3])
        listaEstudiantes.append(estudiante)

for alumno in listaEstudiantes:
    print(f"\n{alumno}")