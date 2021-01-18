import configparser

config = configparser.ConfigParser()

config['content'] = {
    # 'webcam_id': '2',
    'webcam_id': [0, 2],
    'img_width': 1280,
    'img_height': 720,
    'capture_img_per_sec': 3,
    'max_img_counter': '20',
    'save_img_path': '/home/wc/Desktop/code/ML/andfun/studio/images'
    # 'save_img_path': '/usr/aaa'
}


with open('auto_capture_config.txt', 'w') as configfile:
    config.write(configfile)
