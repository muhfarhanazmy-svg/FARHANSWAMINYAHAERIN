my_list=[17, 5, 3, 8, 2, 10, 7, 6, 70, 9, 1,]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)