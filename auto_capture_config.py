import configparser

config = configparser.ConfigParser()

config['content'] = {
	'webcam-id':'2',
	'resolution': [1920, 1080],  # FullHD
	'capture-img-per-sec': 3,
	'total-img-limit': '30',	
	'save-img-path': '/usr/aaa'
}


with open('auto_capture_config.txt', 'w') as configfile:
	config.write(configfile)
