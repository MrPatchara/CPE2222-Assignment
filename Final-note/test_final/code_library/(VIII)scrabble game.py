# โปรแกรมนี้เป็นโปรแกรมที่ใช้ในการหาคำตอบของโจทย์ที่ 8 ในการทดสอบความรู้ของนักเรียนในวิชา Python Programming
data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
            'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
            'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
            'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
            'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
            'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
            'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

sublists = list(map(lambda i: data_game[i:i + 4], range(0, len(data_game), 4)))

def get_top_n_elements(lst, index, n=4, reverse=True):
    return sorted(lst, key=lambda x: x[index], reverse=reverse)[:n]

top_points = get_top_n_elements(sublists, 1)
print("The highest points in the scrabble game:")
print("\n".join(map(lambda i_ch: f"    {i_ch[0] + 1}) '{top_points[i_ch[0]][0]}' with {top_points[i_ch[0]][1]} points.", enumerate(top_points))))

top_amounts = get_top_n_elements(sublists, 2)
print("\nThe highest amount in the scrabble game:")
print("\n".join(map(lambda i_ch: f"    {i_ch[0] + 1}) '{top_amounts[i_ch[0]][0]}' with {top_amounts[i_ch[0]][2]} pieces.", enumerate(top_amounts))))

lowest_ratios = get_top_n_elements(sublists, 3, reverse=False)
print("\nThe lowest ratio in the scrabble game:")
print("\n".join(map(lambda i_ch: f"    {i_ch[0] + 1}) '{lowest_ratios[i_ch[0]][0]}' with {lowest_ratios[i_ch[0]][3]} percent.", enumerate(lowest_ratios))))
