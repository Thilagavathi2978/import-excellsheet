import mysql.connector
import xlrd

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_details"
)
cur = conn.cursor()

loc=("C:\\Users\\ELCOT\\Desktop\\book1.xlsx")

l=list()
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,39):
    l.append(tuple(sheet.row_values(i)))
q="insert into student(rollno,name,percentage,branch)values(%s,%s,%s,%s)"
cur.executemany(q,l)
conn.commit()
conn.close()

