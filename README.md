Tautan repositori: https://github.com/teticeci/Make-me-Up.git

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
                                         <-> 5.Model
1.Client <-> 2.Django <-> 3.URL <-> 4.View
                                         <-> 6.Template
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