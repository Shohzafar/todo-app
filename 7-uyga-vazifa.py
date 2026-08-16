# 1
def talaba_kartochkasi(**talaba_malumotlari):
    for kalit, qiymat, in talaba_malumotlari.items():
        print(f"{kalit}, {qiymat}")

talaba_kartochkasi(ism="shohzafar", fan="jismoniy tarbiya", baho=5)

# 2
yigindi = lambda x, y: x + y
ayirma  = lambda x, y: x - y
tekshir = lambda x: "Musbat" if x > 0 else ("Manfiy" if x < 0 else "Nol")

print(yigindi(5, 10))   
print(ayirma(10, 5))     
print(tekshir(7))    
print(tekshir(-3))     
print(tekshir(0))  

