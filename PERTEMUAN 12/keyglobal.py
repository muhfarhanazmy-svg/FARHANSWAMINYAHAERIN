print("\nSoal no 4")
bilangan = 10
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 5
    return bilangan

print(return_bilangan())
print(bilangan)
