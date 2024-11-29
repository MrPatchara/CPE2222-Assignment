import matplotlib.pyplot as plt


def plot_graph(data):
    plt.plot(data, marker='o')
    plt.title("กราฟแสดงข้อมูลที่ป้อน")
    plt.xlabel("ดัชนี")
    plt.ylabel("ค่า")
    plt.grid(True)
    plt.show()


# ตัวอย่างการใช้งาน
data = list(map(float, input("ใส่ข้อมูล (ตัวเลขคั่นด้วยช่องว่าง): ").split()))
plot_graph(data)