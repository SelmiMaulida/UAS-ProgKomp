# UAS-ProgKomp
Repositori untuk menyimpan UAS Progkomp 2020

## Penjelasan Program Pendataan Jasa Titip Luar Negeri

Program aplikasi pendataan jasa titip luar negeri dirancang khusus bagi pengguna yang memiliki usaha jasa titip barang dari luar negeri. Dengan adanya program ini, diharapkan pelaku jastip lebih mudah, cepat, dan efisien dalam merekap transaksi pesanan dari pembeli yang berada di Indonesia.

Untuk menghindari kesalahan dalam pembelian barang oleh pelaku jastip, program aplikasi ini mampu mengelompokkan pesanan berdasarkan jenis barang dan negara tujuan barang yang dipesan oleh customer. Selain itu, tersedia juga layanan konversi mata uang, sehingga pelaku jastip tidak perlu kesulitan dalam mengonversi mata uang luar negeri ke rupiah. Beberapa fitur yang ditawarkan oleh program ini, yaitu :

* Melakukan pencatatan pesanan Anda
* Melihat pesanan secara langsung
* Menyimpan database pesanan dan pelanggan dalam bentuk csv/excel

## Tahapan penggunaan program aplikasi pendataam jasa titip luar negeri :
a) Menampilkan pilihan menu awal, pengguna diminta input menu yang dipilih.
* `1. List Negara`
* `2. Mulai Pendataan Pesanan`

b) Apabila pengguna memilih `1. List Negara`, maka akan muncul daftar Negara Jastip dan sub menu :
* `1. Tambah Negara`
* `2. Edit Barang Negara`
* `3. Hapus Negara`

c) Jika daftar Negara Jastip masih kosong, pengguna akan diarahkan untuk menambahkan negara.

d) Jika daftar Negara Jastip telah tercetak, maka pengguna dapat memilih opsi `2. Edit Barang Negara` atau `3. Hapus Negara`.

e) Jika pengguna memilih opsi `2. Edit Barang Negara`, maka pengguna diminta input nama negara, dan nilai kurs mata uang negara tersebut ke dalam rupiah, lalu program akan menyimpan data.

f) Jika pengguna memilih opsi `3. Hapus Negara`, maka pengguna diminta input  nomor negara yang akan dihapus datanya, kemudian program akan menghapus data negara tersebut dan menyimpan perubahannya.

g) Apabila pengguna memilih `2. Mulai Pendataan Pesanan`, maka akan muncul daftar negara jastip yang telah di-input-kan oleh pengguna. Pengguna diminta input nomor negara tujuan, lalu akan muncul sub menu :

* `1. Lihat Pesanan`
* `2. Tambah Pesanan`
* `3. Hapus Pesanan`

h) Jika pengguna memilih opsi `1. Lihat Pesanan`, maka program akan menampilkan daftar pesanan yang telah di¬-input¬-kan. Namun jika pengguna belum meng-input pesanan, maka program akan mencetak “Belum ada pesanan”. Pengguna diarahkan untuk menambahkan pesanan di opsi `2. Tambah Pesanan`.

i) Jika pengguna memilih opsi `2. Tambah Pesanan`, maka pengguna diminta untuk input  nama pemesan, pilihan daftar produk yang dipesan, dan jumlah produk. System akan mengolah dan menyimpan data tersebut.

j) Jika pengguna memilih opsi `3. Hapus Pesanan`, maka program secara otomatis akan menghapus data pesanan pada negara tujuan yang dipilih.

k) Hasil akhir dari program berupa file dalam format csv, yang nantinya dapat diconvert dalam bentuk excel, sehingga memudahkan pengguna dalam merekap pesanan sesua negara tujuan dan jenis barang yang dipesan.
