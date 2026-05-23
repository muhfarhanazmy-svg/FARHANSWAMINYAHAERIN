my_tuple = (1, 10, 100, 1000)
t1 = my_tuple + (10000, 100000)   # gabung dua tuple
t2 = my_tuple * 3                  # duplikat tuple 3x

print(len(t2))              # hitung total elemen t2
print(t1)                   # tampilkan t1
print(t2)                   # tampilkan t2
print(10 in my_tuple)       # cek apakah 10 ada dalam tuple
print(-10 not in my_tuple)  # cek apakah -10 TIDAK ada dalam tuple