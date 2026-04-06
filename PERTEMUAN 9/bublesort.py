#bubble sort sederhana dgn user input
my_list = []
num = int(input("Masukkan panjang elemen list: "))

for i in range(num):
    val = float(input(f"Masukkan elemen ke list: "))
    my_list.append(val)

for i in range(len(my_list) - 1):
    for j in range(len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print("\nSorted : ")
print(my_list)
