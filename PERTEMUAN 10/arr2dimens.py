papan_catur=[]
KOSONG = "-"
BENTENG = "B"
KUDA = "K"
for i in range(8):
    baris= [KOSONG for i in range(8)]
    papan_catur.append(baris)

papan_catur[0][0] = BENTENG
papan_catur[0][7] = BENTENG
papan_catur[7][0] = BENTENG
papan_catur[7][7] = BENTENG

papan_catur[1][1] = KUDA
papan_catur[1][6] = KUDA
for baris in papan_catur:
    print(baris)