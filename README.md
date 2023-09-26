Tautan repositori: https://github.com/teticeci/Make-me-Up.git
Tautan aplikasi: https://make-me-up.adaptable.app


(TUGAS 2)

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
Langkah awal saya dimulai dengan membuat repositori lokal dan menghubungkannya dengan repositori di GitHub.
Selanjutnya, membuat new app pada Adaptable.io yang telah dihubungkan dengan repositori proyek GitHub.
Kemudian, membuat aplikasi Django dengan mengaktifkan virtual environment.
Dilanjutkan dengan membuat aplikasi main di dalam proyek dan melakukan implementasi kode pada beberapa file, seperti file models.py, views.py, urls.py, serta tidak lupa menambahkan folder templates sebagai direktori penempatan main.html.
Perlu diperhatikan ketika melakukan perubahan pada kode models.py, maka wajib melakukan migrasi model.
Membuat Django Unit Testing yang berguna untuk melalukan pengujian terhadap kode.
Langkah terakhir yaitu melakukan add, commit, dan push pada virtual environment untuk update perubahan kode ke repositori proyek GitHub.
Repositori proyek GitHub akan langsung terhubung dengan deployment aplikasi di Adapatble.io

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
![google](https://i.postimg.cc/9f3cmCWt/mvt.png)
1. Client membuat request ke website berbasis Django
2. Jika request valid, akan diterima oleh web server dan diteruskan ke Django
3. Kemudian, Django akan mengidentifikasi path URL (urls.py) untuk menentukan view mana yang akan melakukan routing
4-5. View (views.py) akan menggunakan data dari model (models.py) untuk memproses request client, lalu meneruskan ke template
6. Template akan menghasilkan respon yang sesuai, misalnya (berkas html) dan diteruskan kembali ke client

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab:
Virtual environment berguna sebagai wadah untuk menampung modul suatu proyek pekerjaan agar terisolasi dan memungkinkan menggunakan versi Python berbeda untuk setiap proyek. Membuat aplikasi web berbasis Django tanpa virtual environment memang dapat dilakukan, namun tidak disarankan karena tak adanya isolasi proyek.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab:
Model View Controller (MVC) adalah pola desain arsitejtur website/aplikasi yang terbagi ke dalam tiga komponen utama, yaitu model, view, dan controller.
Model View Presenter (MVP) adalah turunan dari model arsitektur MVC yang berfokus pada peningkatan logika presentasi, terbagi ke dalam tiga komponen utama, yaitu model, view, dan presenter.
Model View ViewModel (MVVM) adalah evolusi dari model penggabungan MVC dan MVP yang berfokus pada pemisahan perhatian dan pengujian, terbagi ke dalam tiga komponen, yaitu model, view, dan viewmodel.


(TUGAS 3)

Apa perbedaan antara form POST dan form GET dalam Django?
Jawab:
Form POST berperan untuk mengirimkan data ke action untuk ditampung, tanpa ditampilkan pada URL. Sedangkan form GET berperan untuk menampilkan data pada URL, kemudian akan ditampung oleh action.

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Jawab:
XML (Extensible Markup Language)
Bahasa markup yang digunakan untuk mengirimkan data yang lebih terstruktur.
JSON (JavaScript Object Notation)
Format data yang digunakan untuk mengirimkan data dengan cara menyimpan data dalam bentuk key:value dan dikirimkan melalui internet.
HTML (Hypertext Markup Language)
Bahasa markup yang digunakan untuk mengatur tampilan dan struktur website, bukan untuk pertukaran data. Data dari formulir HTML ke server menggunakan metode HTTP GET atau POST.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Jawab:
JSON termasuk format data yang sering digunakan karena penulisan kode sederhana yang mudah dibaca, dipahami, serta menunjukkan data terstruktur berdasarkan syntax objek JavaScript. Selain itu proses loading data yang lebih ringan karena ukuran file yang kecil.
JSON sering digunakan dalam pengembangan API RESTful, yang menjadi standar dalam komunikasi antara klien dan server dalam aplikasi web modern.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
- Mengatur routing dari main/ ke /
Menggunakan / sebagai basis URL, memiliki fleksibilitas untuk mengubah struktur situs tanpa perlu mengubah URL untuk setiap halaman. Tahapannya yaitu dengan menjalankan virtual environment, lalu membuka urls.py pada folder beauty_store dan mengubah path main/ menjadi ' ' pada urlpatterns.
- Implementasi Skeleton sebagai kerangka views
Skeleton berfungsi dalam memberikan umpan balik visual kepada pengguna bahwa halaman sedang dimuat, sehingga pengguna tahu bahwa aplikasi masih aktif dan bekerja. Tahapannya yaitu membuat root folder templates dan membuat berkas baru di dalamnya yaitu base.html, kemudian sesuaikan kode yang ada agar berkas base.html terdeteksi sebagai berkas template.
- Membuat form input data dan menampilkan data pada HTML
 Form input memungkinkan pengguna untuk berinteraksi dengan aplikasi web secara interaktif. Tahapannya yaitu membuat berkas forms.py di direktori main, lalu menghubungkannya dengan views.py serta urls.py.
- Mengembalikan data dalam bentuk XML dan bentuk JSON
XML sangat terstruktur sehingga mampu mendefinisikan tipe data rumit dengan jelas, ini berguna dalam situasi di mana data memiliki hierarki yang kompleks. JSON memiliki format yang lebih efisien dalam hal penggunaan bandwidth, ini membuatnya cocok untuk aplikasi web yang berfokus pada kinerja dan responsif. Tahapannya yaitu menambahkan fungsi baru di views.py dengan nama show_xml dan show_json, lalu mengimpor fungsi tersebut ke urls.py.
- Mengembalikan data berdasarkan ID dalam bentuk XML dan JSON
XML dan JSON memungkinkan untuk menggambarkan data dalam bentuk ID yang memuat informasi spesifik yang terkait dengan ID tertentu. Tahapannya yaitu membuat fungsi baru di views.py yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id, lalu mengimpor fungsi tersebut ke urls.py.
- Penggunaan Postman sebagai data viewer
Postman menyediakan antarmuka yang intuitif dan mudah digunakan untuk melihat dan menganalisis data yang dikembalikan oleh API. Tahapannya yaitu melakukan send request ke Postman, lalu mengubah url menjadi http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] untuk mengetes fungsi pengambilan data produk berdasarkan ID.

Screenshot dari hasil akses URL pada Postman
![Screenshots]("C:\Users\tetib\OneDrive\Pictures\Screenshots\S__117391362.jpg")
![Screenshots]("C:\Users\tetib\OneDrive\Pictures\Screenshots\Screenshot (284).png")
![Screenshot]("C:\Users\tetib\OneDrive\Pictures\Screenshots\Screenshot (285).png")
![Screenshots]("C:\Users\tetib\OneDrive\Pictures\Screenshots\Screenshot (286).png")
![Screenshots]("C:\Users\tetib\OneDrive\Pictures\Screenshots\Screenshot (287).png")


(TUGAS 4)

Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Jawab:
UserCreationForm merupakan built in form di Django yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web. Terdapat three fields di dalamnya yaitu username, password, dan password confirmation.
Kelebihan:
- Praktis digunakan
Django's built-in authentication system yang praktis penggunaannya, hanya perlu mengimpor dan bisa langsung digunakan.
- Validasi bawaan
Memastikan user memasukkan informasi dengan tingkat keamanan tinggi serta unik untuk username dan password.
Kekurangan:
- Keamanan
Meskipun Django telah menuntun user untuk memasukkan informasi yang unik, terdapat beberapa serangan yang berpotensi menyerang website seperti serangan CSRF attack. Maka dari itu, user perlu menambahkan tag {% csrf_token %} pada template.
- Model user bawaan terbatas
Default yang diberikan masih terbatas, apabila user memiliki kebutuhan tambahan, perlu menyesuaikan dengan form tersebut.

Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Jawab:
Autentikasi dan otorisasi sangat penting bagi aplikasi website karena berfungsi untuk mengamankan informasi pada sistem secara otomatis. Perbedaan utama terletak pada, autentikasi memverifikasi identitas user, sedangkan otorisasi menentukan tindakan apa yang dapat user lakukan dalam aplikasi web. Contohnya otorisasi yang berbeda antara dosen dan mahasiswa di website SIAKNG.

Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Jawab:
Cookies browser adalah istilah kumpulan informasi yang berisi rekam jejak dan aktivitas user saat menelusuri sebuah website. Biasanya, suatu website akan memberikan notifikasi persetujuan penggunaan cookies kepada new visitor. Pada Django, cookies sisi klien menyimpan berbagai data yang berguna untuk aplikasi web, lalu web akan menyimpannya untuk memberikan informasi yang relevan berdasarkan rekam jejak user.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Jawab:
Pada kondisi normal, cookies tidak bisa mentransfer malware/virus karena data yang dibawa cookies tidak dapat dialihkan ketika berpindah dari komputer ke website dan sebaliknya. Maka dari itu, user harus menghindari situs-situs yang mencurigakan dan berpotensi bahaya agar informasi cookies tidak dicuri.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
- Mengimplementasikan fungsi registrasi, login, dan logout dengan cara menambahkan import beserta potongan kode di file main/views.py berupa fungsi def register(request), def login_user(request), dan def logout_user(request). Kemudian, membuat berkas html di file main/templates untuk setiap fungsi yang telah diinisiasi sebelumnya. Terakhir, membuka file main/urls.py lalu menambahkan import fungsi beserta potongan kode di urlspatterns untuk mengakses setiap fungsi yang telah diimpor.
- Membuat dua akun pengguna dengan masing-masing tiga dummy data dengan cara ...
- Menghubungkan model Item dengan User dengan cara menambahkan import beserta potongan kode di file main/models.py berupa ForeignKey di class Product yang berfungsi menghubungkan antara satu produk dengan satu user melalui sebuah relationship. Selanjutnya, mengubah kode di file main/views.py agar  memungkinkan modifikasi sebelum tersimpan ke database. Ubah juga fungsi show_main, kemudian lakukan migrasi model untuk menyimpan semua perubahan yang telah dilakukan.
- Menampilkan detail informasi pengguna yang sedang logged in dengan cara menggunakan data cookies. Melakukan import serta menambahkan potongan kode pada fungsi login_user di file main/views.py dan menambahkan 'last_login': request.COOKIES['last_login'] ke dalam variabel context. Kemudian menambahkan kode di file main.html  untuk menampilkan data last login.
- Langkah paling akhir, melakukan add-commit-push ke GitHub untuk merekap perubahan kode pada project.