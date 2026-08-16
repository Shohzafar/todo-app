# Fayllar bilan ishlash

# Yo'nalishlar 2 xil bo'ladi
# relative(nisbiy)      - siz ishlab turgan faylga nisbatan berilgan yo'nalish (to'liq bo'lmaydi)
# absolute(absolyut)    - tepadan ko'rsatiladigan to'liq yo'nalish

# Faylni 3 xil maqsadda fayllar ochiladi:
#   r   -> read     -> fayl ichidagi ma'lumotlarini o'qish maqsadida
#   w   -> write    -> fayl ichiga ma'lumot yozish maqsadida (agar shu fayl ichida ma'lumot bo'lgan bo'lsa, unda u eski ma'lumot o'chib ketadi va o'rniga siz yuborgan ma'lumot yoziladi)
#   a   -> append   -> fayl ichidagi ma'lumotni saqlagan holda davomiga ma'lumot yozib qo'shib ketish

# file = open(file="ismlar.txt", mode="r")
# information = file.read()
# print(information)


# Foydalanuvchidan ism qabul qilib u ism ismlar.txt
#   faylida mavjudligini tekshiruvchi dastur qilish kerak
# print("Afsus, siz bizni bazamizda topilmadingiz !")
# user_name = input("Ismingiz nima >>> ")

# file = open(file="ismlar.txt", mode="r")

# found = False
# for line in file:
#     name = line.replace("\n", "")

#     if name == user_name:
#         found = True
#         break

# if found:
#     print("Tabriklaymiz, siz bizni bazamizda mavjudsiz !")
# else:
#     print("Afsus, siz bizni bazamizda topilmadingiz !")

file = open("ismlar.txt", "a")

file.write("jonibek")

file.close()

print("odam muvaffaqiyatli qo'shildi")