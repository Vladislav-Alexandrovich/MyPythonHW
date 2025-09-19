import math


def square(number):
    return (number * number)

while True:
    user_input = input("Введите длину стороны или 'exit' для выхода: ")
    if user_input.lower() == 'exit':
        break
    number = float(user_input)

    result = math.ceil(square(number))
    print(f"Площадь квадрата равна: {result}")


# import math
#
#
# def square(number):
#     return (number * number)
#
#
# number = float(input("Введите длину стороны: "))
#
#
# result = math.ceil(square(number))
# print(f"Площадь квадрата равна: {result}")