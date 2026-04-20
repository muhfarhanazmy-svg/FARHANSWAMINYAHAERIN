# ==============================
#  INII FARHAN
# ==============================

import os  # import buat clear layar

# database ruangan
gedung = [
    {"id": 1, "nama": "Aula"},
    {"id": 2, "nama": "Lab 1"},
    {"id": 3, "nama": "Lab 2"},
]

bookings = []

# fungsi clear layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# tampilan menu
def tampil_menu():
    print("="*35)
    print("     🏢 BOOKING RUANGAN")
    print("="*35)
    print("1. 📍 Lihat Ruangan")
    print("2. 📝 Booking")
    print("3. 📅 Lihat Jadwal")
    print("4. ❌ Batalkan Booking")
    print("0. 🚪 Keluar")
    print("="*35)

# pause biar user sempet baca
def pause():
    input("\nTekan ENTER untuk lanjut...")


# ==============================
# 👤 ALFIN KEREN BGT
# ==============================

# lihat daftar ruangan
def lihat_ruangan():
    print("\n📍 Daftar Ruangan:")
    for g in gedung:  # loop semua ruangan
        print(f"{g['id']}. {g['nama']}")  # tampil id + nama


# lihat semua jadwal booking
def lihat_jadwal():
    print("\n📅 Daftar Jadwal:")

    if not bookings:  # cek kalau kosong
        print("❌ Belum ada booking")
        return

    for b in bookings:  # loop semua booking
        # ambil nama ruang berdasarkan id
        nama_ruang = next(g["nama"] for g in gedung if g["id"] == b["gedung_id"])
        
        # tampil data
        print(f"• {b['tanggal']} | {b['jam']} | {nama_ruang} | {b['nama']}")


# ==============================
# 👤 TAOHID KEREN BGT22
# ==============================

def booking():
    print("\n📝 Booking Ruangan")

    nama = input("Nama: ")  # input nama user

    lihat_ruangan()  # tampilkan ruangan

    # input id ruang
    try:
        id_g = int(input("Pilih ruang: "))
    except:
        print("❌ Input harus angka")
        return

    # validasi ruang ada atau tidak
    if not any(g["id"] == id_g for g in gedung):
        print("❌ Ruangan tidak ada")
        return

    # input waktu
    tgl = input("Tanggal (dd/mm): ")
    jam = input("Jam (contoh 08.00): ")

    # cek bentrok booking
    if any(
        b["gedung_id"] == id_g and 
        b["tanggal"] == tgl and 
        b["jam"] == jam 
        for b in bookings
    ):
        print("❌ Sudah dibooking")
        return

    # simpan booking
    bookings.append({
        "gedung_id": id_g,
        "nama": nama,
        "tanggal": tgl,
        "jam": jam
    })

    print("✅ Booking berhasil")


# ==============================
# 👤 UMMI KEREN BGT33
# ==============================

def batal():
    print("\n❌ Batalkan Booking")

    nama = input("Nama: ")

    # ambil booking milik user
    milik = [b for b in bookings if b["nama"] == nama]

    if not milik:
        print("❌ Tidak ada booking")
        return

    # tampil list booking
    for i, b in enumerate(milik):
        print(f"[{i}] {b['tanggal']} {b['jam']} (Ruang {b['gedung_id']})")

    # pilih yang mau dibatal
    try:
        idx = int(input("Pilih yang dibatal: "))
    except:
        print("❌ Input harus angka")
        return

    # validasi index
    if 0 <= idx < len(milik):
        bookings.remove(milik[idx])  # hapus dari list utama
        print("✅ Dibatalkan")
    else:
        print("❌ Salah pilih")


# INI FARHANNN
while True:
    clear()  
    tampil_menu() 

    p = input("👉 Pilih menu: ")

    if p == "1":
        clear()
        lihat_ruangan()
        pause()

    elif p == "2":
        clear()
        booking()
        pause()

    elif p == "3":
        clear()
        lihat_jadwal()
        pause()

    elif p == "4":
        clear()
        batal()
        pause()

    elif p == "0":
        print("👋 Keluar dari sistem...")
        break

    else:
        print("❌ Pilihan salah")
        pause()