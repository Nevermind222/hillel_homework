list_with_digits = [1, 43, 146, 69, 36, 24, 53, 67, 33, 53, 37, 34]

# solution 1
sum_of_even_digits = 0
for integer in list_with_digits:
    if integer % 2 == 0:
        sum_of_even_digits += integer

print("Solution 1: ", sum_of_even_digits)

# solution 2

result = sum([integer for integer in list_with_digits if integer % 2 == 0])

print("Solution 2: ", result)

