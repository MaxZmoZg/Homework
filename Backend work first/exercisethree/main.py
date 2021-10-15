import random

number = random.randint(1, 101)
print(number)
max_ = 100
min_ = 1

while True:

    ir = str(input())
    if ir == "Больше":
        min_ = number
        number = random.randint(number, max_)
        print(number)
        continue
    elif ir == "Меньше":
        max_ = number
        number = random.randint(min_, number)
        print(number)
        continue

    if ir == "Верно":
        print('Correct!')
        break
