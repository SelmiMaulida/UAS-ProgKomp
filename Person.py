import os


class Person:
    _person_name = ""
    _name_kategori_file = ""

    def __init__(self, country, person_name):
        # create folder if not exist
        if not os.path.exists(country):
            os.makedirs(country)
        self._person_name = country
        self._name_kategori_file = os.path.join(country, person_name + ".txt")
        # create file first if not exist
        __file = open(self._name_kategori_file, "a")
        __file.close()

    def add_product(self, product, amount):
        if product not in self._get_list_product():
            __file = open(self._name_kategori_file, "a")
            __file.write(product + "," + str(amount) + "\n")
            __file.close()
        else:
            print("Barang sudah ditambahkan")

    def get_raw_product(self):
        __file = open(self._name_kategori_file, "r")
        return __file.readlines()

    def _get_list_product(self):
        __file = open(self._name_kategori_file, "r")
        list_beli = __file.readlines()
        for index, item in enumerate(list_beli):
            list_beli[index] = item.split(",")[0]
        return list_beli
    
    def delete_product(self,product_name):
        if product_name in self._get_list_product():
            index_product = self._get_list_product().index(product_name)
            list_raw = self.get_raw_product()
            del list_raw[index_product]
            self._update_product(list_raw)
    
    def _update_product(self, list_product):
        __file = open(self._name_kategori_file, "w")
        __file.writelines(list_product)
        __file.close()
