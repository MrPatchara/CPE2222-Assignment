MyI = int(input())


print("#" * MyI)

if MyI >= 2:
    for i in range(MyI - 2):
        print(f"#{' ' * (MyI - 2)}#")
        
if MyI > 1:
    print("#" * MyI)