import random

print("---SAYI TAHMIN OYUNU---")
sayi=random.randint(1,50)
print("1-50 arasinda sayi tuttum,5 hakkin var.")

hak=5
while hak>0:
    tahmin=int(input("tahminin nedir: "))
    if tahmin==sayi:
        print("bildin")
        break
    elif tahmin<sayi:
        print("arttir")
    else:
        print("azalt")
    hak=hak-1
if hak==0:
    print("bilemedin hakkin bitti,sayi:",sayi)
