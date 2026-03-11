# 1-misol: foydalanuvchidan ism olish
ism = input("Ismingizni kiriting: ")
print("Salom", ism)

# 2-misol: foydalanuvchidan son olish
# input orqali kelgan qiymat matn (string) bo‘ladi
# shuning uchun son sifatida ishlatish uchun int() ishlatiladi
son = int(input('son kiriting: '))
print(son)

# 3-misol: ikki son kiritib ularning yig'indisini topish
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
yigindi = son1 + son2
print("Yig'indisi:", yigindi)

# 4-misol: bir nechta ma'lumot olish
shahar = input("Qaysi shaharda yashaysiz: ")
kasb = input("Kasbingiz nima: ")
print("Siz", shahar, "shahrida yashaysiz va", kasb, "bo'lib ishlaysiz.")