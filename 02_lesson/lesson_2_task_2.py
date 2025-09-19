def is_year_leap(number):
    return "true" if number % 4 == 0 else "false"


while True:
    user_input = input("Введите год или 'exit' для выхода: ")
    if user_input.lower() == 'exit':
        break
    number = int(user_input)

    result = is_year_leap(number)
    print(f"год {number}: - {result}")



# def is_year_leap(number):
#     return "true" if number % 4 == 0 else "false"
#
#
# number = int(input("Введите год: "))
#
# result = is_year_leap(number)
#
# print(f"год {number}: - {result}")