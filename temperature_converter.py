def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    temp_celsius =float( input("enter temperature in Celsius:"))
    print(f"{temp_celsius}°C is {celsius_to_fahrenheit(temp_celsius):.2f}°F")
    print(f"{temp_celsius}°C is {celsius_to_kelvin(temp_celsius):.2f}K")

    temp_fahrenheit =float( input("enter temperature in fahrenheit:"))
    print(f"{temp_fahrenheit}°F is {fahrenheit_to_celsius(temp_fahrenheit):.2f}°C")
    print(f"{temp_fahrenheit}°F is {fahrenheit_to_kelvin(temp_fahrenheit):.2f}K")

    temp_kelvin =float( input("enter temperature in kelvin:"))
    print(f"{temp_kelvin}K is {kelvin_to_celsius(temp_kelvin):.2f}°C")
    print(f"{temp_kelvin}K is {kelvin_to_fahrenheit(temp_kelvin):.2f}°F")