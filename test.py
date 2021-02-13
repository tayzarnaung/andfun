import json
import configparser

configparser = configparser.ConfigParser()
configparser.read('auto_capture_config.txt')

print(configparser.sections())

ids_str = configparser['content']['webcam_ids']
# print(ids_str)
# print(configparser['content']['img_width'])

print(configparser.get('content', 'webcam_ids'))

v = json.loads(configparser.get('content','webcam_ids'))
