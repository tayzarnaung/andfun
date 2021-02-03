import configparser
import tkinter as tk
# from tkinter import *
from tkinter import filedialog, messagebox
from usbVideoDevice import UsbVideoDevice


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Webcam Config Settings")

        tk.Label(self, text="Imgae Width:").grid(row=0, column=0)
        tk.Label(self, text="Image Height:").grid(row=1, column=0)
        tk.Label(self, text="Captured Image per second:").grid(row=2, column=0)
        tk.Label(self, text="Max Image to capture:").grid(row=3, column=0)
        tk.Label(self, text="Saved Image Path:").grid(row=4, column=0)

        is_digit = self.register(self.only_numbers)
        self.img_width = tk.Entry(
            self, validate='key', validatecommand=(is_digit, '%S'))
        self.img_width.grid(row=0, column=1, sticky=tk.W, padx=20, pady=20)

        self.img_height = tk.Entry(
            self, validate='key', validatecommand=(is_digit, '%S'))
        self.img_height.grid(row=1, column=1, sticky=tk.W, padx=20, pady=20)

        self.capture_img_per_sec = tk.Entry(
            self, validate='key', validatecommand=(is_digit, '%S'))
        self.capture_img_per_sec.grid(
            row=2, column=1, sticky=tk.W, padx=20, pady=20)

        self.max_img_counter = tk.Entry(self)
        self.max_img_counter.config(
            validate='key', validatecommand=(is_digit, '%S'))
        self.max_img_counter.grid(
            row=3, column=1, sticky=tk.W, padx=20, pady=20)

        self.dir_txt = tk.StringVar()
        self.save_img_path = tk.Button(
            self, text='Browse', command=self.browse)
        self.save_img_path.grid(row=4, column=1, sticky=tk.W, padx=20, pady=20)

        if self.dir_txt:
            tk.Label(self, textvar=self.dir_txt,
                     fg='blue').grid(row=5, column=1)

        tk.Button(self, text="Cancel", command=self.destroy).grid(
            row=6, column=1, sticky=tk.W, padx=20, pady=20)
        tk.Button(self, text="Confirm", bg='blue', fg='white', command=self.confirm).grid(
            row=6, column=1, sticky=tk.E, padx=20, pady=20)

    def browse(self):
        self.dir_selected = filedialog.askdirectory()
        self.dir_txt.set(self.dir_selected)
        print(self.dir_txt.get())

    def only_numbers(self, char):
        return char.isdigit()

    def confirm(self):
        # if False:     # Test
        #     return

        if not self.img_width.get() or not self.img_height.get() or not self.capture_img_per_sec.get() or not self.max_img_counter.get():
            messagebox.showerror("Error", "Entry fields cannot be empty.")

        elif not self.dir_txt.get():
            messagebox.showwarning('Error', "Saved image path is required.")

        else:
            self.capture_img_per_sec = self.capture_img_per_sec.get() if int(self.capture_img_per_sec.get()) in range(1, 11) else 3

            config['content'] = {
                # get() returns str
                'webcam_id': webcam_ids,  # [0, 2]
                'img_width': self.img_width.get(),  # 1280
                'img_height': self.img_height.get(),  # 720
                'capture_img_per_sec': self.capture_img_per_sec,  # 3
                'max_img_counter': self. max_img_counter.get(),   # 20
                'save_img_path': self.dir_txt.get()
                # 'save_img_path': '/home/wc/Desktop/code/ML/andfun/images'
            }

            self.destroy()

            with open('auto_capture_config.txt', 'w') as configfile:
                config.write(configfile)

            print("Config data is saved to auto_capture_config.txt")


usbVideoDevice = UsbVideoDevice()
webcam_ids = usbVideoDevice.getAllIds()  # [0, 2]

config = configparser.ConfigParser()

window = Window()
window.mainloop()
