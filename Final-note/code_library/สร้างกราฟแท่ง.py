import matplotlib.pyplot as plt

def plot_bar_chart(categories, values):
    # สร้างกราฟแท่ง
    plt.bar(categories, values)
    plt.title("กราฟแท่งยอดขายสินค้า")
    plt.xlabel("ประเภทสินค้า")
    plt.ylabel("ยอดขาย")
    plt.show()

# ตัวอย่างการใช้งาน
categories = ["สินค้า A", "สินค้า B", "สินค้า C"]
values = [150, 200, 300]
plot_bar_chart(categories, values)
