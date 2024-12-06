# โปรแกรมนี้จะเอาไว้เรียงลำดับตัวเลขจากมากไปน้อย
num = []

n = int(input())  

for i in range(n):
    amount = int(input())
    i += 1
    num.append(amount)

num.sort(reverse=True)


for number in num:
    print(number)

#บรรทัดแรกสุดจะเอาไว้บอกว่าจะรับข้อมูลทั้งหมดกี่ตัว