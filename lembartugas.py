jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

# Menghitung waktu selesai
total_menit = menit + durasi
jam_selesai = jam + total_menit // 60
menit_selesai = total_menit % 60

# Menampilkan waktu selesai
print("Waktu selesai (jam:menit):", jam_selesai, ":", menit_selesai)