Berikut adalah codding python untuk tugas Capstone Module 1 proses pembelajaran Job Connector Data Science Online Learning 013 mengenai sistem peminjaman buku diperpustakaan
yang dibuat oleh Imam Al Farouqi peserta JCDSOL013-005

===== MENU =====
1. Terdapat menu login untuk masuk kedalam sistem peminjaman buku
2. Setelah login, sistem akan menampilkan pilihan menu untuk masing-masing kategori user (Pegawai / Pengujung)
3. Menu pegawai akan menampilkan :
   1. Lihat Daftar Buku (Read), menampilkan tabel daftar buku yang tersedia terdiri dari Kode Buku, Judul, Pengarang, Kategori, dan Jumlah buku
   2. Filter buku berdarkan kategori buku, menampilkan data buku hanya berdasarkan kategori buku yang dipilih
   3. Tambah Buku (Create), pegawai dapat menambahkan data buku baru seperti Judul, Pengarang, Kategori dan Jumlah buku sedangkan Kode Buku akan otomatis terisi
   4. Ubah buku (Update), pegawai dapat mengubah data buku
   5. Hapus buku (Delete), pegawai dapat menhapus data buku
   6. Logout
   7. Kembali ke menu utama
4. Menu pengunjung akan menampilkan :
   1. Lihat Daftar Buku (Read), menampilkan tabel daftar buku yang tersedia terdiri dari Kode Buku, Judul, Pengarang, Kategori, dan Jumlah buku
   2. Filter buku berdasarkan kategori buku, menampilkan data buku hanya berdasarkan kategori buku yang dipilih
   3. Pinjam buku (Update), dimana ketika pengujung berhasil meminjam buku maka jumlah buku yang ada didalam dictionary akan berkurang 1
   4. Kembalikan buku (Update), dimana ketika pengujung berhasil mengembalikan buku maka jumlah buku yang ada didalam dictionary akan bertambah 1
   5. Logout
   6. Kembali ke menu utama
  
===== FUNGSI YANG DIGUNAKAN =====
1. tabulate, untuk menampilkan daftar buku dalam bentuk tabel
2. prettytable
3. sys, untuk fungsi logout
4. while True, untuk memvalidasi data input
5. global Username, variable global untuk menyimpan data user login
6. .lower(), untuk mencegah error ketika user menginput kategori buku dengan huruf kecil (Case Sensitive)
7. .format, untuk menampilkan informasi berdasarkan variable yang sebelumnya sudah dibuat
8. len(), untuk menghitung jumlah buku yang sudah ada
9. range(jumlah_buku +1, jumlah_buku +2), untuk menghasilkan angka yang berurutan dalam fungsi tambah otomatis kode buku
10. iter(), untuk mengubah objek range menjadi iterator
11. .zfill(3), untuk membuat format angka otomatis pada kode buku menjadi 3 digit
12. .title, untuk mengubah setiap awalan kata menjadi huruf besar ketika user menambahkan buku
