def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    inches = centimeters / 2.54
    return inches

def pounds_to_kilograms(pounds):
    kilograms = pounds * 0.45359237
    return kilograms

def kilograms_to_pounds(kilograms):
    pounds = kilograms / 0.45359237
    return pounds

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    inches = centimeters / 2.54
    return inches

def pounds_to_kilograms(pounds):
    kilograms = pounds * 0.45359237
    return kilograms

def kilograms_to_pounds(kilograms):
    pounds = kilograms / 0.45359237
    return pounds


while True:
    print("Choose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Centimeters")
    print("4. Centimeters to Inches")
    print("5. Pounds to Kilograms")
    print("6. Kilograms to Pounds")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C\n")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F\n")
    elif choice == '3':
        inches = float(input("Enter length in inches: "))
        centimeters = inches_to_centimeters(inches)
        print(f"{inches} inches is equal to {centimeters} centimeters\n")
    elif choice == '4':
        centimeters = float(input("Enter length in centimeters: "))
        inches = centimeters_to_inches(centimeters)
        print(f"{centimeters} centimeters is equal to {inches} inches\n")
    elif choice == '5':
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds_to_kilograms(pounds)
        print(f"{pounds} pounds is equal to {kilograms} kilograms\n")
    elif choice == '6':
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} kilograms is equal to {pounds} pounds\n")
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")