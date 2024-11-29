h = int(input())

for height in range(h):
  for i in range(height + 2):
    space = ' ' * (h - i)
    star = '*' * (2 * i + 1)
    i += 1
    print(space + star)
    
tree_space = ' ' * h
print(f"{tree_space}|")

somthing = '=' * h
print(f"{somthing}V{somthing}")