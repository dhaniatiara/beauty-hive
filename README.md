1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
Pertama, saya membuat direktori baru dan repositori baru di github saya. Setelah itu saya menghubungkan direktori lokal tersebut dengan repositori saya. Kemudian, saya setup Django nya dengan mengikuti Tutorial 0 mulai dari membuat environment dan menyipakan dependencies terlebih dahulu,  kemudian memodivikasi beberapa files seperti settings.py dan membuat git ignore. Setelah itu, saya lanjut membuat aplikasi Django, membuat routing, dan persiapan lainnya yang dijelaskan di Tutorial 1. 

Setelah melakukan hal hal tersebut, saya lanjut dengan membuat model pada aplikasi main dengan nama Product yang di dalamnya ada atribut name, price, description. Name dengan char field, price dengan integer field, description dengan text field, dan size dengan text field.

Setelah itu, saya lanjut membuat fungsi di views.py yang sudah saya sesuaikan dengan website saya. Saya memutuskan untuk membuat e-commerce yang menjual makeup, oleh karena itu, di views.py saya membuat variabel 'product' dengan nama produk, kemudian 'price' dengan harga produk yang ditampilkan,  'desc' dengan dengan informasi barang yang saya jual dan saya juga menambahkan 'size' yang merupakan informasi ukuran produk yang saya tampilkan di web. 

Setelah itu saya memodifikasi main.html saya dengan design yang sebelumnya sudah saya buat di Figma. Saya menaruh judul, subjudul, image, dan box yang berisi deskripsi produk. Deskripsi produknya menampilkan data di views.py dan saya juga menampilkan button 'Buy' yang belum berfungsi. 

Setelah saya memodifikasi main.html saya, saya melakukan deployment ini dengan PWS dengan mengikuti perintah yang ada di Tutorial 0. Setelah saya berhasil deploy, web saya akhirnya bisa di akses di internet dengan link http://dhania-tiaraputri-beautyhivestore.pbp.cs.ui.ac.id/

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab:
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

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawab:
Git merupakan tool yang digunakan untuk manajemen source code. Git digunakan untuk track perubahan dari sebuah source code, sehingga, adanya git membuat berbagai developer dapat bekerja sama dalam non-linear development melalui ribuan branch paralel.

Fungsi dari git antara lain adalah:
- Adanya riwayat perubahan lengkap. Di git terdapat version control system yang dapat melacak setiap perubahan yang dilakukan pada setiap file. Git dapat menunjukkan apa perubahan dilakukan, siapa, kapan, dan mengapa. Adanya riwayat perubahan ini berguna untuk menemukan penyebab bug pada pengembangan perangkat lunak. 
- Git juga memberi fitur "Branching dan Merging". Branching digunakan disaat developer ingin mengerjakan berbagai bagian proyek secara bersamaan. Nantinya, developer dapat "merge" atau menggabungkan bagian yang terpisah tersebut. Branching dan merging akan memastikan bahwa perubahan yang dilakukan di setiap bagian tidak bertentangan satu sama lain.
- Git dapat mempercepat waktu rilis suatu perangkat lunak. Hal ini dikarenakan adanya git dapat membuat distributed development, dimana memungkinkan bagi developer untuk  mengerjakan dan merilis pembaruan kecil secara lebih sering, sehingga waktu rilis menjadi lebih cepat. 
- Komunikasi dan kolaborasi.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Django merupakan salah satu framework yang terkenal untuk pengembangan perangkat lunak. Django menggunakan bahasa Python. Menurut saya, framework Django digunakan untuk permulaan pelajaran ini karena Django menawarkan simplisitas, flesibilitas, reliability, dan scalability. Yang membedakan Django  dengan framework lainnya adalah Django memiliki syntax yang simple, memiliki web sever nya sendiri,  secure, cocok dengan segala proyek platform, memiliki ORM (Object Relational Mapper), library HTTP middleware support, dan unit test python framework.

5. Mengapa model pada Django disebut sebagai ORM?
Jawab:
ORM merupakan singkatan dari Object-relational mapper. ORM membuat kita dapat berinteraksi dengan database seperti saat kita berinteraksi dengan SQL. Model yang kita buat di Django dapat kita modify, delete, menambah, dan query objects. ORM akan digunakan untuk berinteraksi dengan database dan sebagai jembatan antara database dan kode yang kita bikin. ORM membuat sebuah object-oriented layer antara database ddengan object-oriented programming languages tanpa harus menulis SQL queries langsung