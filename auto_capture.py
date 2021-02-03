import cv2
import os
import datetime
import time
import configparser
import json

# Read user configuration data
config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
content = config['content']


webcam_ids = json.loads(config.get('content', 'webcam_id'))
# webcam_ids = [0, 2, -10]    # Testing webcam id that doen't exist

config_path = os.path.expanduser(content['save_img_path'])  # ('/usr/aaa')
# config_path = '/something'

img_width = int(content['img_width'])
img_height = int(content['img_height'])

# Initialize fixed size lists
ret, cap, imgs, webcam_names = [list(range(len(webcam_ids))) for _ in range(4)]

img_counter = 1
now = datetime.datetime.now()
today = now.strftime("%m/%d/%Y")   # text on images
dt_string = now.strftime("%B_%d_%Y_%Hhr_%Mmin")

# webcam_ids = [0,2]
# Reading multiple web cams
for index, webcam_id in enumerate(webcam_ids):  # 0,1,2,3
    webcam_names[index] = 'Webcam: ' + str(webcam_id)

    if cv2.VideoCapture(webcam_id).isOpened():
        cap[index] = cv2.VideoCapture(webcam_id)    # 0, 2
        # cap[index].set(3, 640)   # 1280
        # cap[index].set(4, 480)  # 720
    else:
        print(f"Failed to open webcam id:{webcam_id} and {index}")

        # del webcam_ids[index]        index -= 1
        # webcam_ids.remove(webcam_ids[index])
        # webcam_ids.pop(index)

        
# Separating dir using webcam_ids
paths = [None] * len(webcam_ids)
for i in range(len(webcam_ids)):
    paths[i] = os.path.join(config_path, 'webcam' + str(webcam_ids[i]))

    if not os.path.exists(paths[i]):    # '/usr/aaa'
        try:
            os.makedirs(paths[i])
        except OSError:
            print("Can't create destination directory (%s)!" % paths[i])
            home = os.path.expanduser("~")
            path = os.path.join(home, 'unkonw_path')
            # path = os.path.join(home, 'aaa')
            os.makedirs(path, exist_ok=True)
            print(f"Default path will be used: {path}")

# Image Capturing process
start_time = datetime.datetime.now()
while True:

    for i in range(len(webcam_ids)):
        if isinstance(cap[i], int):
            continue
        ret[i], imgs[i] = cap[i].read()
        cv2.imshow(webcam_names[i], imgs[i])

    # time.sleep(1)
    if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        print("Writing Images . . .")
        # print(start_time.second)

        for _ in range(int(content['capture_img_per_sec'])):
            for j in range(len(webcam_ids)):

                if isinstance(imgs[j], int):
                    continue

                img_name = f"{dt_string}_{img_counter}.png"

                cv2.putText(imgs[j], f"{today}  id:{webcam_ids[j]}", (int(
                    img_width * 0.6), int(img_height * 0.9)), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)

                imgs[j] = cv2.resize(imgs[j], (img_width, img_height))

                isWritten = cv2.imwrite(os.path.join(paths[j], img_name), imgs[j])
                # print(f"{img_name} written! {imgs[j].shape[1]}x{imgs[j].shape[0]} pixels")

                img_counter += 1

    if img_counter >= int(content['max_img_counter']):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()  # close all the opened windows

try:
    if isWritten:
        print("Saved Image Path:" + config_path)
except NameError:
    print("Images are not saved.")
