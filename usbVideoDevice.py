import subprocess


class UsbVideoDevice:
    def __init__(self):
        self.__deviceList = []

        try:
            cmd = 'ls -la /dev/v4l/by-id'
            res = subprocess.check_output(cmd.split())
            by_id = res.decode()
        except Exception:
            return

        try:
            cmd = 'ls -la /dev/v4l/by-path'
            by_path = subprocess.check_output(cmd.split()).decode()
            # print(by_path)
        except Exception:
            return

        # Get device name
        deviceNames = {}
        for line in by_id.split('\n'):
            if('../../video' in line):
                tmp = self.__split(line, ' ')
                if("" in tmp):
                    tmp.remove("")
                name = tmp[8]
                deviceId = tmp[10].replace('../../video', '')
                deviceNames[deviceId] = name

        # Get port number
        for line in by_path.split('\n'):
            if('usb-0' in line):
                # tmp = self.__split(line, '0-usb-0:1.')                
                tmp = line.split('0-usb-0:')
                tmp = tmp[1].split(":")

                # port = int(tmp[0])
                port = float(tmp[0])
                # tmp = self.__split(tmp[1], '../../video')
                tmp = tmp[1].split('../../video')

                deviceId = int(tmp[1])
                if deviceId % 2 == 0:
                    name = deviceNames[str(deviceId)]
                    self.__deviceList.append((deviceId, port, name))

    def __split(self, str, val):
        tmp = str.split(val)
        if('' in tmp):
            tmp.remove('')
        return tmp

    # Display a list of recognized Video devices
    def dispAllInfo(self):
        for (deviceId, port, name) in self.__deviceList:
            print(f'/dev/video{deviceId} port:{port} {name}')
            # print("/dev/video{} port:{} {}".format(deviceId, port, name))

    # Get the Video ID by specifying the port number (1 ..)
    def getId_byPort(self, port):
        for (deviceId, p, _) in self.__deviceList:
            if(p == port):
                return deviceId
        return -1

    def getAllId(self):
        self.ids = []
        for item in self.__deviceList:
            self.ids.append(item[0])
        return self.ids
