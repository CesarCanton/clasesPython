class Date():

  def __init__(self, day, month,year):
    self.day=day
    self.month=month
    self.year=year

  @staticmethod
  def complete_year(year):
    year = str(year)
    return "0"*(4-len(year)) + year

  @staticmethod
  def complete_day_mont(day_month):
    day_month = str(day_month)
    return "0"*(2-len(day_month)) + day_month
  
  @staticmethod
  def complete_month(month):
    month = str(month)
    return "0"*(2-len(month)) + month

  def __str__(self):

    return "{}/{}/{}".format(self.complete_day_mont(self.day), self.complete_day_mont(self.month), self.complete_year(self.year))


fecha = Date(15,7,24)
print(fecha)