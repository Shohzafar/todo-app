# Dars rejasi: Default parametrlar, *args, **kwargs va Lambda funksiyalar

# Ma'lumot turlari
# str
# int
# float
# bool

# def va return kalit so'zlari
# def(define)   - funksiya e'lon qilishda ishlatiladi
# return        - funksiya ichidan qiymat qaytarish uchun

# def summa_chiqar(a, b):
#     return a + b

# natija = summa_chiqar(a=5, b=7)

# print(natija)



# Default parametrlar
# parametr - funksiya tashqaridan qabul qiladigan qiymat uchun saqlab qo'yilgan joy
# argument - saqlab qo'yilgan joyga(parametrga) uzatildigan qiymat

# def salomlash(ism="Mehmon"):
#     print(f"Salom {ism}")

# salomlash(ism="Aziz")       # Salom Aziz
# salomlash(ism="Javohir")    # Salom Javohir
# salomlash()                 # <-- Bu yerda xatolik chiqadi, chunki ism berilmagan


# To'g'ri
# def salomlash(ism, yosh=20):
#     print(f"Salom {ism}, siz {yosh} yoshdasiz")

# salomlash(ism="Alisher", yosh=18)  # Salom Alisher, siz 18 yoshdasiz
# salomlash(ism="Javohir")           # Salom Javohir, siz 20 yoshdasiz


# Xato
# def salomlash(ism="Mehmon", yosh):
#     print(f"Salom {ism}, siz {yosh} yoshdasiz")




# def salomlash(ism="Mehmon", yosh):
#     print(f"Salom {ism}, siz {yosh} yoshdasiz")

# salomlash(18)  # Salom Alisher, siz 18 yoshdasiz



# def malumot_chiqar(ism, manzil="Toshkent", yosh=20):
#     print(ism, yosh, manzil)



# def malumot_chiqar(ism, yosh=18, shahar="Toshkent"):
#     print(f"Ism: {ism}, Yosh: {yosh}, Shahar: {shahar}")

# malumot_chiqar("Dilnoza")
# malumot_chiqar("Dilnoza", 25)
# malumot_chiqar("Dilnoza", 25, "Samarqand")


# Kvadratning yuzini hisoblovchi funksiya yozib bering
# Agar tomon uzunligi berilmasa, u 1 ga teng bo'lsin (default qiymat)

# def kvadrat_yuzi(tomon=1):
#     print(tomon ** 2)

# kvadrat_yuzi(4)  # 16
# kvadrat_yuzi(5)  # 25
# kvadrat_yuzi()   # 1


# Foydalanuvchi haqida ma'lumot chiqaradigan funksiya yozib bering
# ism (majburiy), yosh (default 18) va kasb (default 'O'quvchi')

# def foydalanuvchi(ism, yosh=18, kasb="O'quvchi"):
#     print(f"{ism}, {yosh} yosh, {kasb}")

# # foydalanuvchi()                                     # <-- Xato
# foydalanuvchi('Alisher')                            # Alisher, 18 yosh, O'quvchi
# foydalanuvchi('Alisher', 25)                        # Alisher, 25 yosh, O'quvchi
# foydalanuvchi('Alisher', 27, 'Dasturchi')           # Alisher, 27 yosh, Dasturchi



# *args — cheksiz sonli argumentlar


# def yigindi(*sonlar):  # sonlar=(1, 2)
#     natija = 0

#     for son in sonlar:
#         natija += son

#     print(natija)


# yigindi()               # 0
# yigindi(1, 2)           # 3
# yigindi(1, 2, 3)        # 6
# yigindi(1, 2, 3, 4)     # 10

# kwargs (Keyword Arguments)
# Vazifasi: Funksiyaga istalgancha nomlangan (kalit so'zli) argumentlarni uzatish imkonini beradi (ya'ni kalit=qiymat ko'rinishida).
# Turi: Funksiya ichida bu qiymatlar dict (lug'at) ko'rinishida yig'iladi.
# Asosiy belgi — ikkita yulduzcha ().

def foydalanuvchi_info(**kwargs):
    print(kwargs)  # {'name': 'Ali', 'age': 20, 'role': 'developer'} bo'ladi
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

foydalanuvchi_info(name="Ali", age=20, role="developer")

def malumotlar(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit}, {qiymat} ")
        print("/n")

malumotlar(ism="alisher",yosh=20, manzil="toshkent")
malumotlar(ism="alisher",yosh=20)
malumotlar(ism="alisher")
# Lambda funksiyasi nima?
# lambda — bu Python-dagi nomsiz (anonim) funksiya hisoblanadi. Agar sizga faqat bir marta ishlatiladigan, kichik va oddiy operatsiyani bajaradigan funksiya kerak bo'lsa, def bilan to'liq funksiya ochib o'tirmasdan, lambda dan foydalanasiz.

# Oddiy def orqali:
def kvadrat(x):
    return x ** 2

# Lambda orqali:
kvadrat_lambda = lambda x: x ** 2

print(kvadrat_lambda(5))  # Natija: 25