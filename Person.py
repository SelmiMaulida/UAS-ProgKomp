import os


class Person:
  _person_name = ""
  _name_kategori_file = ""
  
  def __init__(self, country, person_name):
      # create folder if not exist
      if not os.path.exist(country):
          os.makedirs(country)
      self._person_name = country
      self._name_kategori_file = os.path.join(country, person_name + ".txt")
      # create file first if not exist
      __file = open(self._name_kategori_file, "a")
      __file.close()
    
    
