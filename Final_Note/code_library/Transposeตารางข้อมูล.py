#โปรแกรมแปลงแถวข้อมูลเป็นคอลัมน์และคอลัมน์เป็นแถว
def transpose_table(data):
    return list(map(list, zip(*data)))

# ตัวอย่างข้อมูล
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_data = transpose_table(data)
print("ตารางหลัง Transpose:")
for row in transposed_data:
    print(row)