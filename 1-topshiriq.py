# 1 
score = int(input("Baliingizni kiriting: "))

if score > 0 and score <= 59:
    print("Siz yiqildingiz")
elif score >= 60 and score < 80:
    print("Qoniqarli ball")
elif score >= 80 and score < 95:
    print("Yaxshi ball")
elif score >= 95 and score < 100:
    print("A'lo")
else:
    print("Noto'g'ri ball kiritdingiz")

# 2
age = int(input("yoshingizni kiriting: "))
if age > 18:
    print("siz voyaga yetkansiz")
else:
    print("siz voyaga yetmagansiz")
    print(age)
# 3
age=int(input("Yoshingizni kiriting"))
print("siz maktabda o'qiysiz") if age >= 7 and age <=18 else print("siz maktabga o'qimaysiz")