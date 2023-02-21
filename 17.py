with open('17.txt') as f:
    data = [int(i) for i in f]
    sqrtmax = max([i ** 2 for i in data if abs(i) % 10 == 3])
    answer = []
    for i in range(len(data) - 1):
        if (((abs(data[i]) % 10 == 3) and (abs(data[i + 1]) % 10 != 3)) or
            ((abs(data[i]) % 10 != 3) and (abs(data[i + 1]) % 10 == 3))) and \
                (data[i] ** 2 + data[i + 1] ** 2) >= sqrtmax:
            answer.append(data[i] ** 2 + data[i + 1] ** 2)

print(len(answer), max(answer))
