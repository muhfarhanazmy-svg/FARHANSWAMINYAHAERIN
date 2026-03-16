secret_number = 777

print("Selamat datang di game sayahhhhh, Muggle!")
while True:
    guess = int(input("Tebak angka rahasia, cluenya angka: "))
    
    if guess == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")