# вариант 5.1
def Ev(x, y):
    while y != 0:
        ost = x % y
        x = y
        y = ost
    return x

a = int(input('введите число A: '))
b = int(input('введите число B: '))
c = int(input('введите число C: '))
d = int(input('введите число D: '))
ch = a * d - c * b
zn = d * b
print(ch//Ev(ch, zn) , '/', zn//Ev(ch, zn))

# вариант 5.2
a = int(input('ввдите число: '))
m = []
for i in range(1, a + 1):
    if a % i == 0:
        m.append(i)
print(" ".join(map(str, m)))