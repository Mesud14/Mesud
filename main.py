import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifre Uzunluğunu Girin :"))
istek = input('Şifrenizde olmasını istediğiniz karakterleri yazın: (3 tane karakter yazın)')
sifre = ""
for i in range((sifre_uzunlugu - 3)):
    sifre += random.choice(karakterler)


print(sifre,istek)
