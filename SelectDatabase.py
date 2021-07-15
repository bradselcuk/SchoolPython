import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=School;"
    "Trusted_Connection=yes;"
)
print("Opened database successfully")
print(" ")
cursor = conn.execute("select * from student")
# cursor = conn.execute("select count(*) from student")
# cursor = conn.execute("select * from student where city='Adana'")

# for x in cursor: # Ekrana yaz
#     print(x)

with open('your_file.txt', 'w') as f: # Dosyaya yaz
    for item in cursor:
        f.write("%s\n" % item)

