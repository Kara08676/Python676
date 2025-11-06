# Блок А.5
def f(n):
    if n < 10:
        print (n)
    else:
        print (n % 10, end = ' ')
        f(n//10)
n = int(input('введите число: '))
print('ответ: ', f(n))

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

