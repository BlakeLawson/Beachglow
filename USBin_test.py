import usb.core
import usb.util

dev = usb.core.find()

if dev is None:
	raise ValueError('Device not found.')

dev.detach_kernel_driver(0)

dev.set_configuration()

cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

# Dependencies usblib (do 'sudo apt-get install usblib-1.0')
# then git clone https://github.com/walac/pyusb.git
# and run 'python setup.py install' in the new repository.

# I think this is ready to recieve input