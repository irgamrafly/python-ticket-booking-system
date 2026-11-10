umur = int(input("masukan umur: "))
if umur >= 12:
    print("umur anda terpenuhi")
    
    tinggi = int(input("masukan tinggi: "))
    if tinggi >= 150:
        print("tinggi anda terpenuhi")
        
        fasilitas = input("masukan fasilitas yang ingin anda gunakan (vip/reguler): ")
        tiket = 0
        if fasilitas == "vip":
            tiket = 100000
        elif fasilitas == "reguler":
            tiket = 50000
        else:
            print("tidak ada fasilitas tersebut")
            
        makanan = input("masukan makanan yang anda pesan: (popcorn / permen) ")
        harga = 0
        if makanan == "popcorn":
            harga = 15000
        elif makanan == "permen":
            harga = 2000
        else:
            print("anda tidak memesan makanan")
            
        print("Harga tiket anda: Rp", tiket)
        print("harga makanan anda: Rp", harga)
        print("total yang harus dibayar: Rp", tiket + harga)
        
    else:
        print("tinggi anda belum cukup!")
else:
    print("anda belum cukup umur")
