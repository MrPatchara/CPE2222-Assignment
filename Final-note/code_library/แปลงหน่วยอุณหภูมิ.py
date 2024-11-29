def celsius_to_fahrenheit(celsius):
    # แปลง Celsius เป็น Fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    # แปลง Fahrenheit เป็น Celsius
    return (fahrenheit - 32) * 5/9

# ตัวอย่างการใช้งาน
choice = input("เลือกการแปลง (1: Celsius -> Fahrenheit, 2: Fahrenheit -> Celsius): ")
if choice == '1':
    celsius = float(input("ใส่อุณหภูมิใน Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} °C = {fahrenheit:.2f} °F")
elif choice == '2':
    fahrenheit = float(input("ใส่อุณหภูมิใน Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} °F = {celsius:.2f} °C")
else:
    print("ตัวเลือกไม่ถูกต้อง")
