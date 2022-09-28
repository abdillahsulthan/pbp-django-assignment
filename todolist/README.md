# PENJELASAN TUGAS 4

**Link aplikasi Heroku TODOLIST Tugas 4 PBP** : https://webnyakatabtugas2.herokuapp.com/todolist/


**1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**

{% csrf_token %} pada elemen form berfungsi untuk membandingkan dua token yang terdapat pada sisi user dan pada sisi _request_. Jika token tersebut dianggap tidak bersesuaian maka _request_ pada form tersebut akan ditolak. Namun, apabila token yang di _request_ bersesuaian maka form akan merespons OK. Sesuai dengan fungsinya, apabila potongan kode {% csrf_token %} tidak digunakan pada elemen form, maka akan terdapat beberapa pemetaan url atau link yang dapat disalahgunakan oleh orang lain. Akun kita bisa saja terhapus diluar kontrol kita jika seseorang memiliki button ke link tersebut.

**2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**

Pada dasarnya, kita bisa membuat elemen form secara manual. Cara yang bisa kita lakukan adalah dengan menggunakan method POST pada elemen form dan menggunakan {% csrf_token %}. Gambaran besar yang bisa kita lakukan adalah, pertama kita menginisiasi elemen form dengan method POST. Lalu, kita membuat tag table, dengan tag tr didalamnya. Tag tr ini akan digunakan untuk sebagai tempat untuk tag input. Method request.POST.get({nama id input}) dapat digunakan untuk mengakses input

**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Submisi data yang dilakukan pengguna dapat kita akses dengan menggunakan request.POST.get({nama id input}). Lalu, data yang diinput akan disesuaikan dengan models.py yang telah kita buat. Data yang dibuat tadi akan tersimpan pada database Django dan dapat diakses dengan {nama models}.Objects.filter(user=request.user). Hal ini agar data yang akan dipakai difilter berdasarkan user yang kemudian masuk kedalam context pada views.py dan dirender ke html. Data tersebut sekarang dapat ditampilkan sesuai dengan keingin developer.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat aplikasi dengan nama todolist, dengan melakukan perintah python manage.py startapp todolist pada cmd dan mendaftarkan aplikasi todolist ke dalam variabel INSTALLED_APPS pada settings.py project_django

2. membuat fungsi show_todolist dan mendaftarkan path dari todolist.urls pada urls.py di project_django

3. membuat sebuah model Task pada models.py dan membuat field user, date, title, description, dan is_finished.

4. Membuat views login, logout, dan register, beserta template html dari register dan login, yang kemudian fungsi views-views tersebut akan dipetakan ke template yang telah dibuat. Lalu saya menambahkan @login_required(login_url='/todolist/login/') agar setiap ingin mengakses website todolist maka user harus terdaftar terlebih dahulu

5. Melalukan modifikasi pada todolist.html, mulai dari tampilan, pengambilan data, dan melakukan sinkronisasi terhadap fungsi masing-masing button

6. Membuat fungsi baru pada views.py yaitu add_todolist yang berfungsi untuk membuat form yang berisi judul dan deskripsi yang ingin ditambahkan. Data yang ditambahkan akan diupdate dan di save, dan dihungkan pada template html create_task

7. Melakukan routing terhadap seluruh fungsi views.py dengan membuat urls.py pada aplikasi todolist.

8. Melakukan git add,commit, dan push serta melakukan deployment ke heroku

9. Membuat 2 akun yang masing-masing akun berisikan 3 dummy data