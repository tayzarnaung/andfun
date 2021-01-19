import cv2
import os
import datetime
import configparser


config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
content = config['content']
# print(config.sections())

# webcam_ids = [0, 2]
webcam_ids_str = content['webcam_id']
webcam_ids = []
for string in webcam_ids_str:
    try:
        webcam_ids.append(int(string))
    except ValueError:
        continue


ret, cap, imgs, webcam_names = ([] for _ in range(4))

for i in webcam_ids:
    webcam_names.append(('Webcam: ' + str(i)))
# print(webcam_names)

# initialize fixed size lists
for i in range(len(webcam_ids)):
    ret.append(i)
    cap.append(i)
    imgs.append(i)

for index, webcam_id in enumerate(webcam_ids):
    cap[index] = cv2.VideoCapture(webcam_id)
    # cap = cv2.VideoCapture(list(content['webcam_id'])[0])
    # cap = cv2.VideoCapture(0)
    # cap[index].set(3, int(content['img_width']))
    # cap[index].set(4, int(content['img_height']))

start_time = datetime.datetime.now()
# path = os.path.expanduser(content['save_img_path'])
path = os.path.expanduser('/home/wc/Desktop/code/ML/andfun/studio/images')
img_counter = 1

while True:
    for i in range(len(webcam_ids)):
        ret[i], imgs[i] = cap[i].read()
        cv2.imshow(webcam_names[i], imgs[i])

    if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        print(start_time.second)

        # while count > 0:
        for i in range(int(content['capture_img_per_sec'])):
            for j in range(len(webcam_ids)):

                img_name = f"WebCam{webcam_ids[j]}_{img_counter}.png"

                cv2.imwrite(os.path.join(path, img_name), imgs[j])
                print(
                    f"{img_name} written! {imgs[j].shape[1]}x{imgs[j].shape[0]} pixels")

                img_counter += 1
            # count -= 1

    if img_counter >= int(content['max_img_counter']):
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# cap.release()  # close the camera
cv2.destroyAllWindows()  # close all the opened windows
