# temparature conversion


# funtion section
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0
def celsius_to_fahrenheit(c):
    return (c * 9.0/5.0) + 32
def kelvin_to_celsius(k):
    return k - 273.15
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5.0/9.0 + 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9.0/5.0 + 32

# main program
def code():
    print("Temperature Conversion Menu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("Type 'exit' to quit.")
    ValueError = "Invalid temperature input."
    
    choice = input("Choose conversion (1-6): ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        temp = float(input("Enter temperature: "))
        try:
            if choice == '1':
                print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius")
            elif choice == '2':
                print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit")
            elif choice == '3':
                print(f"{temp} Kelvin is {kelvin_to_celsius(temp)} Celsius")
            elif choice == '4':
                print(f"{temp} Celsius is {celsius_to_kelvin(temp)} Kelvin")
            elif choice == '5':
                print(f"{temp} Fahrenheit is {fahrenheit_to_kelvin(temp)} Kelvin")
            elif choice == '6':
                print(f"{temp} Kelvin is {kelvin_to_fahrenheit(temp)} Fahrenheit")
            elif choice == 'exit':
                print("Exiting the program.")
                return
        except:
            while choice not in ['1', '2', '3', '4', '5', '6']:
                print(ValueError)
                choice = input("Choose conversion (1-6): ")
                break
            
    # exit program
    elif choice == 'exit':
        print("Exiting the program.")
        return
    return code()

# run the program
code()
