# Removes vowels from a given text using two different approaches.

def remove_vowels_manual_loop(text):
    """Removes vowels from text using a manual loop."""
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


def remove_vowels_generator_join(text):
    """Removes vowels from text using a generator expression with join()."""
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)


text = input("Enter the text to remove vowels from: ")

print(f"Vowels removed (manual loop): {remove_vowels_manual_loop(text)}")
print(
    f"Vowels removed (generator + join): {remove_vowels_generator_join(text)}")
