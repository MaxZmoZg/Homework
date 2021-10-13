def even(number):
    even_num = 0
    for i in number:
        if int(i)%2 == 0:
            even_num += int(i)
    return even_num

def odd (number):
    odd_sum = 0
    for oddi in number:
        if int(oddi)%2 != 0:
            odd_sum += int(oddi)
    return odd_sum

def itog():
    number = int(input("Введите число в диапазоне от 0 до 10^20: "))
    if number >= 0 and number <= 10**20:
        print(f"{odd(str(number))} {even(str(number))}")
    else:
        print("За пределами диапозона")
itog()
