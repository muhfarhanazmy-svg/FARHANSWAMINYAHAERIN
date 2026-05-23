def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

berat = int(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["normal", "gemuk", "obesitas"]

if index_massa_tubuh < 25.0:
    print("IMT:", index_massa_tubuh, "Kategori:", kategori[0])
elif index_massa_tubuh > 25.0:
    print("IMT:", index_massa_tubuh, "Kategori:", kategori[1])
else:
    print("IMT:", index_massa_tubuh, "Kategori:", kategori[2])