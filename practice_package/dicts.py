# Задача 1: Подсчёт вхождений буквенных символов в строке
count_char_occurrences = lambda text: {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}

# Задача 2: Объединение двух словарей с обработкой конфликтов
merge_dicts = lambda dict1, dict2, conflict_resolver: {
    **dict1, 
    **{key: conflict_resolver(key, dict1.get(key), val) if key in dict1 else val for key, val in dict2.items()}
}

# Задача 3: Инвертирование словаря
invert_dictionary = lambda original_dict: {value: [key for key, val in original_dict.items() if val == value] 
                                          for value in set(original_dict.values())}

# Задача 4: Форматирование словаря в таблицу
dict_to_table = lambda data_dict, columns: (
    " | ".join([col.upper().ljust(max(len(col), max(len(str(row.get(col, "N/A"))) for row in data_dict.values()))) for col in columns]) + "\n"
    + "|".join(["-" * max(len(col), max(len(str(row.get(col, "N/A"))) for row in data_dict.values())) for col in columns]) + "\n"
    + "\n".join([" | ".join([str(row.get(col, "N/A")).ljust(max(len(col), max(len(str(row.get(col, "N/A"))) for row in data_dict.values()))) for col in columns]) 
                 for row in data_dict.values()])
)

# Задача 5: Рекурсивное обновление словаря
deep_update = lambda base_dict, update_dict: {key: deep_update(base_dict.get(key, {}), value) if isinstance(value, dict) and isinstance(base_dict.get(key, {}), dict) else value 
                                              for key, value in {**base_dict, **update_dict}.items()}
