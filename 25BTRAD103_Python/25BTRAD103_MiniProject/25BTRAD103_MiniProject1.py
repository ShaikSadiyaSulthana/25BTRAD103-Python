
print("===== UNIT CONVERTER =====")
print("1. Kilometers to Meters")
print("2. Meters to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    meters = km * 1000
    print("Meters =", meters)

elif choice == 2:
    meters = float(input("Enter meters: "))
    km = meters / 1000
    print("Kilometers =", km)

elif choice == 3:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit =", fahrenheit)

elif choice == 4:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius =", celsius)

else:
    print("Invalid choice!")
