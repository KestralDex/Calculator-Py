unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    unit = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {unit}" )
elif unit=="F":
    unit = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {unit}")
else:
    print("Invalid input")