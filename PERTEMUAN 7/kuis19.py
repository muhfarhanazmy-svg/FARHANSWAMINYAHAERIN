topi_list = [1, 2, 3, 4, 5]

input_angka = int(input("Masukkan angka untuk menggantikan nilai tengah list: "))
topi_list[2] = input_angka

del topi_list[-1]

print("Panjang list:", len(topi_list))

print(topi_list)