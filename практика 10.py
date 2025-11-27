# вариант 5.1
with open('vvod.txt', 'r') as file:
    siz = file.readline().split()
    n = int(siz[0])
    m = int(siz[1])
    A = []
    for i in range(n):
        lin = file.readline().split()
        B = []
        for j in range (m):
            B.append(int(lin[j]))
        A.append(B)

A_cop1 = [B[:] for B in A]      # копия матрицы для 1 задания

# сравниваем значения между собой в пределе строки и переставляем значения от меньшего к большему
for i in range (n):
    for j in range (m - 1):
        for k in range (j + 1, m):
            if A_cop1[i][j] > A_cop1[i][k]:
                o = A_cop1[i][j]
                A_cop1[i][j] = A_cop1[i][k]
                A_cop1[i][k] = o

A_cop2 = [B[:] for B in A]             # копия матрицы для 2 задания

# находим минимальное значение строки матрицы и заменяем по условию
for i in range(n):
    mn = 0
    for j in range(1, m):
        if A_cop2[i][j] < A_cop2[i][mn]:
            mn = j
    if A_cop2[i][mn] % 2 == 0:
        A_cop2[i][mn] = 0
    else:
        A_cop2[i][mn] = 1


with open('vivod.txt', 'w', encoding = 'utf-8') as file:
    file.write('изначальная матрица:\n')
    for i in range(n):
        for j in range(m):
            file.write(str(A[i][j]) + ' ')
        file.write('\n')

    file.write('преобразованная матрица для задания 1: \n')
    for i in range(n):
        for j in range(m):
            file.write(str(A_cop1[i][j]) + ' ')
        file.write('\n')

    file.write('преобразованная матрица для задания 2: \n')
    for i in range(n):
        for j in range(m):
            file.write(str(A_cop2[i][j]) + ' ')
        file.write('\n')

print("Результаты записаны")