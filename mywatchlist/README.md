# PENJELASAN TUGAS 3


**Link aplikasi Heroku HTML Tugas 3 PBP**: https://webnyakatabtugas2.herokuapp.com/mywatchlist/html/

**Link aplikasi Heroku XML Tugas 3 PBP**: https://webnyakatabtugas2.herokuapp.com/mywatchlist/xml/

**Link aplikasi Heroku JSON Tugas 3 PBP**: https://webnyakatabtugas2.herokuapp.com/mywatchlist/json/


**1. Jelaskan perbedaan antara JSON, XML, dan HTML!**

JSON adalah singkatan dari JavaScript Object Notation. JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman. Data pada JSON disimpan dalam bentuk key dan value. Pada contoh di atas yang menjadi key adalah brand, type, color, dan memory. Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek.

XML adalah singkatan dari eXtensible Markup Language. XML didesain menjadi self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanyalah informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. Dokumen XML membentuk struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Dokumen XML harus mengandung sebuah root element yang merupakan parent dari elemen lainnya.

HTML atau Hypertext Markup Language merupakan sebuah bahasa untuk mengembangkan website. Kode HTML tersebut memastikan format teks dan gambar yang tepat untuk browser Internet. Tanpa HTML, browser tidak akan tahu bagaimana menampilkan teks sebagai elemen atau memuat gambar atau elemen lainnya.

**2. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform??**

Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON.

**3. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.**

Pada tugas kali ini, pertama kali saya membuat aplikasi "mywatchlist" pada command prompt, lalu saya mendaftarkan aplikasi tersebut kedalam project_django di settings.py. Lalu, saya membuat model dari mywatchlist pada models.py. Model tersebut lalu saya lakukan migrations dan migrate pada CMD. Selanjutnya, saya membuat folder fixtures pada mywatchlist dengan isi file initial_mywatchlist_data.json untuk menginput 10 data film. Lalu, saya meload data untuk dimasukkan kedalam database django lokal.

Langkah selanjutnya adalah implementasi MVT. Pertama saya membuat kode pada views.py di folder mywatchlist untuk dimapping ke URL lalu ditampilkan di HTML. Lalu, saya membuat file html untuk menampilkan data-data film pada website. Selanjutnya, saya membuat urls.py pada mywatchlist. URLS ini saya akan daftarkan pada project_django. Akhirnya, website yang kita buat akan ditampilkan pada website.

Langkah selanjutnya adalah implementasi Data delivery menggunakan JSON dan XML. Pertama, saya melakukan import HttpResponse dan serializer pada views.py serta membuat fungsi untuk menampilkan xml, json, xml berdasarkan id, dan json berdasarkan id. Lalu, setelah selesai saya memetakannya ke urls.py pada mywatchlist agar bisa diakses. Checklist-checklist yang telah dikerjakan akan dipush ke dalam repo dan dilakukan proses deploy heroku

**POSTMAN**
1. HTML

![html](https://user-images.githubusercontent.com/112261948/191533902-22c4c7bd-00ed-4cc5-80a7-71b8d2783cff.jpg)

2. XML

![xml](https://user-images.githubusercontent.com/112261948/191534135-25bd7038-c97f-467b-bf5c-32abea722331.jpg)

3. JSON

![json](https://user-images.githubusercontent.com/112261948/191534208-c8ecceb5-61b4-4e52-a99d-2fe50b39c6e7.jpg)
