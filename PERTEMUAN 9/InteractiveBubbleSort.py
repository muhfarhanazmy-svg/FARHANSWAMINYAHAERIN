my_list = []
swapped = True
num = int(input("Masukkan panjang elemen list: "))

for i in range(num):
    val = float(input(f"Masukkan elemen ke list: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1): 
        if my_list[i] > my_list[i + 1]:
            swapped
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print("\nSorted : ")
    print(my_list)