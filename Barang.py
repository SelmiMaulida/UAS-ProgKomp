import os
import shutil


class BarangJual:
    _name_kategori_file = ""
    _country_name = ""

    def __init__(self, country):
        # create folder if not exist
        if not os.path.exists(country):
            os.makedirs(country)
        self._country_name = country
        self._name_kategori_file = os.path.join(country, "barang.txt")
        # create file first if not exist
        __file = open(self._name_kategori_file, "a")
        __file.close()

    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def listBarang(self):
        print("Daftar kategori : ")
        kategori = self._get_kategori()
        if len(kategori) != 0:
            for text in kategori:
                print("\t1." + text)
        else:
            print("Kategori kosong")

    def _menu_1(self):
        name = input("Masukkan nama kategori : ")
        harga = input("Masukkan harga(" + self._country_name + ") : ")
        if self._add_kategori(name, harga):
            print("Kategori telah di tambahkan :")
            print(self._get_kategori())
            print("\n")
        else:
            print("Kategori sudah ada")

    def _menu_2(self):
        if len(self._get_kategori()) != 0:
            index_barang = int(input("Pilih barang yang ingin di hapus: ")) - 1
            list_raw = self._get_raw_kategori()
            del list_raw[index_barang]
            self._update_barang(list_raw)
            self.listBarang()
        else:
            print("Belum ada barang yg terdaftar")

    def _default(self):
        print("invalid code, pick again")

    def _update_barang(self, list_barang):
        __file = open(self._name_kategori_file, "w")
        __file.writelines(list_barang)
        __file.close()

    def _get_raw_kategori(self):
        __file = open(self._name_kategori_file, "r")
        return __file.readlines()

    def _get_kategori(self):
        __file = open(self._name_kategori_file, "r")
        list_barang = __file.readlines()
        for index, barang in enumerate(list_barang):
            list_barang[index] = barang.split(",")[0]
        return list_barang

    def delete_country(self):
        shutil.rmtree(self._country_name)

    def _add_kategori(self, kategori, harga):
        if len(self._get_kategori()) == 0 or kategori not in self._get_kategori():
            __file = open(self._name_kategori_file, "a")
            __file.write(kategori + "," + harga + "\n")
            __file.close()
            return True
        else:
            return False
