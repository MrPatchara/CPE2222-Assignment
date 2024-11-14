import urllib.request
import pandas as pd

# URL ของไฟล์ CSV
url = "https://app.bot.or.th/BTWS_STAT/statistics/DownloadFile.aspx?file=EC_MB_001_ENG_ALL.CSV"

# ชื่อไฟล์ที่บันทึกหลังจากดาวน์โหลด
file_name = "downloaded_data.csv"

# ดาวน์โหลดไฟล์จาก URL
urllib.request.urlretrieve(url, file_name)

# อ่านไฟล์ CSV โดยข้ามแถวที่ไม่ต้องการ
df = pd.read_csv(file_name, skiprows=6)

# ตั้งชื่อคอลัมน์ใหม่โดยใช้แถวที่ 6
df.columns = df.iloc[0]
df = df[1:]

# เลือกเฉพาะแถวที่มีข้อมูล 'Monetary Base' (แถวที่ 24)
df = df.iloc[17:18]

# เลือกเฉพาะคอลัมน์ที่มีข้อมูลเดือน (C6 ถึง NP6)
df = df.iloc[:, 2:]

# กรองข้อมูลเพื่อเลือกเฉพาะแถวที่เป็นเดือนกุมภาพันธ์ในปีที่มี 29 วัน (Leap Year)
leap_years = [year for year in range(1900, 2100) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
df_feb_leap = df[(df['Date'].dt.month == 2) & (df['Date'].dt.year.isin(leap_years))]

# คำนวณค่าเฉลี่ยของ 'Monetary Base' ในเดือนกุมภาพันธ์ของปีที่มี 29 วัน
average_monetary_base = df_feb_leap['Monetary Base'].replace('-', pd.NA).astype(float).mean()

print(f"ค่าเฉลี่ยของ 'Monetary Base' ในเดือนกุมภาพันธ์ของปีที่มี 29 วัน: {average_monetary_base}")