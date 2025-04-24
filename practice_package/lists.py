def square_odds(numbers_list):
    result = []
    for num in numbers_list:
        if num % 2 != 0:
            result.append(num ** 2)
    return result


def normalize_names(names_list):
    return [name[0].upper() + name[1:].lower() for name in names_list]


def remove_invalid_emails(email_list):
    valid_emails = []
    for email in email_list:
        if email.count('@') == 1 and len(email) >= 5 and not email.startswith('@') and not email.endswith('@'):
            valid_emails.append(email)
    return valid_emails


def filter_palindromes(words_list):
    return [word for word in words_list if word.lower() == word.lower()[::-1]]


def calculate_factorial(number):
    from math import factorial
    return factorial(number)


def find_common_prefix(strings_list):
    if not strings_list:
        return ""
    prefix = strings_list[0]
    for string in strings_list[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
