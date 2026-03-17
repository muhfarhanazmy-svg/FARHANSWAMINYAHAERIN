#membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0

#membaca angka pertama
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

while angka != 0: #cek apakah angka tidak sama dengan 0
    if angka % 2 == 1: #mengecek apakah sisa bagi dengan angka 2 adalah 1
        angka_ganjil += 1
    else:
        angka_genap += 1
        
#membaca angka selanjutnya
    angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))
#menampilkan total angka ganjil dan angka genap
print("jumlah angka gajil: ", angka_ganjil)
print("jumlah angka genap: ", angka_genap)