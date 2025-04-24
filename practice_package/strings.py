# 1. Извлечение имени файла
def extract_file_name(path: str) -> str:
    base = path.split('/')[-1]  # Извлекаем имя файла
    return base[1:].split('.')[0] if base.startswith('.') and '.' in base[1:] else base.split('.')[0]

# 2. Шифрование предложения
def encrypt_sentence(sentence: str) -> str:
    chars = list(sentence)
    result = [''] * len(chars)
    left, right = 0, len(chars) - 1
    turn = True
    for ch in chars:
        if ch.isalpha():
            if turn:
                result[left] = ch
                left += 1
            else:
                result[right] = ch
                right -= 1
            turn = not turn
        else:
            result[left] = ch
            left += 1
    return ''.join(result)

# 3. Проверка скобок
def check_brackets(expression: str) -> int:
    stack = []
    for i, ch in enumerate(expression):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if not stack:
                return i
            stack.pop()
    return 0 if not stack else -1

# 4. Реверс домена
def reverse_domain(domain: str) -> str:
    return '.'.join(domain.split('.')[::-1])

# 5. Подсчет групп гласных
def count_vowel_groups(word: str) -> int:
    vowels = "aeiouyAEIOUY"
    groups = 0
    in_group = False
    for ch in word:
        if ch in vowels:
            if not in_group:
                groups += 1
                in_group = True
        else:
            in_group = False
    return groups
