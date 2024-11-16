import urllib.request
import pandas as pd

# URL ของไฟล์ CSV
url = "https://app.bot.or.th/BTWS_STAT/statistics/DownloadFile.aspx?file=EC_MB_001_ENG_ALL.CSV"

# ชื่อไฟล์ที่บันทึกหลังจากดาวน์โหลด
file_name = "downloaded_data.csv"

# ดาวน์โหลดไฟล์จาก URL
urllib.request.urlretrieve(url, file_name)

# อ่านไฟล์ CSV 
file_path = 'downloaded_data.csv'
df = pd.read_csv(file_path, skiprows=5) 

# แสดงข้อมูล 5 แถวแรก
print(df.head())

# นําข้อมูลบรรทัดที่ 17
row_17 = df.iloc[17]

# ข้ามคอลัมน์แรกและเปลี่ยนข้อมูลเป็นตัวเลข
values = pd.to_numeric(row_17[1:], errors='coerce')

# คํานวณค่าเฉลี่ย (ignoring NaN)
average = values.mean()

# แสดงค่าเฉลี่ย
print(f"ค่าเฉลี่ยของแถวที่ 17 (เว้นคอลัมน์แรก): {average}")

# แสดงเฉพาะเดือนกุมภาพันธ์ ข้อมูลอยู่บรรทัด 0 ขึ้นต้นด้วย Feb
feb_data = df[df.iloc[:, 0].str.startswith('Feb')]
print(feb_data)









