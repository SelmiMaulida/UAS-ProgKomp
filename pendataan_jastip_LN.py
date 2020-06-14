from os import system

from MenuPesanan import MenuPesanan
from MenuNegara import MenuNegara


class MainMenu:
    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def _default(self):
        print("invalid code, pick the correct code")

    def _menu_1(self):
        print("\n\n")
        _iterasi = True
        menuNegara = MenuNegara()
        while _iterasi:
            system("cls")
            print("\tNegara JasTip")
            if len(menuNegara.listNegara()) != 0:
                for index, country in enumerate(menuNegara.listNegara()):
                    print(str(index + 1) + ". " + country)
            else:
                print("--Masih Kosong--")

            print("Pilih Menu:")
            print("\t1. Tambah Negara\n"
                  "\t2. Edit Barang Negara\n"
                  "\t3. Hapus Negara")
            menu_code = int(input("PIlihan : "))
            menuNegara.switch(menu_code)
            _iterasi = True if (input("Apakah Anda ingin keluar dari menu 1. List Negara? (y/n) ") == "n") else False

    def _menu_2(self):
        print("\n\n")
        menuNegara = MenuNegara()
        if len(menuNegara.listNegara()) == 0:
            print("Belum ada negara yg terdaftar, silahkan menambahkan negara terlebih dahulu")
        else:
            iterasi = True
            while iterasi:
                system("cls")
                print("\tJasa Titip Antar Negara")
                for index, country in enumerate(menuNegara.listNegara()):
                    print(str(index + 1) + ". " + country)
                index_country = int(input("Pilih negara tujuan : ")) - 1
                print("\n")
                print("\t JasTip Negara " + menuNegara.listNegara()[index_country] + "\n")
                menu_code = 1
                menu_pesanan = MenuPesanan(menuNegara.listNegara()[index_country])
                menu_pesanan.switch(menu_code)
                iterasi = True if (input("Apakah Anda ingin keluar dari menu 2. Mulai Pendataan Pesanan? (y/n) ") == "n") else False


if __name__ == "__main__":
    menu = MainMenu()
    iterasi = True
    print("------------------------------------------------------------------------------")
    print("----------SELAMAT DATANG DI PENDATAAN JASA TITIP BARANG LUAR NEGERI-----------")
    print("------------------------------------------------------------------------------")
    while iterasi:
        print("\tPilihan menu")
        print("\t 1. List Negara\n"
              "\t 2. Mulai Pendataan Pesanan")
        menu_kode = int(input("Pilih menu : "))
        menu.switch(menu_kode)
        iterasi = True if (input("Apakah Anda ingin kembali ke menu awal?(y/n) ") == "y") else False
                    
