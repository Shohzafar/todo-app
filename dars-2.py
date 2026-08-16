# ...
# 6.  Shart operatorlari
# 7.  Ternar operatorlar
# 8.  Matn metodlari
# 9.  List metodlari
# 10. Takrorlanish operatorlari (while)
# 11. Takrorlanish operatorlari (for)


# age = 20

# if age == 20:
#     print("Siz 20 yoshdasiz !")

# elif age == 21:
#     print("Siz 21 yoshdasiz !")

# else:
#     print("Sizning yoshingiz noma'lum !")


# 0 < yosh < 18 - Siz o'qishingiz kerak
# 18 < yosh < 60 - Siz ishlashingiz kerak
# 60 < yosh < 100 - Siz pernsionersiz
# 100 < yosh YOKI 0 > yosh - Noto'g'ri yosh kiritildi

# age = int(input("Yoshingizni kiriting: "))

# if age > 0 and age <= 18:               # ..., 1, 2, 3, ... 17, 18
#     print("Siz o'qishingiz kerak")

# elif age > 18 and age <= 60:            # 19, 20, ... 59, 60
#     print("Siz ishlashingiz kerak")

# elif age > 60 and age <= 100:           # 61, 62, ... 99, 100, ...
#     print("Siz pernsionersiz")

# else:
#     print("Noto'g'ri yosh kiritildi")



# Foydalanuvchidan ball so'rang
# Agar ball 0 va 59 orasida bo'lsa - "Siz yiqildingiz"
# Agar ball 60 va 80 orasida bo'lsa - "Qoniqarli ball"
# Agar ball 80 va 95 orasida bo'lsa - "Yaxshi ball"
# Agar ball 95 va 100 orasida bo'lsa - "A'lo ball"




# Ternar operatorlar - 1 qatorli if-else shartlari

# Agar foydalnuvchi yoshi 7 dan katta va 18 dan kichik bo'lsa - "Siz maktabda o'qiysiz" deyish kerak, aks holda "Siz maktabda o'qimaysiz" deyish kerak
# age = int(input("Yoshingizni kiriting: "))

# if age >= 7 and age <= 18:
#     print("Siz maktabda o'qiysiz")
# else:
#     print("Siz maktabda o'qimaysiz")

# # Ternar operatorlar
# # harakat1 if shart else harakat2
# print("Siz maktabda o'qiysiz") if age >= 7 and age <= 18 else print("Siz maktabda o'qimaysiz")



# Matn metodlari
# Ulugbek != uLUGBEK != ulugbek != ULUGBEK

# upper - matn tarkibidagi barcha harflarni katta qiladi
print( "assalomu alaykum".upper() )         # ASSALOMU ALAYKUM

# lower - matn tarkibidagi barcha harflarni kichiklashtiradi
print( "ASSALOMU ALAYKUM".lower() )         # assalomu alaykum

# title - matn tarkibidagi har bir so'zni birinchi harfini katta qilib qolganini majburan kichiklashtiradi
print( "uLUGbek UMARAliyev".title() )       # Ulugbek Umaraliyev

# capitalize - matn tarkibidagi faqat birinchi harfnigina kattalashtiradi
print( "assALOmu ALAYKUM".capitalize() )    # Assalomu alaykum

# replace - matn tarkibidagi biron keraksiz belgini biz istagan belgiga almashtiradi
print( "assalomu*alaykum".replace("*", " ") )         # assalomu alaykum

# strip - matnni ikkala tarafidan biron belgini tozalaydi
print( "__Ulugbek_Umaraliev__".strip("_") )           # Ulugbek_Umaraliev
print( "  Ulugbek_Umaraliev  ".strip(" ") )              # Ulugbek_Umaraliev


# split - matnni biron belgiga qarab bo'laklarga bo'lib, ro'yxatga aylantirib beradi
print( "Ulugbek, Ravshan, Shahnoza, Shohzafar".split(", ") )

# ["Ulugbek", "Ravshan", "Shahnoza", "Shohzafar"]