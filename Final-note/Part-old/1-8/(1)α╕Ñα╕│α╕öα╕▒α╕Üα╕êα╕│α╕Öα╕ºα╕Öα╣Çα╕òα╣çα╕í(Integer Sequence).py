#โปรแกรมในการรับค่าตัวแปร n ที่เป็นจำนวนเต็มเท่านั้น แล้วใช้การโปรแกรมแบบเวียนซ้ำ (RecursiveProgramming) ในการสร้าง Tuple ที่ประกอบด้วยค่าของลำดับจำนวนเต็มนี้ตั้งแต่ 𝐾0 จนถึง 𝐾𝑛 

def integer_sequence(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return integer_sequence(n-3) + 2 * integer_sequence(n-2) + 4 * integer_sequence(n-1)

def generate_tuple(n):
    return tuple(integer_sequence(i) for i in range(n + 1))

while True:
    n = int(input("Enter 'n' of Integer Sequence : "))
    print(f'A tuple of Integer Sequence [n={n}] is {generate_tuple(n)}\n')
    
    if n == -1:
        break