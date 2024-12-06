import os
import json
import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar
import subprocess
from fuzzywuzzy import process  # ใช้สำหรับ fuzzy search

# ฟังก์ชันสร้างไฟล์ JSON
def generate_code_library_json(folder_path, output_file):
    code_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith((".py", ".cpp", ".java", ".txt")):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                code_data.append({
                    "filename": filename,
                    "description": content.split('\n')[0].strip(),
                    "content_snippet": content
                })
            except Exception as e:
                print(f"ไม่สามารถอ่านไฟล์ {filename} ได้: {e}")
    try:
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(code_data, json_file, ensure_ascii=False, indent=4)
        print(f"สร้างไฟล์ JSON สำเร็จ: {output_file}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการเขียนไฟล์ JSON: {e}")

# ฟังก์ชันค้นหาใน JSON (Fuzzy Search)
def search_code(query, json_file, search_by):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    results = []
    for item in data:
        text_to_search = item[search_by]
        if query.lower() in text_to_search.lower():
            results.append(item)
        elif process.extractOne(query, [text_to_search])[1] > 80:
            results.append(item)
    return results

# ฟังก์ชันบันทึกผลลัพธ์
def save_results(results):
    save_path = "search_results.txt"
    try:
        with open(save_path, "w", encoding="utf-8") as file:
            for result in results:
                file.write(f"Filename: {result['filename']}\nDescription: {result['description']}\n\n")
        messagebox.showinfo("Export Results", f"ผลลัพธ์ถูกบันทึกในไฟล์ {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

# ฟังก์ชันการแสดงผลใน UI
def perform_search(*args):
    query = search_var.get()
    search_by = search_by_var.get()
    results_list.delete(*results_list.get_children())
    if query.strip():
        results = search_code(query, output_file, search_by)
        for result in results:
            results_list.insert("", "end", values=(result["filename"], result["description"]))
        status_label.config(text=f"ค้นพบ {len(results)} รายการ")
    else:
        status_label.config(text="กรุณากรอกคำค้นหา")

# ฟังก์ชันแสดงรายละเอียด
def show_details(event=None):
    selected_item = results_list.focus()
    if selected_item:
        item_data = results_list.item(selected_item)['values']
        filename = item_data[0]
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            if item["filename"] == filename:
                preview_window = tk.Toplevel(root)
                preview_window.title(f"Preview: {item['filename']}")
                preview_text = tk.Text(preview_window, wrap=tk.WORD)
                preview_text.insert(tk.END, item["content_snippet"][:1000])
                preview_text.pack(expand=1, fill=tk.BOTH)
                break

# ตั้งค่าโฟลเดอร์และไฟล์ JSON
folder_path = 'code_library'
output_file = 'code_library.json'

# สร้างไฟล์ JSON
generate_code_library_json(folder_path, output_file)

# UI ส่วนค้นหา
root = tk.Tk()
root.title("Code Search")
root.geometry("900x700")

# Main Frame
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Search Section
search_frame = ttk.Frame(main_frame)
search_frame.pack(fill=tk.X, pady=10)

search_var = tk.StringVar()
search_entry = ttk.Entry(search_frame, textvariable=search_var, width=50)
search_entry.pack(side=tk.LEFT, padx=5)

search_by_var = tk.StringVar(value="filename")
search_by_menu = ttk.Combobox(search_frame, textvariable=search_by_var, values=["filename", "description", "content_snippet"], state="readonly")
search_by_menu.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(search_frame, text="ค้นหา", command=perform_search)
search_button.pack(side=tk.LEFT, padx=5)

# Results Section
results_frame = ttk.Frame(main_frame)
results_frame.pack(fill=tk.BOTH, expand=True)

columns = ("filename", "description")
results_list = ttk.Treeview(results_frame, columns=columns, show="headings", selectmode="browse")
results_list.heading("filename", text="Filename")
results_list.heading("description", text="Description")
results_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=results_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_list.config(yscrollcommand=scrollbar.set)

results_list.bind("<Double-1>", show_details)

# Status Section
status_label = ttk.Label(main_frame, text="พลังที่ยิ่งใหญ่ จะมาพร้อมความกั๊กที่ใหญ่ยิ่ง", anchor="w")
status_label.pack(fill=tk.X, pady=5)

root.mainloop()