FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celcius = (fahrenheit - ) * FAHRENHEIT_TO_CELCIUS_FACTOR
    return celcius
def convert_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F)
        
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit")
        except ValueEroor:
        print("Invalid remperature. Please enter a numeric values.")
if __name__ == "__main__":
main()
