# โปรแกรมนี้เป็นตัวอย่างการดึงข้อมูลจากหลาย API พร้อมกัน และบันทึกข้อมูลลงไฟล์ JSON
import requests
import json

def fetch_multiple_apis(api_urls, output_file):
    data = {}
    for name, url in api_urls.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data[name] = response.json()
                print(f"ดึงข้อมูลสำเร็จจาก {name}")
            else:
                print(f"ข้อผิดพลาดในการดึงข้อมูลจาก {name}: {response.status_code}")
        except Exception as e:
            print(f"ข้อผิดพลาด: {e}")

    # บันทึกข้อมูลทั้งหมดลงไฟล์ JSON
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"บันทึกข้อมูลลงไฟล์ {output_file} สำเร็จ")

# ตัวอย่างการใช้งาน
api_urls = {
    "Todos": "https://jsonplaceholder.typicode.com/todos",
    "Posts": "https://jsonplaceholder.typicode.com/posts"
}
output_file = "combined_data.json"
fetch_multiple_apis(api_urls, output_file)