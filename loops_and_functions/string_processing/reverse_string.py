# Reverses a number or string using two different approaches.
# Preserves the negative sign at the beginning of negative numbers.

def reverse_string_slicing(text):
    """Reverse a string using slicing."""
    if text.startswith('-'):
        return '-' + text[1:][::-1]
    return text[::-1]


def reverse_string_join(text):
    """Reverse a string using reversed() combined with join()."""
    if text.startswith('-'):
        return '-' + "".join(reversed(text[1:]))
    return "".join(reversed(text))


text = input("Enter a number or string: ")
print(f"Reversed (slicing): {reverse_string_slicing(text)}")
print(f"Reversed (join): {reverse_string_join(text)}")
