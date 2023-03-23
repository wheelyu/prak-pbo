class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        

class Processor(Komputer):
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, "Processor", harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class RAM(Komputer):
    def __init__(self, merk, nama, harga, kapasitas_ram):
        super().__init__(nama, "RAM", harga, merk)
        self.kapasitas_ram = kapasitas_ram

class HDD(Komputer):
    def __init__(self, merk, nama, harga, kapasitas_hdd,rpm):
        super().__init__(nama, "HDD", harga, merk)
        self.kapasitas_hdd = kapasitas_hdd
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, merk, nama, harga, kapasitas_vga):
        super().__init__(nama, "VGA", harga, merk)
        self.kapasitas_vga = kapasitas_vga

class PSU(Komputer):
    def __init__(self, merk, nama, harga, psu_daya):
        super().__init__(nama, "PSU", harga, merk)
        self.psu_daya = psu_daya

rakit = [[Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz'),
        RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB'),
        HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200),
        VGA('Asus','VGA GTX 1050',250000,'2GB'),
        PSU('Corsair','Corsair V550',250000,'500W')],
         
        [Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz'),
        RAM('G.SKILL','DDR4 2400MHz',328000,'4GB'),
        HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200),
        VGA('Asus','1060Ti',250000,'8GB'),
        PSU('Corsair','Corsair V550',250000,'500W')]]

# Menampilkan setiap komponen untuk setiap komputer yang dirakit oleh Om Bambang
for i, Komputer in enumerate(rakit):
    print("Komputer", i+1)
    for part in Komputer:
        print(part.jenis, part.nama," produksi", part.merk)
    print()