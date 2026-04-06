my_list= [10, 5, 3, 8, 2, 7, 6, 100, 9, 1]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("elemen ditemukan pada indeks", i)
else:
    print("elemen tidak ada dalam list")