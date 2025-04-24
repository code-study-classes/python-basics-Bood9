def calculate_distance(x, y):
    # Находит расстояние между двумя точками на числовой оси
    return abs(y - x)


def calculate_segments(a, b):
    # Находит количество отрезков B, размещенных на отрезке A
    return a // b


def calculate_digit_sum(number):
    # Вычисляет сумму цифр заданного числа
    return sum(map(int, str(abs(number))))


def round_to_multiple(number, multiple):
    # Округляет число до ближайшего кратного указанному значению
    return round(number / multiple) * multiple


def calculate_rect_area(x1, y1, x2, y2):
    # Вычисляет площадь прямоугольника по координатам противоположных вершин
    return abs(x2 - x1) * abs(y2 - y1)
