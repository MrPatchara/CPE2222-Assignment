import matplotlib.pyplot as plt

def plot_pie_chart(categories, values):
    # สร้างกราฟวงกลม
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title("กราฟวงกลมแสดงสัดส่วนยอดขายสินค้า")
    plt.axis('equal')  # เพื่อให้กราฟเป็นวงกลมสมบูรณ์
    plt.show()

# ตัวอย่างการใช้งาน
categories = ["สินค้า A", "สินค้า B", "สินค้า C", "สินค้า D"]
values = [1500, 2500, 2000, 1000]
plot_pie_chart(categories, values)