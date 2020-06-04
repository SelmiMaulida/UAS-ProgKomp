from os import system

from MenuNegara import MenuNegara #import dari MenuNegara.py untuk diproses pada main menu
from MenuPesanan import MenuPesanan


class MainMenu :
  def switch(self, kode) : 
    return getattr(self, "_menu_" + str(kode), lambda: self._default)()
  
  def _default(self) :
    print("invalid code, pick the correct code")
    
  def _menu_1(self) :
    print("\n\n")
    _iterasi = True
    menuNegara = MenuNegara()
    while _iterasi :
      system("cls")
      print("\tNegara JasTip")
      if len(menuNegara.listNegara()) != 0:
         print(menuNegara.listNegara())
      else :
        print("--Masih Kosong--")
        
      print("Pilih Menu :") 
      print("\t1. Tambah Negara\n"
            "\t2. Edit Barang Negara\n"
            "\t3. Hapus Negara")
      menu_code = int(input("Pilihan :"))
      menuNegara.switch(menu_code)
      _iterasi = True if (input("do you want to quit ?(y/n)") == "n") else False
       
  def _menu_2(self) :
    print("\n\n")
    menuNegara = MenuNegara()
    if len(menuNegara.listNegara()) == 0:
      print("Belum ada negara yang terdaftar, silahkan menambahkan negara terlebih dahulu")
    else :
      iterasi = True
      while iterasi :
        system("cls")
        print("\tJasa Titip Antar Negara")
        for index, country in enumerate(menuNegara.listNegara()):
          print(str(index + 1) + "." + country)
        index_country = int(input("Pilih negara tjuan:")) - 1
        print("\n")
        print("\t JasTip Negara" + menuNegara.listNegara()[index_country] + "\n")
        print("Menu JasTip :")
        print("\t1. Tambah Pesanan")
        print("\t2. Hapus Pesanan")
        menu_code = int(input("Pilihan : "))
        menu_pesanan = MenuPesanan(menuNegara.listNegara()[index_country])
        menu_pesanan.switch(menu_code)
        iterasi = True if (input("do you want to quit?(y/n) ") == "n") else False
                                
                                
if __name__ == "__main__":
  menu = MainMenu()
  iterasi = True
   print("------------------------------------------------------------------------------")
   print("----------SELAMAT DATANG DI PENDATAAN JASA TITIP BARANG LUAR NEGERI-----------")
   print("------------------------------------------------------------------------------")
  while iterasi :
    print("\tPilih menu")
    print("\t 1. List Negara\n"
          "\t 2. Mulai Pendataan Pesanan")
    menu_kode = int(input("pilihan menu :")
    menu.switch(menu_kode)
    iterasi = True if (input("start again ? (y/n)") == "y") else print("Terimakasih sudah menggunakan Program ini:) . Pesanan dapat dilihat pada file pesanan.csv")
                    
          
    
    
