def fizz_buzz(number):
    for a in range(1, number+1):
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0:
            print("Fizz")
        else:
            print(a)

while True:
    user_input = input("Введите число или 'exit' для выхода: ")
    if user_input.lower() == 'exit':
        break
    number = int(user_input)
    fizz_buzz(number)


# def fizz_buzz(n):
#     for a in range(1, n+1):
#         if a % 3 == 0 and a % 5 == 0:
#             print("FizzBuzz")
#         elif a % 5 == 0:
#             print("Buzz")
#         elif a % 3 == 0:
#             print("Fizz")
#         else:
#             print(a)
#
#
# n = int(input("Введите число: "))
# result = fizz_buzz(n)
# print(fizz_buzz(n))