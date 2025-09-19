def month_to_season(number):
    if number <= 2:
        print("ЗИМА")
    elif 3 <= number <= 5:
        print("ВЕСНА")
    elif 6 <= number <= 8:
        print("ЛЕТО")
    elif 9 <= number <= 11:
        print("Осень")
    elif 13 <= number:
        print("В году только 12 месяцев!")
    else:
        print("зима")


while True:
    user_input = input("Введите порядковый номер месяца или 'exit' для выхода: ")

    if user_input.lower() == 'exit':
        break
    number = int(user_input)
    month_to_season(number)


# def month_to_season(number):
#     if number <= 2:
#         print("ЗИМА")
#     elif 3 <= number <= 5:
#         print("ВЕСНА")
#     elif 6 <= number <= 8:
#         print("ЛЕТО")
#     elif 9 <= number <= 11:
#         print("Осень")
#     elif 13 <= number:
#         print("В году только 12 месяцев!")
#     else:
#         print("зима")
#
#
# number = int(input("Введите порядковый номер месяца: "))
# result = month_to_season(number)

