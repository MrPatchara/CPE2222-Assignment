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

print("-" * 150)
header = "Pandas Application"
width = 150
print(header.center(width))

print("-" * 150)
print(f"1) Average of 'Monetary Base' [Only February on Leep Years]: {leap_year_avg:,.0f}")
print("-" * 150)



##################################################
# ข้อ 2
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


print("2) Pandas Series of Annual Average of 'Net Claims on Central Government' [1981-1990]:")
# print the average 1981-1990
print(f"1981 {year_1981_avg:.6f}")
print(f"1982 {year_1982_avg:.6f}")
print(f"1983 {year_1983_avg:.6f}")
print(f"1984 {year_1984_avg:.6f}")
print(f"1985 {year_1985_avg:.6f}")
print(f"1986 {year_1986_avg:.6f}")
print(f"1987 {year_1987_avg:.6f}")
print(f"1988 {year_1988_avg:.6f}")
print(f"1989 {year_1989_avg:.6f}")
print(f"1990 {year_1990_avg:.6f}")
print(f"dtypes: float64")
print("-" * 150)


##################################################
# ข้อ 3
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
print("-" * 150)


##################################################
# ข้อ 4 select only years 2000-2005
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
print("4) Within 6-months window, there must be al least 3 months with 'Claims on Financial Institutions' more than '583,758' [2000-2005]:")
if result:
    for month in result:
        print(month)
print("-" * 150)


##################################################
# ข้อ 5 
# Monthly Data All Years
# select only JAN all years
jan_data = [col for col in data.columns if 'JAN' in col]
# select only FEB all years
feb_data = [col for col in data.columns if 'FEB' in col]
# select only MAR all years
mar_data = [col for col in data.columns if 'MAR' in col]
# select only APR all years
apr_data = [col for col in data.columns if 'APR' in col]
# select only MAY all years
may_data = [col for col in data.columns if 'MAY' in col]
# select only JUN all years
jun_data = [col for col in data.columns if 'JUN' in col]
# select only JUL all years
jul_data = [col for col in data.columns if 'JUL' in col]
# select only AUG all years
aug_data = [col for col in data.columns if 'AUG' in col]
# select only SEP all years
sep_data = [col for col in data.columns if 'SEP' in col]
# select only OCT all years
oct_data = [col for col in data.columns if 'OCT' in col]
# select only NOV all years
nov_data = [col for col in data.columns if 'NOV' in col]
# select only DEC all years
dec_data = [col for col in data.columns if 'DEC' in col]


#Other Liability Data
# JAN
# select data in rows 23 related to JAN
jan_data1 = data.loc[23, jan_data]
# Calculate the min of the JAN data
jan_min = jan_data1.min()
# Calculate the average of the JAN data
jan_avg = jan_data1.mean()
# Calculate the max of the JAN data
jan_max = jan_data1.max()

# FEB
# select data in rows 23 related to FEB
feb_data1 = data.loc[23, feb_data]
# Calculate the min of the FEB data
feb_min = feb_data1.min()
# Calculate the average of the FEB data
feb_avg = feb_data1.mean()
# Calculate the max of the FEB data
feb_max = feb_data1.max()

# MAR
# select data in rows 23 related to MAR
mar_data1 = data.loc[23, mar_data]
# Calculate the min of the MAR data
mar_min = mar_data1.min()
# Calculate the average of the MAR data
mar_avg = mar_data1.mean()
# Calculate the max of the MAR data
mar_max = mar_data1.max()

# APR
# select data in rows 23 related to APR
apr_data1 = data.loc[23, apr_data]
# Calculate the min of the APR data
apr_min = apr_data1.min()
# Calculate the average of the APR data
apr_avg = apr_data1.mean()
# Calculate the max of the APR data
apr_max = apr_data1.max()

# MAY
# select data in rows 23 related to MAY
may_data1 = data.loc[23, may_data]
# Calculate the min of the MAY data
may_min = may_data1.min()
# Calculate the average of the MAY data
may_avg = may_data1.mean()
# Calculate the max of the MAY data
may_max = may_data1.max()

# JUN
# select data in rows 23 related to JUN
jun_data1 = data.loc[23, jun_data]
# Calculate the min of the JUN data
jun_min = jun_data1.min()
# Calculate the average of the JUN data
jun_avg = jun_data1.mean()
# Calculate the max of the JUN data
jun_max = jun_data1.max()

# JUL
# select data in rows 23 related to JUL
jul_data1 = data.loc[23, jul_data]
# Calculate the min of the JUL data
jul_min = jul_data1.min()
# Calculate the average of the JUL data
jul_avg = jul_data1.mean()
# Calculate the max of the JUL data
jul_max = jul_data1.max()

# AUG
# select data in rows 23 related to AUG
aug_data1 = data.loc[23, aug_data]
# Calculate the min of the AUG data
aug_min = aug_data1.min()
# Calculate the average of the AUG data
aug_avg = aug_data1.mean()
# Calculate the max of the AUG data
aug_max = aug_data1.max()

# SEP
# select data in rows 23 related to SEP
sep_data1 = data.loc[23, sep_data]
# Calculate the min of the SEP data
sep_min = sep_data1.min()
# Calculate the average of the SEP data
sep_avg = sep_data1.mean()
# Calculate the max of the SEP data
sep_max = sep_data1.max()

# OCT
# select data in rows 23 related to OCT
oct_data1 = data.loc[23, oct_data]
# Calculate the min of the OCT data
oct_min = oct_data1.min()
# Calculate the average of the OCT data
oct_avg = oct_data1.mean()
# Calculate the max of the OCT data
oct_max = oct_data1.max()

# NOV
# select data in rows 23 related to NOV
nov_data1 = data.loc[23, nov_data]
# Calculate the min of the NOV data
nov_min = nov_data1.min()
# Calculate the average of the NOV data
nov_avg = nov_data1.mean()
# Calculate the max of the NOV data
nov_max = nov_data1.max()

# DEC
# select data in rows 23 related to DEC
dec_data1 = data.loc[23, dec_data]
# Calculate the min of the DEC data
dec_min = dec_data1.min()
# Calculate the average of the DEC data
dec_avg = dec_data1.mean()
# Calculate the max of the DEC data
dec_max = dec_data1.max()

#Other Item(net)
# JAN2
# select data in rows 26 related to JAN
jan_data2 = data.loc[26, jan_data]
# Calculate the min of the JAN data
jan_min2 = jan_data2.min()
# Calculate the average of the JAN data
jan_avg2 = jan_data2.mean()
# Calculate the max of the JAN data
jan_max2 = jan_data2.max()

# FEB2
# select data in rows 26 related to FEB
feb_data2 = data.loc[26, feb_data]
# Calculate the min of the FEB data
feb_min2 = feb_data2.min()
# Calculate the average of the FEB data
feb_avg2 = feb_data2.mean()
# Calculate the max of the FEB data
feb_max2 = feb_data2.max()

# MAR2
# select data in rows 26 related to MAR
mar_data2 = data.loc[26, mar_data]
# Calculate the min of the MAR data
mar_min2 = mar_data2.min()
# Calculate the average of the MAR data
mar_avg2 = mar_data2.mean()
# Calculate the max of the MAR data
mar_max2 = mar_data2.max()

# APR2 
# select data in rows 26 related to APR
apr_data2 = data.loc[26, apr_data]
# Calculate the min of the APR data
apr_min2 = apr_data2.min()
# Calculate the average of the APR data
apr_avg2 = apr_data2.mean()
# Calculate the max of the APR data
apr_max2 = apr_data2.max()

# MAY2
# select data in rows 26 related to MAY
may_data2 = data.loc[26, may_data]
# Calculate the min of the MAY data
may_min2 = may_data2.min()
# Calculate the average of the MAY data
may_avg2 = may_data2.mean()
# Calculate the max of the MAY data
may_max2 = may_data2.max()

# JUN2
# select data in rows 26 related to JUN
jun_data2 = data.loc[26, jun_data]
# Calculate the min of the JUN data
jun_min2 = jun_data2.min()
# Calculate the average of the JUN data
jun_avg2 = jun_data2.mean()
# Calculate the max of the JUN data
jun_max2 = jun_data2.max()

# JUL2
# select data in rows 26 related to JUL
jul_data2 = data.loc[26, jul_data]
# Calculate the min of the JUL data
jul_min2 = jul_data2.min()
# Calculate the average of the JUL data
jul_avg2 = jul_data2.mean()
# Calculate the max of the JUL data
jul_max2 = jul_data2.max()

# AUG2
# select data in rows 26 related to AUG
aug_data2 = data.loc[26, aug_data]
# Calculate the min of the AUG data
aug_min2 = aug_data2.min()
# Calculate the average of the AUG data
aug_avg2 = aug_data2.mean()
# Calculate the max of the AUG data
aug_max2 = aug_data2.max()

# SEP2
# select data in rows 26 related to SEP
sep_data2 = data.loc[26, sep_data]
# Calculate the min of the SEP data
sep_min2 = sep_data2.min()
# Calculate the average of the SEP data
sep_avg2 = sep_data2.mean()
# Calculate the max of the SEP data
sep_max2 = sep_data2.max()

# OCT2
# select data in rows 26 related to OCT
oct_data2 = data.loc[26, oct_data]
# Calculate the min of the OCT data
oct_min2 = oct_data2.min()
# Calculate the average of the OCT data
oct_avg2 = oct_data2.mean()
# Calculate the max of the OCT data
oct_max2 = oct_data2.max()

# NOV2
# select data in rows 26 related to NOV
nov_data2 = data.loc[26, nov_data]
# Calculate the min of the NOV data
nov_min2 = nov_data2.min()
# Calculate the average of the NOV data
nov_avg2 = nov_data2.mean()
# Calculate the max of the NOV data
nov_max2 = nov_data2.max()

# DEC2
# select data in rows 26 related to DEC
dec_data2 = data.loc[26, dec_data]
# Calculate the min of the DEC data
dec_min2 = dec_data2.min()
# Calculate the average of the DEC data
dec_avg2 = dec_data2.mean()
# Calculate the max of the DEC data
dec_max2 = dec_data2.max()

# แสดงผลลัพธ์ 
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']  # เดือน

###### 'Other Liabilities' ######
mean_values_liabilities = [jan_avg, feb_avg, mar_avg, apr_avg, may_avg, jun_avg, jul_avg, aug_avg, sep_avg, oct_avg, nov_avg, dec_avg]  # ค่าเฉลี่ย (mean) ของ 'Other Liabilities'

max_values_liabilities = [jan_max, feb_max, mar_max, apr_max, may_max, jun_max, jul_max, aug_max, sep_max, oct_max, nov_max, dec_max]   # ค่าสูงสุด (max) ของ 'Other Liabilities'

min_values_liabilities = [jan_min, feb_min, mar_min,apr_min, may_min, jun_min, jul_min, aug_min, sep_min, oct_min, nov_min, dec_min ]    # ค่าต่ำสุด (min) ของ 'Other Liabilities'


###### 'Other Items (net)' ######
mean_values_other_items = [jan_avg2, feb_avg2, mar_avg2, apr_avg2, may_avg2, jun_avg2, jul_avg2, aug_avg2, sep_avg2, oct_avg2, nov_avg2, dec_avg2]  # ค่าเฉลี่ย (mean) ของ 'Other Items (net)'

max_values_other_items = [jan_max2, feb_max2, mar_max2, apr_max2, may_max2, jun_max2, jul_max2, aug_max2, sep_max2, oct_max2, nov_max2, dec_max2]   # ค่าสูงสุด (max) ของ 'Other Items (net)'

min_values_other_items = [jan_min2, feb_min2, mar_min2, apr_min2, may_min2, jun_min2, jul_min2, aug_min2, sep_min2, oct_min2, nov_min2, dec_min2]    # ค่าต่ำสุด (min) ของ 'Other Items (net)'

# สร้าง DataFrame
data = {
    ('Other Liabilities to Financial Institutions', 'Min'): min_values_liabilities,
    ('Other Liabilities to Financial Institutions', 'Mean'): mean_values_liabilities,
    ('Other Liabilities to Financial Institutions', 'Max'): max_values_liabilities,
    ('Other Items (net)', 'Min'): min_values_other_items,
    ('Other Items (net)', 'Mean'): mean_values_other_items,
    ('Other Items (net)', 'Max'): max_values_other_items,
}

df = pd.DataFrame(data, index=months)

# แสดงผล
print("5) Pandas Data Frame of monthly minimum, mean, and maximum of 'Other Liabilities to Financial Institutions' and 'Other Items (net)' [Double colum level]:")
print(df)
print("-" * 150)
