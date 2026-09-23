import math

radius = float(input("Enter the radius of the circular garden in meters: "))
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

sqrt_area = math.sqrt(area)
area_rnd_down = math.floor(area)
area_rnd_up = math.ceil(area)

print(f"The area of the circular garden is: {area:.2f} square meters")
print(f"The circumference of the circular garden is: {circumference:.2f} square meters")
print(f"The square root of the area is: {sqrt_area:.2f}")
print(f"The area rounded down to the nearest whole number is: {area_rnd_down} square meters")
print(f"The area rounded up to the nearest whole number is: {area_rnd_up} square meters")


