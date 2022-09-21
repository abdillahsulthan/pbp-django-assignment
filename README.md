# PENJELASAN TUGAS 2

**Link aplikasi Heroku Tugas 2 PBP**: https://webnyakatabtugas2.herokuapp.com/katalog/

**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**

![BAGAN MVT](https://user-images.githubusercontent.com/112261948/189924116-b0236873-5685-46b5-84c5-0f0bddb2d0c2.png)

Penjelasan bagan → _User_ akan melakukan _request_ dimana _request_ ini akan diproses pertama kali oleh konfigurasi URL atau “urls.py”, proses ini dilakukan karena pada tahap inilah terdapat definisi alamat rute (URL) dan fungsi yang akan dijalankan di setiap rute. Selanjutnya, _request_ akan dilanjutkan ke views.py, dimana pada views ini akan terjadi beberapa pemrosesan yaitu menulis atau mengambil data dari model, mengelola tampilan data dengan template html, serta mengirim _HTTP Response_ ke _user_.

**2. Jelaskan kenapa menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?**

Pada dasarnya, penggunaan _virtual environment_ bersifat opsional. Namun, penggunaannya sangat direkomendasikan dalam pengembangan sebuah web berbasis Django. _Virtual environment_ merupakan sebuah ruang lingkup virtual yang terisolasi dari _dependencies_ utama. _Virtual environment_ ini sangat berguna ketika kita membutuhkan _dependencies_ yang berbeda pada setiap _project_ yang akan dikembangkan pada _operating system_ yang sama. Sehingga, _virtual environment_ dibutuhkan untuk menjalankan suatu _project_, tanpa merubah konfigurasi _operating system_ yang kita gunakan. Kesimpulan yang bisa didapat adalah bahwa kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_. Namun, apabila _project_ yang ingin dikembangkan banyak dan memiliki _package_ yang berbeda dapat menyebabkan _crash_ pada _operating system_ yang kita miliki.

**3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

**1) Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML**
  
Pada views.py saya membuat sebuah fungsi show_katalog yang akan digunakan untuk me-_return_ _HTTP Response_, sehingga data yang terkandung dapat muncul pada file.html.   Selain itu, saya meng-_import_ data dari models.py untuk menetukan struktur data yang akan disimpan seperti ukuran maksimum. Pada fungsi show_katalog saya menambahkan variabel nama dan npm yang disimpan pada dictionary context, variabel ini akan digunakan pada file html.

**2) Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py**

Fungsi yang telah dibuat pada views.py selanjutnya akan dipetakan ke URL melalui urls.py, pemetaan ini akan membuat sebuah rute atau path dari URL katalog ke URL project. Jadi, pada awalnya saya membuat _pattern_ URL pada URL katalog untuk pemetaan ke URL Project, selanjutnya saya mendaftarkan path URL katalog tadi pada URL project, agar tampilan html bisa ditampilkan pada website

**3) Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template**

Pada halaman html saya melakukan for loop terhadap data list_barang yang telah saya definisikan pada views.py, dimana for loop ini disediakan oleh Django lewat aturan sintaks khusus yang telah dibuat. Selain itu, saya juga menggunakan sintaks khusus “{{data}}” untuk mengambil nama dan npm yang telah saya buat pada views.py

**4) Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

Berkas - berkas yang digunakan pada proses _deployment_ ini adalah Procfile, file ini digunakan oleh Heroku untuk membaca aktivitas log aplikasi ke sistem _monitoring_ internal Heroku. Lalu file dpl.yml, file ini digunakan untuk mengeksekusi _deployment_ oleh saya dari GitHub Actions. Selain itu, saya juga menambahkan konfigurasi berikut pada settings.py pada project_django,

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

Selanjutnya, saya mengambil API Key dari Heroku dan membuat aplikasi baru pada Heroku. Lalu, saya mendaftarkan API Key dan nama aplikasi tersebut kedalam repository secret yang saya miliki. Informasi ini akan berguna untuk mendefinisikan variabel API Key serta APP Name pada file dpl.yml. Dan akhirnya, saya menjalankan workflow dan proses deployment berhasil

SUMBER REFERENSI: 

https://www.petanikode.com/django-untuk-pemula/

https://dev.notnoob.com/tutorial-virtual-environment/