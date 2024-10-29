import math

# Create a nested dictionary for shapes
shapes = {
    "circle": {r: round(math.pi * r**2, 2) for r in range(1, 101)},
    "square": {l: l**2 for l in range(1, 101)},
    "triangle": {l: round((math.sqrt(3) / 4) * l**2, 2) for l in range(1, 101)}
}

while True:
    # Prompt the user to enter a shape
    shape = input("Enter the geometry shape for an area calculation\n[Circle, Square, Triangle]\n[Enter something else to exit this program]: ").strip().lower()
    
    # Check if the shape keyword is valid
    if shape not in shapes:
        print("Exiting program...")
        break

    # Prompt the user to enter the dictionary key (radius or length)
    try:
        index = int(float(input("Enter the dictionary key [1 - 100]: ")))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the index is within the valid range
    if 1 <= index <= 100:
        # Get the area based on the shape and index
        area = shapes[shape][index]
        print(f"The area of {shape.upper()} is {area}")
    else:
        print("!!! The key is out of scope !!!")
        break
