"""04_for.py
for sikli ma'lum bir oraliqdagi qiymatlarni takrorlash uchun ishlatiladi."""

"""Bu faylda boshlovchilar quyidagilarni o‘rganadi:
for sikli
range() ishlatish
ro‘yxat (list) bilan ishlash
matn (string) ustida sikl
qadam (step) ishlatish"""

# 1-misol: 1 dan 5 gacha sonlarni chiqarish
for i in range(1, 6):
    print(i)


# 2-misol: 1 dan 10 gacha sonlarni chiqarish
for i in range(1, 11):
    print("Son:", i)


# 3-misol: sonlarning kvadratini chiqarish
for i in range(1, 6):
    print(i, "ning kvadrati =", i*i)


# 4-misol: ro'yxat elementlarini chiqarish
mevalar = ["olma", "anor", "banan", "uzum"]
for meva in mevalar:
    print(meva)


# 5-misol: matndagi harflarni chiqarish
matn = "Python"
for harf in matn:
    print(harf)


# 6-misol: 1 dan 10 gacha juft sonlarni chiqarish
for i in range(2, 11, 2):
    print(i)


