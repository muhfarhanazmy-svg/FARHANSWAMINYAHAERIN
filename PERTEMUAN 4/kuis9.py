jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

#this is may kodddd
total_menit = menit + durasi
jam_selesai = jam + total_menit // 60 #ini artinyaa 60 menit
menit_selesai = total_menit % 60

print("Waktu selesai (jam:menit):", jam_selesai, ":", menit_selesai)
