#โปรแกรมจัดกลุ่มข้อมูลสินค้าและแสดงยอดขายรวมในแต่ละหมวดหมู่
from collections import defaultdict

def group_sales_by_category(sales_data):
    grouped_data = defaultdict(float)
    for item in sales_data:
        category = item["category"]
        sales = item["sales"]
        grouped_data[category] += sales
    return grouped_data

# ข้อมูลสินค้าและยอดขาย
sales_data = [
    {"category": "อาหาร", "sales": 1500},
    {"category": "เครื่องดื่ม", "sales": 2000},
    {"category": "อาหาร", "sales": 1000},
    {"category": "เครื่องเขียน", "sales": 800},
    {"category": "เครื่องดื่ม", "sales": 500},
]

grouped_sales = group_sales_by_category(sales_data)
print("ยอดขายรวมในแต่ละหมวดหมู่:")
for category, total_sales in grouped_sales.items():
    print(f"{category}: {total_sales} บาท")