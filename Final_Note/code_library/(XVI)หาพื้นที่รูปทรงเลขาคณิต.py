import math

shape_areas = {
    "Circle": {i: round(math.pi * i ** 2, 2) for i in range(1, 101)},
    "Square": {i: i ** 2 for i in range(1, 101)},
    "Triangle": {i: round((math.sqrt(3) / 4) * i ** 2, 2) for i in range(1, 101)}
}

while True:
    shape = input("Enter shape (Circle, Square, Triangle): ").capitalize()
    if shape not in shape_areas:
        print("Shape not in dictionary.")
        break

    try:
        index = int(float(input("Enter the dictionary key [1-100]: ")))
        if 1 <= index <= 100:
            print(f'-' * 50)
            print(f"The area of {shape} with index {index} is:", shape_areas[shape][index])
            print(f'-' * 50)
        else:
            break
    except ValueError:
        break
