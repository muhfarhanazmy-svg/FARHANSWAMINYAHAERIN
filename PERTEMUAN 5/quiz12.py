angka1 = int(input("masukkan angka pertama: "))
angka2 = int(input("masukkan angka kedua: "))
angka3 = int(input("masukkan angka ketiga: "))

#angka paling besar
if angka1 > angka2 and angka1 > angka3:
    angka_besar = angka1
elif angka2 > angka1 and angka2 > angka3:
    angka_besar = angka2
else:
    angka_besar = angka3

print("angka terbesar diantara ketiganya adalah:", angka_besar)