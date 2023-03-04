print("soal 1 ")
print("soal 2 ")
a = int(input("pilih soal : "))

if a==1:
    
    #soal 1
    print("soal nomor 1 ")
    n = int(input("masukkan angka : "))
    for i in range(n):
        for i in range(n):
            print("*", end="")
        print()
elif a==2:    
    #soal 2
    print()
    print("soal nomor 2 ")
    user = "informatika"
    passw = "12345678"

    for i in range(3,0,-1):
        a = input("username anda : ")
        b = input("password anda : ")

        if a==user and b==passw:
            print("berhasil login")
            break
        else:
            if i>1:
                print("username atau password salah, sisa "+ str(i-1)+"x untuk mencoba")
            else:
                print("anda gagal 3x ")
                print("akun anda terblokir")
else:
    print("salah masukkan angka")