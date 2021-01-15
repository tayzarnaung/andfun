import configparser

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

for key in config['topsecret.server.com']:
    print(key)  # user
                # compressionlevel
                # serveraliveinterval
                # compression
                # forwardx11
config['bitbucket.org']['ForwardX11']   # yes
