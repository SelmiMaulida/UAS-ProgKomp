from Barang import BarangJual


class MenuNegara:
  
    def _menu_1(self):
        print("\n")
        country_name = input("Masukkan nama negara : ")
        country_kurs = input("Masukkan nilai kurs ke INA : ")
        if country_name not in self.listNegara():
            __file = open("country_list.txt", "a")
            __file.Write(country_name + "," + country_kurs + "\n")
            __file.close()
            print("Berhasil menambahkan negara")
        else:
            print("Negara sudah ada")
          
    def _menu_2(self):
        print("\n")
        if len(self.listNegara())!=0:
            print("Pilih negara yang ingin di edit barangnya : ")
            for index, country in enumerate(self.listNegara()):
                print("\t" + str(index + 1) + ". " + country)
            index_country = int(input("Pilihan : ")) - 1
            
            iterasi = True
            while iterasi:
                self._menuEditBarangNegara(index_country)
                iterasi = True if input("do you want to quit? (y/n) ") == "n" else False
        else:
            print("Negara belum ada, silahkan menambahkan negara terlebih dahulu")
            
    def _menu_3(self):
        print("\n")
        if len(self.listNegara()) != 0:
            print("Pilih Negara yang ingin di hapus: ")
            for index, country in enumerate(self.listNegara()):
                print("\t" + str(index + 1) + ". " + country)
            index_country = int(input("Pilihan : ")) - 1
            list_raw = self._get_raw_country()
            barang_country = BarangJual(self.listNegara()[index_country])
            barang_country.delete_country()
            del list_raw[index_country]
            self._update_country(list_raw)
            print("Berhasil menghapus negara beserta semua datanya")
        else:
            print("Negara belum ada, silahkan menambahkan negara terlebih dahulu")

