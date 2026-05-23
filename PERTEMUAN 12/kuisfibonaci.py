print("\nSoal no 10")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    hasil_jumlah = 0 
    
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2 
        elem_1 = elem_2
        elem_2 = hasil_jumlah    
    return hasil_jumlah 

for i in range(1, 10):
    print(i, "->", fibonacci(i))
