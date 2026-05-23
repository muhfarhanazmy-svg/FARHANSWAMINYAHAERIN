print("\nSoal no 7")
def cek_segitiga(a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(2,3,4))
print(cek_segitiga(2,8,4))
