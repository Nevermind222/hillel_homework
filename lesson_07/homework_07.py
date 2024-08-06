import re

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    result = 0

    while result <= 25:
        result = number * multiplier
        if  result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two_numbers(num1: int, num2: int):
    sum_output = num1 + num2
    return sum_output

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_from_list(list_of_digits: list[int]):
    average_output = sum(list_of_digits)/len(list_of_digits)
    return average_output

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(string_to_reverse: str):
    reversed_output = string_to_reverse[::-1]
    return reversed_output


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def define_longest_word(list_of_words: list[str]):
    sorted_list = sorted(list_of_words, key=lambda x: len(x))
    return sorted_list[-1]


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""From homework 6.4"""
def even_digits_sum(list_with_digits: list[int]):
    sum_of_even_digits = 0
    for integer in list_with_digits:
        if integer % 2 == 0:
            sum_of_even_digits += integer
    return sum_of_even_digits

# task 8
"""From homework 4 task 7"""
def separate_sentences_in_text(text: str):
    separated_sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    for sentence in separated_sentences:
        print(sentence)

# task 9
"""From homework4 task 5"""
def count_uppercase(text: str):
    count_upper = len(re.findall(r'[A-Z]', text))
    return count_upper

# task 10
"""From homework4 task 3"""
def remove_extra_spaces(text: str):
    text = ' '.join(text.split())
    return text

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""