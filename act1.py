import math

print("welcome to trigonometric Calculator!")
print("You can calculate sine, cosine, and tangent for an angle...")

angle = float(input("Enter the angle (in degrees): "))

radians = math.radians(angle)

sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print(f"Sine of {angle} degrees is: {sine}")
print(f"Cosine of {angle} degrees is: {cosine}")
print(f"Tangent of {angle} degrees is: {tangent}")

print("Job done have a great day!")
