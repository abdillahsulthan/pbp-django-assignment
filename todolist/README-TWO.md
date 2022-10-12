# PENJELASAN TUGAS 6

**Link aplikasi Heroku TODOLIST Tugas 5 PBP** : https://webnyakatabtugas2.herokuapp.com/todolist/

**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming**

Asynchronous programming adalah sebuah pendakatan pemrograman yang tidak terikat pada I/O protocol. Asynchronous programming memungkinkan bagi seorang developer untuk melakukan task codingnya tanpa harus terikat dengan proses lain(independent). Synchronous programming membuat waktu eksekusi program lebih cepat dibanding synchronous. Pendekatan ini membuat tiap modul tidak perlu menunggu task lain selesai berjalan

Synchronous programming memiliki pendekatan yang lebih old school. Pendekatan ini membuat program berjalan secara sequential. Artinya program akan diekseksi berdasarkan antrian eksekusi program. Program dengan pendekatan ini akan lebih lama dieksekusi dibanding asynchronous programming.

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Pada penerapan javascript dan ajax, saya menggunakan event-driven programming, dimana pendekatan ini digunakan untuk menghandle event atau kejadian yang terjadi di website. Misalkan ketika user menekan sebuah tombol. Sebuah function javaScript akan di buat dan dipetakan sebagai sebuah fungsi yang akan dijalankan ketika event dilakukan. Pada todolist.html saya menambahkan on("click") dimana sebuah fungsi akan dijalankan ketika tombol di click. Misalnya pada createtask dan delete

**3. Jelaskan penerapan asynchronous programming pada AJAX.**

Pada javaScript, AJAX merupakan sebuah konsep yang menerapkan asynchronous programming dalam mengeksekusi task pada program. AJAX pada program ini digunakan untuk melakukan pengambilan data dan menangani sebuah response, dalam bentuk JSON. Pada penerapannya AJAX disini menggunakan JQuery dimana kita tidak perlu membuat instance objek. Kita hanya perlu menambahkan library JQuery pada todolist.html. Dengan menggunakan JQuery response handling dapat dilakukan secara langsung dengan memanggil function success dan error

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Saya membuat sebuah views baru untuk mengambil data dari models.py dengan representasi JSON. Lalu, saya memetakannya ke dalam URL 

2. Saya membuat fungsi get data dengan menggunakan ajax pada todolist.html. Data yang akan ditampilkan akan diambil dari url yang sudah dipetakan ke dalam bentuk JSON

3. Lalu saya mengubah link pemetaan setelah meng-click tombol CreateTask menuju target modal. Sebelumnya saya membuat modal terlebih dahulu dengan template pada Bootstrap.

4. Sebelum membuat fungsi AJAX, saya membuat views baru untuk menambahkan data dan memetakannya kedalam URL

5. Lalu saya membuat fungsi AJAX pada todolist.html dengan type POST untuk menambahkan data dari user.

6. Fitur create akan secara asynchronous dilakukan
