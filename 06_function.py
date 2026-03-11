# 06_function.py
# Funksiyalar kodni qayta ishlatish va tartibga solish uchun ishlatiladi


# 1-misol: oddiy funksiya yaratish va chaqirish
def salom():
    print("Salom dasturchi")

salom()  # Funksiyani chaqirish


# 2-misol: parametr bilan funksiya
def salom_ism(ism):
    print("Salom", ism)

salom_ism("Otabek")
salom_ism("Eldor")


# 3-misol: ikki sonni qo‘shish funksiyasi
def yigindi(a, b):
    return a + b  # qiymatni qaytarish

natija = yigindi(5, 7)
print("Yig'indisi:", natija)


# 4-misol: default qiymatli parametr
def salom_shahar(ism, shahar="Toshkent"):
    print(f"Salom {ism}, siz {shahar} shahrida yashaysiz")

salom_shahar("Otabek")
salom_shahar("Eldor", "Samarqand")


# 5-misol: *args bilan funksiya
def summa(*sonlar):
    yig = 0
    for s in sonlar:
        yig += s
    return yig

print("Yig'indisi:", summa(1, 2, 3, 4, 5))


# 6-misol: **kwargs bilan funksiya
def malumot(**kwargs):
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

malumot(ism="Otabek", yosh=20, kasb="Dasturchi")