def pascal_triangle(input_number):
    if input_number == 0:
        return [1]

    else:
        previous_row = pascal_triangle(input_number - 1)
        current_row = [1]

        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i - 1] + previous_row[i])

        current_row.append(1)
        return current_row

input_number = int(input("Please Enter Degree of Pascal Triangle: "))
print(f"{pascal_triangle(input_number)}\n")