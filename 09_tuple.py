# 09_tuple.py
# Tuple – o‘zgarmas (immutable) ro‘yxat. Elementlarini o‘zgartirish mumkin emas


# 1-misol: oddiy tuple yaratish
mevalar = ("olma", "banan", "anor", "uzum")
print("Tuple:", mevalar)


# 2-misol: tuple elementlarini olish
print("Birinchi meva:", mevalar[0])
print("Oxirgi meva:", mevalar[-1])


# 3-misol: for sikli bilan tuple elementlarini chiqarish
for meva in mevalar:
    print("Meva:", meva)


# 4-misol: tuple uzunligini aniqlash
print("Tuple uzunligi:", len(mevalar))


# 5-misol: tuple qo‘shish (yangi tuple hosil bo‘ladi)
mevalar_yangi = mevalar + ("nok", "olcha")
print("Yangilangan tuple:", mevalar_yangi)


# 6-misol: tuple ichidagi element indexini topish
print("Bananning indeksi:", mevalar.index("banan"))


# 7-misol: tuple ichidagi element sonini hisoblash
raqamlar = (1, 2, 3, 2, 4, 2, 5)
print("2 raqami nechta bor:", raqamlar.count(2))