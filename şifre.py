print("---SISTEME GIRIS---")

dogru_sifre="1234"
hak=3

while hak>0:
    sifre=input("sifre: ")
    if sifre==dogru_sifre:
        print("basarili giriliyor")
        break
    else:
        print("Hatali sifre! Kalan hak:",hak-1)
if hak==0:
    print("bloke oldu cok fazla hatali deneme")
