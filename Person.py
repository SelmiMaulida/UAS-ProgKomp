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
    
    
  def _menu_1(self):
      name_person = input("Masukkan nama pemesan : ")
      
      _file = open("person.txt", "a")
      _file.write(name_person)
      _file.close()
      
      produk_iterasi = True
      while produk_iterasi:
          menuBarang = BarangJual(menuNegara.listNegara()[index_country])
          menuPerson = Person(menuNegara.listNegara()[index_country], name_person)
          print("Pilih produk : ")
          for index, product in enumerate(menuBarang.listBarang()):
              print(str(index + 1) + ". " + product)
          index_product = int(input("Pilihan : "))
          jumlah_barang = int(input("Jumlah barang : "))
          menuPerson.add_product(menuBarang.listBarang()[index_country], jumlah_barang)
          print("Berhasil menambahkan data!")
          iterasi = True if input("ingin menambahkan barang lagi?(y/n)") == "y" else False
          
   def add_product(self, product, amount):
       if product not in self.get_list_product():
            __file = open(self._name_kategori_file, "a")
            __file.writer(product + "," amount)
            __file.close()
       else:
            print("Produk telah ditambahkan")
        
            
       
