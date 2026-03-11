# 05_while.py
# while sikli shart to‘g‘ri bo‘lganda ishlaydi
# shart noto‘g‘ri bo‘lsa sikl tugaydi


# 1-misol: 1 dan 5 gacha sonlarni chiqarish
son = 1

while son <= 5:
    print(son)
    son += 1  # sonni 1 ga oshiramiz


# 2-misol: foydalanuvchi "stop" deb yozmaguncha davom etadigan sikl
while True:
    buyruq = input("Buyruq kiriting (to‘xtatish uchun 'stop' deb yozing): ")
    if buyruq.lower() == "stop":
        print("Sikl to‘xtatildi")
        break
    else:
        print("Siz kiritdingiz:", buyruq)


# 3-misol: juft sonlarni chiqarish
i = 2
while i <= 10:
    print(i)
    i += 2


# 4-misol: son yig‘indisi
son = 1
yigindi = 0

while son <= 5:
    yigindi += son
    son += 1

print("1 dan 5 gacha sonlar yig‘indisi:", yigindi)


# 5-misol: continue bilan sikl
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # 3 chiqmasdan davom etadi
    print(i)