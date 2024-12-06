# โปรแกรมรับค่าตัวเลขจากผู้ใช้ และคำนวณดัชนีผลรวมของรายการตัวเลข
def calculate_index_sum(numbers):
    index_sum = 0
    for index, value in enumerate(numbers):
        index_sum += index * value
    return index_sum

# รับค่าจากผู้ใช้
numbers = list(map(float, input("ใส่ตัวเลข (คั่นด้วยช่องว่าง): ").split()))
result = calculate_index_sum(numbers)
print(f"ดัชนีผลรวมของรายการคือ: {result:.2f}")