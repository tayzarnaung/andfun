import datetime
import os
import cv2
import configparser

config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
content = config['content']
print(config.sections())

ret, cap, imgs, webcam_names = ([] for _ in range(4))
# webcam_ids = [0, 2]
webcam_ids = content['webcam_id']
print(webcam_ids)
print(type(webcam_ids))

webcam_id = []
for string in webcam_ids:
    try:
        webcam_id.append(int(string))
    except ValueError:
        continue

print(webcam_id)
print(type(webcam_id))




for i in webcam_ids:
    webcam_names.append(('Webcam: ' + str(i)))
# print(webcam_names)

for i in range(len(webcam_ids)):
    ret.append(i)
    cap.append(i)
    imgs.append(i)

# for index, webcam_id in enumerate(webcam_ids):
#     # cap = cv2.VideoCapture(list(content['webcam_id'])[0])
#     cap[index] = cv2.VideoCapture(webcam_id)
#     # cap[index].set(3, 640)
#     # cap[index].set(4, 480)
#     cap[index].set(3, int(content['img_width']))
#     cap[index].set(4, int(content['img_height']))


# start_time = datetime.datetime.now()
# path = os.path.expanduser(content['save_img_path'])
# # path = os.path.expanduser('/home/wc/Desktop/code/ML/andfun/studio/images')
# img_counter = 1

# while True:
#     for i in range(len(webcam_ids)):
#         ret[i], imgs[i] = cap[i].read()
#         cv2.imshow(webcam_names[i], imgs[i])

#     if (datetime.datetime.now() - start_time).seconds == 1:  # Time elapsed 1 sec
#         start_time = datetime.datetime.now()
#         print(start_time.second)

#         # while count > 0:
#         for i in range(int(content['capture_img_per_sec'])):
#             for j in range(len(webcam_ids)):

#                 img_name = f"WebCam{webcam_ids[j]}_{img_counter}.png"

#                 cv2.imwrite(os.path.join(path, img_name), imgs[j])
#                 print(
#                     f"{img_name} written! {imgs[j].shape[1]}x{imgs[j].shape[0]} pixels")

#                 img_counter += 1
#         # count -= 1

#     if img_counter >= int(content['max_img_counter']):
#         break

#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         # cap.release()
#         break

# cv2.destroyAllWindows()
