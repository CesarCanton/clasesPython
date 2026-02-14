class Persona():
    def __init__ (self, nombres, apellidos, edad):
        self.nombres=nombres
        self.apellidos=apellidos
        self.edad=edad

p1=Persona("Julio Cesar","Canton Rivas",18)
print(p1.nombres)

class Rectangle():

  def __init__(self, base = 1, height = 1, color = "blue"):
    self.base = base
    self.height = height
    self.color = color

  def perimeter(self):
    return 2 * self.base + 2 * self.height

  def area(self):
    return self.base * self.height

  def is_base_big(self, min = 5):
    if self.base > min:
      return True
    return False
  
  def __str__(self):
    return ("Base: {}\nAltura: {}".format(self.base, self.height))
  
rectangulo = Rectangle(2, 3, "red")
print("El perímetro del rectángulo es: ", rectangulo.perimeter())
print("El área del rectángulo es: ", rectangulo.area())

rectangulo = Rectangle(4, 3, "red")
print(rectangulo.is_base_big())
print(rectangulo.is_base_big(3))

rectangulo = Rectangle(10,8, "yellow")
print(rectangulo)

#Agregar 0 en fechas
class Date():
    def __init__(self, day, month,year):
        self.day=day
        self.month=month
        self.year=year

    def __str__(self):
        if self.day < 10:
            day_str = "0" + str(self.day)
        else:
            day_str = str(self.day)

        if self.month < 10:
            month_str = "0" + str(self.month)
        else:
            month_str = str(self.month)

        return "{}/{}/{}".format(day_str, month_str, self.year)
    
fecha = Date(5,7,2024)
print(fecha)
  



