isim = "selim" 
print(isim)
isim = "yusuf"
print (isim)
isim2 = "selim"
print(isim2)

yas = int(input("lütfen yaşınızı girin dahi programcı:"))
print("{}un yası {}".format(isim,yas))

yas2 = int(input("lütfen yaşınızı girermisiniz sayın programcı:"))
print("{}in yası {}".format(isim2,yas2))

def yasÇarpimi(a,b):
    yaslarinÇarpimi =a/b
    print("{}le {}un yasları çarpımı {}".format(isim2,isim,yaslarinÇarpimi))
yasÇarpimi(yas,yas2)