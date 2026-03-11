# 11_class.py
# Python’da class – obyektlar yaratish va ularning xatti-harakatlarini belgilash uchun ishlatiladi


# 1-misol: oddiy class yaratish
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism      # obyektning ism atributi
        self.yosh = yosh    # obyektning yosh atributi

    def tanishtir(self):
        print(f"Salom, men {self.ism}man va yoshim {self.yosh}da")


# 2-misol: class dan obyekt yaratish
talaba1 = Talaba("Otabek", 20)
talaba2 = Talaba("Eldor", 21)

# obyekt metodlarini chaqirish
talaba1.tanishtir()
talaba2.tanishtir()


# 3-misol: classga qo‘shimcha metod
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def tanishtir(self):
        print(f"Salom, men {self.ism}man va yoshim {self.yosh}da")

    def yoshni_yangilash(self, yangi_yosh):
        self.yosh = yangi_yosh

# obyekt yaratish
talaba3 = Talaba("Ali", 19)
talaba3.tanishtir()

# yoshni yangilash
talaba3.yoshni_yangilash(20)
talaba3.tanishtir()


# 4-misol: class va list bilan ishlash
talabalar = [
    Talaba("Otabek", 20),
    Talaba("Eldor", 21),
    Talaba("Ali", 20)
]

for t in talabalar:
    t.tanishtir()