# 3
def max_sonni_top(a: int, b: int, c: int) -> int:
    max = None
    if a > b:
        max = a
    else: 
        max = b
    if c > max:
        max = c
    return max

max1 = max_sonni_top(5, 7, 9)
max2 = max_sonni_top(5, 9, 7)
max3 = max_sonni_top(9, 7, 5)

print(max1, max2, max3)
# 2
aralash_raqamlar = [5, 1, 10, 7, 3, 25, 9, 11]

def max_sonni_top(raqamlar: list) -> int:

    max = raqamlar[0]

    for num in raqamlar[1:]:
        if num > max:
            max = num
    return max
maksimal_son = max_sonni_top(raqamlar=aralash_raqamlar)
print(maksimal_son)

# def salom_ber(name: str):
#     print(f"Assalomu alaykum {name}")


# salom_ber(name="Alex")
# salom_ber(name="John")
# salom_ber(name="Ulugbek")


# Foydalanuvchidan 2 ta qiymat qabul qiling, ism va familiya
# Keyin ularni salom beruvchu funksiyaga uzating
# Funksiya qabul qilingan ism va familiya asosida salom bersin
# Masalan: Salom, Ulugbek Umaraliev
# Funksiyani 3 marta har xil ism va familiyalar bilan ishlating



# def hisobla(a: int, b: int) -> int:
#     return a + b


# natija = hisobla(a=5, b=7)

# ...
# ...
# ...

# print(natija)  # 12




# def maksimal_sonni_top(a: int, b: int, c: int) -> int:
#     max = None

#     if a > b:
#         max = a
#     else:
#         max = b

#     if c > max:
#         max = c

#     return max


# max1 = maksimal_sonni_top(5, 7, 9)  # 9
# max2 = maksimal_sonni_top(5, 9, 7)  # 9
# max3 = maksimal_sonni_top(9, 7, 5)  # 9

# print(max1, max2, max3)  # 9, 9, 9




alaralash_raqamlar = [5, 1, 10, 7, 3, 25, 9, 11]

def maksimal_sonni_top(raqamlar: list) -> int:
    max = raqamlar[0]  # 1

    for num in raqamlar[1:]:
        if num > max:
            max = num

    return max

maksimal_son = maksimal_sonni_top(raqamlar=alaralash_raqamlar)

print(maksimal_son)  # 25









