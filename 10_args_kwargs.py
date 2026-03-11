# 10_args_kwargs.py
# *args va **kwargs – funksiyalarga moslashuvchan parametr uzatish


# 1-misol: oddiy *args
def summa(*sonlar):
    """Noma’lum miqdordagi sonlarni qo‘shadi"""
    yig = 0
    for s in sonlar:
        yig += s
    return yig

print("Yig'indisi:", summa(1, 2, 3, 4))  # 10
print("Yig'indisi:", summa(5, 10, 15))   # 30


# 2-misol: *args bilan stringlar
def salomlar(*ism):
    for i in ism:
        print("Salom", i)

salomlar("Otabek", "Eldor", "Ali")


# 3-misol: oddiy **kwargs
def malumot(**kwargs):
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

malumot(ism="Otabek", yosh=20, kasb="Dasturchi")


# 4-misol: *args va **kwargs birga ishlatish
def funksiya(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

funksiya(1, 2, 3, ism="Otabek", yosh=20)