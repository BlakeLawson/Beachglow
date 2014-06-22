import usb.core
import usb.util

dev = usb.core.find()
interface = 0
endpoint = dev[0][(0,0)][0]
address = endpoint.bEndpointAddress
size = endpoint.wMaxPacketSize

if dev is None:
	raise ValueError('Device not found.')
try:
	dev.detach_kernel_driver(interface)
except:
	pass

dev.set_configuration()
usb.util.claim_interface(dev, interface)
# cfg = dev.get_active_configuration()
# intf = cfg[(0,0)]


# while True:
# 	data = dev.read(0x02, 0x0020)
# 	print(data)



# Dependencies usblib (do 'sudo apt-get install usblib-1.0')
# then git clone https://github.com/walac/pyusb.git
# and run 'python setup.py install' in the new repository.

# I think this is ready to recieve input