my_List = [10, 1, 8, 3, 5]

my_List[0], my_List[4] = my_List[4], my_List[0]
my_List[1], my_List[3] = my_List[3], my_List[1]

print(my_List)

length = len(my_List)

for i in range(length // 2):
    my_List[i], my_List[length - i - 1] = my_List[length - i - 1], my_List[i]

    print(my_List)