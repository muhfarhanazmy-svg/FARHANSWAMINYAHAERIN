lotre = [3, 7, 11, 42, 34, 49]
angka_keluar = [5, 9, 11, 42, 3, 49]
tebakan = 0

for i in range(len(lotre)):
    if lotre[i] in angka_keluar:
        tebakan += 1
print("Anda benar menebak sebanyak", tebakan, "angka.")