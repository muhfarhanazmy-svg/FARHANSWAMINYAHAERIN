#  INII TAOHIDDDDD YUY
import os
import re

# database ruangan
gedung = [
    {"id": 1, "nama": "Aula"},
    {"id": 2, "nama": "Lab 1"},
    {"id": 3, "nama": "Lab 2"},
]

# database booking
bookings = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")#cls tuh perintah clear versi cmd windows mas, sama nt itu kode os, dan windos kodenya itu nt

def tampil_menu():
    print("=" * 35)
    print("      SISTEM BOOKING RUANGAN")
    print("=" * 35)
    print("  1. Lihat Ruangan")
    print("  2. Booking")
    print("  3. Lihat Jadwal")
    print("  4. Batalkan Booking")
    print("  0. Keluar")
    print("=" * 35)

def pause():
    input("\nTekan ENTER untuk lanjut...")

#  ALFIN KEREN BGT
def lihat_ruangan():
    print("\n[ Daftar Ruangan ]")
    print("-" * 20)
    for g in gedung:
        print(f"  {g['id']}. {g['nama']}")
    print("-" * 20)

def lihat_jadwal():
    print("\n[ Daftar Jadwal Booking ]")
    print("-" * 50)
    if not bookings:
        print("  Belum ada booking.")
        print("-" * 50)
        return
    print(f"  {'No':<4} {'Tanggal':<12} {'Jam':<8} {'Ruangan':<10} {'Nama'}")
    print("  " + "-" * 46)
    for i, b in enumerate(bookings, 1):
        nama_ruang = next(g["nama"] for g in gedung if g["id"] == b["gedung_id"])
        print(f"  {i:<4} {b['tanggal']:<12} {b['jam']:<8} {nama_ruang:<10} {b['nama']}")
    print("-" * 50)

#  FARHANNSWAMIHAERIN KEREN BGT22
def validasi_tanggal(tgl):
    """Validasi format tanggal dd/mm"""
    if not re.fullmatch(r"\d{2}/\d{2}", tgl):
        return False, 
    dd, mm = int(tgl[:2]), int(tgl[3:])
    if not (1 <= mm <= 12):
        return False, 
    if not (1 <= dd <= 31):
        return False, 
    return True, ""

def validasi_jam(jam):
    """Validasi format jam HH.MM"""
    if not re.fullmatch(r"\d{2}\.\d{2}", jam):
        return False, "Format jam harus HH.MM (contoh: 08.00)"
    hh, mm = int(jam[:2]), int(jam[3:])
    if not (0 <= hh <= 23):
        return False, "Jam harus antara 00 sampai 23"
    if not (0 <= mm <= 59):
        return False, "Menit harus antara 00 sampai 59"
    return True, ""  


def input_valid_angka(prompt, pilihan_valid=None):
    """Loop input sampai user masukkan angka yang valid"""
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  [!] Input harus berupa angka bulat. Coba lagi.")
            continue
        if pilihan_valid is not None and nilai not in pilihan_valid:
            print(f"  [!] Pilihan tidak tersedia. Pilih dari: {sorted(pilihan_valid)}")
            continue
        return nilai


def input_valid_format(prompt, fungsi_validasi):
    """Loop input sampai format sesuai"""
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("  [!] Input tidak boleh kosong. Coba lagi.")
            continue
        ok, pesan = fungsi_validasi(nilai)
        if not ok:
            print(f"  [!] {pesan}. Coba lagi.")
            continue
        return nilai


def input_nama():
    """Loop input nama sampai tidak kosong dan hanya huruf+spasi"""
    while True:
        nama = input("  Nama      : ").strip()
        if not nama:
            print("  [!] Nama tidak boleh kosong. Coba lagi.")
            continue
        if not re.fullmatch(r"[A-Za-z ]+", nama):  # FIX 2
            print("  [!] Nama hanya boleh mengandung huruf dan spasi. Coba lagi.")
            continue
        return nama


def booking():
    print("\n[ Booking Ruangan ]")
    print("-" * 35)

    nama = input_nama()

    lihat_ruangan()
    id_ruang_valid = {g["id"] for g in gedung}
    id_g = input_valid_angka("  Pilih ID ruang : ", pilihan_valid=id_ruang_valid)

    tgl = input_valid_format(
        "  Tanggal (dd/mm): ",
        validasi_tanggal
    )
    jam = input_valid_format(
        "  Jam (HH.MM)    : ",
        validasi_jam
    )

    nama_ruang = next(g["nama"] for g in gedung if g["id"] == id_g)  # FIX 3 — lookup 1x di sini

    # cek bentrok
    bentrok = [
        b for b in bookings
        if b["gedung_id"] == id_g and b["tanggal"] == tgl and b["jam"] == jam
    ]
    if bentrok:
        print(f"\n  [!] Jadwal bentrok!")
        print(f"      Ruangan '{nama_ruang}' pada {tgl} pukul {jam} sudah dibooking oleh '{bentrok[0]['nama']}'.")
        print("      Silakan pilih ruangan lain, tanggal lain, atau jam yang berbeda.")
        return

    bookings.append({
        "gedung_id": id_g,
        "nama": nama,
        "tanggal": tgl,
        "jam": jam
    })
    print("-" * 35)
    print(f"  Booking berhasil!")
    print(f"  Nama    : {nama}")
    print(f"  Ruangan : {nama_ruang}")
    print(f"  Tanggal : {tgl}")
    print(f"  Jam     : {jam}")
    print("-" * 35)

#  UMMI KEREN BGT33
def batal():
    print("\n[ Batalkan Booking ]")
    print("-" * 35)

    nama = input_nama()

    milik = [b for b in bookings if b["nama"].lower() == nama.lower()]
    if not milik:
        print(f"  [!] Tidak ada booking atas nama '{nama}'.")
        return

    print(f"\n  Booking milik '{nama}':")
    print(f"  {'No':<4} {'Tanggal':<12} {'Jam':<8} {'Ruangan'}")
    print("  " + "-" * 36)
    for i, b in enumerate(milik):
        nama_ruang = next(g["nama"] for g in gedung if g["id"] == b["gedung_id"])
        print(f"  {i:<4} {b['tanggal']:<12} {b['jam']:<8} {nama_ruang}")

    idx = input_valid_angka(
        "\n  Pilih nomor yang dibatalkan : ",
        pilihan_valid=set(range(len(milik)))
    )

    dibatal = milik[idx]
    nama_ruang = next(g["nama"] for g in gedung if g["id"] == dibatal["gedung_id"])
    bookings.remove(dibatal)
    print(f"\n  Booking '{nama_ruang}' pada {dibatal['tanggal']} pukul {dibatal['jam']} berhasil dibatalkan.")
    print("-" * 35)

#  INI TWHIDDD - MAIN LOOP
while True:
    clear()
    tampil_menu()
    p = input("  Pilih menu [0-4] : ").strip()

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
        print("\n  Keluar dari sistem. Sampai jumpa.")
        break
    else:
        print("\n  [!] Pilihan tidak valid. Masukkan angka 0 sampai 4.")
        pause()