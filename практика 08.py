# вариант 5.1
n = int(input('введите количество строк(n): '))
m = int(input('введите количество стобцов(m): '))
A = []
for i in range(n):
    B = []
    for j in range (m):
        B.append(int(input(f'введите элемент {i} {j} матрицы: ')))
    A.append(B)

print('изначалная матрица: ')
for i in range(n):
    for j in range(m):
        print (A[i][j], end = ' ')
    print()

# сравниваем значения между собой в пределе строки и переставляем значения от меньшего к большему
for i in range (n):
    for j in range (m - 1):
        for k in range (j + 1, m):
            if A[i][j] > A[i][k]:
                o = A[i][j]
                A[i][j] = A[i][k]
                A[i][k] = o

print('преобразованная матрица для задания 1: ')
for i in range(n):
    for j in range(m):
        print (A[i][j], end = ' ')
    print()

# вариант 5.2
n = int(input('введите количество строк(n): '))
m = int(input('введите количество стобцов(m): '))
C = []
for i in range(n):
    D = []
    for j in range (m):
        D.append(int(input(f'введите элемент {i} {j} матрицы: ')))
    C.append(D)

print('изначалная матрица: ')
for i in range(n):
    for j in range(m):
        print (C[i][j], end = ' ')
    print()

# находим минимальное значение строки матрицы и заменяем по условию
for i in range(n):
    mn = 0
    for j in range(1, m):
        if C[i][j] < C[i][mn]:
            mn = j
    if C[i][mn] % 2 == 0:
        C[i][mn] = 0
    else:
        C[i][mn] = 1

print('преобразованная матрица для задания 2: ')
for i in range(n):
    for j in range(m):
        print(C[i][j], end = ' ')
    print()