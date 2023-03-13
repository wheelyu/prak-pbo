class Pegawai:
    # atribut global
    jabatan = 'Manager'
    
    def __init__(self, nama, umur, divisi, alamat):
        # atribut publik
        self.nama = nama
        self.divisi = divisi
        # atribut protected
        self._umur = umur
        # atribut private
        self.__alamat = alamat
    
    # fungsi publik
    def Umur(self):
        return self._umur
    
    # fungsi protected
    def gantiUmur(self, x):
        self._umur = x  
        
    def tambahAlamat(self, alamat_baru):   
        # mengubah atribut private (tidak dapat diakses langsung pada main program)
        # misal orang1.__alamat = 'Jakarta'
        # akan menyebabkan AttributeError: 'Manusia' object has no attribute '__alamat'
        self.__alamat = alamat_baru
    
    # fungsi instance private
    # fungsi ini hanya dapat di akses di dalam class tidak dapat di akses di luar class atau di main program
    def printAlamat(self):
        print("Alamat :", self.__alamat)
    
    def info(self):
        print('Nama:', self.nama)
        print('Umur:', self._umur)
        self.printAlamat()
        print('jabatan:', self.jabatan)
        print('divisi:',self.divisi)
        print("")
        
p1 = Pegawai('Brando', 31, "kominfo","Bogor") # membuat objek dari class 
p1.info()

print('jabatan:', Pegawai.jabatan)            # mengakses atribut class
print("")

print('Nama:', p1.nama)                       # mengakses atribut instance publik
print("")

p1.gantiUmur(33)                              # mengubah atribut instance protected
print('Umur:', p1.Umur())
print("")
p1.tambahAlamat("bandung")
p1.info()