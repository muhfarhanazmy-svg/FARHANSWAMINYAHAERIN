from datetime import datetime

# ==========================================
# DATABASE
# ==========================================

database_mahasiswa = {
    "0001": {
        "nama": "muhamad alfin al faruq",
        "absen": 1,
        "kelas": "B",
        "kehadiran": [],       # Menyimpan list tanggal kehadiran
        "tugas_selesai": set() # Menyimpan id tugas yang sudah selesai
    },
    "0002": {
        "nama": "taohid",
        "absen": 2,
        "kelas": "B",
        "kehadiran": [],
        "tugas_selesai": set()
    },
    "0003": {
        "nama": "ummi syahriah",
        "absen": 3,
        "kelas": "B",
        "kehadiran": [],
        "tugas_selesai": set()
    },
    "0004": {
        "nama": "farkhan azmi",
        "absen": 4,
        "kelas": "B",
        "kehadiran": [],
        "tugas_selesai": set()
    }
}

# Jadwal Senin - Jumat sesuai instruksi
jadwal_pelajaran = {
    "Senin"  : "Bahasa Indonesia",
    "Selasa" : "Bahasa Inggris",
    "Rabu"   : "Matematika Aljabar",
    "Kamis"  : "Matematika Diskrit",
    "Jumat"  : "Algoritma Pemrograman"
}

# Daftar tugas dari database (shared, status dicek per-mahasiswa)
daftar_tugas = [
    {"id": 1, "matkul": "Bahasa Indonesia",      "deskripsi": "Ringkasan materi bab 3"},
    {"id": 2, "matkul": "Bahasa Inggris",         "deskripsi": "Latihan soal grammar unit 5"},
    {"id": 3, "matkul": "Matematika Aljabar",     "deskripsi": "Kerjakan soal latihan hal. 45"},
    {"id": 4, "matkul": "Matematika Diskrit",     "deskripsi": "Buat pohon keputusan dari studi kasus"},
    {"id": 5, "matkul": "Algoritma Pemrograman",  "deskripsi": "Buat program sorting sederhana"}
]

# ==========================================
# HELPER
# ==========================================

def garis(char="=", panjang=38):
    print(char * panjang)

def header(judul):
    garis()
    print(f"   {judul}")
    garis()

def get_hari_ini():
    """Mengembalikan nama hari dalam Bahasa Indonesia."""
    hari_map = {
        "Monday"    : "Senin",
        "Tuesday"   : "Selasa",
        "Wednesday" : "Rabu",
        "Thursday"  : "Kamis",
        "Friday"    : "Jumat",
        "Saturday"  : "Sabtu",
        "Sunday"    : "Minggu"
    }
    hari_en = datetime.now().strftime("%A")
    return hari_map.get(hari_en, hari_en)

def get_tanggal_hari_ini():
    """Mengembalikan string tanggal hari ini."""
    return datetime.now().strftime("%d-%m-%Y")

# ==========================================
# LAYER 2.1 - ABSENSI
# ==========================================

def layer_absensi(nim_user):
    data = database_mahasiswa[nim_user]

    while True:
        header("📋 ABSENSI")
        print("  1. Absen Hari Ini")
        print("  2. Lihat Riwayat Kehadiran")
        print("  3. Kembali ke Menu")
        garis("-", 38)
        pilihan = input("  Pilih (1/2/3): ").strip()

        if pilihan == '1':
            tanggal = get_tanggal_hari_ini()
            hari    = get_hari_ini()

            # Cek apakah sudah absen hari ini
            if tanggal in data["kehadiran"]:
                print(f"\n  >> Kamu udah absen hari ini ({hari}, {tanggal})!")
            else:
                data["kehadiran"].append(tanggal)
                print(f"\n  >> ✅ Absen berhasil! ({hari}, {tanggal})")

        elif pilihan == '2':
            header("📅 RIWAYAT KEHADIRAN")
            if not data["kehadiran"]:
                print("  Belum ada riwayat kehadiran.")
            else:
                for i, tgl in enumerate(data["kehadiran"], 1):
                    print(f"  {i}. {tgl}")
                print(f"\n  Total hadir: {len(data['kehadiran'])} kali")
            input("\n  Tekan Enter untuk kembali...")

        elif pilihan == '3':
            break
        else:
            print("  >> Pilihan tidak valid!")

# ==========================================
# LAYER 2.2 - JADWAL
# ==========================================

def layer_jadwal():
    while True:
        header("📅 JADWAL")
        print("  1. Jadwal Satu Minggu")
        print("  2. Jadwal Hari Ini")
        print("  3. Kembali ke Menu")
        garis("-", 38)
        pilihan = input("  Pilih (1/2/3): ").strip()

        if pilihan == '1':
            header("🗓️  JADWAL SATU MINGGU")
            for hari, matkul in jadwal_pelajaran.items():
                print(f"  {hari:<10} : {matkul}")
            input("\n  Tekan Enter untuk kembali...")

        elif pilihan == '2':
            hari_ini = get_hari_ini()
            header(f"📌 JADWAL HARI INI — {hari_ini}")
            if hari_ini in jadwal_pelajaran:
                print(f"  Mata Kuliah : {jadwal_pelajaran[hari_ini]}")
            else:
                print("  Tidak ada kuliah hari ini. Santai dulu! 😎")
            input("\n  Tekan Enter untuk kembali...")

        elif pilihan == '3':
            break
        else:
            print("  >> Pilihan tidak valid!")

# ==========================================
# LAYER 2.3 - TUGAS
# ==========================================

def layer_tugas(nim_user):
    data = database_mahasiswa[nim_user]

    while True:
        header("📝 TUGAS")
        print("  1. Daftar Semua Tugas")
        print("  2. Tugas Belum Selesai")
        print("  3. Tandai Tugas Selesai")
        print("  4. Kembali ke Menu")
        garis("-", 38)
        pilihan = input("  Pilih (1/2/3/4): ").strip()

        if pilihan == '1':
            header("📋 SEMUA TUGAS")
            for tugas in daftar_tugas:
                status = "✅" if tugas["id"] in data["tugas_selesai"] else "❌"
                print(f"  [{status}] ID {tugas['id']} | {tugas['matkul']}")
                print(f"        → {tugas['deskripsi']}")
            input("\n  Tekan Enter untuk kembali...")

        elif pilihan == '2':
            header("⏳ TUGAS BELUM SELESAI")
            belum = [t for t in daftar_tugas if t["id"] not in data["tugas_selesai"]]
            if not belum:
                print("  Semua tugas sudah selesai! 🎉")
            else:
                for tugas in belum:
                    print(f"  ❌ ID {tugas['id']} | {tugas['matkul']}")
                    print(f"        → {tugas['deskripsi']}")
            input("\n  Tekan Enter untuk kembali...")

        elif pilihan == '3':
            header("✅ TANDAI TUGAS SELESAI")
            # Tampilkan dulu tugas yang belum selesai
            belum = [t for t in daftar_tugas if t["id"] not in data["tugas_selesai"]]
            if not belum:
                print("  Semua tugas udah selesai, ga ada yang perlu ditandai!")
                input("\n  Tekan Enter untuk kembali...")
                continue

            for tugas in belum:
                print(f"  ID {tugas['id']} | {tugas['matkul']} → {tugas['deskripsi']}")

            garis("-", 38)
            try:
                id_input = int(input("  Masukkan ID tugas yang selesai: ").strip())
                # Cek apakah ID valid dan ada di daftar belum selesai
                id_belum = [t["id"] for t in belum]
                if id_input in id_belum:
                    data["tugas_selesai"].add(id_input)
                    print(f"  >> ✅ Tugas ID {id_input} berhasil ditandai selesai!")
                elif id_input in [t["id"] for t in daftar_tugas]:
                    print("  >> Tugas itu udah ditandai selesai sebelumnya!")
                else:
                    print("  >> ID tugas tidak ditemukan!")
            except ValueError:
                print("  >> Input harus berupa angka!")

        elif pilihan == '4':
            break
        else:
            print("  >> Pilihan tidak valid!")

# ==========================================
# LAYER 2 - MENU UTAMA
# ==========================================

def layer_menu(nim_user):
    data      = database_mahasiswa[nim_user]
    nama_rapi = data['nama'].title()

    garis()
    print(f"  👋 Halo, {nama_rapi}!")
    print(f"  Absen No.{data['absen']}  |  Kelas {data['kelas']}")
    garis()

    while True:
        header("🏠 MENU UTAMA")
        print("  1. Absensi")
        print("  2. Jadwal")
        print("  3. Tugas")
        print("  4. Keluar")
        garis("-", 38)
        pilih = input("  Pilih menu (1/2/3/4): ").strip()

        if pilih == '1':
            layer_absensi(nim_user)
        elif pilih == '2':
            layer_jadwal()
        elif pilih == '3':
            layer_tugas(nim_user)
        elif pilih == '4':
            print(f"\n  >> Logout berhasil. Dadah, {nama_rapi.split()[0]}! 👋\n")
            break
        else:
            print("  >> Masukkan angka 1-4 aja!")

# ==========================================
# LAYER 1 - LOGIN
# ==========================================

def layer_login():
    while True:
        garis("=", 38)
        print("      🎓 APLIKASI MAHASISWA")
        print("         Kelompok Kelas B")
        garis("=", 38)

        input_nama = input("  Nama : ").lower().strip()
        input_nim  = input("  NIM  : ").strip()

        if input_nim in database_mahasiswa:
            if database_mahasiswa[input_nim]["nama"] == input_nama:
                layer_menu(input_nim)
            else:
                print("\n  >> ❌ Nama tidak cocok dengan NIM. Coba lagi!\n")
        else:
            print("\n  >> ❌ NIM tidak terdaftar. Coba lagi!\n")

# ==========================================
# TRIGGER
# ==========================================

layer_login()