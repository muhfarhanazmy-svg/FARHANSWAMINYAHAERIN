print("\nSoal no 9")
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1): 
        hasil *= i    
    return hasil 

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))
