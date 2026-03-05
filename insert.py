import pandas as pd

# قراءة الملف
df = pd.read_csv("بيان بسيارات الحملة الميكانيكية بمحافظة كفر الشيخ نهائي نوفمبر 2024.csv", encoding="utf-8-sig")

# تنظيف أسماء الأعمدة
df.columns = df.columns.str.strip()

# إعادة تسمية الأعمدة لتكون سهلة
df = df.rename(columns={
    "م": "ID",
    "المركز": "Center",
    "رقم السيارة": "Plate",
    "مكان العمل": "WorkLocation",
    "الموديل": "Model",
    "الموديل ": "Model",
    "نوع السيارة": "CarType",
    "الماركة": "Brand",
    "الشاسية": "Chassis",
    "الموتور": "Engine",
    "الحالة  ( يعمل / لا يعمل )": "Status"
})

# استخراج القيم الفريدة
centers = df["Center"].dropna().unique()
brands = df["Brand"].dropna().unique()
statuses = df["Status"].dropna().unique()

# إنشاء IDs
center_dict = {v:i+1 for i,v in enumerate(centers)}
brand_dict = {v:i+1 for i,v in enumerate(brands)}
status_dict = {v:i+1 for i,v in enumerate(statuses)}

sql_lines = []

# Centers
for name,id in center_dict.items():
    sql_lines.append(f"INSERT INTO Centers (CenterID, CenterName) VALUES ({id}, '{name}');")

# Brands
for name,id in brand_dict.items():
    sql_lines.append(f"INSERT INTO Brands (BrandID, BrandName) VALUES ({id}, '{name}');")

# Status
for name,id in status_dict.items():
    sql_lines.append(f"INSERT INTO OperatingStatus (StatusID, StatusName) VALUES ({id}, '{name}');")

# Vehicles
for i,row in df.iterrows():

    center_id = center_dict.get(row["Center"])
    brand_id = brand_dict.get(row["Brand"])
    status_id = status_dict.get(row["Status"])

    plate = str(row["Plate"]).replace("'", "")
    work = str(row["WorkLocation"]).replace("'", "")
    model = row["Model"] if pd.notna(row["Model"]) else "NULL"
    cartype = str(row["CarType"]).replace("'", "")
    chassis = str(row["Chassis"]).replace("'", "")
    engine = str(row["Engine"]).replace("'", "")

    sql_lines.append(f"""
INSERT INTO Vehicles
(PlateNumber, WorkLocation, ModelYear, CarType, ChassisNumber, EngineNumber, CenterID, BrandID, StatusID)
VALUES
('{plate}', '{work}', {model}, '{cartype}', '{chassis}', '{engine}', {center_id}, {brand_id}, {status_id});
""")

# حفظ الملف
with open("vehicles_inserts.sql","w",encoding="utf-8") as f:
    for line in sql_lines:
        f.write(line+"\n")

print("SQL file generated: vehicles_inserts.sql")