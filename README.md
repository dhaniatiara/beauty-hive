## Beauty Hive App

Nama: Dhania Tiaraputri Herdiani

NPM: 2306165881

Kelas: PBP B

### Tugas 1

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
Pertama, saya membuat direktori baru dan repositori baru di github saya dengan nama Beauty HIve karena tema dari aplikasi saya adalah e-commerce yang menjual makeup. Setelah itu saya menghubungkan direktori lokal tersebut dengan repositori saya dengan cara `git branch -M main` kemudian `git remote add origin https://github.com/dhaniatiara/beauty-hive.git` 

Kemudian, saya setup Django nya dengan mengikuti Tutorial 0 mulai dari menjalankan virtual environment dan menyiapkan dependencies terlebih dahulu, kemudian memodivikasi beberapa files seperti `settings.py`. Setelah itu saya membuat `.gitignore`. Setelah itu, saya lanjut membuat aplikasi Django, membuat routing, dan persiapan lainnya yang dijelaskan di Tutorial 1. 

Setelah itu, saya lanjut ke PWS (Pacil Web Service) untuk membuat project baru. Lalu saya memodifikasi lagi `setting.py` dengan menambahkan URL deployment PWS saya yaitu `dhania-tiaraputri-beautyhiveshop.pbp.cs.ui.ac.id` dan lanjut menjalani langkah langkah deployment PWS seperti di Tutorial.

Setelah melakukan hal hal tersebut, saya lanjut ke repo saya dan membuat model pada aplikasi main dengan nama Product yang di dalamnya ada atribut `name` dengan tipe data `CharField`, `description` dengan tipe data `TextField`, `price` dengan tipe data `IntergerField`, `shade` dengan tipe data `TextField`, dan size dengan tipe data `TextField`.

Setelah itu, saya lanjut membuat fungsi di `views.py` yang sudah saya sesuaikan dengan website saya. Karena memutuskan untuk membuat e-commerce yang menjual makeup, oleh karena itu, di `views.py` saya membuat variabel 'name' dengan nama produk, kemudian 'price' dengan harga produk yang ditampilkan,  'desc' dengan dengan informasi barang yang saya jual dan saya juga menambahkan 'size' yang merupakan informasi ukuran produk yang saya tampilkan di web. 

Setelah itu saya memodifikasi main.html saya dengan design yang sebelumnya sudah saya buat di Figma. Saya menaruh judul, subjudul, image, dan box yang berisi deskripsi produk. Deskripsi produknya menampilkan data di views.py dan saya juga menampilkan button 'Buy' yang belum berfungsi. 

Setelah saya memodifikasi main.html saya, saya melakukan push ke PWS dengan mengikuti perintah yang ada di Tutorial 0 yaitu `git push pws main:master` Setelah saya berhasil push akhir dari website saya, web saya akhirnya bisa di akses di internet dengan link `http://dhania-tiaraputri-beautyhiveshop.pbp.cs.ui.ac.id/`

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

### Tugas 2

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
