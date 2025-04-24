# Задача 1: Квадраты нечётных чисел
def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]

# Задача 2: Нормализация имён
def normalize_names(names):
    return [name.capitalize() for name in names]

# Задача 3: Фильтрация валидных email-адресов
def remove_invalid_emails(emails):
    return [email for email in emails if email.count('@') == 1 and len(email) >= 5 and email[0] != '@' and email[-1] != '@']

# Задача 4: Фильтрация палиндромов
def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]

# Задача 5: Вычисление факториала
def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Задача 6: Наибольший общий префикс
def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
