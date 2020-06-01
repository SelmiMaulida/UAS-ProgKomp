class KategoriBarang:
    _name_kategori_file = "kategori.txt"

    def __init__(self):
        # create file first if not exist
        __file = open(self._name_kategori_file, "a")
        __file.close()

    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def _menu_1(self):
        print("\n")
        print("Daftar kategori : ")
        kategori = self._get_kategori()
        if len(kategori)!=0:
            for text in kategori:
                print(text)
        else:
            print("Kategori kosong")

    def _menu_2(self):
        print("\n")
        name = input("Masukkan nama kategori : ")
        if self._add_kategori(name):
            __file = open(self._name_kategori_file, "r")
            print("Kategori telah di tambahkan :")
            print(__file.readline())
            print("\n")
            __file.close()
        else:
            print("Kategori sudah ada")

    def _menu_3(self):
        print("\n")
        print("comming soon")

    def _default(self):
        print("invalid code, pick again")

    def _get_kategori(self):
        __file = open(self._name_kategori_file, "r")
        return __file.readlines()

    def _add_kategori(self, kategori=""):
        if len(self._get_kategori()) == 0 or (kategori+"\n") not in self._get_kategori():
            __file = open(self._name_kategori_file, "a")
            __file.write(kategori+"\n")
            __file.close()
            return True
        else:
            return False
