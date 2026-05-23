bilangan = 2
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 5
    return bilangan

print(return_bilangan())
print(bilangan)