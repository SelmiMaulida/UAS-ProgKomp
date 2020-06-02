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
    
    
