import cv2
import os
import datetime


start_time = datetime.datetime.now()
print(f'{start_time.hour}hr {start_time.minute}min {start_time.second}sec' )
img_counter = 1

# cap = cv2.VideoCapture('/dev/video0')
cap = cv2.VideoCapture(2)
cap.set(3, 1920)
cap.set(4, 1080)    # to get FHD, but my display is HD(1280x720)

while True:
    ret, img = cap.read()
    cv2.imshow('Studio', img)

    if (datetime.datetime.now() - start_time).seconds == 1: # Time elapsed 1 sec
        start_time = datetime.datetime.now()
        print(start_time)

        freq = 0
        while freq < 3:
            # img_name = "prefix_camera{}.png".format(img_counter)
            img_name = f"prefix_camera{img_counter}.png"

            path = os.path.expanduser("/usr/aaa") 
            # sudo chmod 777 /usr/aaa in terminal, making executable to solve write permission denied

            cv2.imwrite(os.path.join(path, img_name), img)
            print(f"{img_name} written! {img.shape[1]}x{img.shape[0]} pixels")

            img_counter += 1
            freq += 1

    if img_counter == 31:   break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()  # close the camera
cv2.destroyAllWindows()  # close all the opened windows
