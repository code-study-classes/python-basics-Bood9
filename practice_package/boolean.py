# Задача 1 - L
# Функция: check_between_numbers(A, B, C)
# Проверяет, находится ли число B между A и C (строго между, не включая равенство).
check_between_numbers = lambda A, B, C: A < B < C or C < B < A

# Задача 2 - L
# Функция: check_odd_three(number)
# Проверяет, является ли число нечетным трехзначным.
check_odd_three = lambda number: 100 <= abs(number) <= 999 and number % 2 != 0

# Задача 3 - L
# Функция: check_unique_digits(number)
# Проверяет, все ли цифры в трехзначном числе уникальны.
check_unique_digits = lambda number: (
    100 <= abs(number) <= 999 and len(set(str(abs(number)))) == len(str(abs(number)))
)

# Задача 4
# Функция: check_palindrome_number(number)
# Проверяет, является ли число палиндромом.
def check_palindrome_number(number):
    return str(abs(number)) == str(abs(number))[::-1]

# Задача 5 - L
# Функция: check_ascending_digits(number)
# Проверяет, образуют ли цифры числа строго возрастающую последовательность.
check_ascending_digits = lambda number: (
    100 <= abs(number) <= 999 and list(str(abs(number))) == sorted(str(abs(number)))
)
