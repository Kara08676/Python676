# Блок А.5
def f(n):
    if n == 0:
        return
    print (n % 10, end = ' ')
    f(n // 10)
n = int(input('введите натуральное число n: '))
print ('Ответ: ')
f(n)

# Блок Б.1
def f():
    x = int(input('введите число последовтельности, если конец, то введите 0: '))
    if x == 0:
        return x 
    mx = f()
    if mx == 0:
        return x
    else: 
        return max(x, mx)

print(f'максимальное число последовательности: {f()}')



