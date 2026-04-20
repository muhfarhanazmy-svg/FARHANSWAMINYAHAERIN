def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    
    return False

data_uji =[1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th,"->", end="")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("ok")
    else:
        print("gagal")