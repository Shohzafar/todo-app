import math

def kvadrat_yuzi(tomon=1):
 kvadrat_yuzi_top = int(input("kvadrat yuzini kiriting: "))
 print(tomon ** 2)
 print(kvadrat_yuzi_top)

def foydalanuvchi(ism, yosh=18, kasb="o'quvchi"):
 print(f"ism: {ism} yosh: {yosh}, kasb: {kasb}" )
foydalanuvchi('alisher')
foydalanuvchi('alisher', 25)
foydalanuvchi('alisher', 27, "dasturchi")

def yigindi(*sonlar):
 natija = 0
 for son in sonlar:
  natija += son
  return natija
 print(natija)

yigindi()
yigindi(1, 2)
yigindi(1, 2, 3)
yigindi(1, 2, 3, 4)