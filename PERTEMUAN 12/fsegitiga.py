print("\nSoal no 6")
def cek_segitiga(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))
