#โปรแกรมสร้างกราฟวงกลมที่สามารถแยกส่วนได้
import matplotlib.pyplot as plt

def plot_pie_with_explode(labels, sizes, explode):
    plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)
    plt.title("กราฟวงกลมพร้อมแยกส่วน")
    plt.axis('equal')  # เพื่อให้วงกลมสมบูรณ์
    plt.show()

# ตัวอย่างการใช้งาน
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 40, 10]
explode = (0, 0.1, 0, 0)  # แยกส่วนของ 'B'
plot_pie_with_explode(labels, sizes, explode)