import re

text_input = str(input())

numa = re.findall(r'\d+', text_input)

num = sum(int(numb) for numb in numa)

result = str(num).zfill(4)
  
print(result)

#อลิสต้องการส่งรหัสบัตรATM ไปให้บ๊อบแต่เพื่อความปลอดภัยจึงได้นำตัวเลขเหล่านั้นมาซ่อนไว้ในประโยคเช่น
#HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA
#ซึ่งตัวเลขที่ถูกซ่อนอยู่จะถูกนำมาบวกกันเป็น
#45+32+458+6+359+1+589+34+80 = 1604
#นั้นคือบ๊อบจะสามารถใช้รหัส 1604 ในการกดรหัสบัตร ATM ได้นั้นเอง
#โดยถ้าหากผลรวมที่ได้น้อยกว่า 4 หลักให้ทำการเติมเลข 0 ไปด้านหน้า