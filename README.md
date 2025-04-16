# 🏨 Hotel Management System

This is a simple Python-based **Hotel Management System** developed using **MySQL** as the backend. It offers an easy-to-use interface for both guests and administrators, streamlining hotel bookings, restaurant services, payments, and record management.

---

## 📌 Features

### 🔹 Guest Interface
- View room types and rates
- Book a room with check-in/check-out validation
- Generate room numbers automatically
- Order food and beverages via a digital restaurant menu
- View and pay bills

### 🔹 Admin Interface
- Insert new customer records
- Update existing bookings
- Delete records after checkout
- View all current bookings
- Maintains all data in a MySQL database

---

## 🖥️ Tech Stack

- **Language:** Python
- **Database:** MySQL
- **Libraries:** `mysql.connector`, `datetime`, `random`

---

## ⚙️ System Requirements

### Software:
- Python 3.x
- MySQL Server
- MySQL Connector for Python

### Hardware:
- Minimum: Any modern laptop/desktop with ≥ 2GB RAM
- Recommended: ≥ 4GB RAM for smooth MySQL operations


---

## 🧪 How the System Works

1. **Homepage**
   - Display menu for Booking, Restaurant, Payment, Admin.

2. **Booking**
   - Collect customer name, phone number, address.
   - Validate check-in and check-out dates.
   - Assign available room number.
   - Store guest details in MySQL.

3. **Restaurant**
   - Display a full digital menu with item prices.
   - Accept orders by item number.
   - Generate total bill for food and link it to the room.

4. **Admin Panel**
   - Insert, update, delete, and display guest records.
   - All data stored in a MySQL `hotel` database.


This project was developed as part of a Computer Science curriculum at **Presidency School Bangalore South** (2021-2022) and was inspired from the project available on GeeksForGeeks
