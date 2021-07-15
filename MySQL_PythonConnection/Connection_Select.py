import mysql.connector

cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='sakila')

cursor = cnx.cursor()
query = ("SELECT * FROM actor")
cursor.execute(query)

for x in cursor:
    print(x)

cursor.close()
cnx.close()