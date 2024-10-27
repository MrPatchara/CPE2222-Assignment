def main():
    # รับสายอักขระ A และ B
    A = input("Please enter the string in A: ")
    B = input("Please enter the string in B: ")

    #print ----------------------------------------
    print("-------------------------------------------")

    # a) จำนวนตัวอักษรของสายอักขระ A ทั้งหมด
    count_A = len(A)
    print(f"A number of character in A is: {count_A}")

    # b) จำนวนตัวอักษรของสายอักขระ B ทั้งหมด ไม่รวมตัวอักษรที่ซ้ำกัน
    count_B = len(set(B))
    print(f"B number of character in B is: {count_B}")
    

    # c) จำนวนตัวอักษรที่อยู่ในสายอักขระ A และ B ทั้งคู่
    common_chars = set(A) & set(B)
    count_common = len(common_chars)
    print(f"A number of character in both A and B is: {count_common}")

    # d) ตัวอักษรที่อยู่ในสายอักขระ A แต่ไม่อยู่ในสายอักขระ B
    only_in_A = set(A) - set(B)
    print(f"Characters in A but not in B is: {{ {', '.join(only_in_A)} }}")

    # e) ตัวอักษรที่อยู่ในสายอักขระ B แต่ไม่อยู่ในสายอักขระ A
    only_in_B = set(B) - set(A)
    print(f"Characters in B but not in A is: {{ {', '.join(only_in_B)} }}")

    # f) ตัวอักษรที่อยู่ในสายอักขระ A หรือ B แต่ไม่อยู่ในทั้ง 2 สายอักขระพร้อมกันทั้งคู่
    exclusive_chars = (set(A) | set(B)) - common_chars
    print(f"Characters in A or B but not in both A and B is: {{ {', '.join(exclusive_chars)} }}")

    # g) ตัวอักษรทั้งหมดที่อยู่ในสายอักขระ A หรือ B
    all_chars = set(A) | set(B)
    print(f"All Characters in A or B is: {{ {', '.join(all_chars)} }}")

if __name__ == "__main__":
    main()
