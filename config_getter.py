
import configparser
import json
# import cv2

config = configparser.ConfigParser()
config.read('auto_capture_config.txt')
print(config.sections())
# print(config.items('content'))    # list of tuples
# print(dict(config.items('content')))


webcam_ids = json.loads(config.get('content', 'webcam_id'))
# print(webcam_ids)
cap = []
