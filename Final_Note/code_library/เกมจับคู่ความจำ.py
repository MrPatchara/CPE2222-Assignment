# เกมจับคู่ความจำ
import random

def generate_board(size):
    # สร้างตารางพร้อมคู่ตัวเลข
    numbers = list(range(1, (size * size) // 2 + 1)) * 2
    random.shuffle(numbers)
    return [numbers[i:i + size] for i in range(0, len(numbers), size)]

def print_board(board, revealed):
    # แสดงตาราง
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

def play_memory_game(size):
    board = generate_board(size)
    revealed = [[False] * size for _ in range(size)]
    attempts = 0
    pairs_found = 0

    print("เริ่มเกมจับคู่ความจำ!")
    while pairs_found < (size * size) // 2:
        print_board(board, revealed)
        row1, col1 = map(int, input("เลือกตำแหน่งแรก (row col): ").split())
        row2, col2 = map(int, input("เลือกตำแหน่งที่สอง (row col): ").split())
        attempts += 1

        if board[row1][col1] == board[row2][col2]:
            revealed[row1][col1] = True
            revealed[row2][col2] = True
            pairs_found += 1
            print("จับคู่สำเร็จ!")
        else:
            print("จับคู่ไม่สำเร็จ!")
    
    print(f"คุณชนะเกม! ใช้ความพยายามทั้งหมด {attempts} ครั้ง")

# ตัวอย่างการใช้งาน
play_memory_game(4)  # เล่นเกมในตารางขนาด 4x4