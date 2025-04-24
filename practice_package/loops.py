# Задача 1: Сумма четных цифр
def sum_even_digits(number):
    return sum(int(digit) for digit in str(abs(number)) if int(digit) % 2 == 0)

# Задача 2: Количество троек подряд идущих гласных
def count_vowel_triplets(text):
    vowels = "aeiouyAEIOUY"
    return sum(1 for i in range(len(text) - 2) if text[i] in vowels and text[i + 1] in vowels and text[i + 2] in vowels)

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
    return ''.join([string[i] for i in range(len(string)) if i == 0 or string[i] != string[i - 1]])
