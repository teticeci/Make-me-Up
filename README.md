Tautan repositori: https://github.com/teticeci/Make-me-Up.git

Tautan aplikasi: https://make-me-up.adaptable.app


## TUGAS 2

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


## TUGAS 3

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


## TUGAS 4

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

Autentikasi dan otorisasi sangat penting bagi aplikasi website karena berfungsi untuk mengamankan informasi pada sistem secara otomatis. Perbedaan utama terletak pada, autentikasi memverifikasi identitas user, sedangkan otorisasi menentukan tindakan apa yang dapat user lakukan dalam aplikasi web. Contohnya otorisasi yang berbeda antara akun dosen dan akun mahasiswa di website SIAKNG.

Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Jawab:

Cookies browser adalah istilah kumpulan informasi yang berisi rekam jejak dan aktivitas user saat menelusuri sebuah website. Biasanya, suatu website akan memberikan notifikasi persetujuan penggunaan cookies kepada new visitor. Pada Django, cookies sisi klien menyimpan berbagai data yang berguna untuk aplikasi web, lalu web akan menyimpannya untuk memberikan informasi yang relevan berdasarkan rekam jejak user.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Jawab:

Pada kondisi normal, cookies tidak bisa mentransfer malware/virus karena data yang dibawa cookies tidak dapat dialihkan ketika berpindah dari komputer ke website dan sebaliknya. Maka dari itu, user harus menghindari situs-situs yang mencurigakan dan berpotensi bahaya agar informasi cookies tidak dicuri.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
- Mengimplementasikan fungsi registrasi, login, dan logout dengan cara menambahkan import beserta potongan kode di file main/views.py berupa fungsi def register(request), def login_user(request), dan def logout_user(request). Kemudian, membuat berkas html di file main/templates untuk setiap fungsi yang telah diinisiasi sebelumnya. Terakhir, membuka file main/urls.py lalu menambahkan import fungsi beserta potongan kode di urlspatterns untuk mengakses setiap fungsi yang telah diimpor.
- Membuat dua akun pengguna dengan masing-masing tiga dummy data dengan cara melakukan registrasi akun serta melakukan add new product pada web.
- Menghubungkan model Item dengan User dengan cara menambahkan import beserta potongan kode di file main/models.py berupa ForeignKey di class Product yang berfungsi menghubungkan antara satu produk dengan satu user melalui sebuah relationship. Selanjutnya, mengubah kode di file main/views.py agar  memungkinkan modifikasi sebelum tersimpan ke database. Ubah juga fungsi show_main, kemudian lakukan migrasi model untuk menyimpan semua perubahan yang telah dilakukan.
- Menampilkan detail informasi pengguna yang sedang logged in dengan cara menggunakan data cookies. Melakukan import serta menambahkan potongan kode pada fungsi login_user di file main/views.py dan menambahkan 'last_login': request.COOKIES['last_login'] ke dalam variabel context. Kemudian menambahkan kode di file main.html  untuk menampilkan data last login.
- Langkah paling akhir, melakukan add-commit-push ke GitHub untuk merekap perubahan kode pada project.


## TUGAS 5

Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
J
awab:

- Universal Selector ('*') digunakan untuk memberikan design pada seluruh elemen
- Elemen Selecctor digunakan untuk memberikan design pada elemen yang spesifik
- Class Selector (.classname) digunakan untuk memberikan design pada sekelompok elemen
- ID Selector (#idname) digunakan untuk memberikan design pada elemen berdasarkan ID
- Attribute Selector ([attribute=value]) digunakan untuk memilih elemen berdasarkan atribut tertentu
- Descendant Selector (ancestor descendant) digunakan untuk memilih elemen dalam suatu hierarki
- Child Selector (parent > child) digunakan ketika ingin memilih elemen yang merupakan child dari parentnya

Jelaskan HTML5 Tag yang kamu ketahui.

Jawab:

Berikut ini beberapa tag yang tersedia di HTML5:
<article> </article> berguna untuk mendefinisikan sebuah artikel
<audio> </audio> berguna untuk menyematkan audio dalam dokumen HTML
<datalist> </datalist> mewakilkan rangkaian opsi yang telah ditentukan sebelumnya di elemen <input>
<footer> </footer> mewakilkan bagian footer dari suatu dokumen
<header> </header> mewakilkan bagian header dari suatu dokumen

Jelaskan perbedaan antara margin dan padding.

Jawab:

Penggunaan margin dan padding pada CSS, keduanya sama-sama digunakan untuk mengatur space kosong pada website.  Secara garis besar, margin digunakan untuk menata letak dari sisi luar, sedangkan padding digunakan untuk menata letak dari sisi dalam. Analoginya bila terdapat 2 kotak yang didalamnya terdapat teks, margin berguna memberi jarak antara kedua kotak tersebut, sedangkan padding berguna memberi jarak antara teks dengan kotak.

Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Jawab:

Bootstrap dan Tailwind merupakan framework CSS yang memberikan banyak kelebihan dibandingkan CSS yang biasa kita gunakan.
Berikut ini perbedaan antara framework CSS Tailwind dan Bootstrap:
- Desain dan Fleksibilitas
Bootstrap menawarkan framework yang relatif terstruktur dengan banyak komponen set class CSS yang konsisten, sedangkan Tailwind membangun antarmuka dengan menggabungkan class utilitas yang lebih kecil (utility-first) memungkinkan kustomisasi sesuai kebutuhan.
- Ukuran File
Bootstrap memiliki file berukuran lebih besar karena menyediakan banyak fitur dan komponen siap pakai, sedangkan Tailwind dirancang untuk lebih ringan dalam hal ukuran file.
- Kemudahan Penggunaan
Bootstrap cenderung beginner friendly karena dapat mulai dengan komponen yang telah didefinisikan, sedangkan Tailwind cenderung lebih advance karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.
Dalam penggunaannya, Bootstrap lebih cocok untuk membuat website standar dan konsisten dengan desain yang sudah umum digunakan. Sebaliknya, Tailwind lebih cocok untuk membuat website yang memerlukan detailing di dalamnya karena tidak terbatas pada gaya bawaan.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:

- Menjalankan virtual environment setiap ingin mulai memrogram aplikasi
- Menambahkan Bootstrap sebagai framework CSS serta Javascript ke aplikasi dengan menambahkan potongan kode di base.html
- Memanfaatkan template dari Bootstrap untuk membuat beberapa fitur Card pada aplikasi, dengan tambahan modifikasi
- Menambahkan fitur edit dan delete item pada aplikasi, langkah awal yaitu membuat fungsi di file views.py, lalu mengimpor fungsi ke urls.py dan menambahkan path ke urlpatterns, tahap akhir membuat berkas html sesuai dengan fungsi di  main/templates
- Memeriksa output program dengan python manage.py runserver
- Melakukan git add, git commit, dan git push


## TUGAS 6

Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Jawab:

Dalam proses sinkron, setiap fungsi dijalankan satu demi satu, dengan urutan yang telah ditentukan. Apabila sebuah fungsi sedang berjalan, fungsi lainnya harus menunggu hingga fungsi tersebut selesai sepenuhnya sebelum dapat dimulai. Ini sering kali menciptakan ketergantungan waktu yang ketat dan dapat mempengaruhi kecepatan keseluruhan dari sebuah sistem atau aplikasi. Sebaliknya, dalam proses asinkron, fungsi-fungsi dapat berjalan secara independen satu sama lain. Ini memungkinkan beberapa tugas untuk dieksekusi tanpa harus menunggu tugas lain selesai, memberikan fleksibilitas lebih dalam hal pengaturan waktu dan sumber daya, serta meningkatkan efisiensi dalam banyak skenario.

Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Jawab:

Paradigma event-driven programming, juga dikenal sebagai pemrograman berbasis peristiwa, memungkinkan program untuk menanggapi peristiwa yang terjadi, yang biasanya berasal dari input pengguna atau perubahan sistem. Paradigma ini sangat bergantung pada JavaScript, bahasa scripting yang paling banyak digunakan di web, terutama ketika bekerja dengan DOM (Document Object Model) dan teknologi seperti AJAX. Contoh paradigma pada tugas ini yaitu document.getElementById("button_add").addEventListener('click', function(event)), di mana 'click' merupakan nama event dan function(event) merupakan fungsi yang akan dijalankan saat event terjadi.

Jelaskan penerapan asynchronous programming pada AJAX.

Jawab:

- Browser melakukan panggilan JavaScript untuk memulai fungsi tertentu, yang pada gilirannya mengaktifkan objek XMLHttpRequest. Objek ini memungkinkan komunikasi antara browser dan server berjalan asinkron, yang memudahkan pertukaran data tanpa perlu memuat ulang halaman.
- Begitu panggilan XMLHttpRequest dimulai, web browser secara otomatis mengirimkan permintaan HTTP ke server tanpa intervensi pengguna. Permintaan ini biasanya berisi detail terperinci tentang informasi atau tindakan yang diperlukan.
- Setelah server menerima permintaan ini, browser mencari, mengolah, dan mengumpulkan data. Selanjutnya, data dikirim kembali ke web browser dalam format yang telah ditentukan, seperti JSON atau XML.
- Web browser memproses dan menampilkan data atau informasi pada halaman saat server mengirimkannya kembali.

Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Jawab:

- Fetch API
Fetch API tidak membutuhkan pustaka karena berbasis JavaScript. Menggunakan konsep promises, yang memungkinkan penanganan kode asinkron dengan cara yang lebih elegan, terutama saat dikombinasikan dengan fitur async/await. Hal ini memberikan pengembang yang lebih terkontrol tentang bagaimana mengelola permintaan. Dengan menggunakan Fetch API, kode untuk permintaan asinkron menjadi lebih sederhana dan lebih mudah dibaca.
- jQuery
Kode yang digunakan untuk AJAX dan manipulasi DOM seringkali lebih singkat dan mudah digunakan dengan jQuery. Menawarkan banyak alat tambahan untuk mengatur DOM, animasi, pengelolaan event, dan fitur lainnya. Dengan menggunakan jQuery, Anda dapat menambahkan pustaka eksternal ke proyek Anda, yang dapat meningkatkan ukuran dan waktu pemuatan halaman. Meskipun jQuery mendukung callback dan deferred objects, pendekatan asinkronitasnya mungkin tidak sebaik pendekatan Fetch API dengan promises.
Menurut saya, Fetch API adalah pilihan yang lebih baik untuk menangani permintaan asinkron dalam proyek kontemporer dan ingin memanfaatkan fitur JavaScript terbaru sambil mengurangi ketergantungan pada pustaka eksternal. Karena kejelasannya, pendekatan berbasis promise, dan fakta bahwa tidak memerlukan pustaka tambahan.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:

- Mengubah kode card data item agar mendukung AJAX GET dengan menambahkan fungsi baru get_product_json yang menerima parameter request. Lalu mengimpor serta menambahkan path ke urlpatterns di main/urls.py.
- Menambahkan kode agar mendukung AJAX POST dengan membuat fungsi baru create_product_ajax di main/views.py yang menerima parameter request, agar dapat menambahkan item baru tanpa harus me-reload page.
- Melakukan perintah py manage.py collectstatic agar file static dari setiap aplikasi dalam suatu folder yang dapat dengan mudah disajikan pada produksi.
- Melakukan add-commit-push ke GitHub.
- Melakukan deployment ke PaaS PBP Fasilkom UI