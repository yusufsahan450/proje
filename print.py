isim = "selim" 
print(isim)
isim = "yusuf"
print (isim)
isim2 = "selim"
print(isim2)

yas = 13
print("{}un yası {}".format(isim,yas))

yas2 = int(input("yaşınız:"))
print("{}in yası {}".format(isim2,yas2))

def yasToplama(a,b):
    yaslarinToplami =a+b
    print("{}le {}un yasları toplamı {}".format(isim2,isim,yaslarinToplami))
yasToplama(yas,yas2)