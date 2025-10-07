# Student Information System

## Description

This is a simple **Student Information System** built in Python.  
It allows **teachers** to create accounts, login, add student grades, and view grades.  
It also allows **students** to login and view their grades.  
The system uses CSV files to store **user accounts** and **student grade information**.  

---

## Features

1. **Account Management**
   - Create new accounts with username, password, and role (teacher/student)
   - Role-based login restriction (teachers cannot login as students and vice versa)

2. **Teacher Functions**
   - Add student grades
   - View all student grades

3. **Student Functions**
   - View student grades

4. **Data Storage**
   - All data is stored in CSV files:
     - `accountinfo.csv` – stores username, password, role
     - `studentinfo.csv` – stores student number, name, and grades
   - The system automatically creates these CSV files if they do not exist.

5. **Error Handling**
   - Handles invalid inputs with `try/except`
  
  **Notes**
Make sure to enter the role correctly when creating an account (teacher or student).
All grades should be numbers; invalid input is handled gracefully.
