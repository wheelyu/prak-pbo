class data:
   def __init__ (self, a, b, c, d):
        self.nama = a
        self.nim = b
        self.kelas = c
        self.sks = d
   def tampilan(self):
        print("Nama        :" + self.nama)
        print("Nim         :" + self.nim)
        print("Kelas       :" + self.kelas)
        print("Jumlah sks  :" + self.sks)
   def masuk(self):
        print("Kamu masuk  kelas Praktikum PBO")
        data1.tampilan()
        #data2.tampilan()
        
data1 = data("Harun Abdulkarim Khafid","121140147","RB","20")
#data2 = data("a","b","c","d")
data1.masuk()


