# Задача 1 - L
# Функция: extract_file_name(full_file_name)
# Выделяет имя файла (без расширения) из полного пути.
extract_file_name = lambda full_file_name: full_file_name.split('/')[-1].split('.')[0]

# Задача 2
# Функция: encrypt_sentence(sentence)
# Шифрует строку, помещая символы на четных позициях в начало, а на нечетных - в конец в обратном порядке.
def encrypt_sentence(sentence):
    even_chars = sentence[::2]
    odd_chars = sentence[1::2]
    return even_chars + odd_chars[::-1]

# Задача 3
# Функция: check_brackets(expression)
# Проверяет правильность расстановки круглых скобок в строке.
def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return 0 if not stack else -1

# Задача 4
# Функция: reverse_domain(domain)
# Переворачивает доменное имя (разделенное точками).
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(parts[::-1])

# Задача 5
# Функция: count_vowel_groups(word)
# Считает группы подряд идущих гласных букв.
def count_vowel_groups(word):
    vowels = 'aeiouy'
    word = word.lower()
    groups = 0
    in_group = False
    for char in word:
        if char in vowels:
            if not in_group:
                groups += 1
                in_group = True
        else:
            in_group = False
    return groups
