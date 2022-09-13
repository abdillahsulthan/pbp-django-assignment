# PENJELASAN TUGAS 2

Link aplikasi Heroku Tugas 2 PBP: https://webnyakatabtugas2.herokuapp.com/katalog/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![BAGAN MVT](https://user-images.githubusercontent.com/112261948/189924116-b0236873-5685-46b5-84c5-0f0bddb2d0c2.png)

Penjelasan bagan → User akan melakukan request dimana request ini akan diproses pertama kali oleh konfigurasi URL atau “urls.py”, proses ini dilakukan karena pada tahap inilah terdapat definisi alamat rute (URL) dan fungsi yang akan dijalankan di setiap rute. Selanjutnya, request akan dilanjutkan ke views.py, dimana pada views ini akan terjadi beberapa pemrosesan yaitu menulis atau mengambil data dari model, mengelola tampilan data dengan template html, serta mengirim HTTP Response ke user.
