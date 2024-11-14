import urllib.request
import pandas as pd

# URL ของไฟล์ CSV
url = "https://app.bot.or.th/BTWS_STAT/statistics/DownloadFile.aspx?file=EC_MB_001_ENG_ALL.CSV"

# ชื่อไฟล์ที่บันทึกหลังจากดาวน์โหลด
file_name = "downloaded_data.csv"

# ดาวน์โหลดไฟล์จาก URL
urllib.request.urlretrieve(url, file_name)

