import os
import shutil
from Person import Person

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
        print("Daftar barang : ")
        kategori = self.get_kategori()
        if len(kategori) != 0:
            for index, text in enumerate(self.get_kategori()):
                print("\t" + str(index + 1) + ". " + text)
        else:
            print("Barang kosong")

    def _menu_1(self):
        name = input("Masukkan nama barang : ")
        harga = float(input("Masukkan harga barang dalam angka saja(" + self._country_name + ") : "))
        if self._add_kategori(name, harga):
            print("Barang telah di tambahkan :")
            for index, text in enumerate(self.get_kategori()):
                print("\t" + str(index + 1) + ". " + text)
            print("\n")
        else:
            print("Barang sudah ada")

    def _menu_2(self):
        if len(self.get_kategori()) != 0:
            index_barang = int(input("Pilih barang yang ingin di hapus(Jika ada pesanan, maka pesanan otomatis terhapus): ")) - 1
            list_raw = self.get_raw_kategori()
            list_person = self._get_list_person(self._country_name)
            if len(list_person)!=0:
                for person in list_person:
                    Person(self._country_name,person.replace("\n","")).delete_product(self.get_kategori()[index_barang])
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

    def get_raw_kategori(self):
        __file = open(self._name_kategori_file, "r")
        return __file.readlines()

    def get_kategori(self):
        __file = open(self._name_kategori_file, "r")
        list_barang = __file.readlines()
        for index, barang in enumerate(list_barang):
            list_barang[index] = barang.split(",")[0]
        return list_barang

    def delete_country(self):
        shutil.rmtree(self._country_name)

    def _add_kategori(self, kategori, harga):
        if len(self.get_kategori()) == 0 or kategori not in self.get_kategori():
            __file = open(self._name_kategori_file, "a")
            __file.write(kategori + "," + str(harga) + "\n")
            __file.close()
            return True
        else:
            return False
        
    def _get_list_person(self,country_name):
        _file = open(os.path.join(country_name, "person.txt"),"a+")
        _file.seek(0)
        return _file.readlines()
        
