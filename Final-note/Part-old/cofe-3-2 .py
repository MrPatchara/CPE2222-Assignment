print("-"*15, "Drawing the right triangle by '*'","-"*15)
print("[To quit the program by pressing '0']")
print("-"*65)
while True:
    height = int(input("Enter the height of right triangle: "))
    
    if height == 0:
        break  # ออกจากลูปเมื่อใส่ 0
    
    for i in range(1, height + 1):
        if i == 1 or i == height:  # วาดเส้นด้านบนสุดหรือฐานของสามเหลี่ยม
            print("*" * i)
        else:  # วาดเส้นด้านในของสามเหลี่ยม
            print("*" + " " * (i - 2) + "*")
