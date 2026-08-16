# list, list metodlari

# number = 5
# numbers = [1, 2, 3, 4, 5]
# numbers = [1]

#              0    1     2         3        4
# qiymatlar = [False, 5, "salom", [1, 2, 3], 12.3]

# print( qiymatlar[2] )  # "salom"
# print( qiymatlar[4] )  # IndexError

# -1 indeks raqam bu oxiridan birinchi raqam
# print( qiymatlar[-1] ) # 12.3

# print( qiymatlar )
# print( qiymatlar[0:3] )  # [False, 5, "salom"]



# number1 = 5
# number2 = 10
# numbers_list = [1, 2, 3, 4, 5]

# "number in numbers_list" - kompyuterga savol, "number" o'zgaruvchisi ichidagi qiymat "numbers_list" o'zgaruvchisi ichidagi ro'yxat qiymatlari orasida bormi yoki yo'q
# print( number1 in numbers_list )  # True
# print( number2 in numbers_list )  # False


# ismlar = []

# .append(qiymat) - ro'yxat ichiga qiymat qo'shib beradi, ro'yxatni oxiridan qo'shadi
# ismlar.append("Alisher")
# ismlar.append("Javohir")
# print(ismlar)               # ['Alisher', 'Javohir']


# .remove(qiymat) - ro'yxat ichidagi biron qiymatni o'chirib beradi
# ismlar.remove('Alisher')
# ismlar.remove('javohir')  # ValueError
# print(ismlar)


# .index(qiymat) - ro'yxat ichidan biron qiymatni tartib raqamini topib beradi
# ismlar = ['Alisher', 'Javohir', 'Samandar']
# index_raqam = ismlar.index('Javohir')
# print(index_raqam)  # 1


# .insert(index_raqam, qiymat) - ro'yxatni istalgan joyiga qiymat qo'shib beradi
# ismlar = ['Alisher', 'Samandar', 'Javohir']
# ismlar.insert(1, 'Mirjalol')
# print(ismlar)


# .sort() - ro'yxatni saralab beradi.
#           Agar ro'yxatni ichida faqat raqam bo'lsa, unda 0-9
#           Agar ro'yxatni ichida faqat harfli qiymatlar bo'lsa, unda A-Z
# ismlar = ['Mirjalol', 'Alisher', 'Biloldin']
# ismlar.sort()

# raqamlar = [10, 6, 2, 1, 4, 5]
# raqamlar.sort()

# qiymatlar = [5, False, 'Salom', [1, 2, 3]]
# qiymatlar.sort()

# print(ismlar)
# print(raqamlar)


# Foydalanuvchidan 4 ta raqam qabul qiling
# Ularni ro'yxat ichiga jamlang
# Ro'yxat ichida ularni o'sish tartibida joylashtiring
# Hosil bo'lgan ro'yxatni chiqaring

# num1 = int(input('Raqam kiriting: '))
# num2 = int(input('Raqam kiriting: '))
# num3 = int(input('Raqam kiriting: '))
# num4 = int(input('Raqam kiriting: '))

# numbers = []

# numbers.append(num1)
# numbers.append(num2)
# numbers.append(num3)
# numbers.append(num4)

# numbers.sort(reverse=True)  # reverse=True -> 9-0, Z-A

# print(numbers)


# takrorlanish operatorlari
# for       - oxiri mavjud yoki oxiri aniq bo'lgan ketma-ketlik(ro'yxat) uchun qo'llaniladi
# while     - oxiri mavjud emas yoki aniq bo'lmagan narsalar uchun qo'llaniladi


# ismlar = ['Alisher', 'Javohir', 'Samandar', 'Shohzafar', 'Ulugbek']

# YOMON USUL !!!
# print( 'Salom', ismlar[0] )  # Salom Alisher
# print( 'Salom', ismlar[1] )  # Salom Javohir
# print( 'Salom', ismlar[2] )  # Salom Samandar
# print( 'Salom', ismlar[3] )  # Salom Shohzafar

# YAXSHI USUL !!!
# for ism in ismlar:  # ismlar ro'yxati ichidan har bir ismni olib uni 'ism' deb ol
#     print('Salom', ism)



# Uyga vazifa list ning barcha metodlarini o'rganib, qo'llab ko'rib, ta'riflarini eslab qolish
# append, insert, remove, pop, index, count, reverse, count, extend, clear

# for operatori bilan list ichidagi qiymatlarni bitta bitta olish va chiqarish ni mashq qilish

# 1
numbers1 = 5
numbers2 = 10
numbers_list = [1, 2, 3, 4, 5]
print ( numbers1 in numbers_list)
print ( numbers2 in numbers_list)
# 2
ismlar =[]

ismlar.append("Alisher")
ismlar.append("Javohir")
print(ismlar)
# 3
ismlar = ["Alisher", "Javohir"]

ismlar.remove("Javohir")
print(ismlar)

# 5 
ismlar = ["Mirjalol", "Bilolidin", "Javohir"]
ismlar.sort()

raqamlar = [10, 6, 5, 4, 3 ,2, 1]
raqamlar.sort()
print(raqamlar)
#6
num1 = int(input("Raqamni kiriting: "))
num2 = int(input("Raqamni kiriting: "))
num3 = int(input("Raqamni kiriting: "))
num4 = int(input("Raqamni kiriting: "))

numbers_list = []

numbers_list.append(num1)
numbers_list.append(num2)
numbers_list.append(num3)
numbers_list.append(num4)

numbers_list.sort()
print(numbers_list)
 # takrorlanish operatorlari
ismlar = ["Mirjalol", "Bilolidin", "Javohir"]

# print("salom" ismlar[1])
# print("salom" ismlar[2])
# print("salom" ismlar[3])
# print("salom" ismlar[4])
for ism in ismlar:
    print("salom", ism)
