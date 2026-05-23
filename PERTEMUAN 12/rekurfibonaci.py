print("\nSoal no 12")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(1, 10):
    print(i, "->", fibonacci(i))
