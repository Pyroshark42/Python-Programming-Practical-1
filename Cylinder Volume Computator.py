# Cylinder Volume Computator

# Measuring the dimensions of the target cylinder
radius = float(input("Enter radius of cylinder base: "))
length = float(input("Enter length of cylinder: "))

# Compute volume of cylinder
pi = 3.141592654
area = radius * radius * pi
volume = area * length

# Display result
print("{0:.2f}".format(volume))