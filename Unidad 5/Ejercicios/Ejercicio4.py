import os




#Creacion de un archivo vacio


open("listadoProfesor.txt","x")
with open("listadoProfesor.txt", mode="w") as f:
    f.write("Lista de profesores\n")

open("listadoEstudiantes.txt","x")
with open("listadoEstudiantes.txt", mode="w") as f:
    f.write("Listado de estudiantes\n")

class Estudiante():
    def __init__(self, carnet, nombres, apellidos, facultad):
        self.carnet=carnet
        self.nombres= nombres
        self.apellidos=apellidos
        self.facultad=facultad
        
        with open("listadoEstudiantes.txt","a") as f:
            f.write(f"{self.carnet}, {self.nombres}, {self.apellidos}, {self.facultad}\n")
        
        

class Profesor():
    def __init__(self, carnet, nombres, apellidos, facultad):
        self.carnet=carnet
        self.nombres= nombres
        self.apellidos=apellidos
        self.facultad=facultad

        with open("listadoProfesor.txt","a") as f:
            f.write(f"{self.carnet}, {self.nombres}, {self.apellidos}, {self.facultad}\n")

condicion=True


while condicion:
    print("Ingrese el tipo de usuario que agregara")
    
    rol=int(input("\n1.Estudiante\n2.Profesor\n"))
        
    match rol:
        case 1:
            carnet=input("\nIngrese el carnet del estudiante: ")
            nombres=input("\nIngrese el nombre del estudiante: ")
            apellidos=input("\nIngrese los apellidos del estudiante: ")
            facultad=input("\nIngrese la facultad del estudiante: ")
            estudiante=Estudiante(carnet,nombres,apellidos,facultad)

        case 2:
            carnet=input("\nIngrese el carnet del profesor: ")
            nombres=input("\nIngrese el nombre del profesor: ")
            apellidos=input("\nIngrese los apellidos del profesor: ")
            facultad=input("\nIngrese la facultad del profesor: ")
            profesor=Profesor(carnet,nombres,apellidos,facultad)
            
        case _:
            print("Ingrese adecuadamente el valor")
            condicion=True
            
    
    op=input("Quiere agregar otra persona?\n").upper()
    match op:
        case "SI":
            condicion=True
        case "NO":
            condicion=False
    
    
    



