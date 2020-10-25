import mysql.connector

con = mysql.connector.connect(user="root", password="", host="192.168.0.100", database="bdpython")

cursor = con.cursor()

#cursor.execute("CREATE TABLE example (id INT, data VARCHAR (100))")

#cursor.execute("INSERT INTO example (id, data) VALUES (7, 'DATO7')")

cursor.execute("select * from example")# where `id` = 7")
rows = cursor.fetchall()
for row in rows:
    print(row)



#cursor.execute("delete from example where `id` = 9")

con.commit()
cursor.close()
con.close()

