# โปรแกรมคำนวณ Factorial และหารโมดูลัสค่าคงที่
# Factorial ที่หารโมดูลัสค่าคงที่
print('Generating Factorial series with modulus operation')
n = int(input("Enter 'n' for Factorial series: "))
mod_val = int(input("Enter modulus value: "))
result = 1
mod_list = []

# คำนวณ Factorial และหาร mod
for i in range(1, n+1):
    result *= i
    mod_list.append(result % mod_val)  # เก็บค่า mod

# แสดงผล
print(f"Factorial series modulus {mod_val}: {mod_list}\n")
