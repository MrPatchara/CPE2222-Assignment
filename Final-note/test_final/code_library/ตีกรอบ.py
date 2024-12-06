# โปรแกรมสร้างสี่เหลี่ยมจัตุรัสที่มีขนาดของด้านเท่ากับ N โดยที่ N คือจำนวนเต็มที่รับเข้ามาจากผู้ใช้
MyI = int(input())


print("#" * MyI)

if MyI >= 2:
    for i in range(MyI - 2):
        print(f"#{' ' * (MyI - 2)}#")
        
if MyI > 1:
    print("#" * MyI)