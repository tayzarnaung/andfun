Andfun Yangon/Studio
This is auto capturing images from multiple cameras.

Version: 2.0


New Features: 
    Multiple Web cam capturing 3 imgaes per second automatically.


Description:
    I set the maximum limit of auto capturing imgaes just to 20 phtots.


Prerequisite:
    Linux environment, python3, opencv-python
    sudo apt install python3, python3-pip
    pip3 install opencv-python


File Description:

    "usbVideoDevice.py":
        a class to know all connected  wbcam names, webcam_ids and  ports.

    "auto_capture_config.py":
        Only if we run auto_capture_config.py, we will get user's connect web cam ids. 
        No porblem whatever webcam ids are. 
        This code will read connected webcam ids from "UsbVideoDevice class" and write config data to "auto_capture_config.txt".
        In this file, set "save_img_path" where you want to store images. Create folder and set path to it.


    "auto_capture_config.txt":
         input settings that will satisfy user's requirement

    "auto_capture.py":
         will do the main function.


How to run:
    python auto_capture_config.py
    python auto_capture.py
