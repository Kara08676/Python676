# Задание 5
text = input('введите текст, который нужно преобразовать: ')
print("Результат: ", text.lower())

# Задание 10:
text = input("введите текст, который нужно изменить: ") 
if text[-1] == " ":
    print("Error: уберите пробел в конце предложения")
else: 
    text1 = text.split(" ")
    n = 0
    m = []
    for i in text1:
        m.append(text1[n][0].upper() + text1[n][1:]) 
        n += 1
    print ("Результат: ", " ".join(m))
