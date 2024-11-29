#เกมกระดานคลาสสิคที่ผู้เล่นสองคนสามารถเล่นแข่งกันได้
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # ตรวจสอบแถว
    for row in board:
        if all(cell == player for cell in row):
            return True
    # ตรวจสอบคอลัมน์
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # ตรวจสอบแนวทแยง
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"ถึงตาของ {player}")
        row, col = map(int, input("ใส่ตำแหน่ง (row col): ").split())
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"{player} ชนะ!")
                return
            turn += 1
        else:
            print("ตำแหน่งนี้มีคนเลือกแล้ว!")
    print("เสมอกัน!")

# ตัวอย่างการใช้งาน
play_tic_tac_toe()