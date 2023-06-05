def is_palindrome_iterative(word):
    if len(word) != 2:
        return False
    
    first_string, second_string = word
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    
    first_string = sorted(first_string.lower())
    second_string = sorted(second_string.lower())
    
    return first_string == second_string