array_of_str = ['1, 2, 3, 4', '1,2,3,4,50', 'qwerty1,2,3']


def sum_of_integers_in_strings(array: list):
    results = []
    for item in array:
        try:
            sum_of_int = sum(int(number) for number in item.split(','))
            results.append(sum_of_int)

        except ValueError:
            results.append("Can't do this")
    return results



