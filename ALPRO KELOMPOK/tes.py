# ==========================================
# DATABASE APLIKASI
# ==========================================
# Membuat database mahasiswa menggunakan Dictionary (kamus) bersarang
# Key (kunci) utamanya adalah NIM agar mudah dicari
database_mahasiswa = {
    "0001": {"nama": "muhamad alfin al faruq", "absen": 1, "kelas": "b", "kehadiran": 0, "tugas": {}},
    "0002": {"nama": "taohid", "absen": 2, "kelas": "b", "kehadiran": 0, "tugas": {}},
    "0003": {"nama": "ummi syahriah", "absen": 3, "kelas": "b", "kehadiran": 0, "tugas": {}},
    "0004": {"nama": "farkhan azmi", "absen": 4, "kelas": "b", "kehadiran": 0, "tugas": {}}
}

# Membuat database jadwal pelajaran menggunakan Dictionary
jadwal_pelajaran = {
    "Senin": "Bahasa Indonesia",
    "Selasa": "Bahasa Inggris",
    "Rabu": "Matematika Aljabar",
    "Kamis": "Matematika Diskrit",
    "Jumat": "Algoritma Pemrograman",
    "Sabtu": "Mobile Legend",
    "Ahad": "Libur"
}

# ==========================================
# LAYER 3: MENU-MENU FITUR
# ==========================================

# Fungsi untuk layer absensi
def layer_absensi(nim_user):
    # Membuat perulangan agar tetap di menu ini sampai user memilih kembali
    while True:
        # Mencetak pembatas visual
        print("\n=== LAYER ABSENSI ===")
        # Menampilkan opsi 1
        print("1. Absensi Hari Ini")
        # Menampilkan opsi 2
        print("2. Lihat Kehadiran")
        # Menampilkan opsi 3
        print("3. Kembali ke Menu Utama")
        # Meminta input pilihan dari user
        pilihan = input("Pilih menu (1/2/3): ")
        
        # Jika user memilih 1
        if pilihan == '1':
            # Menambah angka kehadiran di database mahasiswa sebanyak 1
            database_mahasiswa[nim_user]["kehadiran"] += 1
            # Menampilkan pesan berhasil
            print(">> Berhasil absen untuk hari ini!")
        # Jika user memilih 2
        elif pilihan == '2':
            # Mengambil total kehadiran saat ini dari database
            total_hadir = database_mahasiswa[nim_user]["kehadiran"]
            # Menampilkan total kehadiran
            print(f">> Total kehadiran kamu saat ini: {total_hadir} kali.")
        # Jika user memilih 3
        elif pilihan == '3':
            # Menghentikan perulangan (kembali ke fungsi sebelumnya/menu utama)
            break
        # Jika input tidak valid (selain 1, 2, 3)
        else:
            # Menampilkan pesan error
            print(">> Pilihan tidak ada, coba lagi ya!")

# Fungsi untuk layer jadwal
def layer_jadwal():
    # Mencetak pembatas visual dan judul
    print("\n=== JADWAL PELAJARAN ===")
    # Melakukan perulangan untuk mengambil hari dan mata kuliah dari database jadwal
    for hari, matkul in jadwal_pelajaran.items():
        # Menampilkan hari dan mata kuliahnya dengan rapi
        print(f"{hari} : {matkul}")
    # Menunggu user menekan tombol enter untuk kembali
    input("\nTekan Enter untuk kembali ke Menu Utama...")

# Fungsi untuk layer tugas
def layer_tugas(nim_user):
    # Membuat daftar hari menggunakan List
    daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Ahad"]
    # Mencetak judul menu tugas
    print("\n=== INPUT TUGAS MINGGUAN ===")
    # Memberikan instruksi kepada user
    print("Silahkan masukkan tugas untuk hari-hari berikut (kosongkan lalu enter jika tidak ada):")
    
    # Melakukan perulangan berdasarkan daftar hari yang sudah dibuat
    for hari in daftar_hari:
        # Meminta input tugas dari user untuk hari tertentu
        tugas_input = input(f"Tugas hari {hari}: ")
        # Menyimpan input tersebut ke dalam database tugas milik user yang sedang login
        database_mahasiswa[nim_user]["tugas"][hari] = tugas_input
    
    # Menampilkan pesan bahwa tugas berhasil disimpan
    print("\n>> Mantap! Semua tugas berhasil disimpan.")
    # Menunggu user menekan enter sebelum kembali
    input("Tekan Enter untuk kembali ke Menu Utama...")

# ==========================================
# LAYER 2: MENU UTAMA
# ==========================================

# Fungsi untuk menampilkan menu utama
def layer_menu(nim_user):
    # Mengambil data lengkap mahasiswa yang sedang login berdasarkan NIM
    data_user = database_mahasiswa[nim_user]
    # Memformat teks welcome sesuai permintaan (Welcome absen [no]. [nama] kls [kelas])
    print(f"\nWelcome absen {data_user['absen']}. {data_user['nama']} kls {data_user['kelas']}")
    
    # Membuat perulangan agar aplikasi tidak langsung mati setelah buka satu fitur
    while True:
        # Menampilkan header menu
        print("\n=== MENU UTAMA ===")
        # Menampilkan opsi absensi
        print("1. Absensi")
        # Menampilkan opsi jadwal
        print("2. Jadwal")
        # Menampilkan opsi tugas
        print("3. Tugas")
        # Menampilkan opsi keluar/logout
        print("4. Keluar")
        
        # Meminta user memilih menu
        pilih_menu = input("Mau buka menu nomor berapa (1/2/3/4)? : ")
        
        # Mengecek jika memilih 1
        if pilih_menu == '1':
            # Memanggil fungsi layer_absensi dan mengirimkan NIM user
            layer_absensi(nim_user)
        # Mengecek jika memilih 2
        elif pilih_menu == '2':
            # Memanggil fungsi layer_jadwal
            layer_jadwal()
        # Mengecek jika memilih 3
        elif pilih_menu == '3':
            # Memanggil fungsi layer_tugas dan mengirimkan NIM user
            layer_tugas(nim_user)
        # Mengecek jika memilih 4
        elif pilih_menu == '4':
            # Menampilkan pesan perpisahan
            print("\n>> Logout berhasil. Kembali ke halaman Login...")
            # Menghentikan perulangan menu utama untuk kembali ke fungsi login
            break
        # Jika input pilihan menu salah
        else:
            # Menampilkan peringatan error
            print(">> Pilihan tidak valid bro, masukin angka 1-4 aja!")

# ==========================================
# LAYER 1: LOGIN (PROGRAM UTAMA BERJALAN)
# ==========================================

# Fungsi untuk layer login
def layer_login():
    # Perulangan utama program agar jika salah login, tetap disuruh login lagi
    while True:
        # Menampilkan pembatas visual
        print("\n" + "="*30)
        # Menampilkan judul aplikasi
        print("   LOGIN APLIKASI MAHASISWA")
        # Menampilkan pembatas visual
        print("="*30)
        
        # Meminta input nama, menggunakan .lower() agar huruf kecil semua dan .strip() hilangkan spasi ujung
        input_nama = input("1. Nama : ").lower().strip()
        # Meminta input NIM, dibiarkan sebagai teks (string)
        input_nim = input("2. NIM  : ").strip()
        
        # Mengecek apakah NIM yang diinput ada di dalam kunci database_mahasiswa
        if input_nim in database_mahasiswa:
            # Jika NIM ada, kita cek apakah nama yang diinput sama dengan nama di database untuk NIM tersebut
            if database_mahasiswa[input_nim]["nama"] == input_nama:
                # Jika nama dan NIM cocok, masuk ke Layer 2 (Menu Utama)
                layer_menu(input_nim)
            else:
                # Jika NIM benar tapi namanya salah ketik
                print("\n>> data anda tidak ada mungkin anda bukan mahasiswa tapi mahasewa :) (canda salah input data)")
        else:
            # Jika NIM tidak terdaftar di database sama sekali
            print("\n>> data anda tidak ada mungkin anda bukan mahasiswa tapi mahasewa :) (canda salah input data)")

# ==========================================
# TRIGGER PROGRAM (MENJALANKAN KODE)
# ==========================================
# Baris ini berfungsi memanggil fungsi layer_login pertama kali saat file dijalankan
layer_login()