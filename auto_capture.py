import cv2
import os
import datetime
import time
import configparser
import json

# Read user configuration data
config = configparser.ConfigParser()
config.read('auto_capture_config.txt')

# webcam_names = json.loads(config.get('content', 'webcam_names'))
# print(webcam_names)
webcam_ids = json.loads(config.get('content', 'webcam_id'))

content = config['content']
img_width = int(content['img_width'])
img_height = int(content['img_height'])
config_path = os.path.expanduser(content['save_img_path'])

# Reading multiple web cams
cap, cap_titles = ([None] * len(webcam_ids) for _ in range(2))
unopened_webcam_ids = []

for index, webcam_id in enumerate(webcam_ids):
    if cv2.VideoCapture(webcam_id).isOpened():
        cap[index] = cv2.VideoCapture(webcam_id)    # 0, 2
        # cap[index].set(3, 640)   # 1280
        # cap[index].set(4, 480)  # 720
        cap_titles[index] = 'Webcam: ' + str(webcam_id)
    else:
        unopened_webcam_ids.append(webcam_id)
        print(f"Failed to open webcam id:{webcam_id}")


# Cleaning failed index of which webcam ids cannot be read
webcam_ids = [ele for ele in webcam_ids if ele not in unopened_webcam_ids]
cap_titles = [ele for ele in cap_titles if ele is not None]

for ele in cap:
    if ele is None:
        cap.remove(ele)


# Initialize fixed size lists
ret, imgs = [list(range(len(webcam_ids))) for _ in range(2)]

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
img_counter = 0
while True:

    for i in range(len(webcam_ids)):
        # if cap[i] is None:  continue
        ret[i], imgs[i] = cap[i].read()
        cv2.imshow(cap_titles[i], imgs[i])

    # time.sleep(1)
    if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        txt_on_imgs = start_time.strftime("%Y_%m_%d_%Hhr_%Mmin_%Ssec")

        print("Writing Images . . .")
        # print(start_time.second)

        for _ in range(int(content['capture_img_per_sec'])):
            img_counter += 1
            for j in range(len(webcam_ids)):

                # if isinstance(imgs[j], int):    continue

                img_name = f"{txt_on_imgs}_{img_counter}.png"

                imgs[j] = cv2.resize(imgs[j], (img_width, img_height))
                cv2.putText(imgs[j], f"id:{webcam_ids[j]}", (int(img_width * 0.6), int(img_height * 0.9)), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                isWritten = cv2.imwrite(
                    os.path.join(paths[j], img_name), imgs[j])
                # print(f"{img_name} written! {imgs[j].shape[1]}x{imgs[j].shape[0]} pixels")


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
