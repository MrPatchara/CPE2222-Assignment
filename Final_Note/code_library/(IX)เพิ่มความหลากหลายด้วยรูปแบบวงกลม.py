# โค้ดสร้างวงกลมแบบง่าย
import math
print('---------- Drawing circles ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    radius = int(input("Please enter the radius (at least 3): "))

    if radius == 0:
        break
    elif radius >= 3:
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if math.sqrt(x**2 + y**2) <= radius:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
    else:
        print("Invalid input. Please enter a radius >= 3.")
