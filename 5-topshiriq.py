# 1
def tanishtir(name, age, city):
    print(f"Assalomu allaykum mening ismim {name}, men {age} yoshdaman, va {city} da yashayman")

tanishtir(name="Jasur", age="22", city="Samarqand")
tanishtir(name="shohzafar", age="20", city="Toshkent")
tanishtir(name="umid", age="20", city="Qashqadaryo")

# 2
import math
def aylana_yuzasi(r: float) -> float:
  S = math.pi * (r ** 2)
  return S
r1 = 5.0
yuza1 = aylana_yuzasi(r1)
print(f"Radiusi {r1} bo'lgan aylananing yuzasi: {round(yuza1, 2)}")

r2 = 2.5
yuza2 = aylana_yuzasi(r2)
print(f"Radiusi {r2} bo'lgan aylananing yuzasi: {round(yuza2, 2)}")

r3 = 10.0
yuza3 = aylana_yuzasi(r3)
print(f"Radiusi {r3} bo'lgan aylananing yuzasi: {round(yuza3, 2)}")

# 3
def bahoni_aniqla(ball: int) -> str:
    
    if 0 <= ball <= 49:
        return "qoniqarsiz"
    elif 50 <= ball <= 69:
        return "qoniqarli"
    elif 70 <= ball <= 89:
        return "yaxshi"
    elif 90 <= ball <= 100:
        return "Alo"
    else:
        return "Noma'lum (bunday ball mavjud emas)"

kiritilgan_ball = int(input("Ballingizni kiriting: "))

natija = bahoni_aniqla(kiritilgan_ball)

print("Sizning bahoyingiz:", natija)

# 4
aralash_sonlar = [5, 1, 15, 20, 3, 0, 15]
def minimal_sonni_top(raqamlar: list) -> int:
 min = raqamlar[0]
 for num in raqamlar[1:]:
        if num < min:
            min = num
 return min
minimal_son = minimal_sonni_top(raqamlar = aralash_sonlar)
print(minimal_son)

# 5
royxat = [5, 15, 20, 30, 40, 44, 99]

def yigindini_hisobla(sonlar: list) -> int:
    yigindi = 0  
    for num in sonlar:  
        yigindi += num
    return yigindi  

my_score = yigindini_hisobla(royxat)

tayyor_sum_natija = sum(royxat)

print(f"Mening funksiyam natijasi: {my_score}")
print(f"Tayyor sum() natijasi: {tayyor_sum_natija}")
print("-" * 30)

if my_score == tayyor_sum_natija:
    print("Natijalar mos keldi! Funksiya to'g'ri yozilgan.")
else:
    print("Xatolik bor! Natijalar mos kelmadi.")

# 6
sozlar = ["uy", "kompyuter", "stol", "IT", "Dasturlash", "University"]

def uzun_sozlar(sozlar: list, min_uzunlik: int) -> list:
    saralangan_sozlar = [] 
    for soz in sozlar:
        if len(soz) >= min_uzunlik:
            saralangan_sozlar.append(soz) 
    return saralangan_sozlar 

min_uzunlik = 6
natija = uzun_sozlar(sozlar, min_uzunlik)
print(natija)