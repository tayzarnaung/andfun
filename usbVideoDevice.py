import subprocess


class UsbVideoDevice:

    def __init__(self):
        try:
            cmd = 'ls /dev'
            res = subprocess.check_output(cmd.split())

            dev_ls = res.decode()
            dev_ls = dev_ls.split('\n')

            video_dev = [
                video_dev for video_dev in dev_ls if video_dev.startswith('video')]

            # print("Device", video_dev)
            self.video_ids = [int(id[5:]) for id in video_dev]
        except Exception:
            return

    def getAllIds(self):
        return self.video_ids