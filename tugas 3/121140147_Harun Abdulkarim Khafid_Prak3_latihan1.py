class Mobil:
    bensin = 0
    def __init__(self,)->None:
        self.__bensin = 0
        self.__mengendarai = 0
        
    def isi_bensin(self):
        self.__bensin = 60
    def mengendarai(self, x):
        if x <= self.__bensin:
            self.__bensin -= x
            self.__mengendarai += x

        elif x > self.__bensin:
            self.__mengendarai += self.__bensin
            self.__bensin -= self.__bensin
            
                
    def lihat_info(self):
        print("odometer berada pada angka ", self.__mengendarai, "km, bensin yang tersisa ",self.__bensin," liter")

mobil = Mobil()
mobil.lihat_info()
mobil.isi_bensin()
mobil.lihat_info()
mobil.mengendarai(20)
mobil.lihat_info()
mobil.mengendarai(50)
mobil.lihat_info()
mobil.mengendarai(10)
mobil.lihat_info()
mobil.isi_bensin()
mobil.isi_bensin()
mobil.lihat_info()
