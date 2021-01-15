import cv2
import os
import datetime
import configparser

config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
# print(config.sections())

content = config['content']

cap = cv2.VideoCapture(int(content['webcam_id']))
cap.set(3, int(content['img_width']))
cap.set(4, int(content['img_height']))    # to get FHD, but my display is HD(1280x720)

start_time = datetime.datetime.now()
path = os.path.expanduser(content['save_img_path'])
img_counter = 1

while True:
    ret, img = cap.read()
    cv2.imshow('Studio', img)

    if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        print(start_time.second)

        # count = int(content['capture_img_per_sec'])
        # while count > 0:
        for i in range(int(content['capture_img_per_sec'])):
            img_name = f"prefix_camera{img_counter}.png"

            cv2.imwrite(os.path.join(path, img_name), img)
            print(f"{img_name} written! {img.shape[1]}x{img.shape[0]} pixels")

            img_counter += 1
            # count -= 1

    if img_counter >= int(content['max_img_counter']):
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()  # close the camera
cv2.destroyAllWindows()  # close all the opened windows
