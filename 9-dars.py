sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

natija = list(filter(lambda x: x % 2 == 0 or x % 3  == 0, sonlar))

print(natija)

students = [
    {
     'name': "shohzafar",
    "age": 20,
    },
     {
      "name": "shohzafar",
     "age": 18,
    },
     {
      "name": "shohzafar",
     "age": 25,
    },
     {
      "name": "shohzafar",
     "age": 15,
    },
     {
      "name": "shohzafar",
     "age": 60,
    },
]

from functools import reduce

ages = list(map(lambda x: x.get('age'), students))
sum = sum(ages)
count = len((students))
avg = sum / count

print('studentlarni ortacha yoshi', avg, 'yosh')

file = open(file="ismlar.txt", mode='r')
information = file.read()
print(information)

user_name = input("ismingiz nima >>>")

file = open(file="ismlar.txt", mode="r")

found = False
for line in file:
    name = line.replace("\n", '')

    if name == user_name:
        found = True
        break

if found:
    print('tabriklaymiz siz bizning bazamizda mavjudsiz')
else:
    print('afsus siz bizning bazamizdan topilmadingiz')

# map, filter, reduce


# map - list olib uni har bir elementi bilan malum bir ish bajarib, shakl almashtirilgan yangi list qaytaradi
# [1, 2, 3, 4] -> [1, 4, 9, 16]

# 1-usul (Eng yomon)
# numbers = [1, 2, 3, 4]
# squares = []

# for num in numbers:
#     squares.append(num ** 2)

# print(squares)


# # 2-usul (Optimal usul)
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)


# # 3-usul (Eng qisqa)
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4])))




# filter - biron ketma ketlik ichida biron shart asosida filterdan o'tgan raqamlarni alohida ro'yxat sifatida ajrtaib beradi
# juft_sonlar = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# print(juft_sonlar)


# 2 ga va 3 ga bo'linadigan sonlarni ajratib alohida ro'yxat sifatida saqlang, filter ishlating
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]





# reduce - biron ro'yxat ichida
# 1 * 2 * 3 * 4 * 5 = 5!
# 1 + 2 + 3 + 4 + 5 = ...

students = [
    {
        'name': 'Alex',
        'age': 20,
    },
    {
        'name': 'Sarah',
        'age': 18,
    },
    {
        'name': 'John',
        'age': 25,
    },
]

# avg -> o'rtacha qiymat
# sum -> summasi
# count -> soni

# avg = sum / count

# from functools import reduce

# ages = list(map(lambda x: x.get('age'), students))
# sum = sum(ages)
# count = len(students)

# avg = sum / count

# print( 'Studentlarni ortacha yoshi', avg, 'yosh' )

