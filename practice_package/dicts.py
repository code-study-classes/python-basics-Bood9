# Задача 1: Подсчёт вхождений буквенных символов в строке
def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

# Задача 2: Объединение двух словарей с обработкой конфликтов
def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, val in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], val)
        else:
            result[key] = val
    return result

# Задача 3: Инвертирование словаря
def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict.setdefault(value, []).append(key)
    return inverted_dict

# Задача 4: Форматирование словаря в таблицу
def dict_to_table(data_dict, columns):
    # Вычисляем максимальную длину для каждого столбца
    column_widths = {col: len(col) for col in columns}
    for row in data_dict.values():
        for col in columns:
            column_widths[col] = max(column_widths[col], len(str(row.get(col, "N/A"))))
    
    # Формируем заголовок таблицы
    table = " | ".join([col.upper().ljust(column_widths[col]) for col in columns]) + "\n"
    table += "|".join(["-" * column_widths[col] for col in columns]) + "\n"
    
    # Формируем строки таблицы
    for row in data_dict.values():
        table += " | ".join([str(row.get(col, "N/A")).ljust(column_widths[col]) for col in columns]) + "\n"
    
    return table

# Задача 5: Рекурсивное обновление словаря
def deep_update(base_dict, update_dict):
    result = base_dict.copy()  # Начинаем с копии base_dict
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_update(result[key], value)  # Рекурсивно обновляем вложенные словари
        else:
            result[key] = value  # Прямое обновление значения
    return result
