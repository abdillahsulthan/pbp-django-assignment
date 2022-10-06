# PENJELASAN TUGAS 5

**Link aplikasi Heroku TODOLIST Tugas 5 PBP** : https://webnyakatabtugas2.herokuapp.com/todolist/

**1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style**

Inline CSS berisi properti CSS pada body sectoon yang dilampirkan dengan elemen yang dikenal sebagai inline CSS. Jenis style ini ditentukan dalam tag HTML menggunakan atribut style.

Internal CSS merupakan kode CSS yang ditulis dalam tag style yang ditulis di bagian header file HTML. Internal CSS digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan di halaman website yang lain.

External CSS merupaka kode CSS yang diletakkan di luar dokumen HTML sebagai file .css.

**Kelebihan dan Kekurangan Inline CSS :**

Kelebihannya adalah kita dapat terbantu untuk menguji dan melihat perubahan pada satu elemen, berfungsi untuk memperbaiki kode dengan cepat, dan proses request HTTP yang lebih kecil sehingga load website lebih cepat. Kekurangannya adalah tidak efisien karena hanya dapat diterapkan pada satu elemen html.

**Kelebihan dan Kekurangan Internal CSS :**

Kelebihannya adalah perubahan pada internal css hanya berlaku pada satu templates saja, class serta id bisa digunakan pada internal stylesheet. Kekurangannya adalah tidak efisien apabila kita ingin menerapkan style pada beberapa templates, membuat performa website lebih lambat.

**Kelebihan dan kekurangan external CSS :**

Kelebihannya adalah file html lebih rapih, load website lebih cepat, file css dapat digunakan pada beberapa file sekaligus. Kekurangannya adalah Halaman akan menjadi berantakan, ketika file css gagal dipanggil oleh HTML.


**2. Jelaskan tag HTML5 yang kamu ketahui**

ada banyak tag yang ada di html 5 misalnya h1 hingga h6 yang biasa kita pakai untuk tulisan header, ada tag p untuk menulis teks, lalu terdapat tag form untuk membuat suatu isian bagi user. Tag a untuk memuat link pada suatu page. Lalu ada tag div untuk membuat section atau container

**3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.**

pertama ada selector tag dimana selector ini akan memilih elemen berdasarkan nama tag, lalu ada selector class dimana selector ini akan memilih elemen berdasarkan elemen berdasarkan nama class. Lalu ada selector id yang memilih elemen berdasarkan id. ID harus bersifat unik, artinya id hanya bisa digunakan pada satu elemen saja.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Meletakkan link bootstrap pada bagian head

2. Pada bagian register saya hanya merubah background color menjadi linear gradient. Mengubah background color ini juga saya lakukan pada seluruh page HTML. Selain itu, saya membuat beberapa referensi styling css login pada google untuk melakukan styling sesuai dengan yang saya inginkan. Hal ini juga saya lakukan pada page todolist.html

3. Pada bagian todolist saya mengubah penampilan todolist dalam bentuk table menjadi bentuk cards, untuk pengambilan data sebenarnya sama saja dengan melakukan for loop pada data todolist dari views.py saya
