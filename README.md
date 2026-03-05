# 🚗 Vehicles Management Database

A database system for managing government vehicles, built using SQL and Python.  
The project is designed to organize and manage vehicle data including centers, brands, operating status, and vehicle details.

This project was developed as a **data management solution for vehicle fleets** such as those used in government departments or organizations.

---

## 📊 Database Structure

The database consists of the following main tables:

### 1️⃣ Centers
Stores the administrative centers where vehicles are assigned.

| Field | Type | Description |
|------|------|-------------|
| CenterID | INT | Primary Key |
| CenterName | VARCHAR | Name of the center |

---

### 2️⃣ Brands
Stores vehicle manufacturers.

| Field | Type | Description |
|------|------|-------------|
| BrandID | INT | Primary Key |
| BrandName | VARCHAR | Vehicle brand |

---

### 3️⃣ OperatingStatus
Stores vehicle operational status.

| Field | Type | Description |
|------|------|-------------|
| StatusID | INT | Primary Key |
| StatusName | VARCHAR | Status (Working / Not Working / Out of Service) |

---

### 4️⃣ Vehicles
Stores all vehicle information.

| Field | Type |
|------|------|
| VehicleID | INT (Auto Increment) |
| PlateNumber | VARCHAR |
| WorkLocation | VARCHAR |
| ModelYear | INT |
| CarType | VARCHAR |
| ChassisNumber | VARCHAR |
| EngineNumber | VARCHAR |
| CenterID | INT (FK) |
| BrandID | INT (FK) |
| StatusID | INT (FK) |

---

## 🔗 Database Relationships


Centers --------
> Vehicles
/
Brands ---------/

OperatingStatus --/


Each vehicle is linked to:
- a **Center**
- a **Brand**
- an **Operating Status**

---

## 🐍 Python Data Import

A Python script is used to convert CSV vehicle data into SQL insert statements.

### Requirements
Python 3
pandas

---

## 🧾 Example SQL Query

Retrieve full vehicle data with relationships:

```sql
SELECT 
    v.VehicleID,
    v.PlateNumber,
    v.WorkLocation,
    v.ModelYear,
    v.CarType,
    b.BrandName,
    c.CenterName,
    s.StatusName
FROM Vehicles v
LEFT JOIN Centers c ON v.CenterID = c.CenterID
LEFT JOIN Brands b ON v.BrandID = b.BrandID
LEFT JOIN OperatingStatus s ON v.StatusID = s.StatusID;
```
Vehicles_dp
│
├── database.sql
├── insert.py
├── vehicles.csv
└── README.md
🎯 Features
Structured relational database

Vehicle fleet management

CSV → SQL data migration

Clean normalized schema

Easy reporting using SQL queries

👨‍💻 Author

Hesham Hamdy

Faculty of Artificial Intelligence
Kafrelsheikh University

GitHub:
https://github.com/hishamhamdysad

