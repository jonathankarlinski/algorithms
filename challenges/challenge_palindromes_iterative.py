def is_palindrome_iterative(word):
    if not word:
        return False

    size = len(word)
    for i in range(size // 2):
        if word[i] != word[size - i - 1]:
            return False

    return True
