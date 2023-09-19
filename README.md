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
![S__117391362](https://github.com/teticeci/Make-me-Up/assets/143377299/728bda41-ea54-4025-9762-eb7a31cacf78)
![Screenshot (285)](https://github.com/teticeci/Make-me-Up/assets/143377299/ba7d8d1b-9386-4e0b-9577-f4b0c32fc4fe)
![Screenshot (284)](https://github.com/teticeci/Make-me-Up/assets/143377299/c3c7f1ab-a7b9-4fc6-972f-4cd7349b8ce4)
![Screenshot (287)](https://github.com/teticeci/Make-me-Up/assets/143377299/4638ba0f-9bf2-410b-96c3-8a568c8764e2)
![Screenshot (286)](https://github.com/teticeci/Make-me-Up/assets/143377299/637d7bd9-7379-471c-8ccf-6b6a08370e09)
