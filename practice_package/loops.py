# Задача 1: Сумма четных цифр
def sum_even_digits(number):
    number = abs(number)  # Игнорируем знак числа
    total = 0
    for digit in str(number):  # Проходим по каждой цифре числа
        if int(digit) % 2 == 0:  # Проверяем, является ли цифра четной
            total += int(digit)
    return total

# Задача 2: Количество троек подряд идущих гласных
def count_vowel_triplets(text):
    vowels = "aeiouyAEIOUY"
    count = 0
    for i in range(len(text) - 2):
        if text[i] in vowels and text[i + 1] in vowels and text[i + 2] in vowels:
            count += 1
    return count

# Задача 3: Индекс числа в последовательности Фибоначчи
def find_fibonacci_index(number):
    a, b = 0, 1
    index = 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1

# Задача 4: Удаление подряд идущих дубликатов
def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]  # Добавляем первый символ
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:  # Если текущий символ не равен предыдущему
            result.append(string[i])
    return ''.join(result)
