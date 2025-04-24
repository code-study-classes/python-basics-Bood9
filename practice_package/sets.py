# Задача 1: Пересечение двух множеств
def find_common_elements(set1, set2):
    return {elem for elem in set1 if elem in set2}

# Задача 2: Проверка на подмножество
def is_superset(set_a, set_b):
    return all(elem in set_a for elem in set_b)

# Задача 3: Удаление дубликатов из списка
def remove_duplicates(items):
    return [x for i, x in enumerate(items) if x not in items[:i]]

# Задача 4: Подсчёт уникальных слов в тексте
def count_unique_words(text):
    return len(set(text.lower().split()))

# Задача 5: Пересечение всех переданных множеств
def find_shared_items(*sets):
    return set.intersection(*sets)
