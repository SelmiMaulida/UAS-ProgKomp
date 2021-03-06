from os import system

from Barang import BarangJual


class MenuNegara:

    def __init__(self):
        __file = open("country_list.txt", "a")
        __file.close()

    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def _default(self):
        print("invalid code, pick again")

    def _menu_1(self):
        system("cls")
        country_name = input("Masukkan nama negara : ")
        country_kurs = float(input("Masukkan nilai kurs ke INA (Hanya Angka): "))
        if country_name not in self.listNegara():
            __file = open("country_list.txt", "a")
            __file.write(country_name + "," + str(country_kurs) + "\n")
            __file.close()
            print("Berhasil menambahkan negara")
        else:
            print("Negara sudah ada")

    def _menu_2(self):
        system("cls")
        if len(self.listNegara())!=0:
            print("Pilih Negara yang ingin di edit barangnya: ")
            for index, country in enumerate(self.listNegara()):
                print("\t" + str(index + 1) + ". " + country)
            index_country = int(input("Pilihan : ")) - 1

            iterasi = True
            while iterasi:
                self._menuEditBarangNegara(index_country)
                iterasi = True if input("Apakah edit Barang Negara sudah selesai? (y/n)") == "n" else False
        else:
            print("Negara belum ada, silahkan menambahkan negara terlebih dahulu")

    def _menu_3(self):
        system("cls")
        if len(self.listNegara()) != 0:
            print("Pilih Negara yang ingin di hapus: ")
            for index, country in enumerate(self.listNegara()):
                print("\t" + str(index + 1) + ". " + country)
            index_country = int(input("Pilihan : ")) - 1
            list_raw = self.get_raw_country()
            barang_country = BarangJual(self.listNegara()[index_country])
            barang_country.delete_country()
            del list_raw[index_country]
            self._update_country(list_raw)
            print("Berhasil menghapus negara beserta semua datanya")
        else:
            print("Negara belum ada, silahkan menambahkan negara terlebih dahulu")

    def _update_country(self, list):
        __file = open("country_list.txt", "w")
        __file.writelines(list)
        __file.close()

    def get_raw_country(self):
        __file = open("country_list.txt", "r")
        return __file.readlines()

    def listNegara(self):
        __file = open("country_list.txt", "r")
        country_list = __file.readlines()
        __file.close()
        for index, country in enumerate(country_list):
            country_list[index] = country.split(",")[0]
        return country_list

    def _menuEditBarangNegara(self, index_country):
        print("\n")
        menu_barang = BarangJual(self.listNegara()[index_country])
        menu_barang.listBarang()
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        code_menu = input("Pilihan : ")

        menu_barang.switch(code_menu)
