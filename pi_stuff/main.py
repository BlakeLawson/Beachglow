import psycopg2
import sys
from datetime import datetime
from getch import _Getch

def updatedb(num):
	# Set up database connections
	localdb = psycopg2.connect('dbname=Inventory host=localhost port=5432 user=postgres password=pline')
	local_cursor = localdb.cursor()

	try:
		remotedb = psycopg2.connect('dbname=Inventory host=23.239.9.120 port=5432 user=postgres password=pline')
		remote_cursor = remotedb.cursor()
	except:
		print "Unexpected error:", sys.exc_info()[0]

	date = datetime.now()
	for i in range(0, num):
		l = "INSERT INTO sales_record_sale (product, time) VALUES ('water', '%s');" % date
		
		local_cursor.execute(l)
		localdb.commit()
		
		try:
			remote_cursor.execute(l)
			remotedb.commit()
		except:
			print "Unexpected error:", sys.exc_info()[0]

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
			print "Unexpected error:", sys.exc_info()[0]

if __name__ == '__main__':
	main()