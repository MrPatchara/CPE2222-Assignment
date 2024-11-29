#โปรแกรมสร้างกราฟพื้นผิว 3 มิติด้วย Matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_surface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # สร้างข้อมูลพื้นผิว
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # พล็อตกราฟ 3 มิติ
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title("กราฟพื้นผิว 3 มิติ")
    plt.show()

# ตัวอย่างการใช้งาน
plot_3d_surface()