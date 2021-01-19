from usbVideoDevice import UsbVideoDevice

usbVideoDevice = UsbVideoDevice()

print("Information List")
usbVideoDevice.dispAllInfo()

print("\nList of port numbers and device IDs")
for port in range(7):
    deviceId = usbVideoDevice.getId_byPort(port)
    if (deviceId != -1):
        print(f"PORT:{port} ID:{deviceId} /dev/video{deviceId}")
        # print("PORT:{} /dev/video{}".format(port, deviceId))

print("Getting All  Web Cam Ids: ", usbVideoDevice.getAllId())  # [2, 0]
