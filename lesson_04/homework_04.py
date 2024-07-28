import re


adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adventures_of_tom_sawyer = ' '.join(adventures_of_tom_sawyer.split())
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count_h = adventures_of_tom_sawyer.count("h")
print(count_h)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

count_upper = len(re.findall(r'[A-Z]', adventures_of_tom_sawyer))
print(count_upper)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index_of_second_tom = adventures_of_tom_sawyer.find("Tom", 1)
print(index_of_second_tom)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawyer_sentences = re.split(r'(?<=[.!?])\s+', adventures_of_tom_sawyer.strip())
'''
Explanation of regex for me in future - ?<= is positive lookbehind assertion, it checks for specified symbols
immediately before the whitespace. \\s+ - checks for whitespace after the specified characters and makes
the split happen on whitespace.
'''

for sentence in adventures_of_tom_sawyer_sentences:
    print(sentence)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adventures_of_tom_sawyer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

found = False
for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith("By the time"):
        found = True
        break
if found:
    print("Yes, there is a sentence that starts with 'By the time'")
else:
    print("No, there is no sentence that starts with 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(len(adventures_of_tom_sawyer_sentences[-1].split()))
