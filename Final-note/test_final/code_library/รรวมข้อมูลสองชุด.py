#โปรแกรมรวมข้อมูลสองชุดตามคีย์ที่กำหนด
def merge_data(data1, data2, key):
    merged_data = {}
    for item in data1:
        merged_data[item[key]] = item
    for item in data2:
        if item[key] in merged_data:
            merged_data[item[key]].update(item)
    return list(merged_data.values())

# ตัวอย่างข้อมูล
data1 = [
    {"id": 1, "name": "สมชาย", "age": 25},
    {"id": 2, "name": "สมหญิง", "age": 30}
]

data2 = [
    {"id": 1, "city": "กรุงเทพ"},
    {"id": 2, "city": "เชียงใหม่"}
]

merged_data = merge_data(data1, data2, "id")
print("ข้อมูลหลังการรวม:")
for item in merged_data:
    print(item)