def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False
def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    return None

def hari_pada_tahun(tahun, bulan, hari):
    jumlah_hari = 0
    for b in range(1, bulan):
        jumlah_hari += hari_didalam_bulan(tahun, b)
    jumlah_hari += hari
    return jumlah_hari

print(hari_pada_tahun(2000, 12, 31))