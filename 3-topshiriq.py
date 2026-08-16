# .append(qiymat) - ro'yxat ichiga qiymat qo'shib beradi, ro'yxatni oxiridan qo'shadi
# ismlar.append("Alisher")
# ismlar.append("Javohir")
# print(ismlar)               # ['Alisher', 'Javohir']
# .remove(qiymat) - ro'yxat ichidagi biron qiymatni o'chirib beradi
# ismlar.remove('Alisher')
# ismlar.remove('javohir')  # ValueError
# .index(qiymat) - ro'yxat ichidan biron qiymatni tartib raqamini topib beradi.
# ismlar = ['Alisher', 'Javohir', 'Samandar']
# index_raqam = ismlar.index('Javohir')
# print(index_raqam)  # 1
# .insert(index_raqam, qiymat) - ro'yxatni istalgan joyiga qiymat qo'shib beradi.
# ismlar = ['Alisher', 'Samandar', 'Javohir']
# ismlar.insert(1, 'Mirjalol')
# print(ismlar)
# .sort() - ro'yxatni saralab beradi.
#           Agar ro'yxatni ichida faqat raqam bo'lsa, unda 0-9
#           Agar ro'yxatni ichida faqat harfli qiymatlar bo'lsa, unda A-Z
# ismlar = ['Mirjalol', 'Alisher', 'Biloldin']
# ismlar.sort()
# pop() - Indeks bo'yicha elementni o'chiradi va qaytaradi.
#cars = ["BMW", "Audi", "Mercedes"]
#deleted = cars.pop(1)
#print(deleted)
#print(cars)
# count() Element necha marta qatnashganini hisoblaydi.
#numbers = [1, 2, 3, 2, 5, 2]
# print(numbers.count(2))
# extend() - Boshqa ro'yxat elementlarini qo'shadi.
#cars1 = ["BMW", "Audi"]
#cars2 = ["Toyota", "Honda"]
#cars1.extend(cars2)
#print(cars1)
# clear() - Ro'yxat ichidagi barcha elementlarni o'chiradi.
#cars = ["BMW", "Audi", "Mercedes"]
#cars.clear()
#print(cars)
# takrorlanish operatorlari
# for       - oxiri mavjud yoki oxiri aniq bo'lgan ketma-ketlik(ro'yxat) uchun qo'llaniladi
# while     - oxiri mavjud emas yoki aniq bo'lmagan narsalar uchun qo'llaniladi
# 1
fruits = ["Apple", "Banana", "Orange", "Mango"]

for fruit in fruits:
    print(fruit)
# 2
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
# 3
fruits = ["Apple", "Banana", "Orange"]

for i in range(len(fruits)):
    print(i, fruits[i])
# 4
fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
# 5
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 2)
# 6
for car in ["BMW", "Audi", "Mercedes"]:
    print(car)
# 7
