def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_string = sorted(first_string.lower())
    second_string = sorted(second_string.lower())

    return first_string == second_string


def check_anagram(first_string, second_string):
    sorted_first = ''.join(sorted(first_string.lower()))
    sorted_second = ''.join(sorted(second_string.lower()))

    return sorted_first, sorted_second, is_anagram(first_string, second_string)
