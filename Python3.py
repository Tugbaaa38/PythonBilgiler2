
#sayinin ussunu nasil aliriz?
sayi=5
kare=sayi**2
kup=sayi**3
print(kare)
print(kup)
#sayiyi kalansiz nasil boleriz?
sayi2=11
print(sayi2//2)
                  #-<Aralarindaki fark birinci ifadede sayi2 degismezken ikinci ifadede sayi2 ye yeni deger ataniyor.
sayi2=11//2
print(sayi2)

#kucuk hatirlatma
a=5
a+=2     #a*=2    a/=2
print(a) #ciktisi=7
#Uzun uzun a=a+2 yazmak yerine islemleri bu sekilde kisaltabiliriz

b=100%24
print(b)
# % isareti mod alma operatorudur.100 ile 24 u boler ve kalan bize modu verir.

#stringlerde toplama
isim="Tugba"
soyisim="Kirac"
print(isim+soyisim) #ciktisi:TugbaKirac
print("35"+"37")  #ciktisi:3537
#stringler arasinda sadece toplama islemi yapabiliriz bu da stringlerin birlesimidir. 
# *,-,/ stringler arasinda soz konusu degildir.
#print("Tugba"+21) #Bu ifade hata verecektir.Tip uyumsuzlugu soz konusudur.

selamla="Merhaba"
#selamla degiskenini dongu kullanmadan 10 kere yazmak istesek?
print(selamla*10)  #bu sekilde kullanmamizin sebebi daha sonrasinda ifadeyi degistirmek istedigimizde bize kolaylik saglamasidir.
print("Merhaba"*10)

#Python da tip donusumleri nasil yapilir?

sayi3=8.7
print(type(sayi3))
sayi3=int(sayi3)    #Donusturmek istedigimiz turun icine donusturmek istedigimiz degiskeni yazariz.
print(type(sayi3))
print(sayi3)         
#ciktisi=8 olacaktir fakat bu tip donusumler sagliksizdir.İslem yapmayi gerektiren kisimlarda kullanmamak daha dogrudur.

print(float("54"))    #Burada "54" string bir ifade iken float'a donusturduk.
#Fakat bunun tam tersi donusum yapmak hatalidir.Yani float veya int bir ifade string e donusturulemez.
#print(string(54.5))  hatali!




