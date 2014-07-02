from getch import _Getch
import keyboardleds
import commands
import sys

keyPress = _Getch()
#device_path = '/dev/input/by-id/usb-099a_USB_Keypad-event-kbd'
#device_path = '/dev/input/by-path/pci-0000:00:12.0-usb-0:1:1.0-event-kbd'
#device_path = '/dev/input/by-path/pci-0000:00:13.2-usb-0:5:1.0-event'
#ledkit = keyboardleds.LedKit(device_path)



while True:
	# ledkit.num_lock.set()
	#print ledkit.num_lock.get()


	# lock_status = commands.getoutput('xset q | grep LED')[65]

	# if lock_status == '1':
	# 	print "Cap lock on."
	# elif lock_status == '0':
	# 	print "Num lock off."
	# elif lock_status == '2':
	# 	print "numlock"

	# raw_input()


	key = keyPress()
	if key == ';':
		break
	# User the '[' to detect the key pressed with numlock off
	elif key == '[':
		print "in elif"
		rest = sys.stdin.read(1)
		print rest

	print key