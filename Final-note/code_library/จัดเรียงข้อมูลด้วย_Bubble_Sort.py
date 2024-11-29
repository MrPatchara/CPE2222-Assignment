#โปรแกรมจัดเรียงตัวเลขโดยใช้ Bubble Sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# รับข้อมูลจากผู้ใช้
numbers = list(map(int, input("ใส่ตัวเลขที่ต้องการจัดเรียง (คั่นด้วยช่องว่าง): ").split()))
sorted_numbers = bubble_sort(numbers)
print(f"ข้อมูลหลังจัดเรียง: {sorted_numbers}")