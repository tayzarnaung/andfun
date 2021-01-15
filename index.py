import cv2
from usbVideoDevice import UsbVideoDevice

usbVideoDevice = UsbVideoDevice()

print("Information List")
usbVideoDevice.disp()

print("\nList of port numbers and device IDs")
for port in range(7):
    deviceId = usbVideoDevice.getId(port)
    if (deviceId != -1):
        print(f"PORT:{port} /dev/video{deviceId}")
        # print("PORT:{} /dev/video{}".format(port, deviceId))


        
