import psycopg2
from time import gmtime, strftime
from getch import _Getch

def updatedb(num):
	# Set up database connections
	dbconn = psycopg2.connect('dbname=Inventory host=localhost port=5432 user=postgres password=pline')
	cursor = dbconn.cursor()

	for i in range(0, num):
		l = "INSERT INTO sales_record_sale (product, time) VALUES ('water', '" + strftime("%Y-%m-%d %H:%M:%S") + "');"
		
		cursor.execute(l)
		dbconn.commit()
		cursor.execute("SELECT * FROM sales_record_sale")
		
		print(cursor.fetchall())
		print(cursor.statusmessage)

# Convert numpad input (with num lock off) to numbers
def numLockConversion(key):
	pass

def main():
	# Initialize getch to read keypresses
	keyPress = _Getch()	

	while True:
		# Read input
		key = keyPress()

		# Check if the key was pressed with numlock off and convert
		if key == '[':
			numLockConversion(key)
		# For testing only!!!
		elif key == 'q':
			break

		try:
			num = int(key)
			# Update database
			updatedb(num)
		except:
			pass

if __name__ == '__main__':
	main()