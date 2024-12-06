# โปรแกรมดึงข้อมูลจาก API และบันทึกข้อมูลลงไฟล์ JSON
import requests
import json

def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
        return None


def save_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"บันทึกข้อมูลลงไฟล์ {filename} เรียบร้อย")

# ตัวอย่างการใช้งาน
url = "https://jsonplaceholder.typicode.com/todos"
data = fetch_api_data(url)
if data:
    save_json_file(data, "todos.json")
