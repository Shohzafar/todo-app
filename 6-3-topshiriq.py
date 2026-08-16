# 1
def tanishtir(ism, familiya, yosh="18"):
    print(f"ism, {ism}, familiya, {familiya}, yosh, {yosh}")
tanishtir(ism="jasur", familiya="qo'chqorboyev")
tanishtir(ism="jasur", familiya="qo'chqorboyev", yosh=20)
tanishtir(ism="jasur", familiya="qo'chqorboyev", yosh=25)
tanishtir(ism="jasur", familiya="qo'chqorboyev", yosh=27)
# 2
aralash_sonlar = [5, 1, 15, 20, 3, 0, 15]

def sonlar(*hisobla):
    min_num = hisobla[0]
    max_num = hisobla[0]
    
    for num in hisobla[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:  
            max_num = num
            
    return min_num, max_num  

minimal_son, maksimal_son = sonlar(*aralash_sonlar)

print(f"Eng kichik son: {minimal_son}")
print(f"Eng katta son: {maksimal_son}")
# 3
def maxsulot_korsat(nomi, narxi, miqdor=1):
    if nomi == "juxori" or nomi == "pomidor":
        jami_narx = narxi * miqdor
        return jami_narx
    else:
        return f"Kechirasiz, {nomi} do'konimizda yoq."

juxori_narxi = maxsulot_korsat(nomi="juxori", narxi=5000)
print(f"Juxori uchun to'lov: {juxori_narxi} so'm")

pomidor_narxi = maxsulot_korsat(nomi="pomidor", narxi=10000, miqdor=10)  
print(f"Pomidor uchun to'lov: {pomidor_narxi} so'm")
# 4
def ortacha_baholar(*baholar):
    if not baholar:
        return 0
    ortacha_baho = sum(baholar) / len(baholar)
    
    return ortacha_baho

son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
son3 = int(input("3-sonni kiriting: "))
son4 = int(input("4-sonni kiriting: "))

natija = ortacha_baholar(son1, son2, son3, son4)

print(f"Kiritilgan sonlarning o'rtacha bahosi: {natija}")
# 4-2
def ortacha_baholar(*baholar):
    if not baholar:
        return 0
    
    yigindi = sum(baholar)
    miqdori = len(baholar)
    ortacha = yigindi / miqdori
    
    return ortacha

natija = ortacha_baholar(5, 4, 3, 5, 4)
print(f"O'rtacha baho: {natija}")