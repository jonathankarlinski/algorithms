def is_anagram(first_string, second_string):
    sorted_string1 = first_string.lower()
    sorted_string2 = second_string.lower()

    if not sorted_string1 and not sorted_string2:
        return (sorted_string1, sorted_string2, False)

    sortWord1 = sort_string(sorted_string1)
    sortWord2 = sort_string(sorted_string2)

    if sortWord1 == sortWord2:
        return sortWord1, sortWord2, True
    else:
        return sortWord1, sortWord2, False


def sort_string(string):
    chars = list(string)

    merge_sort(chars)

    sorted_string = ''.join(chars)
    return sorted_string


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
