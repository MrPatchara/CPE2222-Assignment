import pandas as pd

# Read the CSV file, skipping the first 5 rows (metadata rows)
data = pd.read_csv('downloaded_data.csv', skiprows=5)

# Select only the columns that correspond to the years (from DEC 1970 to DEC 2006)
# Assuming the month columns are labeled from 'JAN 1976' to 'DEC 2006 and we want only the 'FEB' columns
feb_data = [col for col in data.columns if 'FEB' in col]


# select only leap years in feb_data
leap_years = [year for year in feb_data if (int(year.split()[1]) % 4 == 0)]

# select data in rows 17 related to leap years
leap_year_data = data.loc[17, leap_years]

# Calculate the average of the leap year data
leap_year_avg = leap_year_data.mean()
print("-" * 95)
print(f"1) Average of 'Monetary Base' [Only February on Leep Years]: {leap_year_avg:,.0f}")
print("-" * 95)

# 2
# select only years 1981 
year_1981 = [col for col in data.columns if '1981' in col]
year_1981_data = data.loc[8, year_1981]
year_1981_avg = year_1981_data.mean()
# select only years 1982
year_1982 = [col for col in data.columns if '1982' in col]
year_1982_data = data.loc[8, year_1982]
year_1982_avg = year_1982_data.mean()
# select only years 1983
year_1983 = [col for col in data.columns if '1983' in col]
year_1983_data = data.loc[8, year_1983]
year_1983_avg = year_1983_data.mean()
# select only years 1984
year_1984 = [col for col in data.columns if '1984' in col]
year_1984_data = data.loc[8, year_1984]
year_1984_avg = year_1984_data.mean()
# select only years 1985
year_1985 = [col for col in data.columns if '1985' in col]
year_1985_data = data.loc[8, year_1985]
year_1985_avg = year_1985_data.mean()
# select only years 1986
year_1986 = [col for col in data.columns if '1986' in col]
year_1986_data = data.loc[8, year_1986]
year_1986_avg = year_1986_data.mean()
# select only years 1987
year_1987 = [col for col in data.columns if '1987' in col]
year_1987_data = data.loc[8, year_1987]
year_1987_avg = year_1987_data.mean()
# select only years 1988
year_1988 = [col for col in data.columns if '1988' in col]
year_1988_data = data.loc[8, year_1988]
year_1988_avg = year_1988_data.mean()
# select only years 1989
year_1989 = [col for col in data.columns if '1989' in col]
year_1989_data = data.loc[8, year_1989]
year_1989_avg = year_1989_data.mean()
# select only years 1990
year_1990 = [col for col in data.columns if '1990' in col]
year_1990_data = data.loc[8, year_1990]
year_1990_avg = year_1990_data.mean()
# print the average 1981-1990
print(f" [1981]: {year_1981_avg:.6f}")
print(f" [1982]: {year_1982_avg:.6f}")
print(f" [1983]: {year_1983_avg:.6f}")
print(f" [1984]: {year_1984_avg:.6f}")
print(f" [1985]: {year_1985_avg:.6f}")
print(f" [1986]: {year_1986_avg:.6f}")
print(f" [1987]: {year_1987_avg:.6f}")
print(f" [1988]: {year_1988_avg:.6f}")
print(f" [1989]: {year_1989_avg:.6f}")
print(f" [1990]: {year_1990_avg:.6f}")
print(f" dtypes: float64")

# 3
# select only years 1991-2005
year_1991_2005 = [col for col in data.columns if '1991' in col or '1992' in col or '1993' in col or '1994' in col or '1995' in col or '1996' in col or '1997' in col or '1998' in col or '1999' in col or '2000' in col or '2001' in col or '2002' in col or '2003' in col or '2004' in col or '2005' in col]
# match the data in row 0 with the selected years 
year_1991_2005_data = data.loc[0, year_1991_2005]

# ฟังก์ชันเพื่อแปลงชื่อคอลัมน์เป็นรูปแบบ 'JAN 1991'
def convert_to_month_year(col_name):
    return col_name

# ฟังก์ชันสำหรับหาค่าที่ลดลงติดต่อกัน 4 เดือน
def find_four_consecutive_decreasing_months(data_series):
    result = []
    for i in range(len(data_series) - 3):  # ต้องลดลง 4 เดือน จึงต้อง -3
        # ตรวจสอบว่ามีการลดลงติดต่อกัน 4 เดือน
        if data_series.iloc[i] > data_series.iloc[i + 1] > data_series.iloc[i + 2] > data_series.iloc[i + 3]:
            # แปลงชื่อคอลัมน์เป็นชื่อเดือน-ปีสุดท้าย
            last_month = convert_to_month_year(data_series.index[i + 3])
            result.append(last_month)
    return result

# ตรวจสอบและแสดงผล
result = find_four_consecutive_decreasing_months(year_1991_2005_data)
print("3) The 3 consecutive monthly decreases of 'Net Foreign Assets'[1991-2005]:")
if result:
    for month in result:
        print(month)
print("-" * 95)


# 4 select only years 2000-2005
year_2000_2005 = [col for col in data.columns if '2000' in col or '2001' in col or '2002' in col or '2003' in col or '2004' in col or '2005' in col]
# match the data in row 3 with the selected years
year_2000_2005_data = data.loc[3, year_2000_2005]


# ฟังก์ชันเพื่อแปลงชื่อคอลัมน์เป็นรูปแบบ 'JAN 2005'
def convert_to_month_year(col_name):
    return col_name

# ฟังก์ชันสำหรับหาค่าในกรอบเวลา 6 เดือน
def find_six_month_windows_with_values(data_series, threshold=583757):
    result = []
    for i in range(len(data_series) - 5):  # ใช้กรอบเวลา 6 เดือน ดังนั้นต้อง -5
        # เลือกค่าภายในกรอบ 6 เดือน
        six_month_window = data_series.iloc[i:i + 6]
        # ตรวจสอบว่ามีอย่างน้อย 3 เดือนที่ค่ามากกว่า threshold
        if (six_month_window > threshold).sum() >= 3:
            # เก็บเดือนสุดท้ายของกรอบ 6 เดือน
            last_month = convert_to_month_year(six_month_window.index[-1])
            result.append(last_month)
    return result

# เรียกใช้ฟังก์ชัน
result = find_six_month_windows_with_values(year_2000_2005_data)
# แสดงผลลัพธ์
print("4) The last month of 6-month windows with at least 3 months above 5,837,577 [2000-2005]:")
if result:
    for month in result:
        print(month)