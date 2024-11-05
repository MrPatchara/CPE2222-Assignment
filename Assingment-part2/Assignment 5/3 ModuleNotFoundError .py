module_name = input("กรุณาใส่ชื่อโมดูลที่ต้องการนำเข้า: ")

try:
    # พยายามนำเข้าโมดูลที่ผู้ใช้ระบุ
    import importlib # นำเข้าโมดูล importlib
    importlib.import_module(module_name) # ถ้าโมดูลไม่มีอยู่ จะเกิด ModuleNotFoundError
except ModuleNotFoundError as e:
    print("เกิดข้อผิดพลาด:", e)
    print("โมดูลที่ระบุไม่พบในระบบ กรุณาตรวจสอบชื่อโมดูลอีกครั้งหรือทำการติดตั้ง")
else:
    print("โมดูลถูกนำเข้าเรียบร้อย")

