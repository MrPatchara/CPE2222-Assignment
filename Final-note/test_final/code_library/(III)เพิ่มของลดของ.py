# โปรแกรมที่ใช้ในการแสดงข้อมูลสินค้าในคลังสินค้า
product1 = str(input('Enter the 1st Product Name:'))
price1 = float(input('Enter Price of Product:'))
quantity1 = int(input('Enter Quantity of Product:'))

product2 = str(input('Enter the 2nd Product Name:'))
price2 = float(input('Enter Price of Product:'))
quantity2 = int(input('Enter Quantity of Product:'))

product3 = str(input('Enter the 3st Product Name:'))
price3 = float(input('Enter Price of Product:'))
quantity3 = int(input('Enter Quantity of Product:'))
result = quantity1 + quantity2 + quantity3
total = f"Total Quantity = {result}"

width_product = 25
width_price = 10
width_quantity = 15
width_total = 50

print('--------------------------------------------------')
print('                    Inventory                     ')
print('--------------------------------------------------')
print('             Item             Price      Quantity ')
print('--------------------------------------------------')
print(f"{product1:<{width_product}}{price1:>{width_price}}{quantity1:>{width_quantity}}")
print(f"{product2:<{width_product}}{price2:>{width_price}}{quantity2:>{width_quantity}}")
print(f"{product3:<{width_product}}{price3:>{width_price}}{quantity3:>{width_quantity}}")
print('--------------------------------------------------')
print(f"{total:>{width_total}}")
print('--------------------------------------------------')