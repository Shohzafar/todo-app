from random import randint

taxminiy_son = randint(1, 10)
urinish = 0

while True:
    number = int(input("O'ylangan son nechchi edi? "))
    urinish += 1

    if number == taxminiy_son:
        print(f"Siz yutdingiz! Siz sonni {urinish} ta urinishda topdingiz.")
        break

    print("Siz topa olmadingiz, qayta urinib ko'ring...")

    if urinish >= 10:
        print("Urinishlar soni 10 tadan oshib ketdi. Dastur to'xtatildi.")
        print(f"O'ylangan son: {taxminiy_son}")
        break