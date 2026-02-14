from abc import ABC, abstractmethod

##################################
#DuckTyping

class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(duck):
    print(duck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)

########################
# Anulacion de metodos

class shape(ABC):
   @abstractmethod
   def draw(self):
      "Abstract method"
      return

class circle(shape):
   def draw(self):
      super().draw()
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      super().draw()
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()

#######################################
#Sobrecarga de operadores

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

##########################################
#Sobrecarga de metodos
