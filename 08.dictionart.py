# 08_dictionary.py
# Dictionary – kalit (key) va qiymat (value) juftligini saqlash uchun ishlatiladi


# 1-misol: oddiy dictionary yaratish
talaba = {
    "ism": "Otabek",
    "yosh": 20,
    "kasb": "Dasturchi"
}
print("Talaba ma'lumotlari:", talaba)


# 2-misol: dictionary elementlarini olish
print("Ism:", talaba["ism"])
print("Yosh:", talaba["yosh"])


# 3-misol: element qo‘shish yoki o‘zgartirish
talaba["shahar"] = "Toshkent"
talaba["yosh"] = 21
print("Yangilangan ma'lumotlar:", talaba)


# 4-misol: elementni o‘chirish
del talaba["kasb"]
print("Kasb o‘chirildi:", talaba)


# 5-misol: dictionary ichidagi barcha kalit va qiymatlarni ko‘rish
print("Kalitlar:", list(talaba.keys()))
print("Qiymatlar:", list(talaba.values()))
print("Kalit-qiymat juftliklari:", list(talaba.items()))


# 6-misol: for sikli bilan dictionary
for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")


# 7-misol: get() metodi
print("Shahar:", talaba.get("shahar"))
print("Telefon:", talaba.get("telefon", "Yo‘q"))  # default qiymat