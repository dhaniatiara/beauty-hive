# Beauty Hive App

Nama: Dhania Tiaraputri Herdiani

NPM: 2306165881

Kelas: PBP B

## Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
Pertama, saya membuat direktori baru dan repositori baru di github saya dengan nama Beauty HIve karena tema dari aplikasi saya adalah e-commerce yang menjual makeup. Setelah itu saya menghubungkan direktori lokal tersebut dengan repositori saya dengan cara `git branch -M main` kemudian `git remote add origin https://github.com/dhaniatiara/beauty-hive.git` 

Kemudian, saya setup Django nya dengan mengikuti Tutorial 0 mulai dari menjalankan virtual environment dan menyiapkan dependencies terlebih dahulu, kemudian memodivikasi beberapa files seperti `settings.py`. Setelah itu saya membuat `.gitignore`. Setelah itu, saya lanjut membuat aplikasi Django, membuat routing, dan persiapan lainnya yang dijelaskan di Tutorial 1. 

Setelah itu, saya lanjut ke PWS (Pacil Web Service) untuk membuat project baru. Lalu saya memodifikasi lagi `setting.py` dengan menambahkan URL deployment PWS saya yaitu `dhania-tiaraputri-beautyhive.pbp.cs.ui.ac.id` (updated url per 18 Sept 2024, from beautyhiveshop to beautyhive setelah tugas 3 karena pws trouble) dan lanjut menjalani langkah langkah deployment PWS seperti di Tutorial.

Setelah melakukan hal hal tersebut, saya lanjut ke repo saya dan membuat model pada aplikasi main dengan nama Product yang di dalamnya ada atribut `name` dengan tipe data `CharField`, `description` dengan tipe data `TextField`, `price` dengan tipe data `IntergerField`, `shade` dengan tipe data `TextField`, dan size dengan tipe data `TextField`.

Setelah itu, saya lanjut membuat fungsi di `views.py` yang sudah saya sesuaikan dengan website saya. Karena memutuskan untuk membuat e-commerce yang menjual makeup, oleh karena itu, di `views.py` saya membuat variabel 'name' dengan nama produk, kemudian 'price' dengan harga produk yang ditampilkan,  'desc' dengan dengan informasi barang yang saya jual dan saya juga menambahkan 'size' yang merupakan informasi ukuran produk yang saya tampilkan di web. 

Setelah itu saya memodifikasi main.html saya dengan design yang sebelumnya sudah saya buat di Figma. Saya menaruh judul, subjudul, image, dan box yang berisi deskripsi produk. Deskripsi produknya menampilkan data di views.py dan saya juga menampilkan button 'Buy' yang belum berfungsi. 

Setelah saya memodifikasi main.html saya, saya melakukan push ke PWS dengan mengikuti perintah yang ada di Tutorial 0 yaitu `git push pws main:master` Setelah saya berhasil push akhir dari website saya, web saya akhirnya bisa di akses di internet dengan link `http://dhania-tiaraputri-beautyhive.pbp.cs.ui.ac.id/` (new url per 18 Sept 2024)

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab:
![Bagan](https://drive.google.com/uc?export=view&id=1vB-ScwySa6Ldu-i79i8iTL3z9GE3qSF2)
a. Pertama, ada request dari client yang mengirimkan HTTP request ke server Django

b. Server Django akan menerima request dan mencocokkan URL yang diminta dengan pola yang ada di file urls.py. urls.py bertanggung jawab untuk mengatur rute URL yang terakit dengan aplikasi main. 

c. views.py akan memproses request dan akan melakukan beberapa tindakan seperti mengambil data dari database melalui models.py, memproses data. Setelah tindakan tersebut selesai, views.py akan menentukan jenis respon yang akan dikirim ke client, biasanya menggunakan template HTML.

d. models.py merupakan lapisan interaksi dengan database. Saat views.py membutuhkan data, models.py akan digunakan untuk mengambil, menyimpan, atau memperbarui data di database. 

e. HTML : Setelah views.py mendapatkan data yang diperlukan, data tersebut akan dikirim ke berkas HTML yang merupakan template. Berkas html ini akan membentuk tampilan akhir yang akan dilihat oleh user. 

f. Respon: Setelah template terbentuk, Django akan mengirimkan html yang sudah diproses sebagai respon kembali ke client. Client kemudian akan menamoilkan konten ke user.

Kaitan antar semua:
- urls.py : Mengarahkan permintaan ke fungsi di views.py.
- views.py: Menangani logika aplikasi, memanggil models.py untuk data, dan mengirim data ke template.
- models.py: Berinteraksi dengan database untuk mengelola data.
- Berkas HTML: Menampilkan data yang diterima dari views.py dalam format yang user-friendly.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Jawab:
Git merupakan tool yang digunakan untuk manajemen source code. Git digunakan untuk track perubahan dari sebuah source code, sehingga, adanya git membuat berbagai developer dapat bekerja sama dalam non-linear development melalui ribuan branch paralel.

Fungsi dari git antara lain adalah:
- Adanya riwayat perubahan lengkap. Di git terdapat version control system yang dapat melacak setiap perubahan yang dilakukan pada setiap file. Git dapat menunjukkan apa perubahan dilakukan, siapa, kapan, dan mengapa. Adanya riwayat perubahan ini berguna untuk menemukan penyebab bug pada pengembangan perangkat lunak. 
- Git juga memberi fitur "Branching dan Merging". Branching digunakan disaat developer ingin mengerjakan berbagai bagian proyek secara bersamaan. Nantinya, developer dapat "merge" atau menggabungkan bagian yang terpisah tersebut. Branching dan merging akan memastikan bahwa perubahan yang dilakukan di setiap bagian tidak bertentangan satu sama lain.
- Git dapat mempercepat waktu rilis suatu perangkat lunak. Hal ini dikarenakan adanya git dapat membuat distributed development, dimana memungkinkan bagi developer untuk  mengerjakan dan merilis pembaruan kecil secara lebih sering, sehingga waktu rilis menjadi lebih cepat. 
- Komunikasi dan kolaborasi.


### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Jawab:
Django merupakan salah satu framework yang terkenal untuk pengembangan perangkat lunak. Django menggunakan bahasa Python. Menurut saya, framework Django digunakan untuk permulaan pelajaran ini karena Django menawarkan simplisitas, flesibilitas, reliability, dan scalability. Yang membedakan Django  dengan framework lainnya adalah Django memiliki syntax yang simple, memiliki web sever nya sendiri,  secure, cocok dengan segala proyek platform, memiliki ORM (Object Relational Mapper), library HTTP middleware support, dan unit test python framework.

### 5. Mengapa model pada Django disebut sebagai ORM?

Jawab:
ORM merupakan singkatan dari Object-relational mapper. ORM membuat kita dapat berinteraksi dengan database seperti saat kita berinteraksi dengan SQL. Model yang kita buat di Django dapat kita modify, delete, menambah, dan query objects. ORM akan digunakan untuk berinteraksi dengan database dan sebagai jembatan antara database dan kode yang kita bikin. ORM membuat sebuah object-oriented layer antara database ddengan object-oriented programming languages tanpa harus menulis SQL queries langsung.

## Tugas 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawab: Data delivery penting dalam pengimplementasian platform karena dengan dengan data delivery kita bisa menargetkan, memodelkan, dan optimisasi pengunjung di platform kita ataupun dari platform lainnya di perangkat lain. Dengan kata lain, data delivery berpengaruh besar dalam meningkatkan performa platform kita. Beberapa aspek yang terpengaruh dengan adanya data delivery adalah skalabilitas data yang masuk, keamanan data, user experience, akurasi data, dan membantu kemudahan dalam analisis data. 


### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jawab: Menurut saya, XML dan JSON memiliki kelebihannya masing masing dan dapat saling dibutuhkan di situasi tertentu. Contohnya adalah, disaat kita ingin menyimpan berbagai tipe data dengan banyak variables, maka sebaiknya gunakan XML. Karena, XML lebih baik dalam mengecek error pada data yang kompleks secara efisien dibandingkan JSON. Kemudian, kita menggunakan JSON untuk APIs, aplikasi mobile, storage data, karena JSON dirancang untuk interchange data dan memnawarkan format yang lebih simple dan pasti. 

Ada beberapa alasan lain dari mengapa JSON cenderung lebih baik dan lebih populer dibandingkan XML adalah:
- JSON lebih mudah dibaca oleh manusia karena tidak menggunakan tags seperti pada XML. 
- JSON memiliki file size yang lebih kecil dibandingkan XML
- JSON memiliki transimisi data yang lebih cepat dibandingkan XML
- JSON sangat flekksibel sehingga bisa digunakan untuk hampir semua bahasa komputer
- Kemudahan JSON dalam parsing data
- Data modeling yang lebih komprehensif karena struktur JSON yang memfasilitasi enkoding dari data hierarchical

Karena hal hal inilah JSON lebih populer untuk dipakai. 

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawab: method is_valid() adalah method yang digunakan untuk memvalidasi setiap field di form. Selain itu, method is_valid ini juga dibutuhkan agar kita bisa melihat error yang ada pada form Django kita. Terutama disaat adanya data eksternal yang akan diinput ke platform kita. Apabila tidak ada is_valid maka bisa saja data yang masuk itu tidak aman dan memiliki format yang salah. Selain itu, is_valid juga membantu membuat workflow yang lebih terstruktur.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawab: CSRF token di buat oleh Django setiap kali seorang user sedang mengunjungi website kita. Token pada CSRF mengandung forms atau request yang dikirim oleh user dan kemudian di check oleh server apakah request datang dari user yang terpercaya dan bukan dari sumber yang membahayakan. Jadi, CSRF token penting untuk dibuat saat membuat form di Django, karena dapat menghindari dari serangan siber yang membahayakan. Apabila kita tidak menambahkan csrf_token pada form Django, maka disaat adanya request dari user seperti submisi form, server website tidak akan menjalankan action yang di request oleh user.

Tidak adanya csrf_token sering dimanfaatkan oleh penyerang. Karena bisa saja ada penyerang yang melakukan berbagai request atau tindakan yang seolah-olah tindakan tersebut berasal dari user aslinya, padahal sebenarnya user aslinya tidak melakukan tindakan tersebut. Beberapa tindakan yang bisa dilakukan oleh penyerang mentransfer dana, mengubah detail akun, atau mengubah pengaturan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya memulai dengan mengimplementasi Skeleton sebagai kerangka Views. Disini, saya membuat `base.html` yang berisi css untuk design komponen website saya. Kemudian saya mengubah `settings.py` dan memodifikasi `main.html` saya yang disesuaikan dengan `base.html`. 

Setelah itu saya delete `db.sqlite` saya, memodifikasi file `models.py` dengan menambah `import uuid` kemudian saya migrate models saya yang telah saya buat di tugas sebelumnya.

Setelah berhasil migrate models saya, saya mulai membuat form dengan membuat berkas dinamakan `forms.py` dengan nama model `Product` dan fields nya yang berisi `name`, `price`, `description`, `shade`, `size`. Kemudian saya memodifikasi berkas `views.py` dengan `import django.shortcuts`, `ProductForm`, dan `Product`. Setelah itu saya menambah fungsi baru yaitu `create_product_ entry` dengan form `ProductForm` dan return nya yang sama seperti tutorial. 

Lalu, saya ke `views.py` dan memodifikasi fungsi `show_main` dengan menulis `mood_entries = Product.objects.all()` dan di dalam context menambah `mood_entries: mood_entries`. Langkah ini dilakukan untuk mengambil seluruh objek di `Product` yang tersimpan pada database.

Saya kemudian modifikasi `urls.py` dengan import `create_product_entry`. Lalu menambahkan path URL ke dalam variabel urlpatterns seperti `path('create-product-entry', create_product_entry, name='create_product_entry')`

Lalu saya membuat berkas `create_product_entry.html` pada direktori main/templates dengan isi kode untuk mengisi data produk baru.

Kemudian saya buka `main.html` dan menambahkan kode yang akan menampilkan kumpulan hasil data input di dalam desc-box.

Disini aplikasi saya sudah ada forms untuk menambah product baru dan hasilnya akan ditampilkan di home page. 

Untuk mengembalikan data dalam bentuk `xml`, saya buka views.py untuk import `HTTPResponse` dan `Serializer`. Kemudian saya menambahkan fungsi baru dengan nama `show_xml` yang akan meyimpan hasil query dari seluruh data yang ada pada `Product`.  Dan saya juga menambahkan return function yang berupa HttpResponse yang memiliki serilizer yang berfungsi untuk translate objek model menjadi format xml. Kemudian saya import fungsi `show_xml` pada `urls.py` dan menambahkan path url. 

Untuk mengembalikan data dalam bentuk `JSON`, saya melakukan alur yang sama seperti sebelumnya saat setting xml, namun bedanya disini fungsinya bernama `show_json` dan return type nya `content_type=“application/json”`. Kemudian saya menambahkan imoort pada `urls.py` dan menambahkan path url di url patterns.

Untuk mengembalikan data berdasarkan `ID` dalam bentuk `XML` dan `JSON`, saya memasuki 2 fungsi baru yang menerima parameter `request` dan `ID`  di `views.py`. Isi dari fungsi nya seperti yang ada pada tutorial. Kemudian saya menambah import pada `urls.py` dan menambahkan path url di url patterns.

Sehingga, pada akhirnya ada 5 fungsi baru di views.py yaitu fungsi `create_product_entry`, `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id`, dan path url baru di urlpatterns.

### Screenshot hasil akses URL pada Postman

XML:

![XML](https://drive.google.com/uc?export=view&id=11dMrsU0U-ORlXDoRCM89jwleQyuJEbp2)


JSON:

![JSON](https://drive.google.com/uc?export=view&id=1pUNiEkU8W3hOo9E8WPMnFjgAR07IZsp3)


XML ID:

![XML_ID](https://drive.google.com/uc?export=view&id=1QeOYSwnmIr732N2L583WqVAYjd8fGSEu)


JSON ID:

![JSON_ID](https://drive.google.com/uc?export=view&id=1StSehrnB9a2M2uKHlI-uG7P5Bf78S8eU)

## Tugas 4

### Apa perbedaan antara HttpResponseRedirect() dan redirect()

Jawab: HttpResponseRedirect() hanya mengambil single argumen yaitu URL. Sedangkan redirect() pada akhirnya akan return HttpResponseRedirect, dan dapat menerima model, view, URL sebagai argumen "to". 

Redirect sedikit lebih fleksibel dalam hal ke mana ia bisa "redirect" user.

### Jelaskan cara kerja penghubungan model Product dengan User!

- Adanya ForeignKey. ForeignKey ini akan kita taruh di potongan kode pada model kita sehingga akan menghubungan model `Product` dengan `User`. Selain itu, kode akan dilengkapi dengan `on_delete=models.CASCADE` yang artinya dalah jika User dihapus, maka semua produk yang dimiliki pengguna itu juga akan dihapus. Adanya ForeignKey ini dapat menghubungkan setiap produk ke satu user dan satu pengguna bisa memiliki banyak produk (hubungan many-to-one)
- Menetapkan user yang membuat entri produk baru dengan mengisi field `user` di model `Product` dengan pengguna yang sedang login. Hal ini dilakukan dengan modifikasi fungsi `create_product_entry`. user yang sedang log in bisa membuat entry baru dengan form yang sudah dibuat. Adanya `commit=False` akan menambahkan informasi user sebelum objek disimpan ke database. Hal ini dilakukan agar kita bisa memodifikasi objek terlebih dahulu sebelum disimpan ke database. 
- Pada fungsi `show_main` akan akan ada `product_entries = Product.objects.filter(user=request.user)`, potongan kode ini berfungsi untuk menampilkan objek pada `Product` yang berhubungan dengan user yang sedang logged in. 

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Jawab: Authentication akan memverifikasi bahwa pengguna adalah benar - benar siapa yang yang di klaim. Authentication umumnya memasukkan informasi kredensial seperti username dan password. Sedangkan authorization menentukan apa yang diizinkan untuk dilakukan oleh pengguna yang telah di authenticate. 

Django mengimplementasikan konsep authentication dengan cara menggunakan sistem built-in untuk login, logout, dan register. DJango akan memverifikasi kredensial (username dan password) dan membandingkannya dengan data yang ada di database. Apabila cocok, user akan diberikan session ID untuk melacak status login mereka. 

Setelah itu, pada proses authorization, Django akan menentukan apa yang dapat dilakukan oleh user tersebut berdasarkan dengan izin yang sudah ditetapkan diawal, contohnya `@login_required` 

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan Session ID yang disimpan sebagai cookie. Session merupakan suatu token yang mengenali session unik pada aplikasi web tertentu. Session ID yang disimpan di cookies akan dihubungkan dengan data session yang disimpan di server. Akan selalu request dan setiap request berikutnya yang dilakukan oleh pengguna, cookies akan dikirim bersama request http. Django akan memerika cookies untuk mendapatkan session ID kemudian mencari data session di server. Apabila session ID valid dan sesuai dengan data di server, Django akan tahu bahwa pengguna tersebut masih autheticated. 

Beberapa kegunaan lain dari cookies adalah cookies menyimpan preferesni pengguna seperti bahasa pilihan, tema pilihan, dan lain - lain. Selain itu, cookies juga bisa digunakan untuk melacak aktivitas pengguna sehingga bisa dimanfaatkan untuk analitik dan pengelolaan iklan. 

Namun, tidak semua cookies aman digunakan. Cookies yang kurang aman digunakan diantaranay adalah third-party cookies dan cookies yang tidak dienkripsi dan dikirimkan melalui koneksi http. Ada beberapa cookie yang biasanya dimanfaatkan sehingga seorang hacker bisa impersonate cookie sehingga mereka bisa akses akun user karena cookies tidak menyimpen password. Kejadian ini juga bisa mengarahkan kita kepada beberapa masalahh siber lainnya seperti cross-site scripting dan cross site request forgery.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab: 

- Membuat fungsi dan form registrasi dengan memodifikasi `views.py` dan import formulir bawaan dalam aplikasi web. Kemudian menambahkan fungsi `register`.
- Membuat berkas `register.html` untuk menampilkan laman register dan menambahkan path url di `urlpatterns`
- Setelah itu, saya lanjut membuat fungsi login dengan proses yang sama yaitu import fungsi bawaan django yaitu import `authenticate`, `login`, dan `AuthenticationForm` pada `views.py` . Kemudian, menambahkan fungsi `login_user`, membuat berkas `login.html` untuk membuat template laman untuk login dan melakukan url path untuk laman tersebut. 
- Saya lanjut dengan membuat fungsi logout dengan import `logout` pada views.py dan menambahkan fungsi `view.py` untuk melakukan mekanisme logout. Kemudian, saya memodifikasi berkas `main.html` untuk menambahkan hyperlink tag untuk logout. Lalu, saya menambahkan path url di url patterns untuk logout. 
- Setelah berhasil membuat form dan fungsi register, login, dan logout, saya lanjut merestriksi akses halaman main dengan import `login_required`. Saya juga menaruh `@login_required(login_url='/login')` agar halaman main hanya dapat diakses oleh pengguna yang sudah login. 
- Kemudian, saya lanjut setup agar bisa melihat data dari cookies. Hal ini dilakukan dengan menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py`. Saya juga memodifikasi fungsi `login_user` pada blok `if form.is_valid()` yang berfungsi untuk melakukan login terlebih dahulu, untuk membuat respose, dan membuat cookie last_login menambahkan ke response. Kemudian saya menambahkan variabel `'last_login': request.COOKIES['last_login']` pada context agar kita bisa melihat informasi cookie last_login pada web. Kemudian saya memodifikasi fungsi `logout_user` untuk menghapus cookie `last_login` saat pengguna melakukan logout. Saya kemudian menambahkan potongan kode `last_login` pada `main.html` untuk menampilkan informasi cookies di aplikasi web saya. 

- Untuk menghubungkan Model `Product` deengan `User`, saya mulai dengan import `User` pada `models.py` Kemudian, pada model `Product` yang sudah saya buat, saya menambahkan potongan kode seperti `user = models.ForeignKey(User, on_delete=models.CASCADE)` untuk menghubungkan satu product dengan satu user melalui sebuah relationship, dimana sebuah product pasti terasosiasikan dengan seorang user. 
- Saya kemudian membuka `views.py` dan memodifikasi `create_product_entry` seperti yang ada pada tutorial. Perubahan ini dilakukan untuk untuk membantu proses penyimpanan objek pada form ke user yang logged in. 
- Kemudian saya ubah value `product_entries` agar aplikasi hanya menambilkan objek `Product` yang terasosiakan dengan pengguna yang sedang login dan modifikasi pada `context` yaitu `'name': request.user.username,` untuk menampilakn nama user yang sedang logged in. 
- Setelah itu, saya `makemigrations` dan `migrate`sesuai dengan langkah yang ada pada tutorial. 
- Terakhir, saya buka `settings.py` untuk `import os` dan mengubah variabel DEBUG menjadi `PRODUCTION = os.getenv("PRODUCTION", False)` `DEBUG = not PRODUCTION`

## Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jawab: Dalam web developmentm terdapat istilah yang dinamakan CSS specificity. Terdapat beberapa cara untuk mengkalkulasi CSS specificity yaitu menggunakan selektor dan menggunakan decimal number system. Bagi CSS selector, urutan prioritasnya adalah (Prioritas tertinggi-rendah):

1. `!important` rule. `!important` Rule akan mengesampingkan aturan lainnya termasuk inline style. 
2. Inline Style (Atribut `style`) Style yang digunakan langsung pada elemen HTML menggunakana tribut `style` memiliki prioritas lebih tinggi daripada semua selector CSS.
3. ID Selector (#) ID ini diterapkan pada elemen yang memiliki atribut `id`
4. Pseudo-Class Selector (`:`). Selector ini diaplikasikan pada elemen dalam kondisi spesifik seperti `:hover`, `:active`, `:nth-child()`
5. Attribute Selector (`[]`) Selector ini berdasarkan atribut elemen HTML, seperti `[type="text"]` atau `[href]`
6. Class selector (`.`). Class selector merupakan elemen yang memiliki atribut `class`. Class selector memiliki prioritas yang lebih tinggi daripada selector elemen
7. Element Type Selector: Elemen ini mengacu pada tag HTML seperti `div`, `p`, `h1`, dan lain lain. 
8. Universal Selector (`*`)

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Design yang responsive telah menjadi konsep yang penting dalam pengembangan aplikasi web karena alasan - alasan berikut:

- User Experience yang Baik. User experience yang baik sangat penting, terutama jika aplikasi web digunakan sebagai alat pemasaran. Dengan desain yang responsif dan tampilan yang optimal di setiap perangkat, pengalaman brand akan meningkat, yang pada akhirnya meningkatkan reputasi dan daya tarik.
- Low Maintenance. Dulu, kita harus membuat versi berbeda untuk setiap perangkat. Dengan desain responsif, satu situs dapat menyesuaikan tampilannya di semua perangkat, sehingga lebih mudah dikelola.
- Loading time yang lebih cepat. 53% pengguna meninggalkan situs jika memuat lebih dari tiga detik. Desain responsif hanya memuat sumber daya yang diperlukan, membuat situs lebih cepat tanpa perlu pengalihan ke versi lain.
- Beragamnya devices di masa kini. Zaman sekarang, aplikasi web sering di akses dari berbagai perangkat mulai dari handphone, laptop, tv, dan lain - lain. Oleh karena itu, design aplikasi web yang responsive menjadi sangat penting agar pengguna menjadi lebih nyaman dalam mengakses suatu aplikasi web. 

Contoh aplikasi yang SUDA menerapkan responsive design: Tokopedia

Contoh aplikasi yang BELUM menerapkan responsive design: SIAKng

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!


Berikut adalah penjelasan dan contohnya masing - masing:

- Padding adalah ruang antara konten dan border, yang merupakan komponen berikutnya dari box. Kita bisa mengatur padding di setiap sisi. Contoh implementasinya adalah:

```
div {
    padding: 20px; /* Semua sisi akan diberi padding 20px */
    padding-top: 10px; /* Padding hanya pada bagian atas */
    padding-right: 15px; /* Padding hanya pada bagian kanan */
    padding-bottom: 10px; /* Padding hanya pada bagian bawah */
    padding-left: 15px; /* Padding hanya pada bagian kiri */
}
```

- Border adalah garis yang terlihat atau tidak terlihat di sekitar tepi box. Kita bisa mengatur ketebalannya, jenis border, dan warna border
```
div {
    border: 2px solid black; /* Border 2px tebal, jenis solid, warna hitam */
    border-top: 3px dashed red; /* Border atas saja dengan garis putus-putus merah */
}
```

- Margin adalah ruang luar di sekitar box yang mengatur jarak antara elemen dengan elemen lainnya. 
```
div {
    margin: 20px; /* Semua sisi diberi margin 20px */
    margin-top: 10px; /* Margin hanya di bagian atas */
    margin-right: 15px; /* Margin hanya di bagian kanan */
    margin-bottom: 10px; /* Margin hanya di bagian bawah */
    margin-left: 15px; /* Margin hanya di bagian kiri */
}
```

Untuk implementasi ketiga nya dalam satu class:

```
<style>
        .box {
            margin: 30px;            
            padding: 20px;            
            border: 5px solid blue;   
            background-color: lightgray; 
        }
    </style>
```

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

CSS Flexbox adalah tata letak satu dimensi. Ini berguna untuk mengalokasikan dan menyelaraskan ruang di antara item dalam sebuah grid container. Flexbox bekerja dengan berbagai jenis perangkat tampilan dan ukuran layar. Tata letak Flex memudahkan desain dan pembuatan halaman web responsif tanpa menggunakan banyak properti float dan position dalam kode CSS.

Sedangkan, CSS Grid Layout adalah sistem tata letak berbasis grid dua dimensi dengan baris dan kolom. Ini berguna untuk membuat tata letak yang lebih kompleks dan terorganisir.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama, saya menambahkan tailwind ke aplikasi dengan memodifikasi file `base.html` dengan menambahkan tag `<meta name="viewport">` dan `<script src="https://cdn.tailwindcss.com">`
- Setelah itu, saya menambahkan fitur `Edit Product` pada aplikasi. Saya mulai dengan modifikasi file `views.py` dan membuat fungsi baru bernama `edit_product` yang menerima parameter `request` dan `id`. Setelah itu, saya menambahkan import `reverse` dan `HttpResponseRedirect`.
- Kemudian, saya membuat file html baru yang dinamakan `edit_product.html`. Isi dari file ini dapat mengedit inputan dari form sebelumnya dengan struktur design / tampilan yang sama dengan create_product_entryl.html. Setelah itu saya menambahkan path url pada `urls.py`.
- Setelah itu, saya menambahkan fitur hapus product pada aplikasi. Dengan cara menambahkan fungsi baru pada `views.py` seperti yang ada di tutorial  dan melakukan path url yang baru. 
- Saya kemudian menambahkan navigation bar pada aplikasi dengan membuat file html baru dinamakan `navbar.html` dengan design yg backgroundnya putih dan page titles "Home, Desctiption, Categories", "weclome {{nama}}", dan log out button.
- Setelah membuat navbar.html, edit product, dan delete product, saya konfigurasi static files pada aplikasi dengan memodifikasi `settings.py` dan menambahkan `'whitenoise.middleware.WhiteNoiseMiddleware'` pada bagian MIDDLEWARE. Saya juga mengubah bagian `STATIC_ROOT`, `TATICFILES_DIRS`, dan `STATIC_URL`.
- Saya juga menambahkan `global.css` pada folder static/css yang berisi design css saya. Kemudian saya mengubah `base.html` agar style `global.css` dapat digunakan di Django. 
- Lalu saya memodifikasi file `login.html`, `register.html`, `create_product_entry` menjadi styling tailwind. Untuk `login.html` saya menampilkan static image bernama login-photo.png yang akan ditampilkan sebelah login entry.
- Saya juga memb uat file `card_mood.html` yang akan menampilkan card baru untuk setiap product entry baru. Dan di dalam nya ada button untuk edit product dan delete product.
- Setelah menyelesaikan segala berkas html di template, saya akhirnya memodifikasi `main.html` agar segala berkas html lainnya dapat terintegrasi dengan baik. 