# Задача 1 - T
# Функция: is_weekend(day)
# Определяет, является ли день выходным (суббота или воскресенье).
def is_weekend(day):
    return day == 6 or day == 7

# Задача 2 - T
# Функция: get_discount(amount)
# Возвращает размер скидки в зависимости от суммы покупки.
def get_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    else:
        return 0

# Задача 3
# Функция: describe_number(n)
# Возвращает строку-описание числа (четность и разрядность).
def describe_number(n):
    even_odd = "четное" if n % 2 == 0 else "нечетное"
    if 1 <= n <= 9:
        return f"{even_odd} однозначное число"
    elif 10 <= n <= 99:
        return f"{even_odd} двузначное число"
    elif 100 <= n <= 999:
        return f"{even_odd} трехзначное число"

# Задача 4 - T
# Функция: convert_to_meters(unitNumber, lengthInUnits)
# Конвертирует длину в указанных единицах в метры.
def convert_to_meters(unitNumber, lengthInUnits):
    if unitNumber == 1:
        return lengthInUnits * 0.1  # дециметр
    elif unitNumber == 2:
        return lengthInUnits * 1000  # километр
    elif unitNumber == 3:
        return lengthInUnits  # метр
    elif unitNumber == 4:
        return lengthInUnits * 0.001  # миллиметр
    elif unitNumber == 5:
        return lengthInUnits * 0.01  # сантиметр

# Задача 5 - T
# Функция: describe_age(age)
# Возвращает возраст прописью с правильным склонением.
def describe_age(age):
    units = age % 10
    if 11 <= age <= 14:
        return f"{age} лет"
    elif units == 1:
        return f"{age} год"
    elif 2 <= units <= 4:
        return f"{age} года"
    else:
        return f"{age} лет"
