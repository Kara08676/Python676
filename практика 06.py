# Вариант 5.1
spisok = [int(input(f'введите {i} число: ')) for i in range(1, 11)]
n = 0
for n in range(len(spisok)-1):
    if spisok[n]< 0 and spisok[n+1] < 0:
        print(spisok[n], spisok[n+1])
# Вариант 5.2
spisok1 = [int(input(f'введите {i} целое число: ')) for i in range(1, 11)]
spisok2 = []
for b in spisok1:
    if b not in spisok2:
        spisok2.append(b)
print(spisok2)

# Вариант 8.1
numbers= input('Введите все элементы списка(числа) через пробел: ').split(' ')
summa = 0
product = 1
i = 0
while i < len(numbers):
    summa += int(numbers[i])
    product *= int(numbers[i])
    i += 1
print(summa, product)

# Вариант 8.2
spisok = input('Введите числа через пробел: ').split(' ')
summa = 0
for i in range(len(spisok)):
    summa += float(spisok[i])
sr = summa/len(spisok)
for i in range(len(spisok)):
    if float(spisok[i]) == 0:
        spisok[i] = sr
print(spisok)
