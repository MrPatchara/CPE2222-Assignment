#โปรแกรมดึงข้อมูลสภาพอากาศจาก API และแสดงผล
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return weather, temperature
    else:
        print("ไม่สามารถดึงข้อมูลได้")
        return None, None

# ตัวอย่างการใช้งาน
city = input("กรุณาใส่ชื่อเมือง: ")
api_key = "your_api_key_here"  # ใส่ API Key ของคุณ
weather, temp = get_weather(city, api_key)
if weather:
    print(f"สภาพอากาศใน {city}: {weather}, อุณหภูมิ: {temp}°C")