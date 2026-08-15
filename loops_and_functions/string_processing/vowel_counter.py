from collections import Counter


def count_vowels_sum_generator(text):
    """Count total vowels using a generator expression with sum()."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(char in vowels for char in text.lower())


def count_vowels_manual_loop(text):
    """Count vowels per letter using dict comprehension + manual loop."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {v: 0 for v in vowels}
    for char in text.lower():
        if char in vowels:
            counts[char] += 1
    total = sum(counts.values())
    return total, counts


def count_vowels_str_count(text):
    """Count vowels per letter using str.count() inside a dict comprehension."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {v: text.lower().count(v) for v in vowels}
    total = sum(counts.values())
    return total, counts


def count_vowels_counter(text):
    """Count vowels per letter using collections.Counter."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = Counter(c for c in text.lower() if c in vowels)
    # ensure every vowel appears, even with 0
    counts = {v: counts.get(v, 0) for v in vowels}
    total = sum(counts.values())
    return total, counts


text = input("Enter the text: ")

total_sum_generator = count_vowels_sum_generator(text)
total_manual_loop, breakdown_manual_loop = count_vowels_manual_loop(text)
total_str_count, breakdown_str_count = count_vowels_str_count(text)
total_counter, breakdown_counter = count_vowels_counter(text)

print(f"Total vowels (sum + generator): {total_sum_generator}")
print(
    f"Total vowels (manual loop): {total_manual_loop}, breakdown: {breakdown_manual_loop}")
print(
    f"Total vowels (str.count): {total_str_count}, breakdown: {breakdown_str_count}")
print(
    f"Total vowels (Counter): {total_counter}, breakdown: {breakdown_counter}")
