#Mengimport modul tabulate dan prettytable
from tabulate import tabulate
from prettytable import prettytable

# Mengimpor modul sys untuk fungsi logout dengan menggunakan fungsi sys.exit()
import sys

# Dictionary yang berisi data buku
# Format: {kode: {judul, pengarang, kategori, jumlah}}
buku = {
    "B001": {"Judul": "Laskar Pelangi", "Pengarang": "Andrea Hirata", "Kategori": "Novel", "Jumlah": 5},
    "B002": {"Judul": "One Piece", "Pengarang": "Eiichiro Oda", "Kategori": "Komik", "Jumlah": 5},
    "B003": {"Judul": "Barack Obama", "Pengarang": "Barack Obama", "Kategori": "Biografi", "Jumlah": 5},
    "B004": {"Judul": "ERPUL", "Pengarang": "Tim Penyusun", "Kategori": "Ensiklopedia", "Jumlah": 5},
    "B005": {"Judul": "Karawang Bekasi", "Pengarang": "Chairil Anwar", "Kategori": "Puisi", "Jumlah": 5},
    "B006": {"Judul": "Misteri Rumah Nenek", "Pengarang": "Edgar Allan Poe", "Kategori": "Cerpen", "Jumlah": 5},
    "B007": {"Judul": "Under Three Flags", "Pengarang": "Benedict Anderson", "Kategori": "Sejarah", "Jumlah": 5},
    "B008": {"Judul": "Kritik Atas Budi Pekerti", "Pengarang": "Immanuel Kant", "Kategori": "Filsafat", "Jumlah": 5},
    "B009": {"Judul": "A Short Story of Myth", "Pengarang": "Karen Armstrong", "Kategori": "Agama", "Jumlah": 5},
    "B010": {"Judul": "Thingking Fast and Slow", "Pengarang": "Daniel Kahneman", "Kategori": "Psikologi", "Jumlah": 5}
}

# Dictionary yang berisi data pegawai
# Format: {username: password}
pegawai = {
    "adminsatu": "123456",
    "admindua": "654321"
}

# Dictionary yang berisi data pengunjung
# Format: {username: password}
pengunjung = {
    "imam": "111111",
    "lidya": "222222",
    "keenan": "333333"
}

# Variabel global untuk menyimpan username yang login
username = ""

# Fungsi untuk login sebagai pegawai atau pengunjung
def login():
    global username # variabel global untuk menyimpan username yang login
    print("\n==== Selamat datang di sistem peminjaman buku perpustakaan ====\n")
    print("Silakan login untuk melanjutkan")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username.isalpha() and password.isdigit():
        # Mengecek apakah username dan password ada di dictionary pegawai atau pengunjung
        if username in pegawai and password == pegawai[username]:
            print("\nLogin berhasil")
            print("Anda login sebagai pegawai")
            menu_pegawai()
        elif username in pengunjung and password == pengunjung[username]:
            print("\nLogin berhasil")
            print("Anda login sebagai pengunjung")
            menu_pengunjung()
        else:
            print("\nAnda belum terdaftar, silakan hubungi petugas pendaftaran")
            login()
    else:
        print("\n Username dan password tidak valid")
        login()
   
# Fungsi untuk logout dari sistem
def logout():
    global username # variabel global untuk menyimpan username yang login
    print("\nAnda telah logout dari sistem\n")
    username = ""
    menu_utama() # kembali ke menu utama

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("\n=== Menu Utama ===")
    print("1. Login")
    print("2. Keluar")
    # Menerima input pilihan dari user
    pilih = input("Masukkan pilihan Anda: ")
    # Mengubah input menjadi int
    try:
        pilih = int(pilih)
    # Jika terjadi ValueError, maka meminta input lagi
    except ValueError:
        print("\nInput harus berupa angka. Silakan coba lagi.\n")
        menu_utama()
    # Jika input valid, akan dilanjutkan ke program sesuai dengan pilihan
    if pilih == 1:
        # Login sebagai pegawai atau pengunjung
        login()
    elif pilih == 2:
        # Keluar dari program
        print("\n=== Terima kasih telah menggunakan sistem peminjaman buku perpustakaan ===")
        sys.exit()
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.\n")
        menu_utama()


# Fungsi untuk menampilkan menu pilihan pegawai
def menu_pegawai():
    print("\n=== Menu Pegawai:===")
    print("1. Lihat daftar buku")
    print("2. Filter buku berdasarkan kategori")
    print("3. Tambah buku")
    print("4. Ubah data buku")
    print("5. Hapus buku")
    print("6. Logout")
    print("7. Kembali ke menu utama")
    # Validasi input
    while True:
        pilih = input("Masukkan pilihan Anda: ")
        if pilih.isnumeric(): # Cek apakah input berupa angka
            pilih = int(pilih) # Konversi input ke int
            break # Keluar dari loop
        else: # Jika input bukan angka
            print("Input harus berupa angka. Silakan coba lagi.")
    if pilih == 1:
        # Lihat daftar buku
        lihat_buku()
    elif pilih == 2:
        # Filter buku berdasarkan kategori
        filter_buku()
    elif pilih == 3:
        # Tambah buku
        tambah_buku()
    elif pilih == 4:
        # Ubah data buku
        ubah_buku()
    elif pilih == 5:
        # Hapus buku
        hapus_buku()
    elif pilih == 6:
        # Logout
        logout()
    elif pilih == 7:
        # Kembali ke menu utama
        menu_utama()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_pegawai()

# Fungsi untuk menampilkan menu pilihan pengunjung
def menu_pengunjung():
    print("\n=== Menu Pengunjung ===\n")
    print("1. Lihat daftar buku")
    print("2. Filter buku berdasarkan kategori")
    print("3. Pinjam buku")
    print("4. Kembalikan buku")
    print("5. Logout")
    print("6. Kembali ke menu utama")
    # Validasi input
    while True:
        pilih = input("Masukkan pilihan Anda: ")
        if pilih.isnumeric(): # Cek apakah input berupa angka
            pilih = int(pilih) # Konversi input ke int
            break # Keluar dari loop
        else: # Jika input bukan angka
            print("Input harus berupa angka. Silakan coba lagi.")
    if pilih == 1:
        lihat_buku()
    elif pilih == 2:
        filter_buku()
    elif pilih == 3:
        pinjam_buku()
    elif pilih == 4:
        kembalikan_buku()
    elif pilih == 5:
        logout()
    elif pilih == 6:
        menu_utama()
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.\n")
        menu_pengunjung()

# Fungsi untuk menampilkan list daftar buku
def lihat_buku():
    print("\nList Daftar Buku:")
    # Mengimpor modul prettytable
    from prettytable import PrettyTable
    # Membuat objek PrettyTable
    tabel = PrettyTable()
    # Menambahkan kolom-kolom ke tabel
    tabel.add_column("Kode", list(buku.keys()))
    tabel.add_column("Judul", [v["Judul"] for v in buku.values()])
    tabel.add_column("Pengarang", [v["Pengarang"] for v in buku.values()])
    tabel.add_column("Kategori", [v["Kategori"] for v in buku.values()])
    tabel.add_column("Jumlah", [v["Jumlah"] for v in buku.values()])
    # Menampilkan tabel
    print(tabel)
    # Menampilkan pilihan untuk kembali ke menu sebelumnya
    print("1. Kembali ke menu sebelumnya")
    print("2. Keluar")
    pilih = int(input("Masukkan pilihan Anda: "))
    if pilih == 1:
        # Kembali ke menu sesuai dengan jenis pengguna
        if username == "adminsatu" or username == "admindua":
            menu_pegawai()
        else:
            menu_pengunjung()
    elif pilih == 2:
        print("\n=== Terima kasih telah menggunakan sistem peminjaman buku perpustakaan ===\n")
        sys.exit()
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
        lihat_buku()

# Fungsi untuk memfilter dictionary yang berisi data buku
def filter_buku():
    kategori = input("\nMasukkan kategori buku yang ingin Anda lihat: ")
    # Membuat dictionary baru untuk menyimpan hasil filter
    buku_filter = {}
    # Melakukan iterasi pada dictionary buku
    for k, v in buku.items():
        # Mengecek apakah kategori buku sesuai dengan kriteria
        # Menggunakan metode lower () untuk membuat case insensitive
        if v["Kategori"].lower () == kategori.lower ():
            # Menambahkan pasangan key dan value ke dictionary hasil filter
            buku_filter[k] = v
    # Mengecek apakah dictionary hasil filter kosong atau tidak
    if buku_filter:
        # Menampilkan list daftar buku yang sudah difilter
        print("\nList daftar buku berdasarkan kategori {}:".format(kategori))
        # Mengimpor modul prettytable
        from prettytable import PrettyTable
        # Membuat objek PrettyTable
        tabel = PrettyTable()
        # Menambahkan kolom-kolom ke tabel
        tabel.add_column("Kode", list(buku_filter.keys()))
        tabel.add_column("Judul", [v["Judul"] for v in buku_filter.values()])
        tabel.add_column("Pengarang", [v["Pengarang"] for v in buku_filter.values()])
        tabel.add_column("Kategori", [v["Kategori"] for v in buku_filter.values()])
        tabel.add_column("Jumlah", [v["Jumlah"] for v in buku_filter.values()])
        # Menampilkan tabel
        print(tabel)
    else:
        # Menampilkan pesan bahwa tidak ada buku yang sesuai dengan kriteria
        print("\nTidak ada buku dengan kategori {}.".format(kategori))
    # Menampilkan pilihan untuk kembali ke menu sebelumnya
    print("1. Kembali ke menu sebelumnya")
    print("2. Keluar")
    pilih = int(input("Masukkan pilihan Anda: "))
    if pilih == 1:
        # Kembali ke menu sesuai dengan jenis pengguna
        if username == "adminsatu" or username == "admindua":
            menu_pegawai()
        else:
            menu_pengunjung()
    elif pilih == 2:
        print("\n=== Terima kasih telah menggunakan sistem peminjaman buku perpustakaan ===\n")
        sys.exit()
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
        filter_buku()

# Fungsi untuk pinjam buku
def pinjam_buku():
    # Menerima input kode buku yang ingin dipinjam
    kode = input("\nMasukkan kode buku yang ingin Anda pinjam: ")
    # Mengecek apakah kode buku ada di dictionary buku
    if kode in buku:
        # Mengecek apakah jumlah buku masih tersedia
        if buku[kode]["Jumlah"] > 0:
            # Mengurangi jumlah buku sebanyak 1
            buku[kode]["Jumlah"] -= 1
            # Menampilkan pesan bahwa peminjaman buku berhasil
            print("\nAnda berhasil meminjam buku {}.".format(buku[kode]["Judul"]))
            menu_pengunjung()
        else:
            print("\nMaaf, buku {} sedang tidak tersedia.".format(buku[kode]["Judul"]))
            menu_pengunjung()
    else:
        print("\nKode buku yang Anda masukkan tidak valid, kode buku diawali huruf besar\n")
        pinjam_buku()
    
# Fungsi untuk kembalikan buku
def kembalikan_buku():
    # Menerima input kode buku yang ingin dikembalikan
    kode = input("\nMasukkan kode buku yang ingin Anda kembalikan: ")
    # Mengecek apakah kode buku ada di dictionary buku
    if kode in buku:
        # Menambah jumlah buku sebanyak 1
        buku[kode]["Jumlah"] += 1
        # Menampilkan pesan bahwa pengembalian buku berhasil
        print("\n=== Anda berhasil mengembalikan buku {}.===".format(buku[kode]["Judul"]))
        menu_pengunjung()
    else:
        # Menampilkan pesan bahwa kode buku tidak valid
        print("\nKode buku yang Anda masukkan tidak valid, kode buku diawali huruf besar.\n")
        menu_pengunjung()
   
# Fungsi untuk tambah buku
def tambah_buku():
    # Menghitung jumlah buku yang sudah ada
    jumlah_buku = len(buku)
    # Menghasilkan angka yang berurutan dari jumlah buku + 1 sampai jumlah buku + 2
    # Misalnya, jika jumlah buku = 10, maka angka yang dihasilkan adalah 11
    angka = range(jumlah_buku + 1, jumlah_buku + 2)
    # Mengubah objek range menjadi iterator
    angka = iter(angka)
    # Menambahkan kode "B" dan format angka menjadi tiga digit
    # Misalnya, jika angka = 11, maka kode buku = "B011"
    # Membuat kode buku secara otomatis dengan fungsi range() dan metode zfill()
    kode = "B" + str(next(angka)).zfill(3)
    # Menerima input data buku yang ingin ditambahkan
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan pengarang buku: ")
    kategori = input("Masukkan kategori buku: ")
    # Mengubah input menjadi huruf besar pada setiap awal kata
    judul = judul.title()
    pengarang = pengarang.title()
    kategori = kategori.title()
    # Menerima input jumlah buku yang ingin ditambahkan
    jumlah = input("Masukkan jumlah buku: ")
    # Memvalidasi input jumlah
    while True:
        # Mencoba mengubah input jumlah menjadi int
        try:
            jumlah = int(jumlah)
        # Jika terjadi ValueError, maka akan meminta input lagi
        except ValueError:
            print("Jumlah buku harus berupa angka. Silakan coba lagi.")
            jumlah = input("Masukkan jumlah buku: ")
            continue
        # Mengecek apakah jumlah buku positif
        if jumlah > 0:
            break
        else:
            print("Jumlah buku harus lebih dari nol. Silakan coba lagi.")
            jumlah = input("Masukkan jumlah buku: ")
    # Membuat dictionary baru untuk menyimpan data buku
    buku_baru = {"Judul": judul, "Pengarang": pengarang, "Kategori": kategori, "Jumlah": jumlah}
    # Menambahkan pasangan kunci dan nilai ke dictionary buku
    buku[kode] = buku_baru
    # Menampilkan pesan bahwa penambahan buku berhasil
    print("\n== Anda berhasil menambahkan buku {}.==\n".format(judul))
    # Menampilkan menu sebelumnya
    menu_pegawai()

# Fungsi untuk ubah data buku
def ubah_buku():
    # Menerima input kode buku yang ingin diubah
    kode = input("Masukkan kode buku yang ingin Anda ubah: ")
    # Mengecek apakah kode buku ada di dictionary buku
    if kode in buku:
        # Menampilkan data buku yang lama
        print("\nData buku yang lama:")
        print("Kode: {}, Judul: {}, Pengarang: {}, Kategori: {}, Jumlah: {}".format(kode, buku[kode]["Judul"], buku[kode]["Pengarang"], buku[kode]["Kategori"], buku[kode]["Jumlah"]))
        # Menerima input data buku yang baru
        judul = input("\nMasukkan judul buku yang baru: ")
        pengarang = input("Masukkan pengarang buku yang baru: ")
        kategori = input("Masukkan kategori buku yang baru: ")
        # Mengubah input menjadi huruf besar pada setiap awal kata
        judul = judul.title()
        pengarang = pengarang.title()
        kategori = kategori.title()
        # Menerima input jumlah buku yang baru
        jumlah = input("Masukkan jumlah buku yang baru: ")
        # Memvalidasi input jumlah
        while True:
            # Mengubah input jumlah menjadi int
            try:
                jumlah = int(jumlah)
            # Jika terjadi ValueError, maka meminta input lagi
            except ValueError:
                print("Jumlah buku harus berupa angka. Silakan coba lagi.")
                jumlah = input("Masukkan jumlah buku yang baru: ")
                continue
            # Mengecek apakah jumlah buku positif
            if jumlah > 0:
                break
            else:
                print("Jumlah buku harus lebih dari nol. Silakan coba lagi.")
                jumlah = input("Masukkan jumlah buku yang baru: ")
        # Mengubah nilai dictionary buku sesuai dengan input yang baru
        buku[kode]["Judul"] = judul
        buku[kode]["Pengarang"] = pengarang
        buku[kode]["Kategori"] = kategori
        buku[kode]["Jumlah"] = jumlah
        # Menampilkan pesan bahwa perubahan data buku berhasil
        print("\n== Anda berhasil mengubah data buku menjadi {}.==\n".format(judul))
        menu_pegawai()
    else:
        # Menampilkan pesan bahwa kode buku tidak valid
        print("\nKode buku yang Anda masukkan tidak valid, kode buku diawali huruf besar.\n")
        # Menampilkan pilihan untuk kembali ke menu sebelumnya
        menu_pegawai()

# Fungsi untuk hapus buku
def hapus_buku():
    # Menerima input kode buku yang ingin dihapus
    kode = input("Masukkan kode buku yang ingin Anda hapus: ")
    # Mengecek apakah kode buku ada di dictionary buku
    if kode in buku:
        # Menampilkan data buku yang akan dihapus
        print("Data buku yang akan dihapus:")
        print("Kode: {}, Judul: {}, Pengarang: {}, Kategori: {}, Jumlah: {}".format(kode, buku[kode]["Judul"], buku[kode]["Pengarang"], buku[kode]["Kategori"], buku[kode]["Jumlah"]))
        # Menerima input konfirmasi untuk menghapus buku dan validasi input
        while True:
            konfirmasi = input("\nApakah Anda yakin ingin menghapus buku ini? (y/n): ")
            if konfirmasi == "y" or konfirmasi == "n": # Cek apakah input adalah y atau n
                break
            else: # Jika input bukan y atau n
                print("Input harus berupa y atau n (huruf kecil). Silakan coba lagi.")
        if konfirmasi == "y":
            # Menghapus pasangan key dan value dari dictionary buku
            del buku[kode]
            print("\n== Anda berhasil menghapus buku {}.==\n".format(kode))
            menu_pegawai()
        else:
            print("== Anda membatalkan penghapusan buku {}.==".format(kode))
            menu_pegawai()
    else:
        print("Kode buku yang Anda masukkan tidak valid, kode buku diawali huruf besar")
    # Menampilkan pilihan untuk kembali ke menu sebelumnya
        menu_pegawai()

menu_utama()

