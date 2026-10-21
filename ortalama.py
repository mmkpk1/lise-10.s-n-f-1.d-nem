print("---NOT ORTALAMASI HESAPLAMA---")
not1=int(input("1.yazılıyi gir: "))
not2=int(input("2.yazılıyi gir: "))
sozlu=int(input("sozlu notunu gir: "))
ortalama=(not1+not2+sozlu)/3
print("ortalamaniz:", ortalama)

if ortalama>=50:
    print("gectiniz")
else:
    print("kaldiniz")
