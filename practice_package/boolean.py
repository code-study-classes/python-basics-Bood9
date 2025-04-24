
def is_weekend(day):
    return day in (6, 7)


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    return 0.0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    abs_n = abs(n)
    if abs_n < 10:
        digit = "однозначное"
    elif abs_n < 100:
        digit = "двузначное"
    else:
        digit = "трехзначное"
    
    return f"{parity} {digit} число"


def convert_to_meters(unit_number, length_in_units):
    unit_conversions = {
        1: 0.1,    # дециметр
        2: 1000,   # километр
        3: 1,      # метр
        4: 0.001,  # миллиметр
        5: 0.01    # сантиметр
    }
    
    return length_in_units * unit_conversions.get(unit_number, 0)


def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    
    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    if age % 10 == 0 or age in (11, 12, 13, 14):
        return tens.get(age // 10, '') + " лет"
    
    if 5 <= age % 10 <= 9 or age % 10 == 0:
        return tens.get(age // 10, '') + " " + units.get(age % 10, '') + " лет"
    
    if 2 <= age % 10 <= 4:
        return tens.get(age // 10, '') + " " + units.get(age % 10, '') + " года"
    
    return tens.get(age // 10, '') + " " + units.get(age % 10, '') + " год"


check_between_numbers = lambda A, B, C: min(A, C) < B < max(A, C)

check_odd_three = lambda number: 100 <= abs(number) <= 999 and number % 2 != 0

check_unique_digits = lambda number: len(set(str(abs(number)))) == 3 if 100 <= abs(number) <= 999 else False


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


check_ascending_digits = lambda number: (
    100 <= abs(number) <= 999 and 
    sorted(str(abs(number))) == list(str(abs(number))) and 
    all(x < y for x, y in zip(str(abs(number)), str(abs(number))[1:]))
)
