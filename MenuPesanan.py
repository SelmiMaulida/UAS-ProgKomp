import csv
import os
from os import system

from Barang import BarangJual
from MenuNegara import MenuNegara
from Person import Person


class MenuPesanan:
    _country_name = ""
    _file_person_name = ""
    _file_pesanan_csv = ""

    def __init__(self, country):
        self._file_person_name = os.path.join(country, "person.txt")
        self._file_pesanan_csv = os.path.join(country, "pesanan.csv")
        _file = open(self._file_person_name, "a")
        _file.close()

        self._country_name = country

    def switch(self, kode):
        return getattr(self, "_menu_" + str(kode), lambda: self._default)()

    def _default(self):
        print("invalid code, pick again")

    def _menu_1(self):
        name_person = input("Masukkan nama pemesan : ")
        if (name_person+"\n") not in self.get_list_person():
            _file = open(self._file_person_name, "a")
            _file.write(name_person + "\n")
            _file.close()

        produk_iterasi = True
        while produk_iterasi:
            system("cls")
            print("\tPesanan untuk " + name_person)
            menuBarang = BarangJual(self._country_name)
            menuPerson = Person(self._country_name, name_person)
            print("Pilih Produk :")
            for index, product in enumerate(menuBarang.get_kategori()):
                print(str(index + 1) + ". " + product)
            index_product = int(input("Pilihan : ")) - 1
            jumlah_barang = int(input("Jumlah barang : "))
            menuPerson.add_product(menuBarang.get_kategori()[index_product], jumlah_barang)
            print("Berhasil menambahkan data!")
            
            with open(self._file_pesanan_csv, mode="w", newline="") as _file_open:
                _header = ["No", "Nama", "Barang", "Harga Barang", "Jumlah", "Total Harga(" + self._country_name + ")",
                           "Total Harga(INA)"]
                _writer = csv.DictWriter(_file_open, _header)
                _writer.writeheader()

                _count = 1

                for index, name in enumerate(self.get_list_person()):
                    _name = name.replace("\n", "")
                    menuPerson = Person(self._country_name, _name)
                    for index, product in enumerate(menuPerson.get_raw_product()):
                        _item = product.split(",")[0]
                        _amount = product.split(",")[1].replace("\n", "")

                        menuBarang = BarangJual(self._country_name)
                        _index_barang = menuBarang.get_kategori().index(_item)
                        _price = menuBarang.get_raw_kategori()[_index_barang].split(",")[1].replace("\n", "")

                        menuNegara = MenuNegara()
                        index_negara = menuNegara.listNegara().index(self._country_name)
                        _kurs = menuNegara.get_raw_country()[index_negara].split(",")[1].replace("\n", "")

                        _input = {
                            "No": _count,
                            "Nama": _name,
                            "Barang": _item,
                            "Harga Barang": _price,
                            "Jumlah": _amount,
                            "Total Harga(" + self._country_name + ")": float(_price) * int(_amount),
                            "Total Harga(INA)": float(_price) * int(_amount) * float(_kurs)
                        }

                        _writer.writerow(_input)
                        _count += 1

                print("\tCetak list pesanan berdasarkan")
                print("\tSilahkan cek file pesanan.csv di folder [" + self._country_name + "]")
            produk_iterasi = True if input("ingin menambah barang lagi?(y,n)") == "y" else False

    def get_list_person(self):
        _file = open(self._file_person_name, "r")
        return _file.readlines()
