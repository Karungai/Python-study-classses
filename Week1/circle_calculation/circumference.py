import math

def calculate_circumfrence(radius):
    return 2 * math.pi * radius

if __name__== "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circumference = calculate_circumfrence(radius)
    print(f"The circumference of the circle is: {circumference}")
