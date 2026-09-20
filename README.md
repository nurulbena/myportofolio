Nama : Nurul Fikryati Bena

NPM : 2506534825

Kelas : PBP A

Angkatan : 2025

Deskripsi proyek 
Website portofolio pribadi berbasis Django yang menampilkan profil,skills, experience dan education saya sebagai mahasiswa Fasilkom UI

cara menjalankan
1. Aktifkan virtula env: "souce env/Scripts/activate"
2. jalankan server dengan "python manage.py runserver"
3. buka "https://127.0.0.1:8000/" di browser

### Tugas 1
1. saya menggunakan <section> untuk mengelompokkan konten yang ingin saya buat agar lebih rapi dan jelas jika dibaca (profile, skills, experience, education) karena masing masing punya isi yang berbeda. saya juga menggunakan <article> pada bagian skills karena merupakan bagian yang berdiri sendiri dan bisa dipahami terpisah dari konten lain
2. tantangannya terdapat pada penulisan nama class yang tidak konsisten antara HTML dengan CSS, karena nama class yang tidak sama membuat tampilan jadi tidak rapi
3. fitur yang ingin saya tambahkan adalah animasi. misalnya animasi fade in atau slide up ketika di scroll atau transisi yang lebih halus ketika berpindah antar section lewat navbar

### TUGAS 2
1. Saat pengguna mengklik Skills pada navbar, browser mengirim request ke /skills/.portofolio/urls.py (level proyek) menerima request tersebut, dan karena tidak cocok dengan pola admin/, request dilempar ke include("main.urls"). main/urls.py (level aplikasi) mencocokkan path skills/ dan mengarahkannya ke fungsi show_skills di views.py. Di dalam show_skills, baris Skill.objects.all() membuat model Skill melakukan query ke database (db.sqlite3) dan mengambil semua data Skill yang tersimpan. Data tersebut dimasukkan ke dalam context (dictionary) dan dikirim ke template skills.html melalui render(). Template menggunakan {% for skill in skill_list %} untuk melakukan perulangan pada tiap data dan membuat satu kartu HTML per Skill. Django mengembalikan HTML lengkap tersebut ke browser sebagai response, yang kemudian dirender menjadi tampilan yang dilihat pengguna.
2. data baru sebaiknya ditambahkan lewat model dengan Skill.objects.create(...) di shell sehingga otomatis muncul di halaman tanpa perlu mengubah di html, jika data di tulis langsung di template, setiap perubahan memerlukan kita untuk membuat blok baru <article>...</article> secara manual, yang rawan typo. Template bertanggung jawab menampilkan tampilan, sedangkan data adalah tanggung jawab database. jika keduanya digabungkan, setiap kali kita melakukan perubahan data, kita harus otak atik kodenya juga padahal dua hal tersebut bisa dipisahkan agar lebih mudah dikembangkan
3. Makemigrations berfungsi untuk membaca perubahan yang dibuat pada models.py dan membuat berkas migrasi (semacam catatan perubahan) tanpa langsung mengubah database. Berkas ini belum diterapkan ke db.sqlite3. Sedangkan Migrate yang mengeksekusi instruksi dari berkas migrasi tersebut ke database, sehingga perubahan strukturnya (misalnya tabel baru, menambah kolom atau menghapus field) benar-benar terbentuk.
Contohnya saat saya menambahkan model skill pada model.py. Setelah menjalankan python manage.py makemigrations, Django membuat file main/migrations/0002_skill.py yang berisi instruksi  "Create model Skill", namun tabel Skill belum ada di database. Setelah menjalankan python manage.py migrate dan muncul output Applying main.0002_skill...OK, tabel Skill terbentuk di db.sqlite3 dan siap diisi data. Jika hanya menjalankan makemigrations tanpa migrate, halaman /skills/ gagal diakses dan akan menampilkan error karena tabelnya belum ada di database.

### TUGAS 3
1. ModelFrom otomatis generate field HTML sesuai tipe data dari model dan juga otomatis validasi dari constraint yang didefinisikan di model sedangkan {% csrf_token %} wajib digunakan untuk mencegah serangan situs yang mencoba untuk nge-trigger submit form ke situs menggunakan sesi login korban tanpa mereka sadari, misalnya buat menghapus atau mengubah data mereka tanpa izin. Dengan csrf_token ini, Server bisa memastikan request tersebut beneran dikirim dari form situs sendiri, bukan dari situs luar
2. JSON lebih ringkas dan ukurannya lebih kecil. Strukturnya lebih mudah untuk di mapping langsung ke object di hampir semua bahasa pemrograman. Selain itu, JSON juga native ke JavaScript, browser bisa langsung parse JSON pake JSON.parse() tanpa butuh parser tambahan, beda sama XML yang perlu di-parse pake library terpisah. Makanya JSON lebih cocok untuk web modern yang banyak pake JS/AJAX
3. Alurnya: request masuk dan view akan ambil data dari database, lalu di serialize menjadi string JSON dan di bungkus HttpResponse dengan content_type="application/json" lalu dikirim kembali ke client. Serialization diperlukan untuk mengubah objek kompleks (model django) jadi format teks standar (JSON) yang bisa dibaca bahasa apa aja

Dokumentasi & AI Disclosure
saya menggunakan Claude untuk memandu saya dengan strategi bertanya step by step
### tugas 1 ###
bagian yang dibantu AI:
- struktur HTML bagian section pada skills (card layout menggunakan <article>) dan <ul>/<li> untuk timeline pada
bagian experience dan education
- kode CSS untuk grid layout skills card dan bullet point timeline
- debugging saat tampilan tidak sesuai. AI membantu saya menemukan penyebabnya adalah typo penulisan 
(skill-grid vs skills-grid, skills card vs skill card) yang membuat CSS tidak terhubung ke HTML

bagian yang saya kerjakan sendiri:
- menentukan isi konten tiap bagian berdasarkan pengalaman pribadi
- menentukan gaya tampilan yang saya inginkan
- menulis jawaban untuk pertanyaan reflektif sendiri

### tugas 2 ###
bagian yang dibantu AI:
- memahami alur yang terjadi ketika pengguna mengklik salah satu navbar pada halaman portofolio
- kode model Skill, view show_skills, template skills.html, routing di urls.py, dan navbar
- debugging error ImportError (typo Skill vs skill) dan kesalahan push ke branch master alih-alih main
- panduan mengisi data lewat Django shell
- unit test SkillPageTest
- dipandu dengan pertanyaan terarah untuk brainstorming jawaban pertanyaan reflektif

bagian yang saya kerjakan sendiri:
- menentukan isi tiap skill berdasarkan pengalaman pribadi
- menjalankan semua command dan verifikasi hasil di browser
- menulis jawaban akhir pertanyaan reflektif dengan kata-kata sendiri

### tugas 3 ###
bagian yang dibantu AI:
- menyesuaikan pola dan generate kode, nama field dan widget dari contoh tutorial dari project ke skill dan experience 
- review jawaban dari pertanyaan reflektif dan memberikan pemahaman serta mengoreksi kesalahan

bagian yang saya kerjakan sendiri:
- menulis jawaban pertanyaan reflektif dengan pemahaman dan bahasa sendiri
- testing manual di browser untuk setiap fitur yang di tambahkan
- menentukan section mana yang akan dipakai untuk tugas 3