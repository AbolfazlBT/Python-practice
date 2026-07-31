# Number Classification: classify user input as positive, negative, or zero
# Includes exception handling to catch invalid (non-integer) input

# solution 1 (using if-elif-else)
try:
    class_number = None
    number = int(input("Enter a number:"))

    # Classify directly using elif chain
    if number > 0:
        class_number = 'Positive'
    elif number == 0:
        class_number = 'Zero'
    else:
        class_number = 'Negative'
    print(f"The number {number} falls into the {class_number} class")
except ValueError:
    print("Value Error: invalid input expected a numeric value.")
else:
    print("The classification was completed successfully.")
finally:
    print("Program execution has finished")

# Solution 2 (Using Nested if Statements)
try:
    class_number = None
    number = int(input("Enter a number:"))
    # First check sign, then separate zero from positive

    if number >= 0:
        if number == 0:
            class_number = 'zero'
        else:
            class_number = 'Positive'
    else:
        class_number = 'Negative'
    print(f"The number {number} falls into the {class_number} class")
except ValueError:
    print("Value Error: invalid input expected anumeric value.")
else:
    print("The classification was completed successfully.")
finally:
    print("Program execution has finished")
