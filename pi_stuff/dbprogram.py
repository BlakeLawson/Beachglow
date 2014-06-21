import psycopg2
from time import gmtime, strftime


dbconn = psycopg2.connect('dbname=Inventory host=localhost port=5432 user=postgres password=pline')

cursor = dbconn.cursor()

s = ' '

while s != "q":
	s = raw_input("input:")
	# print(cursor.execute(s))
	if s == "g":
		l = "insert into sales_record_sale (product, time) values ('water', '" + strftime("%Y-%m-%d %H:%M:%S") + "');"
		cursor.execute(l)
		dbconn.commit()
		cursor.execute("select * from sales_record_sale")
		print(cursor.fetchall())
		print(cursor.statusmessage)
