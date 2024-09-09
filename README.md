1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat direktori baru dan repositori baru di github saya. Setelah itu saya menghubungkan direktori lokal tersebut dengan repositori saya. Kemudian, saya setup Django nya dengan mengikuti Tutorial 0 mulai dari membuat environment terlebih dahulu, kemudian memodivikasi beberapa files seperti settings.py, membuat aplikasi bernama main, dan membuat routing. Semua ini dijelaskan di Tutorial 0.

Setelah melakukan hal hal tersebut, saya lanjut dengan membuat model pada aplikasi main dengan nama Product yang di dalamnya ada name, price, description. Name dengan tipe data string, price dengan tipe data Integer, dan description dengan tipe data string.

Setelah itu, saya membuat fungsi di views.py yang sudah saya sesuaikan dengan website saya, yaitu dengan membuat mengisi name dengan product name, kemudian price dengan harga, dan description dengan informasi barang yang saya jual. Saya juga menambahkan size dari barang yang saya tampilkan di website. 

Setelah itu saya memodifikasi main.html saya dengan design yang sebelumnya sudah saya buat di Figma. Saya menaruh judul, subjudul, image, dan box yang berisi deskripsi produk. Deskripsi produknya menampilkan data di views.py dan saya juga menambahkan button buy yang belum berfungsi. 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.



3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git merupakan version control system yang digunakan untuk track perubahan pada data di komputer. Git dibuat untuk source code management pada pengembangan perangkat lunak. 

Bagi developer, git berfungsi agar setiap developer memiliki copy dari kode mereka masing masing di perangkat lokal masing - masing. Kemudian, git memberikan kesempatan bagi beberapa developers untuk track perubahan yang ada. Git juga memberi kesempatan pada developer untuk bekerja sama dan git juga membuat adanya komunikasi antara developer developer nya dengan mudah. Git juga meng-support development yang non-linear melalui ribuan branch paralel.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django merupakan salah satu framework yang terkenal untuk pengembangan perangkat lunak. Django menggunakan bahasa Python. Menurut saya, framework Django digunakan untuk permulaan pelajaran ini karena Django menawarkan simplisitas, flesibilitas, reliability, dan scalability. Yang membedakan Django  dengan framework lainnya adalah Django memiliki syntax yang simple, memiliki web sever nya sendiri,  secure, cocok dengan segala proyek platform, memiliki ORM (Object Relational Mapper), library HTTP middleware support, dan unit test python framework.

5. Mengapa model pada Django disebut sebagai ORM?
ORM merupakan singkatan dari Object-relational mapper. ORM membuat kita dapat berinteraksi dengan database seperti saat kita berinteraksi dengan SQL. Model yang kita buat di Django dapat kita modify, delete, menambah, dan query objects. ORM akan digunakan untuk berinteraksi dengan database dan sebagai jembatan antara database dan kode yang kita bikin. ORM membuat sebuah object-oriented layer antara database ddengan object-oriented programming languages tanpa harus menulis SQL queries.



Referensi:
https://www.doprax.com/tutorial/django-tutorial-for-beginners-part-6/#:~:text=What%20is%20Django%20ORM,that%20you%20would%20with%20SQL.
https://djangostars.com/blog/why-we-use-django-framework/#:~:text=Django%20is%20a%20fast%20and,otherwise%20incur%20additional%20costs%20later.
