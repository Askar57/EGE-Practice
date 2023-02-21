from itertools import product

# Восьмеричная система счисления пятизначных чисел
num = product('01234567', repeat=5)
k = 0

for n in num:
    numb = ''.join(n)  # Чтобы избавиться от кортежа и сделать строку
    if numb.count('6') == 1 and numb[0] != '0':
        # только одна цифра 6 и в начале числа не должно быть цифры 0
        if '16' not in numb and '36' not in numb and '56' not in numb and '76' not in numb and \
           '61' not in numb and '63' not in numb and '65' not in numb and '67' not in numb:
           # Рядом с 6 недолжно быть нечетной цифры
            k += 1
print(k)
