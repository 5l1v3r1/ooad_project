import sqlite3

connector=sqlite3.connect("admin.db")

c=connector.cursor()

query="select * from login where username='nikhil'"
c.execute(query)
row=c.fetchall()

print(row)
