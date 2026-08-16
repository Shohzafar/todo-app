# map -list olib uni har bir elementi bilan malum bir ish bajarib shakl almashtirilgan yangi list qaytaradi
# filter - saralash metodi massiv elementlarini ma'lum bir shartga ko'ra saralab (filtrlab) olish uchun ishlatiladi. U shartga mos keladigan elementlardan iborat yangi massiv qaytaradi.
# reduce - (Yig'ish / Umumlashtirish) metodi reduce metodi biroz murakkabroq, ammo juda universal. U massivdagi barcha elementlarni bitta yagona qiymatga (bitta son, bitta satr, bitta obyekt yoki bitta yangi massivga) keltirish (kombinatsiya qilish) uchun ishlatiladi.
# 1 - usul (Eng yomon)
numbers = [1, 2, 3, 4]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)

# 2 - usul (optimal usul)
numbers = [1, 2, 3, 4]
squares = list(map(lambda x:  x ** 2, numbers))
print(squares)

# 3 - Eng qisqa va zo'r yo'l
print(list(map(lambda x:  x ** 2, [1, 2, 3, 4])))

# filter - misol
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))

print(juft_sonlar)

# reduce - misol

from functools import reduce

sonlar = [1, 2, 3, 4, 5]

kopaytma = reduce(lambda x, y: x * y, sonlar)

print(kopaytma)

