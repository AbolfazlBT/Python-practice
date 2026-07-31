"""BMI Calculator

Validates weight and height input, raises BmiError for out-of-range
values, and calculates the corresponding BMI category.
"""


class BmiError(Exception):
    '''Raised when a weight or height value falls outside the physically valid range'''

    def __init__(self, field, value):
        self.value = value
        self.field = field
        message_dic = {
            'weight': '''This weight value is invalid
        because it falls outside the normal range(2kg<weight<500kg).''',
            'height': '''This height value is invalid
        because it falls outside the normal range(0.5m<height<2.8m)'''
        }

        self.message = message_dic.get(field, f"invalid value for{field}")
        super().__init__(self.message)

    def show_error(self):
        # Print a formatted error message with the invalid value highlighted
        print(f"Invalid {self.field} value:>>>{self.value}<<<")


try:
    exceptions = []
    weight = float(input("Enter the weight(kg):"))
    height = float(input("Enter height(m):"))
    bmi_category = None
    # Collect all validation errors instead of stopping at the first one
    if not (2 < weight < 500):
        exceptions.append(BmiError('weight', weight))
    if not (0.5 < height < 2.8):
        exceptions.append(BmiError('height', height))
    if exceptions:
        raise ExceptionGroup('BMI validation faild', exceptions)

    # Classify BMI into standard health categories
    bmi = weight / height ** 2
    if bmi <= 18.5:
        bmi_category = 'Underweight'
    elif bmi <= 24.9:
        bmi_category = 'Normal weight'
    elif bmi <= 29.9:
        bmi_category = 'Overweight'
    elif bmi >= 30:
        bmi_category = 'Obesity'
    print(f"BMI:{bmi: .2f} BMI category: {bmi_category}")
except ValueError:
    print("Invalid input. please enter valid numbers.")
except ExceptionGroup as error:
    for e in error.exceptions:
        print(e)
        e.show_error()
finally:
    print("Program execution has finished.")
