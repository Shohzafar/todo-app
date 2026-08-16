#   w   -> write    -> fayl ichiga ma'lumot yozish maqsadida (agar shu fayl ichida ma'lumot bo'lgan bo'lsa, unda u eski ma'lumot o'chib ketadi va o'rniga siz yuborgan ma'lumot yoziladi)
#   a   -> append   -> fayl ichidagi ma'lumotni saqlagan holda davomiga ma'lumot yozib qo'shib ketish

# write - misol
fayllar = open("ismlar.txt", "w", encoding="utf-8")

fayllar.write("Anvar\n")
fayllar.write("Dilnoza\n")

fayllar.close()

print("w rejimi ishladi: Eski ismlar o'chdi, faqat Anvar va Dilnoza qoldi.")

# append - misol
fayllar = open("ismlar.txt", "a", encoding="utf-8")

fayllar.write("Jasur\n")
fayllar.write("Shahlo\n")

fayllar.close()

print("jasur va shahlo muvaffaqiyatli qo'shildi")