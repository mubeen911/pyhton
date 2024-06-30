import mysql.connector
conn=mysql.connector.connect(host='localhost', username='root',password='pakistan0331')
my_cursor= conn.cursor
conn.commit()
conn.close()
print("connection build")