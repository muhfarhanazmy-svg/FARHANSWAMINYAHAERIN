#Exo merupakan grup vokal asal korea selatan beranggotakan 9 orang: Suho, Kai, Chanyeol, Sehun, DO, Baekhyun, Xiumin, Lay dan Chen.
#Langkah 1: buatlah sebuat list kosong dengan nama exo
#Langkah 2: gunakan method append( ) untuk menambahkan anggota:Suho, Kai, Chanyeol dan Sehun.
#Langkah 3: gunakan for untuk menambahkan anggota: DO, Baekhyun, Kris, Lay, Luhan, Tao, dan Chen.
#Langkah 4: Hapuslah anggota: Kris, Luhan dan Tao
#Langkah 5: gunakan method insert() untuk menambahkan anggota Xiumin pada elemen ke tiga dari terakhir


exo=[]

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

for i in ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]:
    exo.append(i)

exo.remove("Kris")