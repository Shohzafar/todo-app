username = input("Username: ")
parol = input("Parol: ")

attempts = 1

while username != "admin" or parol != 1111:
    attempts += 1

    if attempts >= 3:
        break

    print("sizni tanimadim /n") 
    username = input("Username: ")
    parol = input("Parol: ")

if attempts < 3:
    print("xush kelibsiz")
    print(f"siz {attempts}- urinishda tizimga kirdingiz")
else: 
    print("Siz 3 ta noto'g'ri ueinish qildingiz keyinroq harakat qilib ko'ring")

# Kompyuter son o'ylaydi, ya'ni 'randint' funksiyasi yordamida raqam hosil qilib o'zgaruvchi ichida saqlaydi 1 va 10 orasida
# Foydalanuvchi shu sonni topishi kerak bo'ladi
# Buning uchun kopmyuter foydalanuvchidan son kiritishini so'raydi, masalan: "O'ylangan son nechchi edi ? "
# Agar foydalanuvchi sonni topsa - "Siz yutdingiz !"
# Agar topa olmasa, unda toki topgunga qadar - "Siz topa olmadingiz, qayta urinib ko'ring ..."
# Urinishlar sonini ham saqlab boring
# Agar foydalanuvchi yutsa, unda nafaqat tabrik, balki nechta urinishda topgani haqida ham ma'lumot chiqaring
# Agar foydalanuvchining urinishlar soni 10 ta yoki undan oshib ketsa, unda dastur to'xtashi kerak va urinishlar 10 ta dan oshib ketgani haqida ma'lumot chiqishi kerak
