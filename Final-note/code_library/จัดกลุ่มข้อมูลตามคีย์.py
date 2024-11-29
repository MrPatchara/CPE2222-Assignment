#โปรแกรมจัดกลุ่มข้อมูลตามคีย์และสรุปยอดรวมในแต่ละกลุ่ม
from collections import defaultdict

def group_by_key(data, key, value_key):
    grouped_data = defaultdict(int)
    for item in data:
        grouped_data[item[key]] += item[value_key]
    return grouped_data

# ตัวอย่างข้อมูล
data = [
    {"category": "อาหาร", "sales": 1000},
    {"category": "เครื่องดื่ม", "sales": 500},
    {"category": "อาหาร", "sales": 1200},
    {"category": "เครื่องเขียน", "sales": 300}
]

grouped = group_by_key(data, "category", "sales")
print("ยอดขายรวมในแต่ละหมวดหมู่:")
for category, total in grouped.items():
    print(f"{category}: {total} บาท")