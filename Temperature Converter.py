# Temperature Converter(from Fahrenheit to Celsius)

# Input of temperature in Fahrenheit
fahrenheit = float(input("Enter Temperature: "))

# Convert Fahrenheit to Celsius
celsius = (5/9) * (fahrenheit - 32)

#print converted temperature
print("{0:.1f}".format(celsius))