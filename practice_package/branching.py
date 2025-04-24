# Задача 1 - T
# Функция: is_weekend(day)
# Определяет, является ли день выходным (суббота или воскресенье).
is_weekend = lambda day: day == 6 or day == 7

# Задача 2 - T
# Функция: get_discount(amount)
# Возвращает размер скидки в зависимости от суммы покупки.
get_discount = lambda amount: amount * 0.10 if amount >= 5000 else (amount * 0.05 if amount >= 1000 else 0)

# Задача 3
# Функция: describe_number(n)
# Возвращает строку-описание числа (четность и разрядность).
describe_number = lambda n: f"{'четное' if n % 2 == 0 else 'нечетное'} " + (
    "однозначное число" if 1 <= n <= 9 else (
        "двузначное число" if 10 <= n <= 99 else "трехзначное число"
    )
)

# Задача 4 - T
# Функция: convert_to_meters(unitNumber, lengthInUnits)
# Конвертирует длину в указанных единицах в метры.
convert_to_meters = lambda unitNumber, lengthInUnits: (
    lengthInUnits * 0.1 if unitNumber == 1 else
    (lengthInUnits * 1000 if unitNumber == 2 else
     (lengthInUnits if unitNumber == 3 else
      (lengthInUnits * 0.001 if unitNumber == 4 else
       (lengthInUnits * 0.01 if unitNumber == 5 else 0)))))
       
# Задача 5 - T
# Функция: describe_age(age)
# Возвращает возраст прописью с правильным склонением.
describe_age = lambda age: f"{age} лет" if 11 <= age <= 14 else (
    f"{age} год" if age % 10 == 1 else (
        f"{age} года" if 2 <= age % 10 <= 4 else f"{age} лет"
    )
)
