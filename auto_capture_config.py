import configparser
from tkinter import *
from usbVideoDevice import UsbVideoDevice


usbVideoDevice = UsbVideoDevice()
webcam_ids = usbVideoDevice.getAllIds()

config = configparser.ConfigParser()
# config['content'] = {
#     # 'webcam_id': [0, 2],  # 2
#     'webcam_id': webcam_ids,
#     'img_width': 1280,  # 1280
#     'img_height': 720,  # 720
#     'capture_img_per_sec': 3,
#     'max_img_counter': 20,
#     'save_img_path': '/home/wc/Desktop/code/ML/andfun/images'
# }


window = Tk()
window.title("Webcam Config Settings")
window.geometry('420x240')


def confirm():
    config['content'] = {
        # 'webcam_id': [0, 2],  # 2
        'webcam_id': webcam_ids,
        'img_width': img_width.get(),  # 1280
        'img_height': img_height.get(),  # 720
        'capture_img_per_sec': capture_img_per_sec.get(),
        'max_img_counter': max_img_counter.get(),
        'save_img_path': save_img_path.get()
    }
    window.destroy()


Label(window, text="Imgae Width:").grid(row=0, column=0)
Label(window, text="Image Height:").grid(row=1, column=0)
Label(window, text="Captured Image per second:").grid(row=2, column=0)
Label(window, text="Max Image to capture:").grid(row=3, column=0)
Label(window, text="Saved Image Path:").grid(row=4, column=0)

img_width = Entry(window)
img_width.grid(row=0, column=1, sticky=W)

img_height = Entry(window)
img_height.grid(row=1, column=1, sticky=W)

capture_img_per_sec = Entry(window)
capture_img_per_sec.grid(row=2, column=1, sticky=W)

max_img_counter = Entry(window)
max_img_counter.grid(row=3, column=1, sticky=W)

save_img_path = Entry(window)
save_img_path.grid(row=4, column=1, sticky=W)

Button(window, text="Cancel", command=window.destroy).grid(
    row=5, column=1, sticky=W)
Button(window, text="Confirm", command=confirm).grid(row=5, column=1, sticky=E)

window.mainloop()


with open('auto_capture_config.txt', 'w') as configfile:
    config.write(configfile)

print("Config data is saved to auto_capture_config.txt")
