from KategoriBarang import KategoriBarang


class MainMenu:
    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def _default(self):
        print("invalid code, pick the correct code")

    def _menu_1(self):
        print("\n\n")
        _iterasi = True
        menuKategori = KategoriBarang()
        while _iterasi:
            print("\tKategori Barang")
            print("Pilih :")
            print("\t1. Lihat Kategori"
                  "\t2. Tambah Kategori\n"
                  "\t3. Hapus Kategori")
            menu_kode = int(input("PIlihan : "))
            menuKategori.switch(menu_kode)
            _iterasi = True if (input("do you want to quit?(y/n) ") == "n") else False

    def _menu_2(self):
        print("menu 2")


if __name__ == "__main__":
    menu = MainMenu()
    iterasi = True
    print("\t\t Program Start")
    while iterasi:
        print("\tPilihan menu")
        print("\t 1. Edit Kategori\n"
              "\t 2. Pesanan Customer\n")
        menu_kode = int(input("Pilih menu : "))
        menu.switch(menu_kode)
        iterasi = True if(input("start again?(y/n) ") == "y") else False
