class akunBank:
    list_pelanggan = []
    def __init__(self, no, nama, saldo):
        self.list_pelanggan.append(self)
        self.__no = no
        self.__nama = nama
        self.__saldo = saldo

    def lihat_menu(self):
        print("Halo " + self.__nama +", ingin melakukan apa")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer Saldo")
        print("4. Keluar")
        x = int(input("masukkan nomor input : "))
        if x == 1:
            Akun1.lihat_saldo()
        elif x == 2:
            Akun1.tarik_tunai()
        elif x == 3:
            Akun1.transfer()
        else:
            print("anda berhasil log out")
                

    def lihat_saldo(self):
       print(self.__nama, "memiliki saldo Rp ", self.__saldo)
       print("")
       Akun1.lihat_menu()
       
    def tarik_tunai(self):
        a = 99999999999
        while a > self.__saldo:
            a = int(input("masukkan jumlah nominal yang ingin ditarik: "))
            if a > self.__saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
        self.__saldo -= a
        print("saldo berhasil ditarik, sisa saldo anda Rp",self.__saldo)
        Akun1.lihat_menu()
        
    def transfer(self):
      jumlah = int(input("Masukkan nominal yang ingin ditransfer : "))
      rek = int(input("masukkan no rekening tujuan : "))
      if(jumlah<self.__saldo):
          for i in self.list_pelanggan:
              if(rek == self.__no):
                  print("rekening yang anda masukkan adalah rekening saat ini, kembali ke menu utama...")
                  break
              elif(rek == i.__no):
                  print("transfer Rp",jumlah,"ke",i.__nama,"sukses!")
                  self.__saldo -= jumlah
                  break
          if(rek!= self.__no and rek!= i.__no):
              print("No rekening tujuan tidak dikenal! Kembali ke menu utama ...")
      else: 
        print("saldo tidak cukup, kembali ke menu utama...")
      
      
             
      Akun1.lihat_menu()

          
Akun1 = akunBank(1234, "Harun Abdulkarim Khafid", 5000000000)
Akun2 = akunBank(2345, "Ukraina", 6666666666)
Akun3 = akunBank(3456, "Elon Musk", 9999999999)

print("Selamat datang di Bank Jago")
Akun1.lihat_menu()

