angka_genap = 0
angka_ganjil = 0

angka= int(input("Masukkan angka atau ketik 0 untuk berhenti:   "))
while angka != 0:
    if angka % 2 == 0:
        angka_genap += 1
    else:
        angka_ganjil += 1
    angka = int(input("Masukkan angka atau ketik 0 untuk berhenti:   "))

print(f"Jumlah angka genap: {angka_genap}")
print(f"Jumlah angka ganjil: {angka_ganjil}")