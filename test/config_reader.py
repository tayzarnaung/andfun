import configparser
import json

config = configparser.ConfigParser()

config.sections()   # []
config.read('config.ini')  # ['config.ini']
# config.read('/home/wc/Desktop/code/OpenCV/AndFun/config.ini')
config.sections()   # ['bitbucket.org', 'topsecret.server.com']

'bitbucket.org' in config   # True
'bytebong.com' in config    # False

config['bitbucket.org']['User']     # 'hg'
config['DEFAULT']['Compression']    # 'yes'

topsecret = config['topsecret.server.com']
topsecret['ForwardX11']     # 'no'
topsecret['Port']   # '50022'

# for key in config['topsecret.server.com']:
    # print(key)  # user
    # compressionlevel
    # serveraliveinterval
    # compression
    # forwardx11

config['bitbucket.org']['ForwardX11']   # yes

config.items('content')
# [
#     ('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'),
#     ('forwardx11', 'yes'), ('cost', '[20, 10.5, -1]')
# ]
dict(config.items('content'))
# {
#     'serveraliveinterval': '45', 'compression': 'yes', 'compressionlevel': '9', 
#     'forwardx11': 'yes', 'cost': '[20, 10.5, -1]'
# }
json.loads(config.get("content", "cost"))
# [20, 10.5, -1]    # list
