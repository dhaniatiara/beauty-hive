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
![Bagan](https://s3-alpha-sig.figma.com/img/d77a/1be8/38b3c6aa096db78bf966ad818c505c7e?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=hXbJULU9QOIr-EL6xtr5EQYhD6dNmXOQANnOTBROC7k4tVJ-rnF88bTZpSeH0wqUhPCgpmLTMeN0ClEq-u9g02CSyTtYoYLvMzYoIeiz4a2j5G8m1gJh8IOYV-snJbAlP65RI27T4JsI7Jod9Ob8wmyisFaD~fILqjdjOOLTaLAoHz7~mDVixRlPwDx3bl7aatbeI2ChlzE2E0f6GzBQ97Q-VAa9sk~jgG6kiByrrghxcEAI8UzbSrWbclTk8MXwBcTj3ha~8ZgYyGKrRgZc9w~fOVmIrDoZFkyi9-glYu0d34M5x0r6URQKwjgou-bEsDwCTBFX4waDW3O20w0HmQ__)
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

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Screenshot hasil akses URL pada Postman
![XML](https://s3-alpha-sig.figma.com/img/22e1/7cff/4d6f5bc714ca1e1a199c44469ef47769?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=FF8UNMy9iqzcp233qbC3GQltIAOkeMVhjFwWJd1s5Qd66K-9paiDrL~8b2DpwoSaSlqWKdeF-qo~H6Wf32yLGPk~2dfcpIxIcpxH2vdgd8xMHeOCTrGonaOTNPYLG9eGnfvbxWNgtftgt8rm9Ri00ospvHMiAPsxtRrbIrWt1CbzBy50uuuIse-QFM3BQPtzmRQKQAvQfJXKQ-C9z3TKRc35QlGPAtalY7i3lhou0xYJBFo0vPEPwQDOvD-47NN9qbZKeHdN4Wa1YgdWNBz1N1ySvGsGMJ1TnUUks-Jw1XyZ70Ftk943kyqJcZDACdmubrJ8M9mEuRg4kzHVnA2uiA__)
![JSON](https://s3-alpha-sig.figma.com/img/f86f/f59f/08da73a36ea6dfb04cb97f9e293babaa?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=iKTeKUSC~DMQ7XzlRHe~vVjMgTLJk6sM82cBmZb2uetVOS~R6Tj5Abs8-horjTBW9twCYVLkb5YiRHWsibF4YQi09BTcE7NJFjtul6zL5xG8B7YUJedZGbMuziAkttdYJMzs1Xjsl0WSjjdNLuj7W4mUlbKBwbUlQIWt8g6j5x1OhXuWbMdFMJ8QAwF4edhvYkDULGvP5n-Jt2zu7Os0vwN7EyT-9ChQDMu3OluLD6YSvl4Nce3Da1LpiiRIr3eEkkCCiAJayHDMSFFlNM5sKkjmUyXWnYdfY88FyUAaluubbWd6p8Nojm9DsEgJfZ7aH6E5yzDoqwcmpq0ToQzizw__)
![XML_ID](https://s3-alpha-sig.figma.com/img/c29d/9548/0ec0d0d0c141d374695d41b913a57675?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=h9RQ7565joZ~lzembMHs0PbXN0sqIYypq1I3C~vnpIIDnObAGAzqZoF50U1zr2JIQ-23cN3WcB0zNfhpL65lIHMLoLqzbgO4La~cY0Qnvyvu8cWr7qwTuSvNy9KImwKk2C~yaA-N~Rf2MgzvbtZut3IZsHFNbzZrIYnAxDFCz~FT8IH~OskTY9xte7WsUKMY-0UR2SAgsjtpjxxUE6Lyr8Bo59EJA5KLYe~8nkqD3rVsl3iWter86-KjZpB7rSqHwnfC0DSFa8an4eDgoCqESFWQqJ4WQRgglBsgUrIeuQ8ZFgDWQPNbDxW0RZYvt1NA5jCoKysVxWkqHjNBn2G~aw__)
![JSON_ID](https://s3-alpha-sig.figma.com/img/1802/80dc/66579dd65ff9b0d6c78512475cc3b07b?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=OAdQxeuWvjm6qYm1wjBFlI5RlN2FtbUSzwaV41ewG43TuxGnJTFl24SQe3LjId8kvXrjTHXZtOuMZKUNCqrRkvTzXtBP7tjMoe8vxJyKQxrPiNrOoHD-NRjnW5UkPy14GI6FOcl6P7NscAcbem2AHaHemK8t1Uq2KRIKbzyYNC-7oC0L5-GiVjFju8X19YvAPh~jyPypPKqhaYJDv4jbYV5Dm5MzlFiXJKok6q~fuGH77~EMuQDlUA-uM8M--QAn5f0wCH3gASAY0LIP2OAlXdE1ULvLcbSuqT7c1XRjQmrOIFWRZjb7VFw91zVUc~fTIlLWsL9ro7gATzxzZahRVw__)
