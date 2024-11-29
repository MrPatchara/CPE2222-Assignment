#โปรแกรมสร้างกราฟขั้วเพื่อแสดงข้อมูลในรูปแบบเรขาคณิตขั้ว
import matplotlib.pyplot as plt
import numpy as np

def plot_polar():
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + np.sin(3 * theta)
    plt.polar(theta, r)
    plt.title("กราฟพีชคณิตเชิงขั้ว")
    plt.show()

# ตัวอย่างการใช้งาน
plot_polar()