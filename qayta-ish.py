# 1
def tanishtir(name, age, city):
    print(f"Assalomu allaykum mening ismim {name}, men {age} yoshdaman, va {city} da yashayman")

tanishtir(name="Jasur", age="22", city="Samarqand")
tanishtir(name="shohzafar", age="20", city="Toshkent")
tanishtir(name="umid", age="20", city="Qashqadaryo")

def bahonni_top(ball: int) -> str:

    if ball >= 0 and ball <= 49:
     return "qoniqarsiz"
    elif ball >= 50 and ball <= 69:
       return "qoniqarli"
    elif ball >=70 and  ball <=89:
       return "yaxshi"
    elif ball  >=90 and ball <=100:
       return "alo"
    else:
       return "bunday baho yo'q" 
kiritilgan_ball = int(input("ballingizni kiriting"))
natija = bahonni_top(kiritilgan_ball)
print("Sizning bahoyingiz:", natija)

aralash_sonlar = [5, 1, 15, 20, 3, 0, 15]
def minimal_sonni_top(raqamlar: list) -> int:
 min = raqamlar[0]
 for num in raqamlar[1:]:
        if num < min:
            min = num
 return min
minimal_son = minimal_sonni_top(raqamlar = aralash_sonlar)
print(minimal_son)