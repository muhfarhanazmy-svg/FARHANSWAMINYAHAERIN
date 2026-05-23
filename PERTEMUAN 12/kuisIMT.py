print("\nSoal no 5")
def hitung_imt(berat, tinggi):
    (tinggi * tinggi)
    imt = berat/(tinggi*tinggi)
    return imt

berat = float(input("Masukan berat anda dalam Kilogram: "))
tinggi = float(input("Masukann tinggi anda dalam meter: "))

index_masa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if index_masa_tubuh <= 25.0:
    print("index masa tubuh anda adalah: ", index_masa_tubuh, "termasuk kategori", kategori[0])
elif index_masa_tubuh <= 27.0:
    print("index masa tubuh anda adalah: ", index_masa_tubuh, "termasuk kategori", kategori[1])
else:
    print("index masa tubuh anda adalah: ", index_masa_tubuh, "termasuk kategori", kategori[1], "Ayo diet!!!")
