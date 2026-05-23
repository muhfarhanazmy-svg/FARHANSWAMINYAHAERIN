kelas_informatika = {}

while True:
    try:
        nama = input("Masukkan nama mahasiswa: ")
        if nama == "":
            break

        nilai = int(input("Masukkan nilai (0-10): "))
        if nilai not in range(0, 11):
            raise ValueError

    except ValueError:
        print("Nilai harus angka antara 0 sampai 10!")
        continue
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user")
        break
    except Exception as e:
        print("Terjadi error lain:", e)
        continue

    if nama in kelas_informatika:
        kelas_informatika[nama] += (nilai,)
    else:
        kelas_informatika[nama] = (nilai,)

for nama in sorted(kelas_informatika.keys()):
    total = sum(kelas_informatika[nama])
    jumlah = len(kelas_informatika[nama])
    print(nama, ":", total / jumlah)