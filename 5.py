for n in range(1, 100):
    s = bin(n)[2:]  # Строим двочиную запись числа n
    if s.count('1') % 2 == 0:  # Если сумма цифр четная
        # Дописываем справа 0, а два первых заменяются на 10
        s = '10' + s[2:] + '0'
    else:  # Если сумма цифр нечетная
        # Дописываем справа 1, а два первых заменяются на 11
        s = '11' + s[2:] + '1'

    if int(s, 2) > 40:  # Находим такое число n, при котором R будет больше 40
        print(n)
        break  # Так как надо найти минимальное n