# 07_list.py
# List – bir nechta qiymatlarni saqlash uchun ishlatiladi


# 1-misol: oddiy list yaratish
mevalar = ["olma", "banan", "anor", "uzum"]
print("Mevalar ro'yxati:", mevalar)


# 2-misol: list elementlarini chiqarish
for meva in mevalar:
    print("Meva:", meva)


# 3-misol: listga element qo'shish
mevalar.append("nok")
print("Yangilangan ro'yxat:", mevalar)


# 4-misol: elementni indeks orqali olish
print("Birinchi meva:", mevalar[0])
print("Oxirgi meva:", mevalar[-1])


# 5-misol: elementni o‘zgartirish
mevalar[1] = "apelsin"
print("O'zgartirilgan ro'yxat:", mevalar)


# 6-misol: elementni o‘chirish
mevalar.remove("anor")
print("Anor o‘chirildi:", mevalar)

del mevalar[0]
print("Birinchi element o‘chirildi:", mevalar)


# 7-misol: ro'yxat uzunligi
print("Ro'yxat uzunligi:", len(mevalar))


# 8-misol: ro‘yxatni bo‘lish va indeks yordamida ishlash
raqamlar = [1, 2, 3, 4, 5]
for i in range(len(raqamlar)):
    print(f"Indeks {i} – qiymat {raqamlar[i]}")