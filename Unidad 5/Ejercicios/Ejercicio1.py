class Persona():
  def __init__ (self, nombres, apellidos, edad):
    self.nombres = nombres
    self.apellidos=apellidos
    self.edad=edad
    return

  def __str__(self):
    return(f"Nombre: {self.nombres}\nApellidos{self.apellidos}\n{self.edad}")
  

p1 = Persona("Juan","Rivas",25)
print(p1)