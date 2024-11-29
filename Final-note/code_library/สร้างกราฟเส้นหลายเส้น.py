#โปรแกรมสร้างกราฟเส้นหลายเส้นในกราฟเดียว
import matplotlib.pyplot as plt

def plot_multiple_lines(data_sets, labels, x_label, y_label, title):
    for data, label in zip(data_sets, labels):
        plt.plot(data, label=label, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# ตัวอย่างการใช้งาน
data_sets = [
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [12, 22, 32, 42, 52]
]
labels = ["ชุดที่ 1", "ชุดที่ 2", "ชุดที่ 3"]
plot_multiple_lines(data_sets, labels, "เวลา", "ค่า", "กราฟเปรียบเทียบหลายชุด")