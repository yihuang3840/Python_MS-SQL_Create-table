import pyodbc 
import pandas as pd
import csv
import xlrd


# Read excel
data = pd.read_excel (r"C:\path", keep_default_na = False)   
df = pd.DataFrame(data)

# Database connection
conn = pyodbc.connect(
    Trusted_Connection='no',
    DRIVER='{ODBC Driver 17 for SQL Server}',
    server='Server name',
    DATABASE='DB name',
    UID='USER ID',
    PWD='Password')

cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE teatable_header (
            Date nvarchar(200),
			Month_1 nvarchar(200),
            Month_2 nvarchar(200),
			Month_3 nvarchar(200),
            Month_4 nvarchar(200),
            Month_5 nvarchar(200),
            Month_6 nvarchar(200),
            Month_7 nvarchar(200),
            Month_8 nvarchar(200),
            Month_9 nvarchar(200),
            Month_10 nvarchar(200),
            Month_11 nvarchar(200),
            Month_12 nvarchar(200),
            WorkDayMonth_1 nvarchar(200),
            WorkDayMonth_2 nvarchar(200),
            WorkDayMonth_3 nvarchar(200),
            WorkDayMonth_4 nvarchar(200), 
            WorkDayMonth_5 nvarchar(200), 
            WorkDayMonth_6 nvarchar(200),
            WorkDayMonth_7 nvarchar(200), 
            WorkDayMonth_8 nvarchar(200), 
            WorkDayMonth_9 nvarchar(200), 
            WorkDayMonth_10 nvarchar(200), 
            WorkDayMonth_11 nvarchar(200), 
            WorkDayMonth_12 nvarchar(200) 
            
            )
            ''')

# Insert to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO teatable_header (Date, Month_1, Month_2, Month_3, Month_4, Month_5, Month_6, Month_7, Month_8,
                Month_9, Month_10, Month_11, Month_12, WorkDayMonth_1, WorkDayMonth_2, WorkDayMonth_3, WorkDayMonth_4,
                WorkDayMonth_5, WorkDayMonth_6, WorkDayMonth_7, WorkDayMonth_8, WorkDayMonth_9, WorkDayMonth_10, WorkDayMonth_11,
                WorkDayMonth_12)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                    row.Date,
                    row.Month_1,
                    row.Month_2,
                    row.Month_3,
                    row.Month_4,
                    row.Month_5,
                    row.Month_6,
                    row.Month_7,
                    row.Month_8,
                    row.Month_9,
                    row.Month_10,
                    row.Month_11,
                    row.Month_12,
                    row.WorkDayMonth_1,
                    row.WorkDayMonth_2,
                    row.WorkDayMonth_3,
                    row.WorkDayMonth_4,
                    row.WorkDayMonth_5,
                    row.WorkDayMonth_6,
                    row.WorkDayMonth_7,
                    row.WorkDayMonth_8,
                    row.WorkDayMonth_9,
                    row.WorkDayMonth_10,
                    row.WorkDayMonth_11,
                    row.WorkDayMonth_12
                )
conn.commit()
cursor.close