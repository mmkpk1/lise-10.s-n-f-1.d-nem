print("--- HESAP MAKINESI ---")

print("1-Toplama")
print("2-Cikarma")
print("3-Carpma")
print("4-Bolme")

secim=input("Secimini yap (1/2/3/4): ")
sayi1=int(input("1.sayiyi gir: "))
sayi2=int(input("2.sayiyi gir: "))

if secim=="1":
    print("Sonuc:",sayi1+sayi2)
elif secim=="2":
    print("Sonuc:",sayi1-sayi2)
elif secim=="3":
    print("Sonuc:",sayi1*sayi2)
elif secim=="4":
    if sayi2==0:
        print("bu sayı 0 bolunmez")
    else:
        print("Sonuc:",sayi1/sayi2)
else:
    print("Yanlis secim yaptin!")
