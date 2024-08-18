import re


def sum_of_integers_in_strings(array: list):
    results = []
    for item in array:
        try:
            sum_of_int = sum(int(number) for number in item.split(','))
            results.append(sum_of_int)

        except ValueError:
            results.append("Can't do this")
    return results


def even_digits_sum(list_with_digits: list[int]):
    sum_of_even_digits = 0
    for integer in list_with_digits:
        if integer % 2 == 0:
            sum_of_even_digits += integer
    return sum_of_even_digits


def separate_sentences_in_text(text: str):
    separated_sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return separated_sentences


def count_uppercase(text: str):
    count_upper = len(re.findall(r'[A-Z]', text))
    return count_upper


def remove_extra_spaces(text: str):
    text = ' '.join(text.split())
    return text
