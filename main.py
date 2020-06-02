from MenuNegara import MenuNegara

class MainMenu :
  def switch(self, kode) :
    return getattr(self, "_menu_" + str(kode), lambda: self._default)()
  
  def _default(self) :
    print("invalid code, pick the correct code")
    
  def _menu_1(self) :
    print("\n\n")
    _iterasi = True
    menuNegara = MenuNegara()
    
    while _iteras :
      print("\tNegara JasTip")
      if len(menuNegara.listNegara()) != 0:
         print(menuNegara.listNegara())
      else :
        print("--Masih Kosong--")
        
      print("Pilih Menu :") 
      print("\t1. Tambah Negara\n"
            "\t2. Edit Barang Negara\n"
            "\t3. Hapus Negara")
      menu_kode = int(input("Pilihan :"))
      menuNegara.switch(menu_kode)
      _iterasi = True if (input("do you want to quit ?(y/n)") == "n") else False
       
  def _menu_2(self) :
    print("\n\n")
    menuNegara = MenuNegara()
    if len(menuNegara.listNegara()) == 0:
      print("Belum ada negara yang terdaftar, silahkan menambahkan negara terlebih dahulu")
    else :
      iterasi = True
      while iterasi :
        print("\tJasa Titip Antar Negara")
        for index, country in enumerate(menuNegara.listNegara()):
          print(str(index + 1) + "." + country)
        index_country = int(input("Pilih negara tjuan:")) - 1
        print("\n")
        print("\t JasTip Negara" + menuNegara.listNegara()[index_country] + "\n")
        print("Menu JasTip :")
        print("\t1. Lihat Pesanan")
        print("\t2. Tambah Pesanan")
        print("\t3. Hapus Pesanan")
        
if __name__ == "__main__":
  menu = MainMenu()
  iterasi = True
  print("\t\t Program Start")
  while iterasi :
    print("\tPilih menu")
    print("\t 1. List Negara\n"
          "\t 2. Mulai Pendataan Pesanan")
    menu_kode = int(input("pilihan menu :")
    menu.switch(menu_kode)
    iterasi = True if (input("start again ? (y/n)") == "y") else False
                    
          
    
    
