"""03_if_else.py
if else operatori shart tekshirish uchun ishlatiladi"""

# 1-misol: son juft yoki toq ekanini aniqlash
son = int(input("Son kiriting: "))
if son % 2 == 0:
    print("Bu juft son")
else:
    print("Bu toq son")
  

# 2-misol: son musbat yoki manfiy ekanini aniqlash
son = int(input("Yana bir son kiriting: "))
if son > 0:
    print("Bu musbat son")
else:
    print("Bu manfiy yoki 0 ga teng son")


# 3-misol: ikki sonni solishtirish
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
if a > b:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta yoki teng")


# 4-misol: yoshni tekshirish
yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("Siz voyaga yetgansiz")
else:
    print("Siz hali voyaga yetmagansiz")


# 5-misol: bahoni tekshirish
baho = int(input("Bahoni kiriting: "))
if baho >= 90:
    print("A'lo baho")
elif baho >= 70:
    print("Yaxshi baho")
elif baho >= 50:
    print("Qoniqarli baho")
else:
    print("Yiqildingiz")