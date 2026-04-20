kamar = [[[False for k in range(20)] for i in range(15)] for g in range(3)]

kamar[1][9][13] = True
kamar[0][4][1]= False

tersedia = 0

for no_kamar in range(20):
    if not kamar[2][14][no_kamar]:  # cek kamar di gedung 2, lantai 10
        tersedia += 1

print(f"Kamar tersedia di gedung 2 lantai 14: {tersedia}")
