mylist= [10, 5, 3, 8, 2, 7, 6, 100, 9, 1]
largest = mylist[0]

for i in range(1, len(mylist)):
    if mylist[i] > largest:
        largest = mylist[i]

print(largest)