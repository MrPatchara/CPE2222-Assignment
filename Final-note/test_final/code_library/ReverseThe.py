# โปรแกรมที่รับข้อความเข้ามาแล้ว reverse ข้อความนั้น
text = str(input())

w = text.split()
revers_w = w[::-1]
revers_text = ' '.join(revers_w)

print(revers_text)