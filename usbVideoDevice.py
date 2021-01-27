import subprocess

class UsbVideoDevice:
    def __init__(self):

        self.webcams = {'ids': [], 'names': [], }

        try:
            cmd = 'ls -la /dev/v4l/by-id'
            res = subprocess.check_output(cmd.split())
            by_id = res.decode()
        except Exception:
            return

        # Set connected webcam device names and ids
        for line in by_id.split('\n'):
            if('../../video' in line):
                tmp = line.split('usb-')
                tmp = tmp[1].split('-video-index')

                if tmp[0] not in self.webcams['names']:
                    self.webcams['names'].append(tmp[0])

                tmp = tmp[1].split('../../video')

                try:
                    # if tmp[1] not in self.webcams['ids'] and int(tmp[1]) % 2 == 0:
                    self.webcams['ids'].append(int(tmp[1]))
                except ValueError:
                    print("usbVideoDevice.py can't change to int.")

        print("Usb Video Devices:\n", self.webcams)

    # Get connected webcam ids to take images
    def getAllIds(self):
        return self.webcams['ids']
