secret_number = 28
print("Selamat datang di game tebak angka rahasia pesulap!")
while True:
    guess = int(input("Tebak angka rahasia, cluenya angka: "))
    
    if guess == secret_number:
        print("Selamat, kamu berhasil menebak angka rahasia!")
        break
    else:
        print("Tebakanmu salah, coba lagi!")