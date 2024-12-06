# โปรแกรมสำหรับสร้าง Identity Matrix
print("=" * 80)
size = int(input("Enter the size of the identity matrix (e.g., 2 or 3): "))

if size > 3:  # ตรวจสอบว่าไม่เกินขนาดที่กำหนด
    print("!!! Error: Maximum supported size for identity matrix is 3 !!!\n")
else:
    # สร้าง Identity Matrix โดยให้ตำแหน่งที่ i == j เป็น 1 และตำแหน่งอื่นเป็น 0
    identity_matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    # แสดงผลลัพธ์ของ Identity Matrix
    print(f"Identity Matrix [{size}x{size}]:")
    for row in identity_matrix:
        print(row)
    print("=" * 80 + "\n")