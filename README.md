Nama : Nurul Fikryati Bena

NPM : 2506534825

Kelas : PBP A

Angkatan : 2025

### Tugas 1
1. saya menggunakan <section> untuk mengelompokkan konten yang ingin saya buat agar lebih rapi dan jelas jika dibaca (profile, skills, experience, education) karena masing masing punya isi yang berbeda. saya juga menggunakan <article> pada bagian skills karena merupakan bagian yang berdiri sendiri dan bisa dipahami terpisah dari konten lain
2. tantangannya terdapat pada penulisan nama class yang tidak konsisten antara HTML dengan CSS, karena nama class yang tidak sama membuat tampilan jadi tidak rapi
3. fitur yang ingin saya tambahkan adalah animasi. misalnya animasi fade in atau slide up ketika di scroll atau transisi yang lebih halus ketika berpindah antar section lewat navbar

Deskripsi proyek 
Website portofolio pribadi berbasis Django yang menampilkan profil,skills, experience dan education saya sebagai mahasiswa Fasilkom UI

cara menjalankan
1. Aktifkan virtula env: "souce env/Scripts/activate"
2. jalankan server dengan "python manage.py runserver"
3 buka "https://127.0.0.1:8000/" di browser

Dokumentasi & AI Disclosure
saya menggunakan Claude untuk memandu saya dengan strategi bertanya step by step
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