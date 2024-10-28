print("-"*9,'Drawing the square rectangular by "#"',"-"*9)
print('[To quit this program by pressing "0"]')
print("-"*57)
while True:
    size = int(input("Please enter the size:")) 
    
    if size == 0: 
        break
    
    for i in range(size): #วนลูปเพื่อสร้างรูปทรง
        if i == 0 or i == size - 1: #ถ้า i เท่ากับ 0 หรือ i เท่ากับ size - 1 ให้พิมพ์ # ตามขนาดที่ผู้ใช้ใส่
            print("#" * size)  #พิมพ์ # ตามขนาดที่ผู้ใช้ใส่
        else:
            print("#" + " " * (size - 2) + "#") #พิมพ์ # และเว้นวรรคตามขนาดที่ผู้ใช้ใส่
