"""
Temperature Status Checker

Takes an ambient temperature input from the user and returns
a message describing the corresponding temperature status.
Raises a custom exception if the input is below absolute zero.
"""


class TemperatureError(Exception):
    '''Raised when the given temperature is below absolute zero (-273.15°C).'''

    def __init__(self, temperature):
        self.temperature = temperature
        self.message = (
            f"A temperature of {temperature}°C is not physically possible. "
            f"It is below absolute zero (-273.15°C / 0 K).")
        super().__init__(self.message)

    def show_error(self):
        # Print a formatted error message with the invalid temperature highlighted
        print(f"Invalid temperature:>>>{self.temperature}<<<")


try:
    temperature_status = None
    temperature = float(input("Enter the temperature in Celsius:"))
    # Validate against absolute zero before checking status ranges
    if temperature < -273.15:
        raise TemperatureError(temperature)

    # Classify temperature into status categories
    if temperature <= 0:
        temperature_status = 'Freezing'
    elif temperature <= 10:
        temperature_status = 'Cold'
    elif temperature <= 20:
        temperature_status = 'Cool'
    elif temperature <= 30:
        temperature_status = 'Warm'
    else:
        temperature_status = 'Hot'
    print(f"temperature_status: {temperature_status}")
except ValueError:
    print("ValueError: Invalid temperature.Please enter the temperature in Celsius by typing the number.")
except TemperatureError as e:
    print(e)
    e.show_error()
else:
    # Runs only if no exception occurred
    Kelvin = temperature + 273.15
    print(f"temperature:{temperature:.1f} C ({Kelvin:.2f} K)")
finally:
    print("Program execution has finished.")
