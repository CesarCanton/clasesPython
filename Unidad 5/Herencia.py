# class Adult():

#   is_adult = True

#   def __init__(self, name, surname, age):
#     self.name = name
#     self.surname = surname
#     self.age = age

#   @property
#   def complete_name(self):
#     return "{} {}".format(self.name, self.surname)

#   @complete_name.setter
#   def complete_name(self, name_surname):
#     name, surname = name_surname.split(" ")
#     self.name = name
#     self.surname = surname


# class Children():

#   is_adult = False

#   def __init__(self, name, surname, age):
#     self.name = name
#     self.surname = surname
#     self.age = age

#   @property
#   def complete_name(self):
#     return "{} {}".format(self.name, self.surname)

#   @complete_name.setter
#   def complete_name(self, name_surname):
#     name, surname = name_surname.split(" ")
#     self.name = name
#     self.surname = surname

class Person():

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

  @property
  def complete_name(self):
    return "{} {}".format(self.name, self.surname)

  @complete_name.setter
  def complete_name(self, name_surname):
    name, surname = name_surname.split(" ")
    self.name = name
    self.surname = surname

@property
def introduction(self):
    print("Hola, mi nombre es {}".format(self.complete_name))

class Adult(Person):
  is_adult = True

class Children(Person):
  is_adult = False

child = Children("Juan", "Sánchez", 6)
child.name


#Super, heredando metodos

class TalkativePerson(Person):

    @property
    def introduction(self):
        super().introduction #reciclamos el metodo del super
        print("Un placer conocerte!")


