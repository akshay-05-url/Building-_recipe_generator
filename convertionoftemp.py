def convert_temperature(temperature, unit):
  
    if unit.upper() == 'F':
        # Fahrenheit to Celsius
        celsius = (temperature - 32) * 5/9
        return round(celsius, 2)
    elif unit.upper() == 'C':
        # Celsius to Fahrenheit
        fahrenheit = (temperature * 9/5) + 32
        return round(fahrenheit, 2)
    else:
        raise ValueError("Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")

# Dynamic input section
try:
    temp_input = float(input("Enter the temperature: "))
    unit_input = input("Enter the unit (F or C): ").strip().upper()

    result = convert_temperature(temp_input, unit_input)

    if unit_input == 'C':
        print(f"{temp_input}°C is {result}°F")
    else:
        print(f"{temp_input}°F is {result}°C")

except ValueError as ve:
    print("Error:", ve)
except Exception:
    print("Something went wrong. Please try again.")