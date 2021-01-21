import cv2
import os
import datetime
import configparser
import json


config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
content = config['content']
# print(config.sections())

webcam_ids = json.loads(config.get('content', 'webcam_id'))
# webcam_ids = [0, 2, -10]    # Testing webcam id that doen't exist

# Initialize fixed size lists
ret, cap, imgs, webcam_names = [list(range(len(webcam_ids))) for _ in range(4)]

for index, webcam_id in enumerate(webcam_ids):

    webcam_names[index] = 'Webcam: ' + str(webcam_id)

    if cv2.VideoCapture(webcam_id).isOpened():
        cap[index] = cv2.VideoCapture(webcam_id)    # 0, 2
        cap[index].set(3, int(content['img_width']))
        cap[index].set(4, int(content['img_height']))
    else:
        print(f"Failed to open webcam id:{webcam_id}")
        print(f"{index}: {cap[index]} failed to read cv2.VideoCapture()")

start_time = datetime.datetime.now()
path = os.path.expanduser(content['save_img_path'])  # ('/home/wc/Desktop')
img_counter = 1

while True:
    for i in range(len(webcam_ids)):
        if isinstance(cap[i], int):
            continue
        ret[i], imgs[i] = cap[i].read()
        cv2.imshow(webcam_names[i], imgs[i])

    if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        # print(start_time.second)

        for _ in range(int(content['capture_img_per_sec'])):
            for j in range(len(webcam_ids)):

                img_name = f"WebCam{webcam_ids[j]}_{img_counter}.png"

                cv2.imwrite(os.path.join(path, img_name), imgs[j])
                # print(f"{img_name} written! {imgs[j].shape[1]}x{imgs[j].shape[0]} pixels")

                img_counter += 1

    if img_counter >= int(content['max_img_counter']):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()  # close all the opened windows
print("Saved Image Path:" + content['save_img_path'])
