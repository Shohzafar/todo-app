# 1
age = int(input("Yoshingizni kiriting: "))

if age >= 0 and age <= 7:
    print("Siz o'rganuvchisiz")
elif age >= 8 and age <= 12:
    print("Maktabdagi o'quvchi")
elif age >= 13 and age <= 18:
    print("Maktab bitiruvchisi")
elif age >= 19 and age <= 23:
    print("Ish izlovchi")
elif age >= 24 and age <= 60:
    print("Biznesmen")
elif age >= 61 and age <= 80:
    print("Pensioner")
elif age >= 81 and age <= 100:
    print("Umringiz oxiri")
else:
    print("Noto'g'ri yosh kiritdingiz")
# 2 
#--- Ternar operatorlari ---#
username = input("Username: ")

message = "Welcome Admin" if username == "admin" else "Welcome User"

print(message)

# 3
#--- matn metodlari ---#
# upper - matn tarkibidagi barcha harflarni katta qiladi
print("assalomu allaykum" .upper()) # ASSALOMU ALLAYKUM
# lower - matn tarkibidagi barcha harflarni kichiklashtiradi
print("ASSALOMU ALLAYKUM" .lower()) # assalomu allaykum
# title - matn tarkibidagi har bir so'zdagi birinchi harfini katta qilib qolganlarni majburan kichiklashtiradi
print("AssAlOmU AlLaYkUm" .title()) # Assalomu Allaykum
# capitalize - matn tarkibidagi faqat birinchi harfnigina kattalashtiradi
print( "assALOmu ALAYKUM".capitalize() )    # Assalomu alaykum
# replace - matn tarkibidagi biron keraksiz belgini biz istagan belgiga almashtiradi
print( "assalomu*alaykum".replace("*", " ") )  # assalomu alaykum
# strip - matnni ikkala tarafidan biron belgini tozalaydi
print("  Shohzafar Abdiqahhorov " .strip(" ")) # Shohzafar Abdiqahhorov
print("__Shohzafar__" .strip("_")) # Shohzafar Abdiqahhorov
# split - matnni biron belgiga qarab bo'laklarga bo'lib, ro'yxatga aylantirib beradi
print( "Ulugbek, Ravshan, Shahnoza, Shohzafar".split(", ") ) # ["Ulugbek", "Ravshan", "Shahnoza", "Shohzafar"]
# count - matn ichida biron belgi yoki so'zni nechi marta qatnagani yoki uchrayotganini sanab va qaytarib beradi
print("Assalomu Allaykum".count("a"))
# isdigit - matn tarkibida faqat raqam mavjudmi yoki yo'qmi tekshiradi mavjud bo'lsa True mavjud bo'lmasa False qaytaradi
print("Assalomu Allaykum 123" .isdigit()) # False
print("123".isdigit()) # True
print("12 3".isdigit()) # False
print("-123".isdigit()) # False
# isalnum - matn tarkibida faqat harflardan iborat bo'lsa True qaytaradi.
print("Hello".isalpha())
print("Hello123".isalpha())
# isascii - matndagi barcha belgilar ASCII jadvalidagi belgilar bo'lsa True qaytaradi.
print("Hello".isascii()) # True
print("Salom😊".isascii()) # False
# ascii - jadvalni ichiga ingliz alifbosi raqamlar tinish belgilari bo'sh joy kiradi 
print(ascii("Salom")) # 'Salom'
print(ascii("😊")) # '\U0001f60a'
# find - Matn ichidan so'zni qidiradi va indeksini qaytaradi.
text = "Assalomu Allaykum"
print(text.find("Allaykum")) # 9
# startswith - Matn ma'lum so'z bilan boshlansa True qaytaradi.
text = "Assalomu Allaykum"
print(text.startswith("Assalomu")) # True
# endswith - Matn ma'lum so'z bilan tugasa True qaytaradi.
text = "Assalomu Allaykum"
print(text.endswith("Allaykum")) # True
# isalnum - matn faqat harf va raqamlardan iborat bo'lsa True qaytaradi.
print("Hello123".isalnum()) # True
print("Hello 123" .isalnum()) # False Sababi bo'sh joy bor
# len - matndagi satr uzunligini hisoblaydi.
text = "Assalomu Allaykum"
print(len(text)) # 17
