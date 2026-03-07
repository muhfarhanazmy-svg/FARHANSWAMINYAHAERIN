pndptn_ptahun= int(input("Masukkan pendapatan per tahun: "))

if pndptn_ptahun > 500000000:
    Tpajak = 0.30
elif pndptn_ptahun > 250000000:
    Tpajak = 0.25
elif pndptn_ptahun > 60000000:
    Tpajak = 0.15
else:
    Tpajak = 0.05

pajak = pndptn_ptahun * Tpajak
print("tarif pajak lau:", Tpajak*100, "%")