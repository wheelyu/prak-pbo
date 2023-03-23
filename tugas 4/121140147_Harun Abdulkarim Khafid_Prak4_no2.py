class Robot:
    jumlah_turn = 0
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self,nama):
        if nama == "Antares": 
            if self.jumlah_turn % 3 == 0:
                damage = self.damage * 1.5  
            else:
                damage = self.damage

        elif nama == "Alphasetia":
            if self.jumlah_turn % 2 == 0:
                self.health += 4000  
                print(f'Robot lawan ({nama}) menambah darah sebanyak 4000 HP')
            damage = self.damage

        elif nama == "Lecalicus":
            if self.jumlah_turn % 4 == 0:
                self.health += 7000
                print(f'Robot lawan ({nama}) menambah darah sebanyak 7000 HP')
                damage = self.damage * 2        
            else:
                damage = self.damage
        else:
            damage = self.damage
        return damage
    
    def terima_aksi(self,damage, status,nama):
        self.health -= damage
        if status == 1:
            print(f'Robotmu ({nama}) menyerang sebanyak {int(damage)} DMG')
        elif status == 2:
            print(f'Robot lawan ({nama}) menyerang sebanyak {int(damage)} DMG')

class Antares(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
        
class Alphasetia(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
class Lecalicus(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
        
def pertarungan(p1,p2):
    while True:
        if p1.health <= 0:
            print("robotmu kalah setelah",p1.jumlah_turn,"turn")
            break
        if p2.health <= 0:
            print("robotmu menang setelah",p1.jumlah_turn,"turn")
            break
            
        p1.jumlah_turn +=1
        p2.jumlah_turn +=1
        print("Turn saat ini", p1.jumlah_turn)
        print("Robotmu(",p1.nama,"-",p1.health,"HP),robot lawan(",p2.nama,"-",p2.health,"HP)")
        
        c = int(input(f'Pilih tangan robotmu ({p1.nama}): '))
        d = int(input(f'Pilih tangan robot lawan ({p2.nama}): '))
        if (c < 4 and c > 0) and (d < 4 and d > 0):
            if (c == 1 and d == 3) or (c == 2 and d == 1) or (c == 3 and d == 2):
                aksi1 = p1.lakukan_aksi(p1.nama)
                p2.terima_aksi(aksi1, 1,p1.nama)
            elif (c == 3 and d == 1) or (c == 1 and d == 2) or (c == 2 and d == 3):
                aksi2 = p2.lakukan_aksi(p2.nama)
                p1.terima_aksi(aksi2, 2, p2.nama)
            elif (c == 1 and d == 1) or (c == 2 and d == 2) or (c == 3 and d == 3):
                print("Draw Try Again!!!!!!")      
        else:
            print("tangan robotmu tidak ada")
        
print("Selamat datang di pertandingan robot Yamako")
while True:
    a = int(input("Pilih robotmu (1=Antares, 2=Alphasetia, 3=Lecalicus):"))
    b = int(input("Pilih robot lawan (1=Antares, 2=Alphasetia, 3=Lecalicus):"))
    if (a < 4 and a > 0) and (b < 4 and b > 0):
        if a == 1:
            p1 = Antares("Antares",50000,5000)
        elif a == 2:
            p1 = Alphasetia("Alphasetia",40000,6000)
        elif a == 3:
            p1 = Lecalicus("Lecalicus",45000,5500)
            
        if b == 1:
            p2 = Antares("Antares",50000,5000)
        elif b == 2:
            p2 = Alphasetia("Alphasetia",40000,6000)
        elif b == 3:
            p2 = Lecalicus("Lecalicus",45000,5500)
        break
    else:
        print("robot tidak tersedia")
        
print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

pertarungan(p1,p2)