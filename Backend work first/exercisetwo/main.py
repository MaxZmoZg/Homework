age = int(input("Введите число: "))
if age >= 0 and age <= 200:
    if age != 0 and age not in range(11, 20) and age not in range(111, 120):
        if age % 10 == 1:
            print(str(age) + " год")
        elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
            print(str(age) + " года")
        else:
            print(str(age) + " лет")
    else:
        print(str(age) + " лет")
else:
    print("Больше 200 или меньше 0")
