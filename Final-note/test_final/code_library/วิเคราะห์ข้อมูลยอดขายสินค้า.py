# โปรแกรมนี้เป็นตัวอย่างการวิเคราะห์ข้อมูลยอดขายสินค้า
# การวิเคราะห์ข้อมูลยอดขายสินค้า
def analyze_sales(sales_data):
    total_sales = sum(sales_data.values())
    percent_sales = {product: (sales / total_sales) * 100 for product, sales in sales_data.items()}
    return total_sales, percent_sales

# ข้อมูลยอดขายตัวอย่าง
sales_data = {
    "สินค้า A": 1500,
    "สินค้า B": 2000,
    "สินค้า C": 500,
    "สินค้า D": 2500
}

total, percentages = analyze_sales(sales_data)
print(f"ยอดขายรวม: {total} บาท")
print("เปอร์เซ็นต์ยอดขายของแต่ละสินค้า:")
for product, percent in percentages.items():
    print(f"{product}: {percent:.2f}%")