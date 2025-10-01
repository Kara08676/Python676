# # # Задание 5
# # text = input('введите текст, который нужно преобразовать: ')
# # print(text.lower())

# # # Задание 10:
# # text = input('введите текст, который нужно преобразовать: ')
# # print(text.title())

# text = input('введите предложение, которое нужно преобразовать: ')
# text = text[0].upper() + text[1:]
# b = 0
# for i in text:
#     b = int(text.find(" ")) + 1 
#     text = text[:b] + text[b].upper() + text[b+1:]
# print (text)

text = input('введите предложение, которое нужно преобразовать: ')
text = text[0].upper() + text[1:]
n = text
b = 0
n1 = 0
n = n.replace(' ', '*')
while int(n.count('')) <= int(n.rindex('*')):
    n1 = n.find("*")
    print (n1)